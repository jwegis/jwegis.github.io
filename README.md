# John Wegis

Personal website of John Wegis.

## 🛠️ Technology

This site is built using:
*   [Zensical](https://zensical.org) - Static site generator
*   [uv](https://github.com/astral-sh/uv) - Python package manager
*   Python 3.14+

## 🚀 Getting Started

### Prerequisites

Ensure you have `uv` installed:
```bash
pip install uv
```

### Installation

Install dependencies:
```bash
uv sync
```

### Local Development

Start the local development server:
```bash
zensical serve
```
Visit `http://localhost:8000` to preview changes.

## 🏗️ Building & Formatting

**Important:** This project uses a custom build script to ensure HTML is properly formatted (compact, pretty-printed).

**Do not run `zensical build` directly.** Instead, run:

```bash
uv run python scripts/build.py
```

This script performs two steps:
1.  Runs `zensical build --clean`.
2.  Runs `scripts/format.py` to post-process the HTML files in `site/`.

## 🎨 Customization

*   **Favicon**: Located at `docs/assets/images/favicon.svg` (Project-level configuration in `zensical.toml`).
*   **Formatting**: The HTML formatter logic is in `scripts/format.py` (uses `lxml`).
