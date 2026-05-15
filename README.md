# Xiaohongshu Product Post Packager

Turn product screenshots, setup captures, official source links, and rough notes into a publish-ready Xiaohongshu post pack.

## What it helps with

- Verify current product claims before writing
- Screen screenshots for sensitive data before publishing
- Turn rough notes into a clean Xiaohongshu carousel arc
- Produce final images, caption copy, a manifest, and review artifacts

## Install in Codex

From a machine with Codex skills available, run:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo JasonYeYuhe/xiaohongshu-product-post-packager \
  --path skills/xiaohongshu-product-post-packager
```

Then restart Codex so it discovers the new skill.

## Example prompt

```text
Use xiaohongshu-product-post-packager to turn these screenshots, source links, and rough notes into a publish-ready Xiaohongshu carousel plus caption.
```

## Repository layout

```text
skills/
└── xiaohongshu-product-post-packager/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    └── scripts/
```
