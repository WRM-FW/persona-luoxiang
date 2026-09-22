// Validate the generated skill's YAML surfaces with the same parser family DSH uses.
// Usage: node validate_yaml.mjs <skillDir>
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const YAML = require("yaml");

const skillDir = process.argv[2] ?? ".";
const SKILL_NAME = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

let failures = 0;

function ok(label, extra = "") {
  console.log(`PASS  ${label}${extra ? "  " + extra : ""}`);
}
function bad(label, extra = "") {
  failures += 1;
  console.log(`FAIL  ${label}${extra ? "  " + extra : ""}`);
}

// 1) skill.yaml
try {
  const doc = YAML.parse(readFileSync(join(skillDir, "skill.yaml"), "utf8"));
  ok("skill.yaml parses", `id=${doc.id} version=${doc.version}`);
} catch (error) {
  bad("skill.yaml parses", String(error.message));
}

// 2) SKILL.md frontmatter, mirroring dsh-skill-filesystem's requirements
const raw = readFileSync(join(skillDir, "SKILL.md"), "utf8");
const match = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?/.exec(raw);
if (!match) {
  bad("SKILL.md has YAML frontmatter");
} else {
  let data;
  try {
    data = YAML.parse(match[1]);
    ok("SKILL.md frontmatter parses");
  } catch (error) {
    bad("SKILL.md frontmatter parses", String(error.message));
  }
  if (data) {
    typeof data.name === "string" && data.name
      ? ok("frontmatter.name present", data.name)
      : bad("frontmatter.name present");
    typeof data.description === "string" && data.description
      ? ok("frontmatter.description present", `${data.description.length} chars`)
      : bad("frontmatter.description present");
    typeof data.name === "string" && SKILL_NAME.test(data.name)
      ? ok("frontmatter.name is loader-valid kebab-case")
      : bad("frontmatter.name is loader-valid kebab-case", String(data.name));
    for (const key of ["user-invocable", "disable-model-invocation"]) {
      if (key in data) {
        const value = data[key];
        typeof value === "boolean"
          ? ok(`invocation key parsed as boolean: ${key}`, String(value))
          : bad(`invocation key must be boolean: ${key}`, JSON.stringify(value));
      }
    }
  }
}

// 3) copyright-safety shape required by distilly's quality gate
const body = match ? raw.slice(match[0].length) : raw;
/^\s*>/m.test(body) ? bad("no markdown blockquote lines") : ok("no markdown blockquote lines");
/```/.test(body) ? bad("no code fences") : ok("no code fences");
/\b\d{2}:\d{2}:\d{2}\b/.test(body) ? bad("no timecodes") : ok("no timecodes");

console.log(failures === 0 ? "OVERALL PASS" : `OVERALL FAIL (${failures})`);
process.exit(failures === 0 ? 0 : 1);