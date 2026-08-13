# Fuji Recipe Settings Reference

Everything here is written against current-generation X-Trans bodies (the X-E5's generation). Menu names and exact step increments can shift slightly across firmware/generations — treat the ranges below as "typical," and defer to what the user's actual menu shows if there's a conflict.

## Table of contents
- [Film Simulation](#film-simulation)
- [Grain Effect](#grain-effect)
- [Color Chrome Effect](#color-chrome-effect)
- [Color Chrome FX Blue](#color-chrome-fx-blue)
- [White Balance & WB Shift](#white-balance--wb-shift)
- [Dynamic Range](#dynamic-range)
- [Highlight Tone / Shadow Tone](#highlight-tone--shadow-tone)
- [Color (Saturation)](#color-saturation)
- [Sharpness](#sharpness)
- [High ISO NR](#high-iso-nr)
- [Clarity](#clarity)
- [ISO](#iso)
- [Exposure Compensation](#exposure-compensation)
- [X-E5 hardware notes](#x-e5-hardware-notes)
- [Symptom → dial diagnostic table](#symptom--dial-diagnostic-table)
- [Starter recipes](#starter-recipes)

---

## Film Simulation

The base "film stock" the rest of the recipe builds on top of — it sets the overall color palette, contrast curve, and general character before any other setting is applied. Twenty modes are available across current bodies:

- **PROVIA/Standard** — neutral, balanced baseline. Good default to build a recipe on top of.
- **Velvia/Vivid** — high saturation and contrast; punchy, saturated look, less forgiving of skin tones.
- **ASTIA/Soft** — softer contrast, gentle color, flattering for portraits and skin.
- **Classic Chrome** — desaturated, muted, slightly cool with deep-but-not-crushed shadows; a very common recipe base for a "documentary" or "reportage" feel.
- **PRO Neg. Hi / PRO Neg. Std** — designed for studio/portrait work; Hi has a touch more contrast than Std, both render skin gently.
- **Classic Neg.** — modeled on consumer print film; higher contrast with a distinctive shifted color palette (often described as slightly cyan-green shadows, warm highlights), grittier feel.
- **Nostalgic Neg.** — modeled on a warm American New Color-era look; warm highlights, muted shadow color.
- **Eterna/Cinema** — very flat, low-contrast, desaturated cinema-film emulation. Excellent base for a recipe you plan to grade further (in-camera or in post).
- **Eterna Bleach Bypass** — high contrast, heavily desaturated, gritty — emulates the bleach-bypass film process.
- **ACROS** (No filter / Ye / R / G) — Fuji's premium black-and-white sim; deep blacks, fine tonal separation, subtle grain structure baked into the algorithm itself. The Ye/R/G suffix is a simulated contrast filter (Yellow = mild sky/skin contrast, Red = dramatic sky darkening, Green = skin smoothing/foliage separation).
- **Monochrome** (No filter / Ye / R / G) — a simpler B&W sim than ACROS, flatter tonal response, same filter logic.
- **Sepia** — monochrome with a warm sepia tint baked in.
- **Reala Ace** — newer, high-fidelity sim aimed at accurate, naturalistic color with punchy-but-controlled contrast; a strong PROVIA alternative when you want realism with a bit more bite.

## Grain Effect

Adds simulated film grain to the JPEG. Two axes:
- **Strength:** Off / Weak / Strong.
- **Size:** Small / Large (only selectable once strength is Weak or Strong).

Grain is more visible in flat, evenly-lit midtone areas and in shadows; it can look overdone stacked on top of genuine high-ISO sensor noise, so recipes meant for low light often use a weaker grain setting than recipes meant for bright, low-ISO daylight.

## Color Chrome Effect

Deepens saturation and adds extra gradation specifically in areas that are already highly saturated — most visible in reds/oranges (sunsets, skin, brick, autumn leaves). Off / Weak / Strong. At Strong, it can noticeably slow burst shooting on some bodies because it's more processing-intensive — worth mentioning if the user cares about buffer/frame rate.

## Color Chrome FX Blue

The same idea as Color Chrome Effect, but scoped to blues specifically — skies, water, denim. Off / Weak / Strong. The two Color Chrome settings are independent and commonly used together (e.g., Strong on reds for warm sunset skin tones, Weak on blue for a sky that doesn't turn cartoonish).

## White Balance & WB Shift

- **White Balance mode:** Auto (some bodies split this into Auto / Auto White Priority / Auto Ambience Priority), a Kelvin color-temperature value, Custom (manual gray-card reading), or one of the fixed presets (Fine/Direct Sunlight, Shade, various Fluorescent, Incandescent, Underwater).
- **WB Shift:** a fine offset applied on top of whatever WB mode is chosen, on two independent axes — Red↔Blue (warm↔cool) and Green↔Magenta. Typical range is roughly ±9 on each axis in small steps. This is one of the most powerful "color cast" tools in a recipe: shifting toward red/amber and away from blue gives a warm, golden-hour-adjacent cast even in neutral light; shifting toward blue and magenta gives a cool, clinical, or "digital-cinema" cast.

## Dynamic Range

Controls how much highlight and shadow detail the camera protects by pulling down the tone curve (at the cost of a flatter-looking, lower-contrast starting image that often benefits from added contrast elsewhere in the recipe).

- **DR100:** no additional dynamic-range processing. Deepest shadows, brightest/most easily-clipped highlights — the punchiest, most "straight out of camera" contrast.
- **DR200:** middle ground. Meaningfully protects highlights while keeping reasonable shadow depth. Requires a minimum ISO (commonly ISO 400+) since it works by underexposing the sensor slightly and pulling the JPEG curve back up.
- **DR400:** maximum highlight protection and shadow detail — skies stay detailed, shadows stay open, but the result is the flattest and most obviously "processed" of the three. Requires a higher minimum ISO (commonly ISO 800+).

Unlike most other recipe settings, Dynamic Range's underlying exposure choice also affects the RAW file (because it changes how the sensor is read), even though the tone-curve pull-down itself is JPEG-only and freely adjustable when reprocessing the RAW.

## Highlight Tone / Shadow Tone

Two independent contrast controls, typically ranging roughly -2 to +4 in half-steps.

- **Highlight Tone:** negative values soften highlight contrast (gentler roll-off into bright areas, more retained highlight detail); positive values increase highlight contrast (punchier, more clipped-looking highlights).
- **Shadow Tone:** negative values lift/soften shadows (more open, lower-contrast shadow detail); positive values deepen shadows (more contrast, blocked-up-looking blacks).

These interact with Dynamic Range — a high DR setting already flattens the curve, so a recipe built on DR400 often wants *positive* Highlight/Shadow Tone to reintroduce some punch, while a DR100 recipe usually wants them left near zero or slightly negative if the goal is a softer, faded look.

## Color (Saturation)

Global saturation control, typically -4 to +4. Distinct from Color Chrome Effect/FX Blue in that it affects *all* colors uniformly rather than boosting gradation only in already-saturated areas. Not available on monochrome-family simulations (ACROS/Monochrome/Sepia), since there's no color to adjust.

## Sharpness

Typically -4 to +4. Affects edge-contrast sharpening in the JPEG engine. Negative values give a softer, more film-like rendering (often paired with Grain for a filmic look); positive values give a crisper, more "digital" look. This is JPEG-only processing sharpening, distinct from Clarity (midtone contrast) below.

## High ISO NR

Typically -4 to +4. Controls how aggressively the JPEG engine smooths luminance/chroma noise at higher ISOs. Lower (more negative) values preserve more fine detail and let more grain/noise show through — often intentionally paired with a grain-forward recipe; higher values give cleaner but softer high-ISO images.

## Clarity

Typically -5 to +5. A midtone/local contrast control — distinct from Sharpness (edge contrast) and from Highlight/Shadow Tone (global contrast at the extremes). Negative Clarity gives a soft, slightly hazy, dreamlike look; positive Clarity adds punch and perceived detail/texture to midtones without crushing shadows or blowing highlights the way raising overall contrast would.

## ISO

Recipes typically specify either a fixed ISO or an Auto ISO range (with a max ISO and, often, a minimum shutter speed). The chosen ISO strategy matters because it interacts directly with Dynamic Range (DR200/DR400 need a minimum ISO to engage) and with how visible Grain Effect and High ISO NR settings end up looking — a grain-forward recipe designed at ISO 200 can look very different at ISO 6400 once real sensor noise stacks on top of the simulated grain.

## Exposure Compensation

A recipe-specific exposure bias baked into the shooting recommendation, not a JPEG setting — e.g. "+1/3 to +2/3." This is commonly used to counteract how a flattening DR/Highlight-Tone combination can otherwise leave midtones and skin looking underexposed, or to intentionally bias a recipe toward a brighter, airier look.

---

## X-E5 hardware notes

- Six film-simulation dial positions: PROVIA, VELVIA, ASTIA, CLASSIC CHROME, REALA ACE, ACROS.
- Three custom dial slots — **FS1, FS2, FS3** — each storing a *complete* recipe (every setting on this page, not just a film simulation choice) for instant, menu-free recall.
- Access to all 20 film simulations (including Classic Neg., Nostalgic Neg., Eterna, Eterna Bleach Bypass, Sepia, Monochrome, PRO Neg. Hi/Std) through the menu, even though only six are printed on the dial — any of these can still be saved into an FS slot.
- When drafting a recipe meant to live in an FS slot, always specify every field on this page so the recipe is fully reproducible and nothing is left at an ambiguous "whatever it happened to be" default.

## Symptom → dial diagnostic table

Use this when refining an existing recipe from user feedback on a test shot. Change one row at a time.

| Symptom in the test JPEG | Adjust |
|---|---|
| Highlights blown out / no sky detail | Raise Dynamic Range (100→200→400) and/or lower Highlight Tone |
| Image looks flat/lifeless, wants more punch | Raise Highlight Tone and/or Shadow Tone (toward positive), or increase Clarity |
| Shadows crushed to solid black, no detail | Lower Shadow Tone (toward negative), or raise Dynamic Range |
| Skin tones look orange/too warm | Shift WB toward blue, and/or reduce Color Chrome Effect strength |
| Skin tones look sickly/too cool or green | Shift WB toward red/amber (and check for a green WB shift creeping in) |
| Greens/foliage look neon or oversaturated | Lower Color (saturation) and/or Color Chrome Effect strength |
| Sky looks artificially electric blue | Lower Color Chrome FX Blue |
| Overall image looks washed out / too pastel | Raise Color (saturation), and check Dynamic Range isn't set higher than needed |
| Grain looks like ugly noise rather than film texture, especially in shadows | Lower Grain Effect strength, or switch Grain Size from Large to Small, or raise High ISO NR |
| Image looks too soft/mushy overall | Raise Sharpness and/or Clarity |
| Image looks too "digital"/harsh-edged | Lower Sharpness, consider adding Grain |
| Recipe looks great in daylight but muddy indoors | Re-check WB Shift and Dynamic Range under the specific indoor light — recipes are not universally portable across lighting |

## Starter recipes

These are original starting points for common requests, not reproductions of any specific published creator's named recipe — treat them as drafts to hand to the user for field-testing and refinement, not finished answers.

**"Faded Warm Film"** — soft, warm, lifted-shadow look reminiscent of an aged color-negative print.
```
Film Simulation: Classic Chrome
Grain Effect: Weak, Large
Color Chrome Effect: Weak
Color Chrome FX Blue: Off
White Balance: Auto, +3 Red / -2 Blue
Dynamic Range: DR200
Highlight Tone: -1.5
Shadow Tone: -1.5
Color: -2
Sharpness: -1
High ISO NR: -2
Clarity: -3
ISO: Auto, up to 3200
Exposure Compensation: +1/3
```

**"High-Contrast Street B&W"** — punchy, grainy black-and-white for street/documentary work.
```
Film Simulation: ACROS+R
Grain Effect: Strong, Large
Color Chrome Effect: Off
Color Chrome FX Blue: Off
White Balance: Auto, 0 / 0
Dynamic Range: DR100
Highlight Tone: +2
Shadow Tone: +1
Sharpness: +1
High ISO NR: -3
Clarity: +2
ISO: Auto, up to 12800
Exposure Compensation: 0
```

**"Clean Punchy Everyday"** — a reliable, saturated daily-driver look with minimal texture effects.
```
Film Simulation: Reala Ace
Grain Effect: Off
Color Chrome Effect: Weak
Color Chrome FX Blue: Weak
White Balance: Auto, 0 / 0
Dynamic Range: DR200
Highlight Tone: 0
Shadow Tone: 0
Color: +1
Sharpness: 0
High ISO NR: 0
Clarity: +1
ISO: Auto, up to 6400
Exposure Compensation: 0
```

**"Teal-Orange Cinematic"** — a cinema-leaning look built on the flat Eterna base, pushed toward a teal-shadow/orange-highlight split.
```
Film Simulation: Eterna
Grain Effect: Weak, Small
Color Chrome Effect: Weak
Color Chrome FX Blue: Weak
White Balance: Auto, +1 Red / +2 Blue (net: slightly cool base to lean into with post/further shift)
Dynamic Range: DR400
Highlight Tone: +1
Shadow Tone: +1
Color: -1
Sharpness: 0
High ISO NR: -1
Clarity: 0
ISO: Auto, up to 3200
Exposure Compensation: -1/3
```
