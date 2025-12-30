import os
import logging
from lxml import html, etree

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("formatter")

def format_site(site_dir="site"):
    """
    Format all HTML files in the site directory using lxml.
    """
    if not os.path.exists(site_dir):
        logger.warning(f"Site directory '{site_dir}' does not exist.")
        return

    logger.info(f"Formatting HTML in {site_dir} using lxml...")
    count = 0
    for root, dirs, files in os.walk(site_dir):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()

                    doc = html.fromstring(content)

                    # Clean up whitespace
                    for element in doc.iter():
                        if element.text and not element.text.strip():
                            element.text = None
                        if element.tail and not element.tail.strip():
                            element.tail = None

                    # Serialize with pretty_print=True
                    # method='html' ensures proper rendering of void tags
                    pretty_html = etree.tostring(doc, encoding="unicode", pretty_print=True, method="html")

                    with open(path, "w", encoding="utf-8") as f:
                        f.write("<!doctype html>\n" + pretty_html)

                    count += 1
                except Exception as e:
                    logger.warning(f"Failed to format {path}: {e}")

    logger.info(f"Formatted {count} HTML files.")

if __name__ == "__main__":
    format_site()
