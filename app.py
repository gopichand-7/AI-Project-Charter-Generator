import os
import re
from datetime import datetime

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

# ------------------------------------
# Load Environment Variables
# ------------------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API key not found. Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3-flash-preview")

# ------------------------------------
# Streamlit Page Configuration
# ------------------------------------
st.set_page_config(
    page_title="AI Project Charter Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Project Charter Generator")

st.markdown(
    """
Generate professional **AI-powered Project Charters** using Google Gemini.
"""
)

st.divider()

# ------------------------------------
# User Inputs
# ------------------------------------
project_name = st.text_input("Project Name")

project_description = st.text_area(
    "Project Description",
    height=220
)

generate = st.button(
    "🚀 Generate Project Charter",
    use_container_width=True
)

# ------------------------------------
# Session State
# ------------------------------------
if "charter" not in st.session_state:
    st.session_state.charter = ""

# ------------------------------------
# Current Date
# ------------------------------------
today = datetime.now().strftime("%B %d, %Y")

# ------------------------------------
# PDF Styles
# ------------------------------------
styles = getSampleStyleSheet()

title_style = styles["Title"]
title_style.alignment = TA_CENTER
title_style.textColor = colors.HexColor("#1F4E79")

heading_style = styles["Heading1"]
heading_style.textColor = colors.HexColor("#1F4E79")

normal_style = styles["BodyText"]
normal_style.leading = 18

# ------------------------------------
# Prompt Template
# ------------------------------------
PROMPT_TEMPLATE = """
Act as a Senior Technical Program Manager at a Fortune 500 technology company.

Based on the project description below, create a professional Project Charter suitable for executive approval.

Today's Date:
{today}

Project Description:
{description}

Generate the charter in Markdown using the following structure.

# Business Need

# Objectives

# Scope

## In Scope

## Out of Scope

# Key Stakeholders

# Deliverables

# Timeline

# Assumptions & Constraints

# Estimated Budget (ROM)

# Risks

# Project Manager & Authority Level

# Success Criteria

# Sponsor Approval

Requirements:

- DO NOT generate the Project Overview section.
- DO NOT generate Project Name, Date or Project Status.
- The application will generate those automatically.
- Start your response directly with "# Business Need".
- Use professional project management terminology.
- Use realistic assumptions where information is missing.
- Keep every section concise and executive-friendly.
- Include measurable objectives.
- Provide a realistic Rough Order of Magnitude (ROM) budget estimate.
- Use "To Be Assigned (TBA)" if Project Manager is unknown.
- Use "Executive Sponsors" if multiple sponsors exist.
- Generate deliverables specific to the project.
- End with a Sponsor Approval section.
- Do not use Markdown code blocks, HTML code tags or inline code.
- Return only Markdown.
"""
# ------------------------------------
# Build PDF
# ------------------------------------
def build_pdf(markdown_text):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.8 * inch,
        bottomMargin=0.8 * inch
    )

    story = []

    story.append(
        Paragraph(
            "AI Project Charter",
            title_style
        )
    )

    story.append(Spacer(1, 0.30 * inch))

    lines = markdown_text.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            story.append(Spacer(1, 0.12 * inch))
            continue

        # Heading 1
        if line.startswith("# "):
            story.append(
                Paragraph(
                    line.replace("# ", ""),
                    heading_style
                )
            )
            story.append(Spacer(1, 0.12 * inch))
            continue

        # Heading 2
        if line.startswith("## "):
            story.append(
                Paragraph(
                    f"<b>{line.replace('## ', '')}</b>",
                    normal_style
                )
            )
            story.append(Spacer(1, 0.08 * inch))
            continue

        # Bullet points
        if line.startswith("- ") or line.startswith("* "):
            story.append(
                Paragraph(
                    f"• {line[2:]}",
                    normal_style
                )
            )
            continue

        # Numbered lists
        if re.match(r"^\d+\.", line):
            story.append(
                Paragraph(
                    line,
                    normal_style
                )
            )
            continue

        # Bold Markdown
        line = re.sub(
            r"\*\*(.*?)\*\*",
            r"<b>\1</b>",
            line
        )

        story.append(
            Paragraph(
                line,
                normal_style
            )
        )

    # Footer
    def add_footer(canvas, doc):

        canvas.saveState()

        canvas.setFont("Helvetica", 9)

        canvas.drawString(
            40,
            20,
            "Generated using AI Project Charter Generator"
        )

        canvas.drawRightString(
            560,
            20,
            f"Page {doc.page}"
        )

        canvas.restoreState()

    doc.build(
        story,
        onFirstPage=add_footer,
        onLaterPages=add_footer
    )

    pdf = buffer.getvalue()

    buffer.close()

    return pdf
# ------------------------------------
# Generate Charter
# ------------------------------------
if generate:

    if not project_name.strip() or not project_description.strip():

        st.warning(
            "Please enter both the Project Name and Project Description."
        )

    else:

        with st.spinner("Generating Project Charter..."):

            try:

                prompt = PROMPT_TEMPLATE.format(
                    today=today,
                    description=project_description
                )

                response = model.generate_content(prompt)

                charter = response.text

                # ------------------------------------
                # Clean Gemini Output
                # ------------------------------------

                charter = re.sub(
                    r"```(?:markdown|md|text)?",
                    "",
                    charter,
                    flags=re.IGNORECASE
                )

                charter = charter.replace("```", "")
                charter = charter.replace("`", "")

                charter = re.sub(
                    r"</?code.*?>",
                    "",
                    charter,
                    flags=re.IGNORECASE
                )

                charter = (
                    charter
                    .replace("\u200b", "")
                    .replace("\ufeff", "")
                    .replace("\u2060", "")
                    .replace("\u200c", "")
                    .replace("\u200d", "")
                )

                charter = charter.replace("$", "\\$")

                charter = re.sub(
                    r"\n{3,}",
                    "\n\n",
                    charter
                )

                charter = re.sub(
                    r"(\d[\d,]*)\s+to\s+(\d[\d,]*)",
                    r"\1 – \2",
                    charter
                )

                charter = charter.strip()

                # ------------------------------------
                # Project Overview (Generated by App)
                # ------------------------------------

                overview = f"""# Project Overview

**Project Name:** {project_name}

**Date:** {today}

**Project Status:** Initiation

The project aims to deliver a strategic solution based on the approved project scope and business objectives described in this charter.

"""

                st.session_state.charter = overview + charter

            except Exception as e:

                st.error(
                    f"Unable to generate the Project Charter.\n\n{e}"
                )

# ------------------------------------
# Display Output
# ------------------------------------
if st.session_state.charter:

    st.success("✅ Project Charter Generated Successfully!")

    st.divider()

    st.markdown(
        st.session_state.charter,
        unsafe_allow_html=False
    )

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            label="📥 Download Markdown",
            data=st.session_state.charter,
            file_name=f"{project_name.replace(' ', '_')}_Project_Charter.md",
            mime="text/markdown",
            use_container_width=True
        )

    with col2:

        try:

            pdf_text = st.session_state.charter.replace("\\$", "$")
            pdf_data = build_pdf(pdf_text)

            st.download_button(
                label="📄 Download PDF",
                data=pdf_data,
                file_name=f"{project_name.replace(' ', '_')}_Project_Charter.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        except Exception as e:

            st.error(f"PDF generation failed: {e}")