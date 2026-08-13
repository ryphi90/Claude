---
name: fuji-lightroom-recipes
description: "Use this skill whenever the user wants to build, refine, or troubleshoot a Fujifilm in-camera film simulation recipe (especially for the X-E5 and its custom dial slots), or wants a Lightroom preset or profile created from a text description of a look, from reference/inspiration photos, or translated from an existing Fuji recipe. Trigger on mentions of 'Fuji recipe,' 'film sim recipe,' 'X-E5 recipe,' 'Classic Chrome,' 'Color Chrome Effect,' 'Grain effect,' 'Dynamic Range,' 'Lightroom preset,' 'Lightroom profile,' 'XMP preset,' 'DNG profile,' 'match this photo's look,' 'make this look like film,' or 'recreate this editing style' — even if the user only shares a photo and asks to copy its look, or only describes a mood/vibe without naming a specific tool or file type. Covers making something brand new AND iteratively refining an existing recipe/preset/profile against test shots."
metadata:
  version: 1.0.0
---

# Fuji Recipes & Lightroom Presets/Profiles

You are helping a photographer design film-simulation "recipes" for their Fujifilm X-E5, and/or build Lightroom presets and profiles that achieve a target look — whether that look is described in words, shown in a reference photo, or ported over from a Fuji recipe. Both halves of this skill share the same underlying craft: translate a *desired look* into a small set of *concrete numeric parameters*, then refine those parameters against real images instead of guessing once and stopping.

## Step 0: Figure out what's actually being asked

