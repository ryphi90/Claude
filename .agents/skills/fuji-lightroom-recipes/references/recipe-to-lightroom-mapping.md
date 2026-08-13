# Fuji Recipe → Lightroom Mapping

For editing RAW files shot with a specific Fuji recipe, so the RAW edit approximates what the in-camera JPEG would have looked like. This is inherently approximate — Fuji's JPEG engine and Lightroom's Develop engine are different rendering pipelines with different tone curves and color science — so present the result as a starting draft to refine against the user's actual photos, the same as any other preset workflow in this skill.

| Fuji recipe setting | Lightroom equivalent | Notes |
|---|---|---|
| Film Simulation | Profile Browser → **Camera Matching** → the profile named after the simulation (e.g. "Camera PROVIA/Standard," "Camera Velvia/Vivid," "Camera Classic Chrome," "Camera Astia/Soft," "Camera PRO Neg. Hi/Std," "Camera Monochrome," "Camera Sepia") | Adobe ships camera-matching profiles reproducing most classic Fuji sims for X-Trans RAW files. Newer sims (Classic Neg., Nostalgic Neg., Eterna, Eterna Bleach Bypass, Reala Ace) may not have a matching profile depending on Lightroom/ACR version and how recently the camera was added — check the Profile Browser first; if the matching profile isn't there, start from **Adobe Color** or **Adobe Standard** and rebuild the palette with Color Grading + HSL instead. |
| Grain Effect (strength + size) | Effects panel → Grain (Amount, Size, Roughness) | Weak ≈ low Amount (10–25); Strong ≈ higher Amount (35–60). Large grain size ≈ higher Size value; Small ≈ lower Size value. Roughness adds irregularity — higher for a more "vintage" grain texture. |
| Color Chrome Effect | Color Grading (push saturation/luminance in reds/oranges) or HSL → Red/Orange channel saturation boost | There's no 1:1 slider; approximate by selectively increasing saturation in the affected hue range rather than globally. |
| Color Chrome FX Blue | HSL → Blue/Aqua channel saturation boost, or Color Grading shadows/midtones toward blue with a saturation lift | Same caveat as Color Chrome Effect — it's a selective, gradation-aware effect that sliders only approximate. |
| White Balance + WB Shift | Temp and Tint sliders | WB Shift toward Red/Blue maps roughly to Temp; Green/Magenta shift maps to Tint. Treat the camera's shift values as a direction/magnitude hint, not a literal Kelvin conversion. |
| Dynamic Range (DR100/200/400) | Highlights, Shadows, and Tone Curve shape | Higher DR ≈ flatter starting curve: pull Highlights down and lift Shadows more as DR increases. DR400 often also wants a slight Whites pull-down to avoid a washed-out look once ported to Lightroom's different highlight-rolloff behavior. |
| Highlight Tone | Highlights slider, and the upper region of the Tone Curve | Negative Highlight Tone ≈ positive Highlights slider (protects/softens highlights); positive Highlight Tone ≈ negative Highlights or a steeper upper curve. |
| Shadow Tone | Shadows slider, and the lower region of the Tone Curve | Negative Shadow Tone ≈ positive Shadows slider (lifts shadows); positive Shadow Tone ≈ negative Shadows or a steeper lower curve (deeper blacks). |
| Color (saturation) | Saturation slider (global) or Vibrance if skin tones need protecting | Fuji's Color setting is a uniform saturation change; Saturation is the closer analog, Vibrance is a reasonable substitute when portraits are involved. |
| Sharpness | Detail panel → Sharpening Amount | Negative Fuji Sharpness ≈ lower Lightroom Sharpening Amount than the RAW default; there's no true "negative" equivalent in Lightroom, so a very negative Fuji value may also want a touch of extra softness via reduced Clarity/Texture. |
| High ISO NR | Detail panel → Noise Reduction (Luminance) | Lower Fuji NR (more visible grain/noise) ≈ lower Lightroom Luminance NR; note this only addresses sensor noise, not the simulated Grain Effect, which is handled separately via the Effects panel. |
| Clarity | Clarity slider | Direct 1:1 conceptually — both are midtone/local-contrast controls. Values don't convert numerically, but the sign and rough proportion carry over. |
| ISO / Exposure Compensation | Not a Develop setting — these were shooting decisions | Note them for context only (they explain why a given RAW file has the noise/exposure characteristics it does); they don't map to a slider to set in the preset itself. |

## Practical order of operations

1. Apply the Camera Matching profile matching the recipe's Film Simulation (if available) as the base rendering.
2. Build/apply a preset carrying the rest of the mapped settings on top.
3. Fine-tune white balance and exposure per-photo, since lighting varies shot to shot even within one recipe.
