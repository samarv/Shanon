#!/usr/bin/env python3
"""
Markdown to PDF Converter

Converts Markdown files to professional PDF documents using WeasyPrint.
Runs in sandbox environment with no subprocess calls.

Usage:
    python convert_md_to_pdf.py input.md output.pdf [options]

Options:
    --css PATH          Custom CSS file path
    --page-size SIZE    Page size: a4, letter, legal (default: a4)
    --margin SIZE       Page margin (default: 2.5cm)
    --title TEXT        Document title for header
    --no-toc            Disable table of contents
    --no-header         Disable page header
    --no-footer         Disable page footer
    --allow-remote      Allow remote images (URLs)
    --debug             Output intermediate HTML for debugging
"""

import argparse
import os
import sys
from pathlib import Path
from datetime import datetime

# Third-party imports (require pip install)
try:
    import markdown
    from markdown.extensions.toc import TocExtension
except ImportError:
    print("Error: 'markdown' package not installed.")
    print("Run: pip install markdown")
    sys.exit(1)

try:
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration
except ImportError:
    print("Error: 'weasyprint' package not installed.")
    print("Run: pip install weasyprint")
    print("On macOS, you may also need: brew install pango")
    sys.exit(1)


class MarkdownToPDF:
    """Converts Markdown to PDF with customizable styling."""

    # Page size presets (width, height in mm)
    PAGE_SIZES = {
        'a4': (210, 297),
        'letter': (216, 279),
        'legal': (216, 356),
        'a3': (297, 420),
        'a5': (148, 210),
    }

    def __init__(
        self,
        css_path: str = None,
        page_size: str = 'a4',
        margin: str = '2.5cm',
        title: str = None,
        show_toc: bool = True,
        show_header: bool = True,
        show_footer: bool = True,
        allow_remote: bool = False,
        debug: bool = False,
    ):
        self.css_path = css_path
        self.page_size = page_size.lower()
        self.margin = margin
        self.title = title
        self.show_toc = show_toc
        self.show_header = show_header
        self.show_footer = show_footer
        self.allow_remote = allow_remote
        self.debug = debug
        self.font_config = FontConfiguration()

        # Validate page size
        if self.page_size not in self.PAGE_SIZES:
            print(f"Warning: Unknown page size '{page_size}', using 'a4'")
            self.page_size = 'a4'

    def _get_markdown_extensions(self) -> list:
        """Configure Markdown extensions for rich formatting."""
        extensions = [
            'extra',           # Tables, fenced code, footnotes, etc.
            'codehilite',      # Syntax highlighting
            'meta',            # YAML metadata support
            'sane_lists',      # Better list handling
            'smarty',          # Smart quotes
            'nl2br',           # Newlines to <br>
        ]

        if self.show_toc:
            extensions.append(TocExtension(
                baselevel=1,
                toc_depth=3,
                title='Table of Contents',
                anchorlink=True,
            ))

        return extensions

    def _get_extension_configs(self) -> dict:
        """Configure Markdown extension settings."""
        return {
            'codehilite': {
                'css_class': 'code-highlight',
                'linenums': False,
                'guess_lang': True,
            },
        }

    def _build_page_css(self) -> str:
        """Generate CSS for page layout and headers/footers."""
        width, height = self.PAGE_SIZES[self.page_size]

        css_parts = [f"""
@page {{
    size: {width}mm {height}mm;
    margin: {self.margin};
"""]

        if self.show_header:
            title_text = self.title if self.title else ''
            css_parts.append(f"""
    @top-left {{
        content: "{title_text}";
        font-size: 9pt;
        color: #666666;
    }}
    @top-right {{
        content: "{datetime.now().strftime('%Y-%m-%d')}";
        font-size: 9pt;
        color: #666666;
    }}
""")

        if self.show_footer:
            css_parts.append("""
    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-size: 9pt;
        color: #666666;
    }
""")

        css_parts.append("}")

        return ''.join(css_parts)

    def _get_default_css(self) -> str:
        """Return default document styling."""
        return """
/* Base Typography */
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #1a1a1a;
    max-width: 100%;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    line-height: 1.3;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
    page-break-after: avoid;
}

h1 {
    font-size: 24pt;
    color: #1D91D0;
    border-bottom: 2px solid #1D91D0;
    padding-bottom: 0.3em;
    page-break-before: always;
}

h1:first-of-type {
    page-break-before: avoid;
}

h2 {
    font-size: 18pt;
    color: #333333;
    border-bottom: 1px solid #dddddd;
    padding-bottom: 0.2em;
}

h3 {
    font-size: 14pt;
    color: #444444;
}

h4 {
    font-size: 12pt;
    color: #555555;
}

/* Paragraphs */
p {
    margin: 0.8em 0;
    orphans: 3;
    widows: 3;
}

/* Links */
a {
    color: #1D91D0;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* Lists */
ul, ol {
    margin: 0.5em 0;
    padding-left: 2em;
}

li {
    margin: 0.3em 0;
}

/* Nested lists */
li > ul, li > ol {
    margin: 0.2em 0;
}

/* Task lists */
li.task-list-item {
    list-style-type: none;
    margin-left: -1.5em;
}

li.task-list-item input {
    margin-right: 0.5em;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
    font-size: 10pt;
    page-break-inside: avoid;
}

th, td {
    border: 1px solid #dddddd;
    padding: 8px 12px;
    text-align: left;
}

th {
    background-color: #f5f5f5;
    font-weight: 600;
    color: #333333;
}

tr:nth-child(even) {
    background-color: #fafafa;
}

/* Code */
code {
    font-family: 'SF Mono', 'Monaco', 'Inconsolata', 'Fira Mono', monospace;
    font-size: 9pt;
    background-color: #f5f5f5;
    padding: 0.2em 0.4em;
    border-radius: 3px;
}

pre {
    background-color: #f5f5f5;
    padding: 1em;
    border-radius: 5px;
    overflow-x: auto;
    font-size: 9pt;
    line-height: 1.4;
    page-break-inside: avoid;
}

pre code {
    background: none;
    padding: 0;
}

/* Code highlighting */
.code-highlight {
    background-color: #f5f5f5;
}

/* Blockquotes */
blockquote {
    border-left: 4px solid #1D91D0;
    margin: 1em 0;
    padding: 0.5em 1em;
    background-color: #f8f9fa;
    color: #555555;
    font-style: italic;
}

blockquote p {
    margin: 0.3em 0;
}

/* Horizontal rules */
hr {
    border: none;
    border-top: 2px solid #eeeeee;
    margin: 2em 0;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1em auto;
}

/* Footnotes */
.footnote {
    font-size: 9pt;
    color: #666666;
}

/* Table of Contents */
.toc {
    background-color: #f8f9fa;
    border: 1px solid #e0e0e0;
    border-radius: 5px;
    padding: 1em 1.5em;
    margin: 1em 0;
}

.toc ul {
    list-style-type: none;
    padding-left: 1em;
}

.toc > ul {
    padding-left: 0;
}

.toc a {
    color: #333333;
    text-decoration: none;
}

.toc a:hover {
    color: #1D91D0;
}

/* Emphasis */
strong, b {
    font-weight: 600;
}

em, i {
    font-style: italic;
}

/* Definition lists */
dl {
    margin: 1em 0;
}

dt {
    font-weight: 600;
    margin-top: 0.5em;
}

dd {
    margin-left: 2em;
    margin-bottom: 0.5em;
}

/* Print optimizations */
@media print {
    body {
        font-size: 10pt;
    }

    h1, h2, h3, h4, h5, h6 {
        page-break-after: avoid;
    }

    table, pre, blockquote {
        page-break-inside: avoid;
    }

    img {
        page-break-inside: avoid;
        page-break-before: auto;
        page-break-after: auto;
    }
}
"""

    def _load_custom_css(self, css_path: str) -> str:
        """Load custom CSS from file."""
        css_file = Path(css_path)
        if not css_file.exists():
            print(f"Warning: CSS file not found: {css_path}")
            return ""
        return css_file.read_text(encoding='utf-8')

    def _wrap_html(self, content: str) -> str:
        """Wrap HTML content in a complete document."""
        title = self.title or "Document"
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>
{content}
</body>
</html>
"""

    def convert_string(
        self,
        markdown_text: str,
        output_path: str,
        title: str = None,
        base_path: str = None,
    ) -> dict:
        """
        Convert Markdown string to PDF.

        Args:
            markdown_text: Markdown content as string
            output_path: Path for output PDF file
            title: Optional document title (overrides instance title)
            base_path: Base path for resolving relative image paths

        Returns:
            dict with status, pages, file_size, etc.
        """
        if title:
            self.title = title

        # Convert Markdown to HTML
        md = markdown.Markdown(
            extensions=self._get_markdown_extensions(),
            extension_configs=self._get_extension_configs(),
        )
        html_content = md.convert(markdown_text)

        # Extract title from metadata if available
        if hasattr(md, 'Meta') and 'title' in md.Meta:
            if not self.title:
                self.title = md.Meta['title'][0]

        # Wrap in HTML document
        full_html = self._wrap_html(html_content)

        if self.debug:
            debug_path = Path(output_path).with_suffix('.debug.html')
            debug_path.write_text(full_html, encoding='utf-8')
            print(f"Debug HTML written to: {debug_path}")

        # Build CSS
        css_parts = [
            self._build_page_css(),
            self._get_default_css(),
        ]

        if self.css_path:
            custom_css = self._load_custom_css(self.css_path)
            if custom_css:
                css_parts.append(custom_css)

        combined_css = '\n'.join(css_parts)

        # Generate PDF
        html_doc = HTML(
            string=full_html,
            base_url=base_path or str(Path.cwd()),
        )
        css_doc = CSS(string=combined_css, font_config=self.font_config)

        # Determine URL fetcher based on allow_remote setting
        if not self.allow_remote:
            def url_fetcher(url):
                """Block remote URLs for security."""
                if url.startswith(('http://', 'https://')):
                    print(f"Warning: Blocked remote URL: {url}")
                    print("Use --allow-remote to enable remote images")
                    return {'string': b'', 'mime_type': 'image/png'}
                # Use default fetcher for local files
                from weasyprint import default_url_fetcher
                return default_url_fetcher(url)
        else:
            url_fetcher = None  # Use default

        # Write PDF
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        doc = html_doc.render(stylesheets=[css_doc], font_config=self.font_config)
        doc.write_pdf(str(output_file))

        # Get file info
        file_size = output_file.stat().st_size
        page_count = len(doc.pages)

        return {
            'status': 'success',
            'output_path': str(output_file),
            'pages': page_count,
            'file_size_bytes': file_size,
            'file_size_kb': round(file_size / 1024, 1),
        }

    def convert_file(
        self,
        input_path: str,
        output_path: str,
        title: str = None,
    ) -> dict:
        """
        Convert Markdown file to PDF.

        Args:
            input_path: Path to input Markdown file
            output_path: Path for output PDF file
            title: Optional document title

        Returns:
            dict with status, pages, file_size, etc.
        """
        input_file = Path(input_path)

        if not input_file.exists():
            return {
                'status': 'error',
                'error': f"Input file not found: {input_path}",
            }

        if not input_file.suffix.lower() in ['.md', '.markdown', '.txt']:
            print(f"Warning: Input file may not be Markdown: {input_file.suffix}")

        # Read input file
        markdown_text = input_file.read_text(encoding='utf-8')

        # Use filename as title if not provided
        if not title and not self.title:
            title = input_file.stem.replace('-', ' ').replace('_', ' ').title()

        # Convert with base_path set to input file's directory (for images)
        return self.convert_string(
            markdown_text=markdown_text,
            output_path=output_path,
            title=title,
            base_path=str(input_file.parent),
        )


def main():
    """Main entry point for CLI usage."""
    parser = argparse.ArgumentParser(
        description='Convert Markdown to PDF',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Basic conversion:
    python convert_md_to_pdf.py document.md output.pdf

  With custom CSS:
    python convert_md_to_pdf.py document.md output.pdf --css custom.css

  Letter size with title:
    python convert_md_to_pdf.py document.md output.pdf --page-size letter --title "My Document"
        """,
    )

    parser.add_argument('input', help='Input Markdown file path')
    parser.add_argument('output', help='Output PDF file path')
    parser.add_argument('--css', help='Custom CSS file path')
    parser.add_argument(
        '--page-size',
        default='a4',
        choices=['a4', 'letter', 'legal', 'a3', 'a5'],
        help='Page size (default: a4)',
    )
    parser.add_argument('--margin', default='2.5cm', help='Page margin (default: 2.5cm)')
    parser.add_argument('--title', help='Document title for header')
    parser.add_argument('--no-toc', action='store_true', help='Disable table of contents')
    parser.add_argument('--no-header', action='store_true', help='Disable page header')
    parser.add_argument('--no-footer', action='store_true', help='Disable page footer')
    parser.add_argument('--allow-remote', action='store_true', help='Allow remote images')
    parser.add_argument('--debug', action='store_true', help='Output intermediate HTML')

    args = parser.parse_args()

    # Create converter
    converter = MarkdownToPDF(
        css_path=args.css,
        page_size=args.page_size,
        margin=args.margin,
        title=args.title,
        show_toc=not args.no_toc,
        show_header=not args.no_header,
        show_footer=not args.no_footer,
        allow_remote=args.allow_remote,
        debug=args.debug,
    )

    # Convert
    print(f"Converting: {args.input}")
    result = converter.convert_file(args.input, args.output)

    if result['status'] == 'success':
        print(f"\n✓ PDF Generated Successfully")
        print(f"  Output: {result['output_path']}")
        print(f"  Pages:  {result['pages']}")
        print(f"  Size:   {result['file_size_kb']} KB")
    else:
        print(f"\n✗ Conversion Failed")
        print(f"  Error: {result.get('error', 'Unknown error')}")
        sys.exit(1)


if __name__ == '__main__':
    main()
