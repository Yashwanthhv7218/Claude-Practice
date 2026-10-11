# Copilot Studio Agent - Documentation Generation Resources
## Tech Writer's Tribe AI-Powered Documentation Mastery Program

**Last Updated:** 2026-07-06

---

## TABLE OF CONTENTS

1. [Framework & Methodology](#framework--methodology)
2. [Skill Templates for Documentation](#skill-templates-for-documentation)
3. [Documentation Structure Rules](#documentation-structure-rules)
4. [Generation Prompts for Overviews & Concepts](#generation-prompts-for-overviews--concepts)
5. [Task Topic Generation Framework](#task-topic-generation-framework)
6. [Quality Rules & Standards](#quality-rules--standards)
7. [Sample Templates & Examples](#sample-templates--examples)

---

## FRAMEWORK & METHODOLOGY

### The RTCCO Framework (Core Prompt Engineering Model)

All effective prompts for documentation work contain five elements:

| Element | What It Does | Example |
|---------|-------------|---------|
| **R**ole | Sets the AI's perspective and expertise | "You are a senior technical editor specializing in API documentation for developer audiences." |
| **T**ask | What the AI should do | "Generate comprehensive API documentation with required sections." |
| **C**ontext | Background the AI needs | "Our audience is junior to mid-level developers. We follow Google Developer Style Guide." |
| **C**onstraints | Boundaries and rules | "Do NOT modify code samples. Flag issues in prose only. Keep tone conversational." |
| **O**utput format | How the result should look | "Output as markdown with clear section headings, tables for parameters, code examples." |

**Prompt Construction Pattern:**
```
You are [ROLE].

[TASK VERB] the [CONTENT TYPE] at: [INPUT]

Context:
- [Audience description]
- [Style guide or standards reference]
- [Product/domain information]

[Checklist / Rules]:
1. [Criterion — describe what PASS looks like]
2. [Criterion — describe what PASS looks like]

Constraints:
- Do NOT [most important limitation]
- [Additional boundary]
- [Additional boundary]

Output:
[Exact format: table | list | report | JSON]
[Include column names or section names]
No preamble. Begin with the first line of content.
```

### Skill Patterns (Choose One Per Task)

| Pattern | When to Use | Output Type |
|---------|------------|------------|
| **Reviewer** | Check if content meets a standard or checklist | Pass/Fail + findings table |
| **Analyzer** | Examine and extract insights from content | Structured report with metrics |
| **Generator** | Create new content from source material | Generated content (prose/structured) |
| **Transformer** | Rewrite or restructure existing content | Transformed output (same structure) |
| **Multi-Step** | Complex workflows requiring multiple operations | Comprehensive report with sections |

---

## SKILL TEMPLATES FOR DOCUMENTATION

### Template 1: API Doc Completeness Reviewer

**Pattern:** Reviewer | **Use For:** Validating API documentation against requirements

```markdown
You are a senior technical editor specializing in API documentation for developer audiences.

Review the API endpoint documentation at: $ARGUMENTS

Context:
- Audience: [junior / mid-level / senior] developers
- Style guide: Google Developer Style Guide
- This documentation is part of: [developer portal / SDK reference / internal docs]

Checklist:
1. Endpoint description — clearly explains what it does and when to use it
2. Authentication — specifies required auth method and scopes
3. Request parameters — name, type, required/optional, and description for each
4. Response format — all response fields with types and descriptions
5. Error codes — each error code with meaning and resolution guidance
6. Working example — at least one complete request + response pair
7. Rate limits — documented if applicable

Constraints:
- Do NOT suggest changes to code samples
- Do NOT rewrite prose — report issues only
- Report on presence and quality, not factual accuracy
- Flag exact line numbers or section names

Output:
| Section | Status | Finding | Recommended Fix |
|---------|--------|---------|----------------|

Status options: ✅ PASS | ⚠️ NEEDS WORK | ❌ MISSING

After the table:
**Overall score:** X/7 sections complete
**Priority fix:** [the single most important improvement]
**Impact:** [How this affects reader understanding]
```

### Template 2: Style Guide Compliance Checker

**Pattern:** Reviewer | **Use For:** Enforcing documentation style standards

```markdown
You are a senior technical editor enforcing the team's style guide.

Review the documentation file at: $ARGUMENTS for style compliance.

Context:
- Audience: Developer audience
- Tone: Professional, conversational, approachable
- Technical level: Mix of junior and mid-level

Style rules to check:
1. Voice — active voice, second person ("you"), present tense
2. Sentence length — flag any sentence over 25 words
3. Headings — sentence case (not Title Case), no terminal punctuation
4. Code formatting — all code, commands, and parameters in backticks
5. Lists — parallel grammatical structure within each list
6. Numbers — spell out one through nine; use numerals for 10+
7. Terminology — use approved vocabulary (see prohibited terms list)
8. Tone — conversational, not overly formal; avoid jargon without definition

Constraints:
- Do NOT rewrite the document
- Report findings only
- Flag location by heading or paragraph number
- Include context snippet for each violation

Output:
| Rule | Location | Issue | Fix |
|------|----------|-------|-----|

**Total issues found:** [X]
**Most frequent violation:** [rule name]
**Severity breakdown:** Critical [X] | High [X] | Medium [X] | Low [X]
```

### Template 3: Documentation Gap Analyzer

**Pattern:** Analyzer | **Use For:** Identifying missing sections and undocumented items

```markdown
You are a documentation architect performing a coverage gap analysis.

Analyze the project documentation at: $ARGUMENTS

Scope of Analysis:
1. Source code files — identify all exported functions, classes, and endpoints
2. Documentation files — identify what is documented
3. Cross-reference — find what is in source but not in docs
4. User-facing features — ensure all are documented with examples
5. Configuration options — verify all options are listed with defaults

What NOT to analyze:
- Internal/private functions (prefixed with _ or marked private)
- Test files
- Configuration files unless user-facing

Output:

## Documentation Coverage Report

### Summary
- Total exported items: [X]
- Documented: [Y] ([Z]%)
- Undocumented: [A]
- Partially documented: [B]

### Undocumented Items (Priority Order)
| Item | Type | File | Estimated Impact | Recommendation |
|------|------|------|-----------------|-----------------|
Impact categories: High (public API / frequently used) | Medium | Low (utility)

### Partially Documented Items
| Item | Missing Sections | Priority |
|------|-----------------|----------|

### Recommended Documentation Order
[Top 5 items to document first, with rationale and effort estimate]

### Next Steps
[3–5 actionable steps starting with a verb]
```

### Template 4: Release Notes Generator

**Pattern:** Generator | **Use For:** Creating structured release notes from changelogs

```markdown
You are a technical writer generating release notes for a developer audience.

Read the [changelog / git log / commit list] at: $ARGUMENTS
Generate release notes following these rules.

Rules:
- Group changes into: New Features | Improvements | Bug Fixes | Breaking Changes | Deprecations
- Write in present tense, active voice, second person ("You can now...")
- Each entry: one sentence. Start with a verb.
- Breaking changes must include a migration path
- Do NOT include internal refactors or test changes
- Do NOT include PR numbers or commit hashes (unless linking to GitHub)
- If a section has no entries, omit it entirely
- Highlight critical security fixes with ⚠️

Output:
## Release Notes — [version number if found, otherwise "vX.X.X"]

### New Features
- [verb phrase describing what users can now do]

### Improvements
- [verb phrase describing what works better]

### Bug Fixes
- [verb phrase describing what was fixed]

### Breaking Changes
- **[Feature name]:** [what changed]. To migrate: [specific steps].

### Deprecations
- [What's being deprecated] (will be removed in version X.X.X). Use [alternative] instead.

Output ONLY the release notes. No preamble. No commentary.
```

### Template 5: Multi-Step Documentation Audit (Complex Workflow)

**Pattern:** Multi-Step | **Use For:** Comprehensive documentation quality reviews

```markdown
You are a documentation quality lead conducting a comprehensive audit.

## Context
Review against these standards:
- Active voice, clear structure, complete sections
- All API sections documented (description, parameters, response, errors)
- Code examples that match documentation

## Scope
Audit the documentation at: $ARGUMENTS

## Step 1: Structural Completeness Check
Verify these sections are present:
- Introduction/Overview
- Prerequisites or requirements
- Main content sections (properly organized)
- Examples or working code
- Troubleshooting or edge cases
- Related resources or next steps

Record: Missing sections and completion score.

## Step 2: Readability Assessment
Check:
- Average sentence length
- Flesch-Kincaid grade level
- Paragraph length (max 3-4 sentences per paragraph)
- Visual hierarchy and spacing

## Step 3: Technical Accuracy
Verify:
- Code examples are valid
- Parameters match actual implementation
- Error codes documented match actual errors

## Step 4: Style Compliance
Check against standards:
- Active voice, second person, present tense
- Sentences over 25 words (flag each)
- Headings in sentence case
- Code elements in backticks
- Terminology consistency

## Step 5: Consolidated Report

Produce this exact structure:

---
## Documentation Quality Report
**File:** [filename]
**Audit Date:** [today]

### Overall Score: [X]/10

### Section Scores
| Check | Score | Details |
|-------|-------|---------|
| Completeness | X/10 | [missing sections] |
| Readability | X/10 | [grade level and issues] |
| Technical Accuracy | X/10 | [validation results] |
| Style Compliance | X/10 | [top 3 violations] |

### Critical Issues (must fix before publication)
1. [Location + issue + specific fix]
2. [Location + issue + specific fix]

### Recommended Improvements (this sprint)
1. [Issue with context]
2. [Issue with context]

### Nice-to-Have Polish (backlog)
1. [Minor enhancement]
2. [Minor enhancement]

### Summary
[2–3 sentences: Honest assessment. What is this document's biggest strength and weakness?]

---
```

---

## DOCUMENTATION STRUCTURE RULES

### Structure Rules by Document Type

```json
{
  "how-to": {
    "required": ["Overview", "Prerequisites", "Steps", "Result"],
    "optional": ["Troubleshooting", "Next steps", "Related"],
    "description": "Task-focused guide with sequential steps"
  },
  "reference": {
    "required": ["Description", "Parameters", "Response", "Errors"],
    "optional": ["Authentication", "Example", "Rate Limits", "Notes"],
    "description": "API or technical reference documentation"
  },
  "tutorial": {
    "required": ["Introduction", "Prerequisites", "Steps", "Summary"],
    "optional": ["Next steps", "Resources", "Troubleshooting"],
    "description": "Learning-oriented, hands-on guide"
  },
  "release-note": {
    "required": ["What's new", "Fixed"],
    "optional": ["Known issues", "Deprecated", "Breaking changes", "Upgrade guide"],
    "description": "Version release summary"
  },
  "concept": {
    "required": ["Definition", "Why it matters", "Key concepts", "How it works"],
    "optional": ["Examples", "Related concepts", "Best practices"],
    "description": "Explanation-focused conceptual guide"
  },
  "overview": {
    "required": ["Purpose", "Key features", "Scope", "Audience"],
    "optional": ["Architecture", "Components", "Quick start"],
    "description": "High-level introduction to system/module"
  }
}
```

### Required Sections Checklist

#### For API Documentation
- ✅ Endpoint description (what it does, when to use it)
- ✅ HTTP method and endpoint path (e.g., `POST /api/users`)
- ✅ Authentication (required method and scopes)
- ✅ Request parameters (name, type, required/optional, description)
- ✅ Response format (all fields with types and descriptions)
- ✅ Error codes (code, HTTP status, meaning, resolution)
- ✅ Rate limits (if applicable)
- ✅ Working example (request + response pair)

#### For How-To Guides
- ✅ Clear, specific title (verb-noun: "Create an API key")
- ✅ Overview (why someone would do this)
- ✅ Prerequisites (what's needed before starting)
- ✅ Sequential steps (numbered, action-oriented)
- ✅ Expected result (what success looks like)
- ✅ Troubleshooting (common issues + fixes)

#### For Concept Documentation
- ✅ Definition (what is it, in plain language)
- ✅ Why it matters (business/technical value)
- ✅ Key concepts (core ideas explained)
- ✅ How it works (mechanism or workflow)
- ✅ Real examples (concrete use cases)

---

## GENERATION PROMPTS FOR OVERVIEWS & CONCEPTS

### Generate Overview Prompt

```markdown
You are a technical documentation expert skilled at writing clear, accessible overviews for technical audiences.

Generate a comprehensive overview document for: [PRODUCT/SERVICE/MODULE]

Requirements:
1. Start with a one-line description that a non-expert can understand
2. Explain the purpose: What problem does it solve? Who should use it?
3. List 3-5 key features or capabilities
4. Define the scope: What's included? What's NOT included?
5. Identify the target audience (junior devs / experienced devs / architects / business users)
6. Include a quick orientation: "You'll use this by [common workflow]"
7. Point to next steps: "To get started, see [specific section]"

Tone: Professional, welcoming, avoiding jargon unless defined
Length: 200-400 words
Format: Markdown with clear headings

Structure:
## [Product Name] Overview

### What is [Product Name]?
[1-sentence definition]

### Why Use It?
[2-3 sentences about problems it solves]

### Key Features
- [Feature 1 with 1-sentence explanation]
- [Feature 2 with 1-sentence explanation]
- [Feature 3 with 1-sentence explanation]

### Who Should Read This?
[Target audience: "If you are a...")

### Scope
**Included:** [What's covered]
**Not included:** [What's deliberately excluded]

### Quick Orientation
[How it fits into the user's workflow]

### Next Steps
- To [common first task], see [section]
- To [common second task], see [section]
```

### Generate Concept Document Prompt

```markdown
You are a technical writer specializing in clear explanations of technical concepts for mixed-skill audiences.

Generate a concept explanation for: [CONCEPT/PATTERN/PRINCIPLE]

Requirements:
1. Start with a plain-language definition (a non-technical person should understand it)
2. Explain WHY it matters (business value, technical benefit, or problem it solves)
3. Break down the core components or steps (how does it actually work?)
4. Provide 2-3 concrete examples (from real scenarios, not abstract)
5. Show the relationship to related concepts (how does it fit into the bigger picture?)
6. Include best practices or common pitfalls
7. Suggest where to learn more (links to deeper docs)

Tone: Conversational, educational, avoiding condescension
Length: 300-500 words
Format: Markdown with clear sections

Structure:
## Understanding [Concept Name]

### Definition
[1-2 sentences: What is it? What's its core purpose?]

### Why This Matters
[2-3 sentences: Business value, technical benefit, or problem solved]

### How It Works
[Step-by-step breakdown of the mechanism or workflow]

1. [First component or step]
2. [Second component or step]
3. [Third component or step]

### Real-World Examples
**Example 1:** [Scenario from [domain]]
[How the concept applies in this scenario]

**Example 2:** [Scenario from [domain]]
[How the concept applies in this scenario]

### Related Concepts
- [Related concept 1]: [How it relates] (see also: [link])
- [Related concept 2]: [How it relates] (see also: [link])

### Best Practices
- [Practice 1 with brief explanation]
- [Practice 2 with brief explanation]

### Common Pitfalls to Avoid
- **[Pitfall 1]:** [Why it's a problem] → [How to avoid it]
- **[Pitfall 2]:** [Why it's a problem] → [How to avoid it]

### Learn More
- [Link to deeper concept]
- [Link to practical how-to]
```

---

## TASK TOPIC GENERATION FRAMEWORK

### Generate Task Topics Prompt

```markdown
You are a curriculum designer expert at breaking down complex work into clear, actionable learning tasks.

Generate task-based topics for: [TOPIC/DOMAIN/PROJECT]

Input context:
- Learning level: [Novice / Beginner / Intermediate / Advanced]
- Learner audience: [e.g., technical writers, developers, content designers]
- Time available: [e.g., 2 hours, 1 week]
- Prior knowledge: [e.g., "familiar with Git, new to LLMs"]

Requirements:
1. Break the topic into 5-8 concrete, achievable tasks
2. Each task should take 15-30 minutes to complete
3. Tasks should build progressively (learn before doing)
4. Each task must have a clear success criterion
5. Include at least one hands-on, "build something" task
6. Include at least one review or reflection task

Output format:

## Task Topics: [Main Topic]

### Task 1: [Action Verb + Object]
**Objective:** [What you'll be able to do]
**Time:** 15-20 min
**Prerequisites:** None

**What you'll do:**
[2-3 sentences describing the activity]

**Success criteria:**
- ✓ [Criterion 1 — observable outcome]
- ✓ [Criterion 2 — observable outcome]

**Resources:**
- [Link to guide/doc]
- [Link to example]

---

### Task 2: [Action Verb + Object]
[Same structure as Task 1]

---

[Continue for 5-8 tasks]

### Task Summary Table
| Task | Skills Practiced | Output | Time |
|------|-----------------|--------|------|
| Task 1 | [skill], [skill] | [deliverable] | 20 min |
| Task 2 | [skill], [skill] | [deliverable] | 20 min |
```

### Generate Learning Path Prompt

```markdown
You are an instructional designer expert at sequencing learning from simple to complex.

Create a learning path structure for: [SKILL/TOPIC]

Input context:
- Target audience: [e.g., technical writers with no AI experience]
- Total time: [e.g., 2 hours]
- End goal: [e.g., "write and publish a working Claude Skill"]
- Constraints: [e.g., "assumes no coding experience"]

Output format:

## Learning Path: [Topic Name]

### Path Overview
**Audience:** [Description of learner]
**Duration:** [Total time]
**Outcome:** [What learners will be able to do]

### Prerequisite Check
Before starting, you should be able to:
- [Prerequisite 1]
- [Prerequisite 2]

### Module Structure
| Module | Duration | Key Concept | Hands-On Activity | Outcome |
|--------|----------|------------|------------------|---------|
| 1 | 20 min | [Concept 1] | [Activity 1] | [Output 1] |
| 2 | 20 min | [Concept 2] | [Activity 2] | [Output 2] |
| 3 | 20 min | [Practice] | [Project] | [Portfolio item] |

### Detailed Module Breakdown

#### Module 1: [Title]
**Duration:** 20 min
**Objective:** [What you'll learn]

[Module content structure]

---

[Repeat for each module]
```

---

## QUALITY RULES & STANDARDS

### Terminology Standards (Inclusive Language)

Approved terminology to use:

| ❌ Avoid | ✅ Use Instead | Reason |
|---------|----------------|--------|
| whitelist | allowlist | Inclusive language standard |
| blacklist | blocklist | Inclusive language standard |
| master | primary | Inclusive language standard |
| slave | replica | Inclusive language standard |
| abort | cancel | Less alarming in user-facing copy |
| login (verb) | sign in | Use 'login' only as a noun |
| execute | run | Simpler verb for developer audiences |
| utilize | use | Simpler — rarely adds meaning |
| leverage | use | Business jargon — avoid |
| simply | [delete/rephrase] | Condescending |
| just | [delete/rephrase] | Assume confidence-checking |
| easy | [delete/rephrase] | Different for every reader |
| obviously | [delete] | Condescending |

### Writing Style Standards

**Voice & Tone:**
- ✅ Active voice (preferred): "You create a key" vs. "A key is created"
- ✅ Second person: "You can use..." vs. "One can use..."
- ✅ Present tense: "Click the button" vs. "You will click the button"
- ✅ Conversational, professional tone
- ❌ Passive voice, future tense, overly formal

**Sentence & Paragraph:**
- ✅ Maximum 25 words per sentence (flag violations)
- ✅ 1-3 sentences per paragraph (break up long blocks)
- ✅ Scannable with clear headings
- ✅ Bullet lists for 3+ related items

**Headings:**
- ✅ Sentence case ("Create an API key") not Title Case
- ✅ Action-oriented where possible ("Generate an overview")
- ✅ No terminal punctuation (no colons or periods)

**Code & Technical:**
- ✅ All code, commands, parameters in backticks: `npm install`
- ✅ File paths in backticks: `src/components/`
- ✅ Variable/placeholder names in ALL_CAPS: `YOUR_API_KEY`

**Lists:**
- ✅ Parallel structure: "Do X, Do Y, Do Z" (not "Do X, You should Y, Z is done")
- ✅ Consistent punctuation (either all periods or none)
- ✅ Single line or clear sub-bullets

### Content Completeness Checklist

For **API Documentation**:
- [ ] Endpoint HTTP method and path clearly shown
- [ ] Description of what the endpoint does
- [ ] Authentication requirements and scopes
- [ ] All request parameters (name, type, required, description)
- [ ] All response fields (name, type, description)
- [ ] Error codes with meanings and resolution steps
- [ ] Rate limit information (if applicable)
- [ ] At least one complete working example
- [ ] Warnings for breaking or unusual behavior

For **How-To Guides**:
- [ ] Specific, action-oriented title
- [ ] Who this is for and what they'll accomplish
- [ ] Prerequisites or setup required
- [ ] Numbered steps (not bullets for sequential actions)
- [ ] Expected result or success indicators
- [ ] Troubleshooting section for common issues
- [ ] Links to related tasks or concepts

For **Concept Documents**:
- [ ] Plain-language definition
- [ ] Why it matters (business or technical value)
- [ ] Core components clearly explained
- [ ] 2-3 real-world examples
- [ ] Relationship to related concepts
- [ ] Best practices and common pitfalls
- [ ] Links to deeper documentation

---

## SAMPLE TEMPLATES & EXAMPLES

### Sample API Documentation Template

```markdown
# [API Name / Endpoint] API Reference

## Overview
[1-2 sentences: What this API does and when to use it]

## Endpoint
```
METHOD /path/to/endpoint
```

## Description
[Clear explanation of what this endpoint does]

## Authentication
**Type:** [OAuth 2.0 / API Key / JWT / etc.]
**Required scopes:** [Scope 1, Scope 2]
**Header:** `Authorization: Bearer YOUR_TOKEN`

## Request

### Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `param1` | string | Yes | [Description] |
| `param2` | integer | No | [Description, default: X] |

### Example Request
```bash
curl -X POST https://api.example.com/path/to/endpoint \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"param1": "value1"}'
```

## Response

### Success Response
**Code:** 200 OK

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier |
| `status` | string | Current status [active/inactive] |
| `created_at` | ISO 8601 | Creation timestamp |

### Example Response
```json
{
  "id": "abc123",
  "status": "active",
  "created_at": "2024-07-06T10:00:00Z"
}
```

## Error Codes
| Code | Status | Meaning | Resolution |
|------|--------|---------|-----------|
| `INVALID_PARAM` | 400 | Parameter validation failed | Check parameter types and values |
| `UNAUTHORIZED` | 401 | Authentication failed or invalid | Verify your API token is valid |
| `RATE_LIMITED` | 429 | Too many requests | Wait before retrying |

## Rate Limits
- **Requests per minute:** 100
- **Requests per day:** 10,000
- **Reset time:** Midnight UTC

## Related Endpoints
- [Create resource](/docs/create-resource)
- [List resources](/docs/list-resources)
```

### Sample How-To Template

```markdown
# How to [Specific Task]

## Overview
[1-2 sentences about what you'll do and why]

**Time required:** 15 minutes
**Prior knowledge needed:** [Any prerequisites]

## Prerequisites
- [Prerequisite 1]
- [Prerequisite 2]
- [Access/tool requirement]

## Steps

### Step 1: [Action-oriented title]
[Specific instruction or context]

[If needed: screenshot or code example]

### Step 2: [Action-oriented title]
[Specific instruction]

### Step 3: [Action-oriented title]
[Specific instruction]

### Step 4: Verify your work
[What success should look like]

## Result
[1-2 sentences: What you've accomplished and what happens next]

## Troubleshooting

**Issue:** [Common problem]
**Solution:** [Step-by-step fix]

**Issue:** [Common problem]
**Solution:** [Step-by-step fix]

## Next Steps
- [Related task 1](/docs/...)
- [Related task 2](/docs/...)

## Related Resources
- [Concept guide](/docs/...)
- [API reference](/docs/...)
```

### Sample Concept Template

```markdown
# Understanding [Concept]

## What is [Concept]?
[1-2 sentences: Plain-language definition that anyone can understand]

## Why This Matters
[2-3 sentences explaining business value, technical benefit, or problems it solves]

This is important if you:
- [Scenario 1]
- [Scenario 2]
- [Scenario 3]

## How It Works

### Core Components
1. **[Component 1]:** [Explanation]
2. **[Component 2]:** [Explanation]
3. **[Component 3]:** [Explanation]

### The Workflow
[Step-by-step or diagrammatic explanation of how it operates]

## Real-World Examples

### Example 1: [Scenario]
[How the concept applies in this practical scenario]

**Outcome:** [What happens as a result]

### Example 2: [Scenario]
[How the concept applies]

**Outcome:** [What happens as a result]

## Related Concepts
- **[Related Concept 1]:** [Brief explanation of relationship] (see: [link])
- **[Related Concept 2]:** [Brief explanation of relationship] (see: [link])

## Best Practices
- **[Best practice 1]:** [Why it matters and how to do it]
- **[Best practice 2]:** [Why it matters and how to do it]
- **[Best practice 3]:** [Why it matters and how to do it]

## Common Pitfalls to Avoid
- **[Pitfall 1]:** [Why it's a problem] → **How to avoid it:** [Solution]
- **[Pitfall 2]:** [Why it's a problem] → **How to avoid it:** [Solution]

## Learn More
- Deeper dive: [Link to advanced guide]
- Practical guide: [Link to how-to]
- See also: [Link to related concept]
```

---

## PROMPT LIBRARY FOR SPECIFIC TASKS

### Generate Table of Contents for Documentation

```markdown
You are a documentation architect organizing content for clarity and discoverability.

Create a comprehensive table of contents for documentation about: [TOPIC]

Requirements:
1. Organize content hierarchically (3-4 levels max)
2. Include both conceptual (understanding) and task-based (doing) sections
3. Progress from simple to advanced
4. Use action verbs for task-based sections
5. Group related topics together logically
6. Ensure even distribution across sections

Output format:

## Table of Contents

### Getting Started
- What is [topic]? (concept)
- Why use [topic]? (value)
- [Quick start task] (task)

### Core Concepts
- Understanding [concept 1] (concept)
- Understanding [concept 2] (concept)

### How-To Guides
- How to [common task 1] (task)
- How to [common task 2] (task)

### Advanced Topics
- [Advanced concept] (concept)
- [Advanced task] (task)

### Reference
- API reference (reference)
- Configuration options (reference)
- Troubleshooting (reference)
```

### Generate FAQ Section

```markdown
You are a technical writer familiar with common user questions about: [TOPIC]

Generate an FAQ section addressing the most common questions.

Requirements:
1. Include 5-10 questions that real users ask
2. Group by topic if there are many questions
3. Start each question with real user language (not marketing speak)
4. Keep answers concise (1-3 sentences typically)
5. Link answers to longer documentation where appropriate
6. Progress from basic ("What is...?") to advanced ("How do I...?")

Output:
## Frequently Asked Questions

### Basics
**Q: [Question in plain language]**
A: [1-3 sentence answer with link to detailed docs if needed]

### [Topic]
**Q: [Question]**
A: [Answer]

[Continue grouping by topic]
```

### Generate Troubleshooting Guide

```markdown
You are a support specialist familiar with common issues in: [PRODUCT/SERVICE]

Generate a troubleshooting guide for: [PROBLEM AREA]

Requirements:
1. List 5-8 common issues users encounter
2. For each issue: symptom, root causes, solutions
3. Order by frequency (most common first)
4. Include diagnostic steps
5. Suggest when to escalate to support
6. Include preventive tips

Output format:

## Troubleshooting

### Issue: [Symptom users see]
**What's happening:** [Explanation of the problem]

**Possible causes:**
1. [Cause 1]
2. [Cause 2]

**Solutions:**
1. [Try this first] — [explanation]
2. [If that doesn't work] — [explanation]
3. [Advanced option] — [explanation]

**Prevention:** [How to avoid this in the future]

---

[Repeat for each issue]

### When to Contact Support
[Criteria for when self-service troubleshooting isn't enough]
```

---

## IMPLEMENTATION INSTRUCTIONS FOR COPILOT STUDIO

### Loading These Prompts into Your Agent

1. **Copy the RTCCO Framework** as a system prompt or knowledge base document
2. **Store Skill Templates** as reusable prompt templates in your knowledge base
3. **Load Structure Rules** as reference data or documents
4. **Store Generation Prompts** as callable templates with parameters
5. **Create Task Chains** that use multiple templates in sequence

### Prompt Parameter Configuration

For your Copilot Studio agent, configure these variables:

| Parameter | Usage | Example |
|-----------|-------|---------|
| `$ARGUMENTS` | Input file or content | `sample-docs/orders-api.md` |
| `$AUDIENCE` | Target reader level | `junior developers` |
| `$STYLE_GUIDE` | Documentation standard | `Google Developer Style Guide` |
| `$DOCUMENT_TYPE` | Type of content | `api-reference`, `how-to`, `concept` |
| `$TONE` | Desired voice | `professional`, `conversational`, `formal` |
| `$LENGTH` | Output length | `200-400 words` |

### Agent Configuration Example

```
Agent Name: Documentation Generator
Primary Role: Generate and review technical documentation

Knowledge Base includes:
- RTCCO Framework (core methodology)
- Skill Templates (6 reusable templates)
- Structure Rules (required sections per doc type)
- Terminology Standards (inclusive language guide)
- Quality Checklists (completeness requirements)

Callable Functions:
- generate_overview($TOPIC, $AUDIENCE)
- generate_concept($CONCEPT, $EXAMPLES_DOMAIN)
- generate_tasks($TOPIC, $LEVEL, $TIME)
- review_documentation($DOCUMENT, $DOCUMENT_TYPE)
- check_style_compliance($DOCUMENT)
- extract_gaps($CONTENT, $REQUIRED_STRUCTURE)

Conversation Flow:
1. User specifies document type and topic
2. Agent determines which template to use
3. Agent gathers necessary parameters
4. Agent generates content using appropriate prompt
5. Agent validates against quality checklist
6. Agent presents output and offers refinements
```

---

## QUICK REFERENCE FOR AGENT PROMPTING

### When User Wants to Generate Content

1. **Identify document type** (API reference, how-to, concept, overview, task list)
2. **Confirm audience** (junior dev, experienced engineer, business user)
3. **Determine scope** (time available, related topics)
4. **Select template** from this library
5. **Fill parameters** (topic, examples, constraints)
6. **Generate** using appropriate prompt
7. **Validate** against checklist
8. **Refine** based on feedback

### When User Wants to Review Content

1. **Identify document type**
2. **Select review template** (completeness, style, coverage)
3. **Generate review** using template prompt
4. **Present findings** in structured format
5. **Recommend improvements** with priority ranking
6. **Track status** (critical/high/medium/low)

### When User Wants to Define Learning Path

1. **Understand learner** (level, background, time)
2. **Define outcome** (what they should be able to do)
3. **Use learning path template**
4. **Break into tasks** (15-30 min chunks)
5. **Define success criteria** (observable outcomes)
6. **Present sequenced path** with progression

---

## ADDITIONAL RESOURCES

- **Full Training Materials:** `/TWTAI/modules/` contains lesson content for all modules
- **Sample Documentation:** `/TWTAI/sample-docs/` includes example API docs with seeded issues
- **Working Skill Examples:** `/TWTAI/skills/` contains production-ready skill files
- **Project Guidelines:** `/Project_guidelines.md` defines project team structure and requirements

---

**Document Version:** 1.0  
**Last Updated:** July 6, 2026  
**For:** Tech Writer's Tribe AI-Powered Documentation Mastery Program
