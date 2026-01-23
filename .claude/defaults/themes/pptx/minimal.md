# Minimal Theme

A clean, professional theme with no brand-specific elements.

## Color Palette

| Color | Name | Hex | Usage |
|-------|------|-----|-------|
| ⬛ | Black | `#1a1a1a` | Primary text, dark backgrounds |
| ⬜ | White | `#FFFFFF` | Light backgrounds, text on dark |
| 🩶 | Gray | `#6b7280` | Secondary text, subtle elements |
| 🔵 | Accent | `#3b82f6` | Links, highlights, call-to-action |

## Typography

```css
font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
```

### Hierarchy
- **Headlines**: Bold, 32-48pt
- **Subheads**: Medium, 18-24pt
- **Body text**: Regular, 14-16pt
- **Captions**: Regular, 10-12pt, Gray

## Design Principles

- Clean, minimal layouts
- Strong contrast (black/white)
- No decorative elements
- Generous white space
- Left-aligned content

## Slide Patterns

### Title Slide
- Background: White
- Headline: Black, centered
- Subtitle: Gray

### Content Slide
- Background: White
- Headlines: Black
- Body text: Dark gray
- Accent color for emphasis

## CSS Variables

```css
:root {
  --minimal-black: #1a1a1a;
  --minimal-white: #FFFFFF;
  --minimal-gray: #6b7280;
  --minimal-accent: #3b82f6;
  --minimal-font: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
```

## PptxGenJS Color Values

```javascript
const MINIMAL = {
  BLACK: '1a1a1a',
  WHITE: 'FFFFFF',
  GRAY: '6b7280',
  ACCENT: '3b82f6'
};
```
