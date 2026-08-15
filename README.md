### DOCX/TXT to PDF Converter

A Streamlit-based document conversion application that converts DOCX and TXT files into downloadable PDF documents. The application supports .docx, .DOCX, .txt, and .TXT file formats through a web-based upload interface.
It uses Python and python-docx to extract text from Microsoft Word documents and standard Python file handling for TXT files. ReportLab is used to generate properly formatted PDF documents with A4 page layout and configurable margins. Streamlit provides the interactive frontend, including file upload, document preview, conversion, and download functionality. The application includes input validation and exception handling to identify unsupported or invalid document files.

Technologies: Python, Streamlit, python-docx, ReportLab, BytesIO, and virtual environment (venv).

### Instructions to install
python -m venv .venv

.venv\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt

streamlit run app.py


### Screenshots

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/575f63a3-98b0-4a77-a1cc-5688c3bddc68" />

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/37f5107b-15f5-4a58-b39f-bcba4a321351" />

### Deploy to Streamlit 

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/35cbfe4c-8372-45c7-b9bd-f5d2d7c81a2e" />

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/72280257-b250-459c-af66-e95f76eb7da4" />