| The user wants... | Go to |
|---|---|
| A recipe to dial into the X-E5 (or another X-Trans body) | [Path A](#path-a-fuji-in-camera-recipes) |
| A Lightroom preset or profile from a text prompt or a reference image | [Path B](#path-b-lightroom-presets-and-profiles) |
| A Lightroom preset that approximates an existing Fuji recipe (for editing the RAW files from shots taken with that recipe) | Path A first to lock the recipe, then [the bridging workflow](#bridging-a-fuji-recipe-into-lightroom) in Path B |

If it's ambiguous, ask — a "recipe" is camera-side and only really matters if they own a Fuji body; a "preset/profile" is Lightroom-side and works on anyone's photos.

---

## Path A: Fuji in-camera recipes

### The core idea

A recipe is just a saved bundle of the camera's JPEG-rendering settings. Everything except Dynamic Range and white balance is baked into the JPEG only — the RAW file is untouched and can always be reprocessed later. That's why the single most useful piece of process advice (from Tom England's recipe-building writeup) is to **shoot RAW+JPEG while developing a recipe**: the RAW is your uncorrupted reference, the JPEG is the recipe's actual output, and comparing them side by side is how you tell whether a setting did what you expected.

Read `references/fuji-recipe-settings.md` before writing out a full recipe — it has the complete parameter dictionary (every setting, what it visually does, and its range), the X-E5's specific hardware layout, a symptom-to-dial troubleshooting table, and four original starter recipes you can adapt instead of starting from a blank slate.

### X-E5 specifics to keep in mind

- The physical Film Simulation dial has six fixed positions (PROVIA, VELVIA, ASTIA, CLASSIC CHROME, REALA ACE, ACROS) plus **three custom slots (FS1–FS3)** that store complete recipes — not just a film simulation choice, but every parameter in the recipe — for instant recall without diving into menus.
- The menu itself exposes all 20 film simulations (the six on the dial, plus PRO Neg Hi/Std, Classic Neg, Nostalgic Neg, Eterna, Eterna Bleach Bypass, Sepia, and the monochrome family — ACROS and Monochrome each with No filter/Ye/R/G). A recipe built for a menu-only simulation still needs to live in one of the three FS custom slots if the user wants dial-speed recall.
- Exact numeric step sizes for Highlight/Shadow Tone, WB Shift, etc. have shifted slightly across Fuji generations — confirm increments against the user's actual firmware menu if precision matters, rather than assuming an older body's exact figures carry over unchanged.

### Workflow: building a new recipe

1. **Establish the target look.** Ask for (any of): a mood/word ("faded," "punchy," "moody teal-and-orange"), a reference film stock, or — best of all — a reference photo. If given a photo, describe what you see in recipe-relevant terms: overall contrast, whether shadows are lifted or crushed, whether highlights are soft or clipped, color cast, saturation level, grain visibility, sharpness/softness.
2. **Draft starting parameters.** Use `references/fuji-recipe-settings.md` to pick a base film simulation and starting values for every setting. Don't leave settings at "whatever's default" — a recipe should specify every field so it's fully reproducible.
3. **Present the recipe in the standard shareable format** (see below) so it's easy to dial in on the camera.
4. **Field-test across varied light.** Recipes behave very differently in bright sun, flat/overcast light, and mixed indoor light — a look that's perfect at golden hour can go muddy indoors. Ask the user to shoot RAW+JPEG in at least a couple of different lighting conditions before calling a recipe finished.
5. **Refine from feedback, one variable at a time.** When the user reports back ("shadows are too blocked up," "skin looks orange," "too much grain in a dark corner"), use the diagnostic table in the reference file to change the *specific* parameter responsible rather than re-rolling the whole recipe. Changing multiple settings at once makes it impossible to learn what each one is doing.
6. **Save to a custom slot.** Once it's stable across test conditions, tell the user which FS slot to save it to (FS1–FS3) if they want dial-speed recall.

### Recipe output format

Always present a finished or draft recipe as a labeled block, e.g.:

```
Film Simulation: Classic Chrome
Grain Effect: Strong, Large
Color Chrome Effect: Strong
Color Chrome FX Blue: Weak
White Balance: Auto, +2 Red / -3 Blue
Dynamic Range: DR200
Highlight Tone: -1
Shadow Tone: +1
Color: -2
Sharpness: -1
High ISO NR: -3
Clarity: -2
ISO: Auto, up to 6400
Exposure Compensation: +1/3
```

This is the community-standard field order — keep it even when a field is left at 0/default, so nothing is ambiguous.

---

## Path B: Lightroom presets and profiles

### Preset vs. profile, briefly

A **preset** is a saved set of Develop-panel slider values (exposure, contrast, color, grain, etc.) applied on top of whatever's already happening to the image — think of it as a one-click macro you can always see and further adjust in the sliders. A **profile** works one level deeper: it changes the foundational color/tone rendering *before* any slider adjustments are applied — closer to swapping the camera or film stock than to editing. Profiles can achieve looks (especially B&W tonal separation and non-linear color transforms) that sliders alone can't fully reproduce, but they're not something you can freehand as easily as a preset.

Read `references/lightroom-presets-vs-profiles.md` for the full explanation, including how each is actually built and what Claude can and can't generate directly (short version: a real, working `.xmp` **preset** file is something this skill can generate for the user right now; a **profile** requires an interactive step in Adobe Camera Raw or Lightroom itself, though this skill can hand the user the exact numbers to enter there).

**Default to building a preset** unless the user specifically wants a profile, or the look genuinely can't be done with sliders (e.g., a nonlinear B&W conversion, or "I want this baked in before I even start editing"). Presets are more portable, more editable later, and are what this skill can hand back as a finished file.

### Workflow: text prompt → preset

1. Parse the aesthetic description into concrete axes: overall contrast, warm/cool color cast, saturation, shadow/highlight rendering, midtone punch (clarity/texture), grain, and any color-specific shifts (e.g., "teal shadows," "faded blacks").
2. Map each axis to specific Develop sliders — Exposure, Contrast, Highlights, Shadows, Whites, Blacks, Clarity, Texture, Dehaze, Vibrance, Saturation, the Tone Curve, the eight HSL channels, Color Grading (shadows/midtones/highlights), Grain, Sharpening, and Camera Calibration if relevant.
3. Generate the actual preset file with `scripts/generate_xmp_preset.py` (usage documented in that script and in the reference file) rather than hand-writing the XML — the script guarantees valid structure and a fresh UUID.
4. Hand back the resulting `.xmp` file and a short plain-English description of what it does, so the user can sanity-check it before importing.

### Workflow: reference image → preset

1. Look at the image (use the Read tool if it's a local file, or ask the user to share one).
2. Describe what you observe in the same axes as above — this is the analysis step, do it explicitly rather than jumping straight to numbers.
3. Translate the observed look into slider values the same way as the text-prompt workflow.
4. Be upfront that this produces a *starting point*, not a guaranteed pixel match — different source photos (lighting, subject, camera) will render the same preset differently. Treat the first version as a draft and iterate: apply it to a couple of the user's other photos, ask what's off, adjust specific sliders.

### Bridging a Fuji recipe into Lightroom

When the user wants to edit RAW files shot with a specific Fuji recipe as if the recipe's JPEG look had been applied, use `references/recipe-to-lightroom-mapping.md` for the parameter crosswalk (e.g., Fuji film simulation → Adobe's built-in Camera Matching profile of the same name, Grain Effect → the Effects panel's Grain sliders, Color Chrome Effect → targeted HSL/Color Grading adjustments, Dynamic Range → Highlights/Shadows/tone-curve shape). This mapping is inherently approximate — Fuji's in-camera color science and Lightroom's Develop engine are different pipelines — so say so, and treat the result the same way as any other preset draft: generate it, then refine against real photos.

### Building a profile (when a preset genuinely won't do)

Profiles aren't hand-authored the way presets are. Point the user to `references/lightroom-presets-vs-profiles.md` for the exact in-app steps (editing an image in Adobe Camera Raw, then Alt/Option-clicking "New Preset" to get "New Profile"). Your job is to work out and hand over the specific Point Curve, Color Grading, and HSL numbers to enter during that session — computed the same way as the preset workflows above — so the user isn't guessing once they're in the dialog.

---

## Reference files

- `references/fuji-recipe-settings.md` — full parameter dictionary, X-E5 hardware notes, symptom→dial diagnostic table, and starter recipes.
- `references/lightroom-presets-vs-profiles.md` — deep dive on how presets and profiles differ, the `.xmp` file format, and the exact steps to build each.
- `references/recipe-to-lightroom-mapping.md` — crosswalk table for translating a Fuji recipe into Lightroom Develop settings, plus Adobe's Camera Matching profile names.
- `scripts/generate_xmp_preset.py` — turns a JSON parameter spec into a valid, importable Lightroom `.xmp` preset file. Run `python scripts/generate_xmp_preset.py --help` for usage.
