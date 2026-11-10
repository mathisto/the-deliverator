import { readFile, writeFile, mkdir, copyFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';
const root = fileURLToPath(new URL('../', import.meta.url));
const map = JSON.parse(await readFile(resolve(root, 'ui/icon-map.json'), 'utf8'));
const pkg = resolve(root, 'node_modules/@phosphor-icons/core');
const icons = {};
const symbols = [];
for (const [name, asset] of Object.entries(map)) {
  const source = (await readFile(resolve(pkg, 'assets', asset), 'utf8')).trim();
  if (!source.startsWith('<svg ') || /<script|onload=|<foreignObject/.test(source)) throw new Error(`Invalid icon ${name}`);
  icons[name] = source.replace('<svg ', `<svg data-dv-icon="${name}" aria-hidden="true" focusable="false" `);
  symbols.push(`<symbol id="${name}" viewBox="0 0 256 256" fill="currentColor" stroke="none">${source.replace(/^<svg[^>]+>/, '').replace(/<\/svg>$/, '')}</symbol>`);
}
// Compatibility aliases for the existing portfolio. New markup uses semantic names above.
const aliases = { 'arrow-up-right': 'open-project', 'arrow-up': 'back-to-top', 'rotate-ccw': 'reset', hourglass: 'sand', droplet: 'water', mountain: 'stone', eraser: 'erase', x: 'close' };
for (const [alias, name] of Object.entries(aliases)) symbols.push(symbols.find(s=>s.startsWith(`<symbol id="${name}" `)).replace(`id="${name}"`, `id="${alias}"`));
await writeFile(resolve(root, 'ui/icons.generated.ts'), '// Generated from pinned @phosphor-icons/core by tools/build-icons.mjs. Do not edit.\nexport const icons: Record<string, string> = ' + JSON.stringify(icons, null, 2) + ';\n');
await mkdir(resolve(root, 'dist'), { recursive: true });
await writeFile(resolve(root, 'dist/icons.svg'), '<!-- Phosphor Icons, MIT. See PHOSPHOR-LICENSE.txt. Generated subset. -->\n<svg xmlns="http://www.w3.org/2000/svg">' + symbols.join('') + '</svg>\n');
await copyFile(resolve(pkg, 'LICENSE'), resolve(root, 'dist/PHOSPHOR-LICENSE.txt'));
console.log(`Generated ${Object.keys(icons).length} Phosphor icons and compatibility sprite.`);
