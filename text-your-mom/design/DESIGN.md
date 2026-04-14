# Design System Strategy: The Digital Living Room

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Digital Living Room."** 

In a world of rigid, clinical B2C interfaces, this system rejects the "app-as-a-tool" mentality. Instead, it treats the interface as an extension of the home—warm, textured, and inherently comfortable. We move beyond standard UI by embracing **Soft Asymmetry** and **Tonal Depth**. By avoiding harsh lines and utilizing a "stacked paper" metaphor, we create an environment where family connections feel organic rather than transactional. The experience is defined by "breathing room," editorial pacing, and a tactile quality that invites touch.

---

## 2. Color & Atmosphere
Our palette is rooted in sunset warmth, sky clarity, and botanical softness. It is designed to feel "lived-in" and comforting.

### The "No-Line" Rule
To achieve a premium, high-end feel, **do not use 1px solid borders to define sections.** Boundaries must be created through background color shifts. For instance, a profile card should not have a stroke; it should be a `surface-container-lowest` element resting on a `surface-container-low` background.

### Surface Hierarchy & Nesting
Treat the UI as a physical landscape. Use the surface-container tiers to create an "interior architecture":
- **Base Layer:** `surface` (#fff8f4) – The expansive, warm canvas.
- **Sectioning:** `surface-container-low` (#fff1e6) – Used for broad content groupings.
- **Interactive Cards:** `surface-container-lowest` (#ffffff) – The "top" layer, providing maximum contrast and perceived lift.
- **Callouts:** `surface-container-highest` (#ffddba) – For high-importance information that needs "weight."

### The "Glass & Gradient" Rule
Standard flat colors feel static. To inject "soul":
- **Floating Navigation:** Use Glassmorphism. Apply `surface-bright` at 80% opacity with a `backdrop-blur` of 20px.
- **Hero Transitions:** Utilize subtle linear gradients from `primary` (#914d00) to `primary-container` (#ffaf6d) to create a sense of glowing, natural light.

---

## 3. Typography: The Editorial Voice
We utilize a two-font system to balance modern precision with a personal, approachable touch.

*   **Display & Headlines (Plus Jakarta Sans):** This is our "Modern Voice." Its geometric yet rounded forms feel professional but kind. Use `display-lg` and `headline-md` with generous tracking (-1%) to create a sophisticated, editorial header style.
*   **Body & Labels (Be Vietnam Pro):** This is our "Personal Voice." It is highly legible at small sizes. The rounded terminals mirror the friendly nature of the app while ensuring that long-form family updates are easy to digest.

**Hierarchy Tip:** Use `on-surface-variant` (#7e5728) for secondary body text. It maintains warmth while providing enough contrast for accessibility, avoiding the "coldness" of pure grey.

---

## 4. Elevation & Depth
Depth in this system is achieved through light and layering, never through heavy shadows.

### The Layering Principle
Stacking is our primary tool. A common pattern:
1.  **Background:** `surface`
2.  **Parent Container:** `surface-container`
3.  **Content Card:** `surface-container-lowest` (This creates a "natural lift" via value shifts).

### Ambient Shadows
When a physical "float" is required (e.g., a Floating Action Button), use an **Ambient Shadow**:
- **X: 0, Y: 8px, Blur: 24px**
- **Color:** `on-surface` (#4b2b00) at **6% opacity**. 
This mimics natural sunlight falling on a soft surface rather than a digital drop-shadow.

### The "Ghost Border" Fallback
If contrast is needed for accessibility in complex lists, use a **Ghost Border**:
- `outline-variant` (#daa972) at **15% opacity**. It should be felt, not seen.

---

## 5. Components

### Buttons
- **Primary:** `primary` (#914d00) background with `on-primary` (#fff7f4) text. Use a `lg` (2rem) corner radius. For a premium touch, add a subtle inner shadow (1px) to give a "pressed" tactile feel.
- **Secondary:** `secondary-container` (#b7eaff) background. This introduces the "gentle blue" to signify supporting actions.
- **Tertiary:** No background. Use `primary` text with a `sm` (0.5rem) radius on the hover state.

### Cards & Lists
- **The Rule:** No divider lines. Separate list items using `md` (1.5rem) vertical spacing or by nesting them in `surface-container-low` rounded boxes.
- **Card Shape:** Use the `md` (1.5rem) or `lg` (2rem) corner radius. The large radius communicates the "soft and friendly" brand promise.

### Input Fields
- **Container:** `surface-container-highest` with a 10% opacity `outline`. 
- **States:** On focus, transition the background to `surface-container-lowest` and increase the ghost border opacity to 40% using the `primary` color.

### Signature Component: The "Memory Thread"
A custom vertical timeline component that uses a `secondary-fixed-dim` (#8ce0ff) stroke-based line (2px, dashed) to connect family updates, ending in a `tertiary` (#006d42) "bloom" icon to represent growth.

---

## 6. Do’s and Don’ts

### Do:
- **Embrace Asymmetry:** Align text to the left but allow images to "break the grid" with varying border radii (e.g., top-left 3rem, bottom-right 1rem).
- **Use Tonal Overlays:** When placing text over images, use a `surface-dim` tint at 20% to keep the warmth consistent.
- **Prioritize Negative Space:** If a screen feels "busy," increase the spacing between containers rather than adding borders.

### Don’t:
- **No Pure Black/Grey:** Never use #000000 or neutral greys. Every "dark" tone must be a deep brown (`on-surface`) to maintain the "Warm" prompt requirements.
- **No Sharp Corners:** Avoid the `none` or `sm` roundedness tokens for major containers. Sharp corners break the "approachable" psychology.
- **No High-Contrast Dividers:** Avoid `outline` (#9d7240) at 100% opacity; it creates a "cage" effect that feels restrictive for a family app.