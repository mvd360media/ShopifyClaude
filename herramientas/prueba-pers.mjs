import { chromium } from 'playwright';
import fs from 'node:fs';
const [,, url, out, foto] = process.argv;
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell', args: ['--no-sandbox'] });
const ctx = await b.newContext({ viewport: { width: 1366, height: 900 } });
const p = await ctx.newPage();
await p.goto(url, { waitUntil: 'networkidle', timeout: 90000 }).catch(e => console.log('goto', e.message));
console.log('url final:', p.url().slice(0, 80));
const enc = await p.evaluate(() => { const f = document.querySelector('[data-oc-pers]')?.closest('form'); return f ? [f.getAttribute('enctype'), f.getAttribute('action')] : null; });
console.log('form:', enc);
console.log('pers presente:', await p.locator('[data-oc-pers]').count(), '| opciones:', await p.evaluate(() => [...document.querySelectorAll('.oc-opcion legend')].map(l => l.textContent).join(' > ')));
console.log('muestras de color:', await p.locator('.oc-muestra').count(), '| subtítulo:', await p.evaluate(() => document.querySelector('.oc-compra__intro')?.textContent?.trim().slice(0,60)));
console.log('aviso:', await p.evaluate(() => document.querySelector('.oc-aviso-fechas')?.textContent), '| plazo:', await p.evaluate(() => document.querySelector('.oc-envio')?.textContent?.trim()));
await p.evaluate(() => document.querySelectorAll('.shopify-pc__banner__dialog, #shopify-pc__banner').forEach(e => e.remove()));
await p.screenshot({ path: out + '-1.png', fullPage: false });
// 1) enviar vacío
await p.click('.oc-compra__boton');
await p.waitForTimeout(500);
console.log('error vacío:', await p.locator('[data-oc-error]').textContent(), '| sigue en página:', p.url().includes('/products/'));
// 2) texto demasiado largo (maxlength)
const t = p.locator('[data-oc-contador]');
if (await t.count()) { await t.fill('123456789012345678901234567890'); console.log('texto guardado:', (await t.inputValue()).length, 'caracteres'); await t.fill('Lila'); }
// 3) formato no permitido
const f = p.locator('[data-oc-pers] input[type=file]');
if (await f.count()) {
  fs.writeFileSync('/tmp/claude-0/gen/malo.gif', 'GIF89a');
  await f.setInputFiles('/tmp/claude-0/gen/malo.gif');
  await p.click('.oc-compra__boton'); await p.waitForTimeout(300);
  console.log('error formato:', await p.locator('[data-oc-error]').textContent());
  await f.setInputFiles(foto);
}
const s = p.locator('[data-oc-pers] select');
if (await s.count()) await s.selectOption({ index: 1 });
await p.locator('[data-oc-confirmacion]').check();
await p.screenshot({ path: out + '-2.png', fullPage: true });
// 4) añadir al carrito
const [resp] = await Promise.all([p.waitForNavigation({ timeout: 60000 }).catch(() => null), p.click('.oc-compra__boton')]);
await p.waitForTimeout(1500);
console.log('tras enviar:', p.url().slice(0, 90));
const cart = await p.evaluate(async () => { try { const r = await fetch('/cart.js'); return await r.json(); } catch (e) { return String(e); } });
console.log('carrito:', JSON.stringify(cart?.items?.map(i => ({ t: i.title, v: i.variant_title, props: i.properties })) ?? cart).slice(0, 800));
await p.screenshot({ path: out + '-3.png', fullPage: false });
await b.close();
