# style-guide-enforcer

MCP server that checks documentation for terminology violations, passive voice, structure completeness, and readability.

## Tools

| Tool | Description |
|------|-------------|
| `check_terminology` | Flags banned terms and suggests approved alternatives from `data/glossary.json` |
| `detect_passive_voice` | Finds passive voice sentences and suggests active rewrites |
| `validate_doc_structure` | Checks required sections by doc type (how-to, reference, tutorial, release-note) |
| `grade_readability` | Returns Easy / Moderate / Complex grade based on sentence length |

## Resources

| Resource URI | Description |
|---|---|
| `style-guide://glossary` | The approved terms list as JSON |
| `style-guide://structure-rules` | Required and optional sections per doc type as JSON |

## Installation

```bash
npm install
npm run build
claude mcp add style-guide-enforcer -- node /absolute/path/to/dist/index.js
```

## Usage

```
Use check_terminology on docs/my-article.md
Use detect_passive_voice on docs/my-article.md
Use validate_doc_structure on docs/my-article.md with docType "how-to"
Use grade_readability on docs/my-article.md
```

## Customizing

### Glossary (`data/glossary.json`)
Each entry: `{ "banned": "word", "approved": "replacement", "note": "reason" }`.
Set `approved` to `""` to flag the word for deletion without a replacement.

### Structure rules (`data/structure-rules.json`)
Each doc type maps to `required` (must have) and `optional` (nice to have) section name arrays.
Matching is case-insensitive and partial — a heading "Next Steps" matches rule "Next steps".

## Publishing

```bash
npm login
npm publish --access public
```

Registry namespace: `io.github.Yashwanthhv7218/style-guide-enforcer`

## License

MIT
