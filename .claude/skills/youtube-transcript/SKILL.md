---
name: youtube-transcript
description: Download YouTube transcripts using yt-dlp. Outputs markdown with timestamps (default) or VTT. Use when extracting subtitles/captions from YouTube for analysis or reference.
---

# YouTube Transcript Downloader

## Quick Start

```bash
# Download transcript (markdown with timestamps)
python scripts/download_transcript.py "https://youtube.com/watch?v=VIDEO_ID"

# Output: VideoTitle.en.md
```

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `--lang LANG` | `en` | Language code |
| `--format {md,vtt}` | `md` | Output format |
| `--output-dir DIR` | `.` | Output directory |
| `--auto-only` | - | Auto-generated subs only |
| `--list` | - | List available subtitles |
| `--check-setup` | - | Verify environment |

## Examples

```bash
# List available subtitles
python scripts/download_transcript.py "URL" --list

# Download VTT format
python scripts/download_transcript.py "URL" --format vtt

# Spanish transcript to specific folder
python scripts/download_transcript.py "URL" --lang es --output-dir ./transcripts
```

## Output Formats

**Markdown (default):**
```markdown
# Transcript

**[00:00:00]** Hello everyone and welcome back.

**[00:00:03]** Today we'll be discussing...
```

**VTT:**
```
WEBVTT

00:00:00.000 --> 00:00:03.500
Hello everyone and welcome back.
```

## Setup

```bash
# Check environment
python scripts/download_transcript.py --check-setup

# Install yt-dlp
brew install yt-dlp    # macOS
pip install yt-dlp     # in venv
```
