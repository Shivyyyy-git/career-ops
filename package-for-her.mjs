#!/usr/bin/env node
// Packages this repo into a clean, local-only copy for a non-technical user.
// Strips: his personal data, GitHub/OSS scaffolding, build artifacts, dev tooling.
// Keeps:  the app, the modes, the templates, the placeholder setup prompt.
//
// Usage:
//   node package-for-her.mjs                 # writes to ../career-ops-for-her
//   node package-for-her.mjs <dest>          # writes to <dest>
//   node package-for-her.mjs <dest> --force  # overwrite if dest exists
//   node package-for-her.mjs --dry-run       # show what would be copied/dropped
//
// After running, the destination folder is ready to be zipped and handed off.
// She opens the folder, runs `npm install`, then pastes HER_SETUP_PROMPT.md
// into Claude Code. The prompt does the rest on her machine.

import { promises as fs } from "node:fs";
import path from "node:path";
import process from "node:process";

const SRC = path.resolve(new URL(".", import.meta.url).pathname);

// Anything matching these (relative to repo root) is dropped.
// Order: full path matches, then directory names, then suffixes.
const DROP_PATHS = new Set([
  // his personal data — replaced with templates or omitted entirely
  "cv.md",
  "article-digest.md",
  "portals.yml",
  "config/profile.yml",
  "modes/_profile.md",
  "data/applications.md",
  "data/pipeline.md",
  "data/scan-history.tsv",
  "data/follow-ups.md",
  "HER_SETUP_PROMPT.md",        // re-emitted as a fresh placeholder below

  // GitHub / OSS scaffolding she does not need
  ".coderabbit.yaml",
  ".release-please-manifest.json",
  "renovate.json",
  ".envrc",
  ".env.career-ops",
  "AGENTS.md",
  "CHANGELOG.md",
  "CITATION.cff",
  "CODE_OF_CONDUCT.md",
  "CONTRIBUTING.md",
  "GOVERNANCE.md",
  "SECURITY.md",
  "SUPPORT.md",
  "README.es.md",
  "README.ja.md",
  "README.ko-KR.md",
  "README.pt-BR.md",
  "README.ru.md",
  "README.zh-TW.md",
  "flake.nix",
  "flake.lock",
  "render.yaml",

  // dev / packaging artifacts and infra she will never touch
  "update-system.mjs",
  "test-all.mjs",
  "package-for-her.mjs",        // don't ship the packager itself
  "package-lock.json",
]);

const DROP_DIRS = new Set([
  ".git",
  ".github",
  ".opencode",
  "node_modules",
  "cron",
  "docs",
  "reports",
  "output",
  "interview-prep",
  "jds",
  "batch",
  // inside .claude — drop his settings, keep the skill
  ".claude/settings.local.json",
]);

const DROP_SUFFIXES = [".DS_Store"];

// Files we want to exist in the destination but with empty/template content.
// rel → contents
const EMIT_EMPTY = {
  "data/applications.md":
    "# Applications Tracker\n\n| # | Date | Company | Role | Score | Status | PDF | Report | Notes |\n|---|------|---------|------|-------|--------|-----|--------|-------|\n",
  "data/pipeline.md":
    "# Pipeline Inbox\n\n_Pending URLs and pasted JDs land here._\n",
  "HER_SETUP_PROMPT.md":
    `<!--\n  PLACEHOLDER — the actual setup prompt will be added here later.\n\n  When ready, this file will hold the single message to paste into\n  Claude Code on first run. The prompt will (a) finish stripping any\n  developer-facing language from this folder, (b) walk through CV +\n  profile setup in plain English, and (c) lock the workflow to:\n  paste a job-description PDF -> get an evaluation. If a link is\n  pasted, Claude must say the link will not work and ask for a PDF\n  saved from Chrome (File -> Print -> Save as PDF) instead.\n-->\n\n# Setup prompt — TO BE WRITTEN\n\n(Placeholder. Real content coming later.)\n`,
};

function isDropped(rel) {
  if (DROP_PATHS.has(rel)) return true;
  for (const suf of DROP_SUFFIXES) if (rel.endsWith(suf)) return true;
  // dir match: rel === dir, or rel starts with dir + "/"
  for (const dir of DROP_DIRS) {
    if (rel === dir || rel.startsWith(dir + "/")) return true;
  }
  return false;
}

async function walk(dir, base = "") {
  const out = [];
  const entries = await fs.readdir(path.join(SRC, dir), { withFileTypes: true });
  for (const e of entries) {
    const rel = base ? `${base}/${e.name}` : e.name;
    if (e.isDirectory()) {
      if (isDropped(rel)) continue;
      out.push(...(await walk(path.join(dir, e.name), rel)));
    } else {
      out.push(rel);
    }
  }
  return out;
}

async function main() {
  const args = process.argv.slice(2);
  const dryRun = args.includes("--dry-run");
  const force = args.includes("--force");
  const positional = args.filter((a) => !a.startsWith("--"));
  const dest = path.resolve(positional[0] || path.join(SRC, "..", "career-ops-for-her"));

  if (dest === SRC) {
    console.error("refusing to overwrite the source repo");
    process.exit(1);
  }

  const allFiles = await walk(".");
  const kept = [];
  const dropped = [];
  for (const rel of allFiles) {
    if (isDropped(rel)) dropped.push(rel);
    else kept.push(rel);
  }

  console.log(`source:      ${SRC}`);
  console.log(`destination: ${dest}`);
  console.log(`keeping:     ${kept.length} files`);
  console.log(`dropping:    ${dropped.length} files`);
  console.log("");

  if (dryRun) {
    console.log("--- would drop ---");
    for (const r of dropped) console.log("  -", r);
    console.log("\n--- would keep (first 40) ---");
    for (const r of kept.slice(0, 40)) console.log("  +", r);
    if (kept.length > 40) console.log(`  ... and ${kept.length - 40} more`);
    console.log("\ndry run — nothing written");
    return;
  }

  // Refuse to clobber unless --force.
  try {
    await fs.access(dest);
    if (!force) {
      console.error(`destination exists: ${dest}\nrerun with --force to overwrite`);
      process.exit(1);
    }
    await fs.rm(dest, { recursive: true, force: true });
  } catch {
    // does not exist — fine
  }

  for (const rel of kept) {
    if (rel in EMIT_EMPTY) continue; // emitted explicitly below
    const from = path.join(SRC, rel);
    const to = path.join(dest, rel);
    await fs.mkdir(path.dirname(to), { recursive: true });
    await fs.copyFile(from, to);
  }

  for (const [rel, content] of Object.entries(EMIT_EMPTY)) {
    const to = path.join(dest, rel);
    await fs.mkdir(path.dirname(to), { recursive: true });
    await fs.writeFile(to, content);
  }

  console.log(`wrote ${kept.length} files to ${dest}`);
  console.log("\nnext steps:");
  console.log(`  1. cd "${dest}" && npm install`);
  console.log(`  2. zip the folder, hand it to her`);
  console.log(`  3. she opens it, runs npm install, then pastes HER_SETUP_PROMPT.md into Claude Code`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
