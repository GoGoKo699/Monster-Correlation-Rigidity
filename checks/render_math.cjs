#!/usr/bin/env node
// Parse the exported active-page corpus with MathJax. This is not GitHub's UI.
// Dependency used for this regression: mathjax-full 3.2.1, installed separately.
const fs = require('fs');
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');
if (!process.argv[2]) throw new Error('Usage: render_math.cjs corpus.json [rendered.json]');
const corpus = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
if (!Array.isArray(corpus) || !corpus.length) throw new Error('Empty math corpus');
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const document = mathjax.document('', {
  InputJax: new TeX({packages: AllPackages}),
  OutputJax: new SVG({fontCache: 'none'})
});
const rendered = corpus.map((entry) => {
  if (typeof entry.tex !== 'string') throw new Error('Missing TeX input');
  const html = adaptor.outerHTML(document.convert(entry.tex, {display: entry.display}));
  if (html.includes('data-mjx-error') || html.includes('data-mml-node="merror"')) {
    throw new Error('TeX error in ' + entry.page + ': ' + entry.tex);
  }
  return {...entry, html};
});
if (process.argv[3]) fs.writeFileSync(process.argv[3], JSON.stringify(rendered));
console.log(JSON.stringify({status: 'PASS MathJax syntax', expressions: corpus.length,
  mathjax_version: require('mathjax-full/package.json').version,
  live_GitHub_render_verified: false}, null, 2));
