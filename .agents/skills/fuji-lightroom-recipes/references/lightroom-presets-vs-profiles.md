# Lightroom Presets vs. Profiles

## The core distinction

- A **preset** is a saved snapshot of Develop-panel slider positions — Exposure, Contrast, Highlights/Shadows/Whites/Blacks, Clarity, Vibrance/Saturation, Tone Curve, HSL, Color Grading, Grain, Sharpening/Noise Reduction, Vignette, and so on. Applying a preset just moves those sliders to saved values; you can see exactly what changed and keep adjusting from there. Presets stack and layer easily, and are fully visible/editable after the fact.
- A **profile** operates one layer beneath the sliders — it defines the base color and tone rendering the image starts from, before any slider adjustment happens. Choosing a profile is conceptually closer to choosing which camera or film stock rendered the RAW data than to "editing" it. Profiles generally do not move the visible Develop sliders, so switching profiles doesn't disturb whatever edits are already in place on top.
- Because a profile can encode non-linear, per-channel transforms (a proper 3D lookup table or an editor-built point-curve + HSL rendering), it can produce looks — especially certain black-and-white separations and film-like color crossovers — that plain sliders can't fully replicate. Presets are faster to build, easier to inspect/tweak, and more portable; reach for a profile only when the look genuinely needs that deeper rendering, or when the user wants something that survives underneath whatever preset/edits get layered on top of it.

**Recommended workflow when using both:** apply the profile first (it sets the base rendering), then apply a preset on top (it does the stylistic edit), then fine-tune exposure/white balance/masking by hand. Profiles can be layered under any preset, but not cleanly the other way around.

## Two different kinds of "profile" — this matters for what's actually buildable

1. **Legacy camera profiles (.dcp)** — the original Adobe/DNG profile format: a compiled binary 3D lookup table, built either from Adobe's own camera-characterization process (the "Adobe Standard," "Camera Matching," and other built-in profiles that ship with Lightroom/ACR) or by a photographer using Adobe's **DNG Profile Editor** against a physical color target shot under controlled light. These are **not** something that can be hand-authored as a text file — building one legitimately requires the DNG Profile Editor tool and, for an accurate result, a calibration target.
2. **User-created "Profiles" via Adobe Camera Raw / Lightroom's in-app profile creation** — a newer, more accessible path. You edit a photo using the Point Curve, Color Grading, and HSL tools (deliberately *not* the basic sliders, which stay live underneath a profile), then in the Presets panel click "New Preset," hold **Alt (Windows) / Option (Mac)**, and the dialog becomes **"New Profile."** Name it, save it, and it appears under **User Profiles** in the Profile Browser from then on, available to apply to any photo. This is the realistic path for "build me a profile from this photo" requests.

Because this second path is interactive (it happens inside Photoshop/ACR's or Lightroom's live editing UI, not as a file you can hand someone), **this skill's job is to compute the exact numbers to enter** — Point Curve control points, Color Grading shadow/midtone/highlight hue-saturation-luminance values, and the specific HSL channel adjustments — rather than to claim it can output a finished `.dcp`/profile file directly. Hand the user a clear, ordered list of values to punch into each control during that session.

## The .xmp preset file format

Every modern Lightroom/ACR preset is a plain-text XMP (XML) file using the `crs:` (Camera Raw Settings) namespace — openable and editable in any text editor. This skill can generate a fully valid one directly; use `scripts/generate_xmp_preset.py` rather than hand-writing the XML, since the script guarantees correct structure and a fresh, valid UUID.

Minimal shape of a preset file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"
    crs:PresetType="Normal"
    crs:UUID="..."
    crs:ProcessVersion="15.4"
    crs:Version="17.0"
    crs:Exposure2012="0.00"
    crs:Contrast2012="0"
    crs:Highlights2012="0"
    crs:Shadows2012="0"
    crs:Whites2012="0"
    crs:Blacks2012="0"
    crs:Clarity2012="0"
    crs:Vibrance="0"
    crs:Saturation="0"
    crs:Texture="0"
    crs:Dehaze="0"
    ...
    crs:HasSettings="True">
   <crs:Name>
    <rdf:Alt><rdf:li xml:lang="x-default">Preset Name</rdf:li></rdf:Alt>
   </crs:Name>
   <crs:Group>
    <rdf:Alt><rdf:li xml:lang="x-default">Group Name</rdf:li></rdf:Alt>
   </crs:Group>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
```

Import location: drop the finished `.xmp` file into Lightroom Classic's User Presets, or the shared ACR/Lightroom settings folder (macOS: `~/Library/Application Support/Adobe/CameraRaw/Settings`; Windows: `%AppData%\Adobe\CameraRaw\Settings`) — or just tell the user to use Lightroom's Import Preset dialog, which is simpler and works regardless of OS folder layout.

## Practical slider vocabulary (for translating a look into numbers)

| Aesthetic axis | Primary sliders |
|---|---|
| Overall brightness | Exposure, Whites, Blacks |
| Global contrast | Contrast, Tone Curve steepness |
| Highlight rolloff | Highlights, top of Tone Curve |
| Shadow depth/lift | Shadows, Blacks, bottom of Tone Curve |
| Midtone punch/texture without crushing extremes | Clarity, Texture |
| Overall color intensity | Vibrance (protects skin tones) vs. Saturation (uniform, more aggressive) |
| Selective color shifts (e.g. "teal shadows," "warm skin only") | Color Grading (shadow/midtone/highlight wheels), HSL per-channel Hue/Saturation/Luminance |
| Color cast / warmth | Temp, Tint |
| Atmospheric haze look | Dehaze (negative = add haze, positive = remove it) |
| Film grain texture | Effects > Grain (Amount, Size, Roughness) |
| Vintage faded blacks | Raise the black point via the Tone Curve or Blacks, rather than just lowering Contrast |
| Vignette | Effects > Vignette (Amount, Midpoint, Roundness, Feather) |
