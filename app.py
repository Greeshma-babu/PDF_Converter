import streamlit as st
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT
from io import BytesIO


# Streamlit configuration
st.set_page_config(
    page_title="DOCX/TXT to PDF Converter",
    page_icon=None,
    layout="centered"
)

st.title("Full Stack PDF Converter Application")
st.write("Convert DOCX and TXT files into PDF format.")


# File upload
uploaded_file = st.file_uploader(
    "Upload a DOCX or TXT file",
    type=["docx", "DOCX", "txt", "TXT"]
)


# Extract text from DOCX
def extract_text_from_docx(file):

    document = Document(file)

    text = []

    for paragraph in document.paragraphs:
        text.append(paragraph.text)

    return text


# Extract text from TXT
def extract_text_from_txt(file):

    content = file.read()

    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        text = content.decode("latin-1")

    return text.splitlines()


# Create PDF
def create_pdf(lines):

    pdf_buffer = BytesIO()

    document = SimpleDocTemplate(
        pdf_buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    normal_style = styles["Normal"]
    normal_style.fontName = "Helvetica"
    normal_style.fontSize = 10
    normal_style.leading = 14
    normal_style.alignment = TA_LEFT

    story = []

    for line in lines:

        if line.strip():

            safe_line = (
                line.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
            )

            story.append(
                Paragraph(safe_line, normal_style)
            )

            story.append(
                Spacer(1, 6)
            )

        else:

            story.append(
                Spacer(1, 10)
            )

    document.build(story)

    pdf_buffer.seek(0)

    return pdf_buffer


# Process uploaded file
if uploaded_file is not None:

    file_name = uploaded_file.name

    st.success(f"File uploaded: {file_name}")

    # Convert extension to lowercase
    file_extension = file_name.rsplit(".", 1)[-1].lower()

    # DOCX / docx / DOCX
    if file_extension == "docx":

        uploaded_file.seek(0)

        try:
            lines = extract_text_from_docx(uploaded_file)

        except Exception as e:

            st.error(
                "Unable to read this DOCX file. "
                "Please make sure it is a valid Microsoft Word document."
            )

            st.stop()

    # TXT / txt / TXT
    elif file_extension == "txt":

        uploaded_file.seek(0)

        lines = extract_text_from_txt(uploaded_file)

    else:

        st.error(
            "Unsupported file type. Please upload a DOCX or TXT file."
        )

        st.stop()


    # Preview
    st.subheader("File Preview")

    preview_text = "\n".join(lines)

    st.text_area(
        "File Content",
        preview_text,
        height=300
    )


    # Convert
    if st.button("Convert to PDF"):

        pdf_file = create_pdf(lines)

        output_name = (
            file_name.rsplit(".", 1)[0] + ".pdf"
        )

        st.success("PDF created successfully.")

        st.download_button(
            label="Download PDF",
            data=pdf_file,
            file_name=output_name,
            mime="application/pdf"
        )