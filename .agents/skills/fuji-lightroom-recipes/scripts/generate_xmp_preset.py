#!/usr/bin/env python3
"""Generate a valid Lightroom / Camera Raw .xmp preset file from a JSON spec.

Why this exists: Lightroom presets are plain-text XMP files using the
`crs:` (Camera Raw Settings) namespace. Hand-writing that XML is easy to get
subtly wrong (missing a required flag, reusing a UUID, bad escaping of the
preset name). This script takes a small JSON description of the desired
slider values and emits a complete, importable .xmp file.

Usage:
    python generate_xmp_preset.py --spec spec.json --output "My Preset.xmp"
    cat spec.json | python generate_xmp_preset.py --output "My Preset.xmp"

Spec JSON shape:
{
  "name": "Faded Warm Film",
  "group": "Fuji Recipes",          # optional
  "settings": {                      # any crs: field, WITHOUT the "crs:" prefix
    "Exposure2012": "0.00",
    "Contrast2012": "-10",
    "Highlights2012": "-20",
    "Shadows2012": "25",
    "Whites2012": "-5",
    "Blacks2012": "10",
    "Clarity2012": "-8",
    "Vibrance": "-5",
    "Saturation": "-10",
    "Temperature": "5600",
    "Tint": "+8",
    "GrainAmount": "35",
    "GrainSize": "30",
    "GrainFrequency": "40"
  }
}

Values are written verbatim as XMP attribute strings, so pass them as you'd
want them to appear (e.g. "+8", "-10", "0.00"). Unrecognized field names are
still written through as-is -- this script does not maintain an exhaustive
allowlist of every crs: field Adobe has ever shipped, since that list grows
with every Lightroom/ACR release. See references/lightroom-presets-vs-profiles.md
in this skill for a vocabulary of common fields per aesthetic axis.
"""

import argparse
import json
import sys
import uuid
from xml.sax.saxutils import escape, quoteattr

# Sensible defaults so the preset is valid and complete even if the caller
# only specifies the handful of sliders they actually care about changing.
DEFAULT_SETTINGS = {
    "PresetType": "Normal",
    "Cluster": "",
    "SupportsAmount": "False",
    "SupportsColor": "True",
    "SupportsMonochrome": "True",
    "SupportsHighDynamicRange": "True",
    "SupportsNormalDynamicRange": "True",
    "SupportsSceneReferred": "True",
    "SupportsOutputReferred": "True",
    "CameraModelRestriction": "",
    "Copyright": "",
    "ContactInfo": "",
    "Version": "17.0",
    "ProcessVersion": "15.4",
    "HasSettings": "True",
    "HasCrop": "False",
    "AlreadyApplied": "False",
}


def build_xmp(name: str, group: str | None, settings: dict) -> str:
    merged = dict(DEFAULT_SETTINGS)
    merged.update(settings)
    merged["UUID"] = str(uuid.uuid4()).upper()

    attrs = "\n    ".join(
        f"crs:{key}={quoteattr(str(value))}" for key, value in merged.items()
    )

    group_block = ""
    if group:
        group_block = f"""
   <crs:Group>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{escape(group)}</rdf:li>
    </rdf:Alt>
   </crs:Group>"""

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 7.0-c000">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"
    {attrs}>
   <crs:Name>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{escape(name)}</rdf:li>
    </rdf:Alt>
   </crs:Name>{group_block}
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--spec", help="Path to a JSON spec file. Reads stdin if omitted.")
    parser.add_argument("--output", required=True, help="Path to write the .xmp file to.")
    args = parser.parse_args()

    if args.spec:
        with open(args.spec, "r", encoding="utf-8") as f:
            spec = json.load(f)
    else:
        spec = json.load(sys.stdin)

    name = spec.get("name")
    if not name:
        parser.error("spec must include a 'name' field")
    group = spec.get("group")
    settings = spec.get("settings", {})

    xmp = build_xmp(name, group, settings)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(xmp)

    print(f"Wrote preset '{name}' to {args.output}")


if __name__ == "__main__":
    main()
