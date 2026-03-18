# Ad Copy Skill Pack (6 languages) — Claude Code Project

> License: CC BY-NC-SA 4.0 · Author: Marek Kujda · See LICENSE file for details

## Purpose
Generate high-quality Responsive Search Ad (RSA) copy for Google Ads campaigns.
Output: CSV files ready for direct upload to Google Ads Editor.

## RSA Specifications (Google Ads Requirements)
- **Headlines**: Up to 15 per ad group (required: min 3, recommended: 15)
  - Max 30 characters each (including spaces)
  - At least 1 must contain the primary keyword
  - No excessive punctuation or ALL CAPS
- **Descriptions**: Up to 4 per ad group (required: min 2, recommended: 4)
  - Max 90 characters each (including spaces)
  - At least 1 must contain a CTA
- **Display URL paths**: 2 fields, max 15 characters each

## Quality Rules
1. Every headline and description MUST respect character limits — validate before output
2. Never repeat the same concept across headlines — each must offer a unique angle
3. Mix headline types: benefit-driven, feature-driven, keyword-rich, CTA, social proof, urgency
4. Include dynamic keyword insertion {KeyWord:Default} where appropriate
5. Descriptions should complement headlines, not repeat them
6. Use sentence case (not Title Case) unless brand name requires it
7. Avoid generic filler ("best", "top", "leading") unless backed by specifics
8. Every ad must have at least 2 headlines containing the exact target keyword or close variant

## Headline Angle Categories (aim for diversity)
- **Keyword match**: Contains exact target keyword
- **Benefit**: What the user gains
- **Feature**: Product/service capability
- **CTA**: Direct action ("Get", "Try", "Start", "Request")
- **Social proof**: Numbers, testimonials, awards
- **Urgency/Scarcity**: Time-limited offers
- **Question**: Engages curiosity
- **Differentiator**: What makes this offer unique

## Skills
- `.claude/skills/ads/` — main `/ads` command + CSV template + validation script
- `.claude/skills/ads-batch/` — bulk generation for multiple ad groups
- `.claude/skills/ads-multi/` — multilingual generation (2+ languages from one brief)
- `.claude/skills/ads-review/` — audit existing RSA copy with scoring and replacement suggestions
- `.claude/skills/ads-refresh/` — refresh stale copy to combat ad fatigue (light / medium / full)
- `.claude/skills/sitelinks/` — generate sitelink extensions with buyer-journey mapping
- `.claude/skills/brand-voice/` — brand tone, USPs, CTAs (⚠️ edit before first use)
- `.claude/skills/icp/` — ideal customer profile + buyer personas (⚠️ edit before first use)
- `.claude/skills/landing-pages/` — URL registry with cached page analysis (⚠️ edit before first use)
- `.claude/skills/google-ads-rules/` — platform specs, character limits, DKI syntax
- `.claude/skills/auto-setup/` — bootstrap brand voice, ICP, and landing pages from website URLs

## Output
All output goes to `output/` directory as CSV files compatible with Google Ads Editor.
After generating, run validation: `python .claude/skills/ads/validate.py output/<file>.csv`

## Workflow
1. User provides: campaign name, ad group, target keywords, landing page URL, USP/offers
2. Claude loads brand-voice and google-ads-rules skills automatically
3. Claude analyzes the landing page (if URL provided) and keywords
4. Claude generates 15 headlines + 4 descriptions per ad group
5. Claude validates all character limits
6. Claude outputs CSV to `output/` directory
7. User reviews and refines through conversation

## Important
- Always count characters BEFORE presenting output
- Flag any headline >30 chars or description >90 chars
- When in doubt, shorter is better — Google truncates without warning
- Polish language ads: ą, ę, ł etc. = 1 char each

## First Run Detection
If brand-voice, ICP, or landing-pages skills still contain `[bracketed]` placeholder text, the user hasn't configured them yet. Before running any ad generation command, mention: "It looks like brand voice and ICP haven't been set up yet. Run /auto-setup with your website URL to configure them automatically, or edit the files manually." Do this once — don't repeat on every message.
