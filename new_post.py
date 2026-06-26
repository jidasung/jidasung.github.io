#!/usr/bin/env python3
"""Create a new Jekyll post skeleton.

Usage:
    python new_post.py "My Post Title"
    python new_post.py "My Post Title" --category "AI Projects" --tags ai retrospective

Creates `_posts/YYYY-MM-DD-my-post-title.md` with a ready-to-edit YAML
front matter block that matches this blog's theme.
"""

import argparse
import datetime
import re
import sys
import unicodedata
from pathlib import Path

POSTS_DIR = Path(__file__).resolve().parent / "_posts"

# Default categories mirror the interests configured in _config.yml.
DEFAULT_CATEGORIES = ["AI Projects", "OMSCS", "Scuba Diving"]


def slugify(title: str) -> str:
    """Turn a title into a URL/filename-friendly slug.

    Keeps Unicode word characters (so Korean titles survive) and collapses
    everything else into single hyphens.
    """
    # Normalize so composed/decomposed Unicode compares consistently.
    value = unicodedata.normalize("NFC", title).strip().lower()
    # Replace any run of non-word characters (keeping unicode letters) with "-".
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s_-]+", "-", value, flags=re.UNICODE)
    return value.strip("-")


def build_front_matter(title: str, category: str, tags: list[str], date: datetime.datetime) -> str:
    tag_line = "[" + ", ".join(tags) + "]" if tags else "[]"
    return (
        "---\n"
        f'title: "{title}"\n'
        f"date: {date:%Y-%m-%d %H:%M:%S %z}\n"
        f"categories: {category}\n"
        f"tags: {tag_line}\n"
        'description: ""\n'
        "# img: post-image.jpg   # optional cover image in /assets/img\n"
        "---\n\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new Jekyll post.")
    parser.add_argument("title", help="The post title (wrap in quotes).")
    parser.add_argument(
        "--category",
        default=DEFAULT_CATEGORIES[0],
        help=f"Post category (default: {DEFAULT_CATEGORIES[0]!r}).",
    )
    parser.add_argument(
        "--tags",
        nargs="*",
        default=[],
        help="Optional space-separated tags.",
    )
    args = parser.parse_args()

    title = args.title.strip()
    if not title:
        print("Error: title must not be empty.", file=sys.stderr)
        return 1

    # Local time, including the UTC offset so Jekyll orders posts correctly.
    now = datetime.datetime.now().astimezone()
    slug = slugify(title)
    if not slug:
        print("Error: title produced an empty slug.", file=sys.stderr)
        return 1

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"{now:%Y-%m-%d}-{slug}.md"
    path = POSTS_DIR / filename

    if path.exists():
        print(f"Error: {path} already exists. Aborting.", file=sys.stderr)
        return 1

    body = f"# {title}\n\nStart writing here...\n"
    path.write_text(build_front_matter(title, args.category, args.tags, now) + body, encoding="utf-8")

    print(f"Created {path.relative_to(POSTS_DIR.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
