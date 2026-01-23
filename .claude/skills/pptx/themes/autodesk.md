# Autodesk Brand Theme

Official Autodesk brand guidelines for presentation design.

**Source:** [Autodesk Brand Hub](https://brand.autodesk.com)

---

## Color Palette

### Primary Colors (Always Lead)

| Color | Name | Hex | RGB | Usage |
|-------|------|-----|-----|-------|
| ⬛ | Autodesk Black | `#000000` | (0, 0, 0) | Primary text, dark backgrounds |
| ⬜ | Autodesk White | `#FFFFFF` | (255, 255, 255) | Light backgrounds, text on dark |
| 🟨 | Hello Yellow | `#FFFF00` | (255, 255, 0) | Highlight, accent, reveal moments |

**Rules:**
- Autodesk Black and White should always be used as-is (no tints)
- Hello Yellow is the signature accent—use sparingly for impact
- Tints of Hello Yellow are allowed, but pure yellow should be predominant

### Secondary Colors (For Hierarchy)

| Color | Name | Hex | RGB | Usage |
|-------|------|-----|-----|-------|
| 🩶 | Warm Slate | `#D5D5CB` | (213, 213, 203) | Subtle backgrounds, secondary elements |
| ⬜ | Slate | `#666666` | (102, 102, 102) | Body text, secondary text |

**Use when:**
- Size contrast isn't enough to establish text hierarchy
- Chart values need differentiation or gradation
- Complex information needs visual organization

### Tertiary Colors (Functional Only)

| Color | Name | Hex | RGB | Usage |
|-------|------|-----|-----|-------|
| 🟠 | Dawn | `#F09D4F` | (240, 157, 79) | Status, emphasis, warnings |
| 🔴 | Dusk | `#F2520A` | (242, 82, 10) | Alerts, critical actions |
| 🔵 | Twilight | `#1D91D0` | (29, 145, 208) | Feature callouts, links, info |
| 🟢 | Morning | `#2AD0A9` | (42, 208, 169) | Success states, positive indicators |

**Rules:**
- Use for functional purposes only (status, emphasis, action needed)
- In presentations, can highlight key points/features/actions
- Never compete with or appear as primary brand colors

---

## Typography

### Font Stack
```css
font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
```

### Web-Safe Alternatives
- **Primary:** Arial, Helvetica
- **Fallback:** sans-serif

### Hierarchy Guidelines
- **Headlines:** Bold, large (32-48pt)
- **Subheads:** Regular or medium weight (18-24pt)
- **Body text:** Regular weight (12-16pt)
- **Captions:** Regular weight (10-12pt), Slate color

---

## Design Principles

### Premium Authenticity
- Clean, confident layouts
- Strong contrast (black/white)
- Minimal decoration
- Purposeful use of color

### Visual Style
- Bold typography with clear hierarchy
- Geometric shapes over organic forms
- High-contrast color combinations
- Generous white space

### Layout Patterns
- Left-aligned content with clear structure
- Accent bars (4-8pt) for visual interest
- Grid-based layouts
- Consistent margins (40-50pt)

---

## CSS Variables for HTML Slides

```css
:root {
  /* Primary */
  --adsk-black: #000000;
  --adsk-white: #FFFFFF;
  --adsk-yellow: #FFFF00;
  
  /* Secondary */
  --adsk-warm-slate: #D5D5CB;
  --adsk-slate: #666666;
  
  /* Tertiary */
  --adsk-dawn: #F09D4F;
  --adsk-dusk: #F2520A;
  --adsk-twilight: #1D91D0;
  --adsk-morning: #2AD0A9;
  
  /* Typography */
  --adsk-font: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
```

---

## PptxGenJS Color Values

**Important:** PptxGenJS requires hex colors **without** the `#` prefix.

```javascript
const AUTODESK = {
  // Primary
  BLACK: '000000',
  WHITE: 'FFFFFF',
  YELLOW: 'FFFF00',
  
  // Secondary
  WARM_SLATE: 'D5D5CB',
  SLATE: '666666',
  
  // Tertiary
  DAWN: 'F09D4F',
  DUSK: 'F2520A',
  TWILIGHT: '1D91D0',
  MORNING: '2AD0A9'
};
```

---

## Slide Patterns

### Title Slide (Dark)
- Background: Autodesk Black
- Headline: Autodesk White
- Accent word: Hello Yellow
- Top accent bar: Hello Yellow (8pt)
- Logo: Autodesk White, bottom right

### Content Slide (Light)
- Background: Autodesk White
- Headlines: Autodesk Black
- Body text: Slate
- Left accent bar: Hello Yellow or Twilight (6-8pt)
- Icons/bullets: Tertiary colors

### Feature Highlight Slide
- Background: Autodesk Black
- Headlines: Autodesk White
- Feature icons: Tertiary colors (Dawn, Twilight, Morning)
- Badges/tags: Morning with Black text

### CTA Slide
- Background: Autodesk Black
- Headline: White with Yellow highlight
- Button: Hello Yellow with Black text
- Bottom accent line: Hello Yellow

---

## Accessibility Notes

Autodesk brand colors are selected for inclusive viewing:
- Black/White: Maximum contrast (21:1)
- Yellow on Black: High contrast for visibility
- Avoid Yellow text on White (low contrast)
- Use Slate (#666666) for secondary text, not lighter grays

---

## Example HTML Slide Structure

```html
<!DOCTYPE html>
<html>
<head>
<style>
html { background: #000000; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 0;
  background: #000000;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  display: flex;
}
.accent-bar { height: 8pt; background: #FFFF00; }
h1 { color: #FFFFFF; font-size: 36pt; font-weight: bold; }
.highlight { color: #FFFF00; }
p { color: #D5D5CB; font-size: 16pt; }
</style>
</head>
<body>
<div class="accent-bar"></div>
<div class="content">
  <h1>Headline with <span class="highlight">Yellow</span> accent</h1>
  <p>Body text in Warm Slate color</p>
</div>
</body>
</html>
```

---

*Last updated: January 2026*
*Based on: brand.autodesk.com*
