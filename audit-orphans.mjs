#!/usr/bin/env node
// Audit a resume HTML for lines with <3 words (orphan rule).
// Usage: node audit-orphans.mjs <input.html>
// Exits 1 if any violations are found, 2 on usage error.

import { chromium } from 'playwright';
import { resolve } from 'path';
import { pathToFileURL } from 'url';

if (!process.argv[2]) {
  console.error('Usage: node audit-orphans.mjs <input.html>');
  process.exit(2);
}

const input = resolve(process.argv[2]);
const url = pathToFileURL(input).href;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 816, height: 1056 } }); // 8.5x11 in @ 96dpi
await page.goto(url, { waitUntil: 'networkidle' });

// Force print media size
await page.emulateMedia({ media: 'print' });
await page.setViewportSize({ width: 816, height: 1056 });

const violations = await page.evaluate(() => {
  function getLines(el) {
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    const lines = [];
    let cur = null;
    while (walker.nextNode()) {
      const node = walker.currentNode;
      for (let i = 0; i < node.length; i++) {
        const r = document.createRange();
        r.setStart(node, i);
        r.setEnd(node, i + 1);
        const rect = r.getBoundingClientRect();
        if (rect.width === 0 && rect.height === 0) continue;
        if (cur === null || Math.abs(rect.top - cur.y) > 2) {
          if (cur) lines.push(cur.text);
          cur = { y: rect.top, text: node.textContent[i] };
        } else {
          cur.text += node.textContent[i];
        }
      }
    }
    if (cur) lines.push(cur.text);
    return lines;
  }
  const selectors = ['.summary-text', '.job li', '.projects-list li', '.skill-line', '.edu-honors', '.edu-main'];
  const out = [];
  selectors.forEach(sel => {
    document.querySelectorAll(sel).forEach((el, i) => {
      const lines = getLines(el);
      lines.forEach((line, idx) => {
        const words = line.trim().split(/\s+/).filter(w => w.length > 0).length;
        if (words < 3) {
          out.push({
            selector: sel,
            elementIndex: i,
            lineIndex: idx,
            totalLines: lines.length,
            words,
            text: line.trim(),
            elementPreview: el.textContent.slice(0, 100).replace(/\s+/g, ' '),
          });
        }
      });
    });
  });
  return out;
});

await browser.close();

console.log(JSON.stringify(violations, null, 2));
console.log(`\nTotal violations: ${violations.length}`);

if (violations.length > 0) process.exit(1);
