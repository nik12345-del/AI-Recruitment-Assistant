from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor
from datetime import datetime


def generate_report(
    filename,
    ats_score,
    matched_skills,
    missing_skills,
    analysis
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title = styles["Heading1"]
    title.alignment = TA_CENTER
    title.textColor = HexColor("#2563EB")

    heading = styles["Heading2"]

    normal = styles["BodyText"]

    story = []

    story.append(Paragraph("AI Recruitment Assistant Report", title))
    story.append(Paragraph("<br/><br/>", normal))

    story.append(
        Paragraph(
            f"<b>Generated:</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            normal
        )
    )

    story.append(Paragraph("<br/>", normal))

    story.append(Paragraph("ATS Score", heading))
    story.append(
        Paragraph(f"<b>{ats_score}%</b>", normal)
    )

    story.append(Paragraph("<br/>", normal))

    story.append(Paragraph("Matched Skills", heading))

    if matched_skills:
        for skill in matched_skills:
            story.append(Paragraph(f"• {skill}", normal))
    else:
        story.append(Paragraph("None", normal))

    story.append(Paragraph("<br/>", normal))

    story.append(Paragraph("Missing Skills", heading))

    if missing_skills:
        for skill in missing_skills:
            story.append(Paragraph(f"• {skill}", normal))
    else:
        story.append(Paragraph("None", normal))

    story.append(Paragraph("<br/>", normal))

    story.append(Paragraph("AI Resume Analysis", heading))
    story.append(Paragraph(analysis.replace("\n", "<br/>"), normal))

    doc.build(story)