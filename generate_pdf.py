from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = "/home/user/Claude/photographers_guide_posing.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=1 * inch,
    rightMargin=1 * inch,
    topMargin=1 * inch,
    bottomMargin=1 * inch,
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    "BookTitle",
    parent=styles["Title"],
    fontSize=16,
    leading=20,
    spaceAfter=6,
    textColor=colors.HexColor("#1a1a1a"),
)
chapter_style = ParagraphStyle(
    "ChapterHead",
    parent=styles["Heading1"],
    fontSize=13,
    leading=16,
    spaceBefore=18,
    spaceAfter=6,
    textColor=colors.HexColor("#1a1a1a"),
    borderPad=4,
)
section_style = ParagraphStyle(
    "SectionHead",
    parent=styles["Heading2"],
    fontSize=11,
    leading=14,
    spaceBefore=14,
    spaceAfter=4,
    textColor=colors.HexColor("#333333"),
)
problem_style = ParagraphStyle(
    "Problem",
    parent=styles["Normal"],
    fontSize=10,
    leading=14,
    spaceAfter=2,
    textColor=colors.HexColor("#cc0000"),
    fontName="Helvetica-Bold",
)
solution_style = ParagraphStyle(
    "Solution",
    parent=styles["Normal"],
    fontSize=10,
    leading=14,
    spaceAfter=2,
    textColor=colors.HexColor("#006600"),
    fontName="Helvetica-Bold",
)
body_style = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontSize=10,
    leading=14,
    spaceAfter=6,
    textColor=colors.HexColor("#222222"),
)
bullet_label_style = ParagraphStyle(
    "BulletLabel",
    parent=styles["Normal"],
    fontSize=10,
    leading=14,
    leftIndent=18,
    spaceAfter=5,
    textColor=colors.HexColor("#222222"),
)
annotation_style = ParagraphStyle(
    "Annotation",
    parent=styles["Normal"],
    fontSize=9,
    leading=12,
    leftIndent=24,
    spaceAfter=3,
    textColor=colors.HexColor("#555555"),
    fontName="Helvetica-Oblique",
)
caption_style = ParagraphStyle(
    "Caption",
    parent=styles["Normal"],
    fontSize=9,
    leading=12,
    spaceAfter=4,
    textColor=colors.HexColor("#444444"),
    fontName="Helvetica-Bold",
)


def hr():
    return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc"), spaceAfter=8, spaceBefore=4)


def sp(n=6):
    return Spacer(1, n)


def label_para(label, text):
    return Paragraph(f"<b>{label}:</b> {text}", bullet_label_style)


story = []

# ── Title ──────────────────────────────────────────────────────────────────
story.append(Paragraph("The Photographer's Guide to Posing", title_style))
story.append(Paragraph("Techniques for Flattering Your Subjects", section_style))
story.append(hr())
story.append(sp(4))

# ══════════════════════════════════════════════════════════════════════════
# SHOT #1
# ══════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Shot #1", chapter_style))
story.append(hr())

# Problems
story.append(Paragraph("✗  Problems  (Figure 12.19)", problem_style))
story.append(sp(4))

story.append(label_para(
    "Mergers",
    "The arm on the left of the frame is tight against the subject's body, "
    "creating a merger that makes her appear wide."
))
story.append(label_para(
    "Hand",
    "Her hand is in an awkward position, pointing at the camera."
))
story.append(label_para(
    "Hips",
    "Her hips are very broad and square to the camera, making her look wider."
))
story.append(label_para(
    "Chin",
    "Her chin is too neutral, so the jawline is not as defined as is desirable."
))
story.append(label_para(
    "Posture",
    "The subject is subtly leaning back away from the camera, making her head "
    "appear smaller and neck appear shorter."
))
story.append(label_para(
    "Camera Angle",
    "The camera angle is approximately even with her midsection—quite low in the frame."
))

story.append(sp(6))
story.append(Paragraph("Figure 12.19 annotations:", caption_style))
story.append(Paragraph("• Merger: arm merged to body, making her look wider", annotation_style))
story.append(Paragraph("• Hips: too broad/square to camera", annotation_style))
story.append(Paragraph("• Hand: somewhat awkward", annotation_style))

story.append(sp(10))

# Solutions
story.append(Paragraph("✓  Solutions  (Figures 12.20, 12.21, and 12.22)", solution_style))
story.append(sp(4))

