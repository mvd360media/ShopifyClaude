import { chromium } from 'playwright';
const [,, url, out] = process.argv;
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell', args: ['--no-sandbox'] });
const p = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1 });
await p.goto(url, { waitUntil: 'load', timeout: 90000 }); await p.waitForTimeout(3000);
const sw = await p.evaluate(() => document.documentElement.scrollWidth); console.log('ancho de página:', sw);
await p.evaluate(() => document.querySelector('[data-oc-pers]')?.scrollIntoView({ block: 'start' })); await p.waitForTimeout(800);
await p.screenshot({ path: out });
await b.close();
