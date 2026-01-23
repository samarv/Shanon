# Pitch Examples

Examples of well-shaped pitches with breadboards and proper structure.

---

## Example 1: Appointment Booking View

### Problem

Project coordinators need to book client meetings but can't easily see which time slots are available across a two-month horizon. Currently they flip between calendar views and email threads, often double-booking or missing optimal slots. They need to see availability at a glance and book in under 2 minutes.

### Appetite

6 weeks - This is a core workflow improvement affecting 80% of daily coordinator tasks.

### Solution

A dedicated appointment view with two synchronized panels: a two-month dot grid showing availability density, and a sliding agenda showing details for the selected day.

Tapping any day on the dot grid reveals that day's appointments in the agenda. Empty days show prominent "Book Now" affordance. Booked days show the appointment list with quick-edit capability.

No new data entry flows - this uses existing booking infrastructure.

### Breadboard

```
[Appointments View]
    |
    ├── [2-Month Dot Grid]
    |       • Green dot = available
    |       • Yellow dot = partial
    |       • Red dot = full
    |       └── tap day → updates [Agenda Panel]
    |
    └── [Agenda Panel]
            • Shows selected day's appointments
            • Empty state → [Book Now] button
            • Appointment row → tap → [Quick Edit Sheet]
                                    └── tap → [Full Appointment Detail]
```

### Fat Marker Sketch

```
┌─────────────────────────────────┐
│  ← Jan 2026 →  │  ← Feb 2026 →  │
│  ● ● ○ ● ● ● ○ │  ○ ● ● ● ○ ○ ● │
│  ● ○ ● ● ○ ● ● │  ● ● ○ ● ● ● ○ │
│  ...            │  ...            │
├─────────────────────────────────┤
│  Thursday, Jan 15                │
│  ┌───────────────────────────┐  │
│  │ 9:00  Client A - Review   │  │
│  │ 11:00 Client B - Kickoff  │  │
│  │ 2:00  [Available]         │  │
│  └───────────────────────────┘  │
│        [+ Book Appointment]      │
└─────────────────────────────────┘
```

### Rabbit Holes

| Rabbit Hole | Risk | Mitigation |
|-------------|------|------------|
| Calendar sync complexity | Could require real-time sync with external calendars | Scope to internal appointments only; external sync is future work |
| Performance with many appointments | 2-month view could be slow with dense data | Engineer confirmed: pagination + lazy load handles this |
| Recurring appointments | Display logic gets complex | Show as individual instances; no recurring UI in this cycle |

### No-Gos

- External calendar integration (Google, Outlook)
- Recurring appointment creation
- Multi-user availability comparison
- Mobile-optimized view (desktop only this cycle)

### Nice-to-Haves

- Color-coding by appointment type
- Drag-to-reschedule
- Week view toggle

---

## Example 2: Status Update Templates

### Problem

Team leads spend 2+ hours each Friday compiling status updates by copying content from various sources into email. They lose formatting, forget sections, and the output is inconsistent. They need to produce professional, consistent updates in under 30 minutes.

### Appetite

2 weeks - Small scope, high-frequency pain point.

### Solution

A template picker with 3 pre-built status formats. User selects template, fills in sections using a guided form, and exports to formatted email or PDF.

No rich text editor - just structured fields that output clean formatting.

### Breadboard

```
[Status Updates] (entry point)
    |
    └── [Template Picker]
            • "Weekly Team Update"
            • "Project Milestone"
            • "Executive Summary"
            │
            └── select → [Template Form]
                            • Section 1: [Key Wins] - textarea
                            • Section 2: [Blockers] - bullet list input
                            • Section 3: [Next Week] - textarea
                            │
                            └── [Preview] ←→ [Edit]
                                    │
                                    └── [Export]
                                            • Copy to clipboard
                                            • Download PDF
```

### Rabbit Holes

| Rabbit Hole | Risk | Mitigation |
|-------------|------|------------|
| Template customization | Users will want to edit templates | Out of scope - 3 fixed templates only |
| Rich text in fields | Markdown/formatting adds complexity | Plain text with auto-formatting on export |
| Saved drafts | Storage and state management | No drafts - form state persists only during session |

### No-Gos

- Custom template creation
- Rich text editing
- Draft saving/auto-save
- Team template sharing

### Nice-to-Haves

- Pre-fill from last week's update
- Direct email send (vs. copy to clipboard)

---

## Breadboard Notation Guide

| Element | Represents | Example |
|---------|------------|---------|
| `[Name]` | A place (screen, dialog, panel) | `[Dashboard]` |
| `• item` | An affordance (button, field, link) | `• [Save] button` |
| `→` | Navigation/flow | `tap → [Detail View]` |
| `├──` / `└──` | Hierarchy/containment | Shows what's inside a place |
| `←→` | Toggle/switch between states | `[Preview] ←→ [Edit]` |

## What Makes These Good

1. **Bounded scope** - Explicit no-gos prevent scope creep
2. **Engineering-validated** - Rabbit holes show technical feasibility was checked
3. **Logic over UI** - Breadboards show flow, not pixel-perfect layouts
4. **Flexible finish line** - Nice-to-haves give the team dials to turn
5. **Standalone comprehension** - A reader understands "the whole idea" without additional context
