#!/usr/bin/env python3
"""
Download YouTube transcripts using yt-dlp. Outputs markdown (default) or VTT.

Usage:
    download_transcript.py <url> [--lang LANG] [--format FORMAT] [--output-dir DIR]
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


def is_in_virtualenv() -> bool:
    """Check if running inside a virtual environment."""
    return (
        hasattr(sys, "real_prefix")
        or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
        or os.environ.get("VIRTUAL_ENV") is not None
    )


def find_existing_venv() -> str | None:
    """Look for existing venv in common locations."""
    cwd = Path.cwd()
    for name in ["venv", ".venv", "env", ".env"]:
        venv_path = cwd / name
        if venv_path.is_dir() and (venv_path / "pyvenv.cfg").exists():
            return str(venv_path)
    return None


def check_setup() -> bool:
    """Check environment and show setup guidance."""
    print("=" * 50)
    print("ENVIRONMENT CHECK")
    print("=" * 50 + "\n")
    
    # Check venv
    if is_in_virtualenv():
        print(f"✅ Virtual environment: {os.environ.get('VIRTUAL_ENV', sys.prefix)}")
    else:
        existing = find_existing_venv()
        if existing:
            print(f"⚠️  Found venv at: {existing}")
            print(f"   Activate with: source {existing}/bin/activate")
        else:
            print("⚠️  No virtual environment detected.")
            print("   Create with: python3 -m venv venv && source venv/bin/activate")
        print()
    
    # Check yt-dlp
    try:
        result = subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
        print(f"✅ yt-dlp installed: {result.stdout.decode().strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ yt-dlp not installed.")
        print("\nInstall with:")
        print("   brew install yt-dlp     # macOS")
        print("   pip install yt-dlp      # in venv")
        return False


def vtt_to_markdown(vtt_path: Path) -> str:
    """Convert VTT to clean markdown with timestamps."""
    content = vtt_path.read_text()
    lines = content.split('\n')
    
    # Parse VTT entries
    entries = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Match timestamp line: 00:00:00.000 --> 00:00:02.869
        if '-->' in line:
            timestamp_match = re.match(r'(\d{2}:\d{2}:\d{2})\.\d{3}\s*-->', line)
            if timestamp_match:
                start_time = timestamp_match.group(1)
                # Get text lines until empty line
                text_lines = []
                i += 1
                while i < len(lines) and lines[i].strip():
                    # Remove VTT formatting tags like <00:00:00.240><c>
                    clean_line = re.sub(r'<[^>]+>', '', lines[i])
                    clean_line = clean_line.strip()
                    if clean_line:
                        text_lines.append(clean_line)
                    i += 1
                if text_lines:
                    # Take last line (most complete version for rolling captions)
                    entries.append((start_time, text_lines[-1]))
        i += 1
    
    # Deduplicate consecutive identical texts
    deduped = []
    for ts, text in entries:
        if not deduped or deduped[-1][1] != text:
            deduped.append((ts, text))
    
    # Format as markdown
    md_lines = ["# Transcript\n"]
    for ts, text in deduped:
        md_lines.append(f"**[{ts}]** {text}\n")
    
    return '\n'.join(md_lines)


def download_transcript(url: str, lang: str = "en", output_dir: str = ".",
                        fmt: str = "md", auto_only: bool = False) -> int:
    """Download transcript from YouTube video."""
    output_path = Path(output_dir).resolve()
    output_path.mkdir(parents=True, exist_ok=True)

    cmd = [
        "yt-dlp", "--skip-download", "--sub-format", "vtt", "--sub-langs", lang,
        "-o", str(output_path / "%(title)s.%(ext)s"), url,
    ]
    if auto_only:
        cmd.insert(2, "--write-auto-subs")
    else:
        cmd.insert(2, "--write-subs")
        cmd.insert(3, "--write-auto-subs")

    print(f"Downloading: {url} (lang={lang}, format={fmt})\n")
    result = subprocess.run(cmd)

    if result.returncode != 0:
        return result.returncode

    # Find downloaded VTT
    vtt_files = list(output_path.glob(f"*.{lang}.vtt")) or list(output_path.glob("*.vtt"))
    if not vtt_files:
        print("❌ No transcript found")
        return 1

    vtt_path = vtt_files[-1]
    
    if fmt == "md":
        # Convert to markdown
        md_content = vtt_to_markdown(vtt_path)
        md_path = vtt_path.with_suffix('.md')
        md_path.write_text(md_content)
        vtt_path.unlink()  # Remove VTT
        print(f"\n✅ Saved: {md_path}")
    else:
        print(f"\n✅ Saved: {vtt_path}")

    return 0


def list_subtitles(url: str) -> int:
    """List available subtitles."""
    return subprocess.run(["yt-dlp", "--list-subs", url]).returncode


def main():
    parser = argparse.ArgumentParser(description="Download YouTube transcripts")
    parser.add_argument("url", nargs="?", help="YouTube URL")
    parser.add_argument("--lang", default="en", help="Language code (default: en)")
    parser.add_argument("--format", choices=["md", "vtt"], default="md",
                        help="Output format (default: md)")
    parser.add_argument("--output-dir", default=".", help="Output directory")
    parser.add_argument("--auto-only", action="store_true", help="Auto-generated only")
    parser.add_argument("--list", action="store_true", dest="list_subs", help="List subtitles")
    parser.add_argument("--check-setup", action="store_true", help="Check environment")
    args = parser.parse_args()

    if args.check_setup or args.url is None:
        ok = check_setup()
        print("\n" + "=" * 50)
        print("✅ Ready!" if ok else "⚠️  Complete setup above.")
        print("=" * 50)
        if args.url is None:
            print("\nUsage: python download_transcript.py <URL>")
        sys.exit(0 if ok else 1)

    # Check yt-dlp silently
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ yt-dlp not installed. Run --check-setup for help.")
        sys.exit(1)

    if args.list_subs:
        sys.exit(list_subtitles(args.url))
    
    sys.exit(download_transcript(args.url, args.lang, args.output_dir,
                                  args.format, args.auto_only))


if __name__ == "__main__":
    main()
