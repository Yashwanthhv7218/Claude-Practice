#!/usr/bin/env node
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import * as fs from "fs";
import * as path from "path";
import { z } from "zod";

const server = new McpServer({
  name: "style-guide-enforcer",
  version: "1.0.0",
});

// ── Tool: check_terminology ───────────────────────────────────────────────────

server.tool(
  "check_terminology",
  "Flag banned terms in a document and suggest approved alternatives from the team glossary",
  z.object({
    filePath: z.string().describe("Path to the documentation file to check"),
    glossaryPath: z.string().optional().describe("Path to the glossary JSON file (defaults to data/glossary.json)"),
  }),
  async ({ filePath, glossaryPath }) => {
    const resolvedGlossary = glossaryPath || path.join(__dirname, "../data/glossary.json");
    const content = fs.readFileSync(filePath, "utf-8");

    type GlossaryEntry = { banned: string; approved: string; note?: string };
    const glossary: GlossaryEntry[] = JSON.parse(fs.readFileSync(resolvedGlossary, "utf-8"));

    const violations = glossary
      .filter(({ banned }) => new RegExp(`\\b${banned}\\b`, "gi").test(content))
      .map(({ banned, approved, note }) => ({ found: banned, use_instead: approved, note }));

    return {
      content: [{
        type: "text",
        text: JSON.stringify({
          file: filePath,
          violations_found: violations.length,
          violations,
          status: violations.length === 0 ? "PASS" : "NEEDS_REVISION"
        }, null, 2)
      }]
    };
  }
);

// ── Tool: detect_passive_voice ────────────────────────────────────────────────

server.tool(
  "detect_passive_voice",
  "Find passive voice sentences in a documentation file and suggest revisions",
  z.object({
    filePath: z.string().describe("Path to the documentation file to check"),
  }),
  async ({ filePath }) => {
    const content = fs.readFileSync(filePath, "utf-8");

    const plainText = content
      .replace(/```[\s\S]*?```/g, "")
      .replace(/`[^`]+`/g, "")
      .replace(/#+\s/g, "")
      .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1");

    const passivePattern = /\b(is|are|was|were|has been|have been|will be|can be|should be|must be)\s+\w+ed\b/gi;
    const sentences = plainText.split(/[.!?]+/).filter(s => s.trim().length > 10);

    const passiveSentences = sentences
      .filter(s => passivePattern.test(s))
      .map(s => s.trim().replace(/\n/g, " "));

    passivePattern.lastIndex = 0;

    return {
      content: [{
        type: "text",
        text: JSON.stringify({
          file: filePath,
          passive_sentences_found: passiveSentences.length,
          sentences: passiveSentences,
          tip: "Rewrite using active voice: name the subject doing the action.",
          status: passiveSentences.length === 0 ? "PASS" : "REVIEW_RECOMMENDED"
        }, null, 2)
      }]
    };
  }
);

// ── Tool: validate_doc_structure ──────────────────────────────────────────────

server.tool(
  "validate_doc_structure",
  "Check that a document has all required sections for its type (how-to | reference | tutorial | release-note)",
  z.object({
    filePath: z.string().describe("Path to the documentation file to validate"),
    docType: z.string().describe("The type of document: how-to | reference | tutorial | release-note"),
    rulesPath: z.string().optional().describe("Path to the structure rules JSON file (defaults to data/structure-rules.json)"),
  }),
  async ({ filePath, docType, rulesPath }) => {
    const resolvedRules = rulesPath || path.join(__dirname, "../data/structure-rules.json");
    const content = fs.readFileSync(filePath, "utf-8");

    type StructureRules = Record<string, { required: string[]; optional: string[] }>;
    const rules: StructureRules = JSON.parse(fs.readFileSync(resolvedRules, "utf-8"));

    if (!rules[docType]) {
      return {
        content: [{
          type: "text",
          text: JSON.stringify({
            error: `Unknown doc type: "${docType}". Valid types: ${Object.keys(rules).join(", ")}`
          }, null, 2)
        }]
      };
    }

    const { required, optional } = rules[docType];
    const headings = (content.match(/^#{1,3}\s+.+/gm) || []).map(h => h.replace(/^#+\s+/, "").toLowerCase());

    const missingRequired = required.filter(
      section => !headings.some(h => h.includes(section.toLowerCase()))
    );
    const presentOptional = optional.filter(
      section => headings.some(h => h.includes(section.toLowerCase()))
    );

    return {
      content: [{
        type: "text",
        text: JSON.stringify({
          file: filePath,
          doc_type: docType,
          missing_required_sections: missingRequired,
          present_optional_sections: presentOptional,
          required_score: `${required.length - missingRequired.length}/${required.length}`,
          status: missingRequired.length === 0 ? "COMPLETE" : "INCOMPLETE"
        }, null, 2)
      }]
    };
  }
);

// ── Tool: grade_readability ───────────────────────────────────────────────────

server.tool(
  "grade_readability",
  "Grade the readability of a documentation file based on average sentence length",
  {
    filePath: {
      type: "string",
      description: "Path to the documentation file to grade",
    },
  },
  async ({ filePath }) => {
    const content = fs.readFileSync(filePath, "utf-8");

    const plainText = content
      .replace(/```[\s\S]*?```/g, "")
      .replace(/`[^`]+`/g, "code")
      .replace(/#+\s/g, "")
      .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1");

    const sentences = plainText.split(/[.!?]+/).filter(s => s.trim().length > 10);
    const words = plainText.split(/\s+/).filter(w => w.length > 0);
    const avgSentenceLength = sentences.length > 0 ? words.length / sentences.length : 0;

    let grade: string;
    let recommendation: string;
    if (avgSentenceLength < 15) {
      grade = "Easy";
      recommendation = "Good readability for developer audiences.";
    } else if (avgSentenceLength < 25) {
      grade = "Moderate";
      recommendation = "Acceptable. Consider shortening the longest sentences.";
    } else {
      grade = "Complex";
      recommendation = "Too complex. Target sentences under 25 words for developer docs.";
    }

    return {
      content: [{
        type: "text",
        text: JSON.stringify({
          file: filePath,
          avg_sentence_length: Math.round(avgSentenceLength),
          grade,
          recommendation,
          sentence_count: sentences.length,
          word_count: words.length
        }, null, 2)
      }]
    };
  }
);

// ── Resource: Glossary ────────────────────────────────────────────────────────

server.resource(
  "glossary",
  "style-guide://glossary",
  async (uri) => {
    const glossaryPath = path.join(__dirname, "../data/glossary.json");
    const content = fs.readFileSync(glossaryPath, "utf-8");
    return {
      contents: [{ uri: uri.href, mimeType: "application/json", text: content }]
    };
  }
);

// ── Resource: Structure rules ─────────────────────────────────────────────────

server.resource(
  "structure-rules",
  "style-guide://structure-rules",
  async (uri) => {
    const rulesPath = path.join(__dirname, "../data/structure-rules.json");
    const content = fs.readFileSync(rulesPath, "utf-8");
    return {
      contents: [{ uri: uri.href, mimeType: "application/json", text: content }]
    };
  }
);

// ── Start the server ──────────────────────────────────────────────────────────

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch(console.error);
