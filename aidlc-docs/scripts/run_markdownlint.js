const fs = require('fs');
const path = require('path');
const markdownlint = require('markdownlint');
// simple recursive collector to avoid extra dependencies
function collectMarkdownFiles(startDir) {
  const results = [];
  function walk(dir) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const e of entries) {
      const full = path.join(dir, e.name);
      if (e.isDirectory()) {
        if (e.name === 'node_modules' || e.name === '.git') continue;
        walk(full);
      } else if (e.isFile() && full.toLowerCase().endsWith('.md')) {
        results.push(path.relative(process.cwd(), full));
      }
    }
  }
  walk(startDir);
  return results;
}

(async () => {
  try {
    const files = collectMarkdownFiles(process.cwd());
    if (!files || files.length === 0) {
      fs.mkdirSync(path.dirname('aidlc-docs/markdownlint-report.json'), { recursive: true });
      fs.writeFileSync('aidlc-docs/markdownlint-report.json', JSON.stringify({ files: [] }, null, 2), 'utf8');
      console.log('No markdown files found. Wrote empty report.');
      return;
    }

    const options = { files };
    // use callback API to be compatible with installed markdownlint
    markdownlint(options, function (err, result) {
      if (err) {
        console.error('markdownlint error:', err);
        process.exit(1);
      }
      const rawResults = String(result || '').trim();
      const report = {};
      if (rawResults.length === 0) {
        // no issues
        for (const f of files) report[f] = [];
      } else {
        // rawResults is lines like: "file.md: N: M rule description"
        const lines = rawResults.split(/\r?\n/).filter(Boolean);
        for (const line of lines) {
          const m = line.match(/^([^:]+):\s*(.*)$/);
          if (m) {
            const fname = m[1];
            const rest = m[2];
            report[fname] = report[fname] || [];
            report[fname].push({ raw: rest });
          }
        }
        // ensure all files appear
        for (const f of files) if (!report[f]) report[f] = [];
      }

      fs.mkdirSync(path.dirname('aidlc-docs/markdownlint-report.json'), { recursive: true });
      fs.writeFileSync('aidlc-docs/markdownlint-report.json', JSON.stringify(report, null, 2), 'utf8');
      console.log('Wrote markdownlint report for', Object.keys(report).length, 'files.');
    });

    fs.mkdirSync(path.dirname('aidlc-docs/markdownlint-report.json'), { recursive: true });
    fs.writeFileSync('aidlc-docs/markdownlint-report.json', JSON.stringify(report, null, 2), 'utf8');
    console.log('Wrote markdownlint report for', Object.keys(report).length, 'files.');
  } catch (err) {
    console.error('Error generating markdownlint report:', err);
    process.exit(1);
  }
})();
