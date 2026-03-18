# Ad Copy Skill Pack (6 languages) for Claude Code

Generate, audit, and refresh responsive search ad copy — 10 skills for Claude Code.
Works with Google Ads Editor CSV format. Multilingual (EN, DE, FR, ES, AR, PL).

Inspired by [how Anthropic's growth team uses Claude Code for ad creation](https://claude.com/blog/how-anthropic-uses-claude-marketing).

---

## Quick Start (5 minutes)

### 1. Install Claude Code

**macOS / Linux (native installer — recommended):**
```bash
curl -fsSL https://claude.ai/install.sh | sh
```

**macOS (Homebrew):**
```bash
brew install claude-code
```

**Windows:**
```powershell
winget install Anthropic.ClaudeCode
```

> Requires a Claude Pro ($20/mo), Max ($100/mo), Team, or Enterprise plan.
> The free plan does not include Claude Code access.

### 2. Authenticate
```bash
claude
```
Your browser will open — sign in with your Anthropic account.

### 3. Clone this project
```bash
cd ~/Projects
git clone https://github.com/marek-kujda/ad-copy-skill-pack.git   # or unpack the archive
cd ad-copy-skill-pack
```

### 4. Configure brand voice, ICP, and landing pages

> **Can't see the `.claude/` folder?** It's hidden by default on all operating systems.
>
> | OS      | How to reveal                                                        |
> |---------|----------------------------------------------------------------------|
> | macOS   | In Finder press `Cmd + Shift + .` to toggle hidden files             |
> | Windows | In File Explorer → View → Show → Hidden items                        |
> | Linux   | In your file manager press `Ctrl + H`, or use `ls -a` in terminal    |

**Option A: Auto-setup from your website (recommended)**
```bash
claude
```
Then type:
```
/auto-setup
```
Provide your website URL(s) and Claude will analyze your site and pre-fill brand voice, ICP, and landing pages automatically. Review the drafts and confirm.

**Option B: Manual setup**
Edit these three files — replace all `[bracketed]` placeholders:
- `.claude/skills/brand-voice/SKILL.md` — your tone, USPs, CTAs
- `.claude/skills/icp/SKILL.md` — ideal customer profile and buyer personas
- `.claude/skills/landing-pages/SKILL.md` — register your landing page URLs so you don't have to paste them every time

See `examples/` for filled-in references.

### 5. Generate ads
```bash
claude
```
Then type:
```
/ads
```
Claude will ask for campaign details and produce a ready-to-upload CSV.

---

## Project Structure

```
google-ads-rsa-generator/
├── CLAUDE.md                                    # Project memory — RSA rules, quality checks
├── LICENSE                                      # CC BY-NC-SA 4.0
├── README.md                                    # This file
├── .claude/
│   └── skills/
│       ├── ads/                                 # /ads command
│       │   ├── SKILL.md                         #   Skill definition + workflow
│       │   ├── template.csv                     #   Google Ads Editor CSV template
│       │   └── validate.py                      #   Character limit validator
│       ├── ads-batch/                           # /ads-batch command
│       │   └── SKILL.md                         #   Bulk generation workflow
│       ├── ads-multi/                           # /ads-multi command
│       │   └── SKILL.md                         #   Multilingual generation (2+ languages)
│       ├── ads-review/                          # /ads-review command
│       │   └── SKILL.md                         #   Audit existing RSA copy
│       ├── ads-refresh/                         # /ads-refresh command
│       │   └── SKILL.md                         #   Refresh stale copy (ad fatigue)
│       ├── sitelinks/                           # /sitelinks command
│       │   └── SKILL.md                         #   Sitelink extensions generator
│       ├── brand-voice/                         # Brand guidelines
│       │   └── SKILL.md                         #   ⚠️ EDIT THIS before first use
│       ├── icp/                                 # Target audience
│       │   └── SKILL.md                         #   ⚠️ EDIT THIS — ICP + buyer personas
│       ├── landing-pages/                       # URL registry
│       │   └── SKILL.md                         #   ⚠️ EDIT THIS — add your URLs
│       ├── auto-setup/                          # /auto-setup command
│       │   └── SKILL.md                         #   Bootstrap context from website URLs
│       └── google-ads-rules/                    # Platform rules
│           └── SKILL.md                         #   Char limits, DKI, CSV format
├── examples/
│   ├── brand-voice-example-saas.md              # Filled-in brand voice example
│   └── icp-example-saas.md                      # Filled-in ICP + personas example
└── output/                                      # Generated CSVs land here
```

### Why `.claude/skills/` instead of `.claude/commands/`?

Skills are the current Claude Code standard. They work exactly like slash commands but can bundle supporting files (CSV templates, validation scripts) alongside the prompt. Your existing `.claude/commands/` files still work — skills are a superset.

---

## Usage

### First-time setup
```
/auto-setup
```
Provide your website URL(s). Claude analyzes your site and generates brand voice, ICP, and landing pages automatically. Review and confirm — then you're ready to generate ads.

### Single ad group
```
/ads
```
Claude will ask for: campaign, ad group, keywords, landing page URL, USPs.

### Multiple ad groups at once
```
/ads-batch
```
Provide a list of ad groups with keywords — get a single CSV with all of them.

### Multiple languages from one brief
```
/ads-multi
```
Provide your brief once, pick languages (e.g., EN, DE, FR, ES, AR, PL). Claude generates native copy per language — not translations — and lets you choose between separate CSVs per language or one combined file.

### Audit existing ads
```
/ads-review
```
Paste or upload your current RSA copy. Claude scores it, flags duplicate concepts, missing keywords, weak descriptions, and suggests concrete replacements.

### Refresh stale copy
```
/ads-refresh
```
Combat ad fatigue. Provide your current copy and optional performance data. Choose light (swap 3–5 weakest), medium (~50% replaced), or full refresh (keep only proven winners). Claude preserves what works and replaces what doesn't.

### Generate sitelink extensions
```
/sitelinks
```
Generate 4–8 sitelinks mapped to the buyer journey. Claude pulls URLs from the landing pages registry, creates titles (≤25 chars) and descriptions (≤35 chars each), and exports a CSV ready for Google Ads Editor. Works with the same language-aware URL resolution as `/ads-multi`.

### Iterating on copy
After generation, refine in natural language:
- `change headline #7 to a stronger CTA`
- `add more social proof in descriptions`
- `generate a German version of this ad group`
- `headlines 3 and 8 are too similar — diversify`

### Validating output
```bash
python .claude/skills/ads/validate.py output/rsa_campaign_adgroup_20260314.csv
```

---

## Pro Tips

1. **Start with brand voice** — the better your tone and USP description, the better the output.
2. **Provide a landing page URL** — Claude will analyze the page and align messaging.
3. **Iterate, don't accept first drafts** — as Austin Lau from Anthropic puts it: the real work is in the riffing.
4. **Test across languages** — German compound nouns, French articles, and Polish declensions eat into the 30-char limit. Arabic needs RTL review. Spanish and English are typically the easiest to fit.
5. **Add your own skills** — create `.claude/skills/meta-ads/SKILL.md` or `.claude/skills/linkedin-ads/SKILL.md` to extend the toolkit.

---

## Extending

### Add a new skill
Create a folder in `.claude/skills/[name]/` with a `SKILL.md` file inside. Claude Code will automatically recognize `/name` as a new command. Add supporting files (scripts, templates) in the same folder.

### Landing page analysis
Instead of pasting URLs every time, register them once in `.claude/skills/landing-pages/SKILL.md`. Claude analyzes each page on first use and caches the results. On subsequent runs, just say `landing page: pricing` and Claude uses the cached analysis — no re-fetching, no wasted tokens. Say `refresh landing page: pricing` after a page redesign to update the cache.

### Figma Ad Creative Generator
Pair this skill pack with the [Ad Creative Generator](https://github.com/marek-kujda/ad-creative-generator) to complete the pipeline: generate copy here → apply it to Figma templates → export display ad variations.

### Google Ads API integration (advanced)
For automated CSV upload, consider:
- An MCP server for Google Ads (e.g., Adspirer or custom)
- A Zapier / n8n webhook to auto-import the CSV

---

## Requirements

**For Claude Code (terminal):**
- Claude Code (native installer or npm)
- Claude Pro, Max, Team, or Enterprise plan
- macOS, Linux, or Windows (with Git for Windows)
- Internet connection

**For claude.ai (web/desktop app):**
- Claude Pro, Max, Team, or Enterprise plan
- Code execution enabled in Settings → Capabilities
- See `INSTALL.md` in the claude.ai package for setup instructions

---

## License

This project is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

**You can:** use, modify, and build on this project — for free.

**You must:** give credit (link to the original), indicate changes, and share modifications under the same license.

**You cannot:** use it commercially (sell it, bundle it in paid courses, or offer it as a service).

Author: Marek Kujda — [linkedin.com/in/marekkujda](https://www.linkedin.com/in/marekkujda/)

---

## Disclaimer

This skill pack is provided "as is" without warranty of any kind. The author is not responsible for ad copy that violates platform policies, account suspensions, revenue losses, or inaccurate outputs. All AI-generated copy should be reviewed by a human before uploading to any advertising platform. See LICENSE for full terms.
