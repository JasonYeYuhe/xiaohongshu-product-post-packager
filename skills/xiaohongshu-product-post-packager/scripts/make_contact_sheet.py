#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


SUPPORTED = {".png", ".jpg", ".jpeg", ".webp"}


def build_contact_sheet(input_dir: Path, output: Path, thumb_w: int = 240, thumb_h: int = 240, cols: int = 4) -> None:
    files = [p for p in sorted(input_dir.iterdir()) if p.suffix.lower() in SUPPORTED]
    if not files:
        raise SystemExit(f"No supported images found in {input_dir}")

    font = ImageFont.load_default()
    tile_w, tile_h = thumb_w + 20, thumb_h + 48
    rows = math.ceil(len(files) / cols)
    sheet = Image.new("RGB", (tile_w * cols, tile_h * rows), (245, 245, 245))

    for i, path in enumerate(files):
        image = Image.open(path).convert("RGB")
        original_size = image.size
        image.thumbnail((thumb_w, thumb_h), Image.LANCZOS)

        tile = Image.new("RGB", (tile_w, tile_h), "white")
        x = (tile_w - image.width) // 2
        y = 8
        tile.paste(image, (x, y))

        draw = ImageDraw.Draw(tile)
        draw.text((10, thumb_h + 14), path.name, fill="black", font=font)
        draw.text((10, thumb_h + 30), f"{original_size[0]}x{original_size[1]}", fill="black", font=font)

        sheet.paste(tile, ((i % cols) * tile_w, (i // cols) * tile_h))

    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a labeled contact sheet from a folder of screenshots.")
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--cols", type=int, default=4)
    parser.add_argument("--thumb-width", type=int, default=240)
    parser.add_argument("--thumb-height", type=int, default=240)
    args = parser.parse_args()

    build_contact_sheet(
        input_dir=args.input_dir,
        output=args.output,
        thumb_w=args.thumb_width,
        thumb_h=args.thumb_height,
        cols=args.cols,
    )


if __name__ == "__main__":
    main()
