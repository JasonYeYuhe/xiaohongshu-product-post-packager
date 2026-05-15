---
name: xiaohongshu-product-post-packager
description: Turn product screenshots, setup captures, official source links, and rough notes into a publish-ready Xiaohongshu post pack. Use when Codex needs to create or revise a Xiaohongshu carousel/tutorial post, verify product claims against current sources, screen inputs for sensitive data, write platform-appropriate Chinese copy, and deliver final images plus caption files.
---

# Xiaohongshu Product Post Packager

Build a post pack that is safe to publish, easy to skim, and already packaged for handoff.

## Workflow

1. **Read the room first.**
   - Inspect the available screenshots, rough copy, and any linked source material before deciding the post shape.
   - Identify the intended reader: beginners, power users, builders, buyers, or peers.
   - If the topic is current, niche, or the user cites an official page, verify the factual spine from current sources before writing.

2. **Audit every input image before using it.**
   - Create a contact sheet for fast review with `scripts/make_contact_sheet.py`.
   - Reject, redact, or avoid images containing secrets, credentials, QR codes intended for authentication, MFA / OTP codes, recovery codes, API keys, private email addresses, account identifiers, personal notifications, or anything that would be harmful if reposted.
   - If a screenshot is both useful and risky, prefer a safer neighboring screenshot over heroic editing.
   - Read `references/sensitive-data-checklist.md` when reviewing setup flows, login screens, dashboards, or mobile screenshots.

3. **Find the cleanest story, not the fullest dump.**
   - Default to a 6–8 card arc:
     1. Hook / cover
     2. Why it matters
     3. What it can do
     4. Setup step 1
     5. Setup step 2
     6. Setup step 3 or result
     7. Caveats / reminders
   - Prefer one idea per card.
   - Use exact UI screenshots where they teach; use text-only cards where screenshots would only add noise.
   - Read `references/carousel-patterns.md` when choosing the arc or caption tone.

4. **Write claims that can survive contact with reality.**
   - Keep the first line strong enough to stand alone in the feed.
   - Separate:
     - what is officially documented,
     - what the user personally observed,
     - what is inference or commentary.
   - Remove unsupported comparisons, speculative policy claims, or lines that create heat without helping the reader.
   - Prefer crisp caveats over footnote sludge: supported platforms, account requirements, admin requirements, rollout limits, and obvious failure cases.

5. **Produce a complete publish pack.**
   - Use Xiaohongshu-friendly portrait images unless the user requests another format; `1080x1440` is a strong default.
   - Deliver:
     - numbered final images in posting order,
     - `caption.txt`,
     - a short manifest or README describing the files,
     - a compressed archive when useful,
     - a contact sheet for quick review.
   - Keep filenames sortable and explicit, for example:
     - `01_cover.png`
     - `02_features.png`
     - `03_step1.png`

6. **Run final QA before handoff.**
   - Re-read the caption after the visuals exist; remove lines no card supports.
   - Check that every claim is either sourced, obviously descriptive, or clearly framed as opinion.
   - Confirm no sensitive screenshot survived into the final pack.
   - Confirm the first card works even if the user only sees it for one second.

## Output Standard

- Favor a restrained, editorial look over a noisy “template” look.
- Preserve the product UI; decorate around it rather than burying it.
- Keep typography large, sparse, and mobile-readable.
- If the user gives a rough caption, improve it without sanding away their voice.
- When there is a tension between completeness and publishability, choose publishability.

## Useful Bundled Resources

- `scripts/make_contact_sheet.py` — generate a labeled contact sheet from a folder of images for quick review.
- `references/sensitive-data-checklist.md` — inspect likely leak points before using screenshots.
- `references/carousel-patterns.md` — pick a strong post arc and concise caption pattern.

## Example Requests

- “我有一堆截图和一段草稿，帮我做成一套能直接发的小红书素材包。”
- “把这个新功能写成小红书教程，顺便检查截图里有没有不该发的东西。”
- “这是官方链接和产品图，帮我做一套 7 张轮播图加文案。”