story.append(label_para(
    "Mergers",
    "By placing her left hand on her hip, we've created negative space between "
    "the arm and the body, which now flatters the form."
))
story.append(label_para(
    "Hand",
    "The right hand is in a much more natural and comfortable position."
))
story.append(label_para(
    "Hips",
    "The hips are turned slightly away from the camera, making them appear narrower."
))
story.append(label_para(
    "Chin",
    "The subject has a more defined jawline, with the chin out and down."
))
story.append(label_para(
    "Posture",
    "The subject has improved posture and is leaning toward the camera."
))
story.append(label_para(
    "Camera Angle",
    "The camera angle is slightly higher. Combined with the subject's lean forward, "
    "there is now more attention to the face and bust, instead of to the midsection."
))

story.append(sp(8))
story.append(Paragraph(
    "This shot is successful with multiple crops, whether it is a tight close-up, "
    "a mid-length shot, or a full-length shot. This full-length image creates strong, "
    "powerful, and flattering lines for the subject. The strong angles communicate the "
    "subject's strength, which is reflected by the bold choice of clothing and dramatic "
    "hair and makeup. With a softer outfit or more demure subject, I may have selected "
    "a curvier, gentler pose. This image, however, is all about her strength. Always ask "
    "yourself: What is this image about? Are all the pieces—lighting, posing, styling, "
    "color—working together to express the purpose?",
    body_style
))

story.append(sp(6))
story.append(Paragraph(
    "When examining the final, retouched shots side by side (Figures 12.21 and 12.22), "
    "notable changes include: the left side of the jacket along the body is smoother—its "
    "original bulge was making the subject look wider, corrected using the Liquify filter "
    "in Photoshop. You will also notice changes in the shoulder area and overall silhouette.",
    body_style
))

story.append(sp(14))

# ══════════════════════════════════════════════════════════════════════════
# SHOT #2
# ══════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Shot #2", chapter_style))
story.append(hr())

# Problems
story.append(Paragraph("✗  Problems  (Figure 12.23)", problem_style))
story.append(sp(4))

story.append(label_para(
    "Mergers",
    "One arm is tight to the body, making her body appear wider."
))
story.append(label_para(
    "Foreshortening",
    "The arm on the chair appears drastically foreshortened with no forearm visible."
))
story.append(label_para(
    "Posture",
    "The subject is slouching, essentially falling into her shoulders, which raises "
    "the shoulders and shortens the neck."
))
story.append(label_para(
    "Shape",
    "The body is too square to the camera and appears at its widest angle."
))

story.append(sp(6))
story.append(Paragraph("Figure 12.23 annotations:", caption_style))
story.append(Paragraph("• Mergers: arm against body, making it appear wider", annotation_style))
story.append(Paragraph("• Foreshortening: forearm straight toward camera", annotation_style))
story.append(Paragraph("• Shape: body too square to camera (appears wider)", annotation_style))

story.append(sp(10))

# Solutions
story.append(Paragraph("✓  Solutions  (Figure 12.24)", solution_style))
story.append(sp(4))

story.append(label_para(
    "Merger",
    "Although one arm is still close to the body, the bend in the arms works to create "
    "the illusion of a waist because the arms meet across the body at the natural waist."
))
story.append(label_para(
    "Shape",
    "Her body has been rotated away from the camera. This helps to narrow her frame, "
    "including her legs and midsection."
))
story.append(label_para(
    "Foreshortening",
    "Her arm has been turned in, eliminating the foreshortening."
))
story.append(label_para(
    "Narrowing Point",
    "Her thighs have been posed in a way that creates a narrowing point at the knees."
))
story.append(label_para(
    "Posture",
    "The posture has been improved. The neck looks longer and the chin more defined."
))

story.append(sp(14))

# ══════════════════════════════════════════════════════════════════════════
# SHOT #3
# ══════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Shot #3", chapter_style))
story.append(hr())

story.append(Paragraph("✗  Problems  (Figure 12.25)", problem_style))
story.append(sp(4))
story.append(Paragraph(
    "(Content from Figure 12.25 continues beyond the captured screenshots.)",
    annotation_style
))

story.append(sp(20))
story.append(hr())
story.append(Paragraph(
    "Source: The Photographer's Guide to Posing: Techniques to Flatter Everyone",
    annotation_style
))

doc.build(story)
print(f"PDF saved to: {OUTPUT}")
