# SaaS Project Management Tool - Opportunity Solution Tree

## Outcome
Increase trial-to-paid conversion from 12% to 18% by Q2

## Visual Tree

```mermaid
graph TD
    Outcome["<b>OUTCOME</b><br/>Increase trial-to-paid conversion<br/>from 12% to 18% by Q2"]

    %% Phase 1: Sign-up & First Session
    O1["<b>OPPORTUNITY 1.1</b><br/>I don't know what to do first after signing up<br/><i>High confidence: 9/12 users</i>"]
    S1_1["<b>Solution 1.1.1</b><br/>Interactive onboarding tour<br/>Status: Testing"]
    S1_2["<b>Solution 1.1.2</b><br/>Pre-populated demo project<br/>Status: Idea"]
    S1_3["<b>Solution 1.1.3</b><br/>Quick-win first task<br/>Status: Idea"]
    T1["<b>TEST</b><br/>A/B test onboarding tour<br/>200 users, 60% completion target"]

    %% Phase 2: Setup & Configuration
    O2["<b>OPPORTUNITY 2.1</b><br/>I can't import my existing work from other tools<br/><i>Medium confidence: 5/12 users</i>"]
    S2_1["<b>Solution 2.1.1</b><br/>CSV import<br/>Status: Validated via fake door"]
    S2_2["<b>Solution 2.1.2</b><br/>Direct integrations<br/>Status: Testing"]
    S2_3["<b>Solution 2.1.3</b><br/>Manual migration assistant<br/>Status: Idea"]
    T2["<b>TEST</b><br/>Fake door: 67% clicked Import<br/>Survey: Which tools to integrate"]

    %% Phase 3: Daily Task Management
    O3["<b>OPPORTUNITY 3.1</b><br/>I can't see all my tasks across projects in one view<br/><i>High confidence: 10/12 users</i>"]
    O3_1["<b>SUB-OPPORTUNITY 3.1.1</b><br/>I can't tell which tasks are most urgent<br/><i>Medium confidence: 3/12 users</i>"]

    S3_1["<b>Solution 3.1.1</b><br/>Master task list view<br/>Status: Shipped - Low adoption"]
    S3_2["<b>Solution 3.1.2</b><br/>Smart 'Today' view<br/>Status: Testing"]
    S3_3["<b>Solution 3.1.3</b><br/>Customizable dashboard<br/>Status: Idea"]
    S3_4["<b>Solution 3.1.4</b><br/>Search-first interface<br/>Status: Idea"]

    T3["<b>TEST</b><br/>Smart Today prototype with 10 users<br/>Measure task completion from view"]
    L3["<b>LEARNING</b><br/>Master list too overwhelming<br/>Validates need for prioritization"]

    %% Connections
    Outcome --> O1
    Outcome --> O2
    Outcome --> O3

    O1 --> S1_1
    O1 --> S1_2
    O1 --> S1_3
    S1_1 --> T1

    O2 --> S2_1
    O2 --> S2_2
    O2 --> S2_3
    S2_1 --> T2
    S2_2 --> T2

    O3 --> O3_1
    O3 --> S3_1
    O3 --> S3_2
    O3 --> S3_3
    O3 --> S3_4
    S3_1 --> L3
    S3_2 --> T3
    L3 --> S3_2

    %% Styling
    classDef outcomeStyle fill:#FFD700,stroke:#FF8C00,stroke-width:3px,color:#000
    classDef oppStyle fill:#87CEEB,stroke:#4682B4,stroke-width:2px,color:#000
    classDef subOppStyle fill:#B0E0E6,stroke:#4682B4,stroke-width:2px,color:#000
    classDef solutionStyle fill:#98FB98,stroke:#228B22,stroke-width:2px,color:#000
    classDef testStyle fill:#FFB6C1,stroke:#DC143C,stroke-width:2px,color:#000
    classDef learningStyle fill:#DDA0DD,stroke:#8B008B,stroke-width:2px,color:#000

    class Outcome outcomeStyle
    class O1,O2,O3 oppStyle
    class O3_1 subOppStyle
    class S1_1,S1_2,S1_3,S2_1,S2_2,S2_3,S3_1,S3_2,S3_3,S3_4 solutionStyle
    class T1,T2,T3 testStyle
    class L3 learningStyle
```

## Legend

- **Gold** - Outcome (root goal)
- **Sky Blue** - Opportunities (customer needs)
- **Light Blue** - Sub-opportunities (decomposed needs)
- **Green** - Solutions (multiple approaches per opportunity)
- **Pink** - Active Tests (validation experiments)
- **Purple** - Learnings (insights from tests)

## Experience Map Phases

1. **Sign-up & First Session**
2. **Setup & Configuration**
3. **Daily Task Management**
4. **Team Collaboration**
5. **Progress Tracking**
