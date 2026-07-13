try:
    import fitz
    HAS_FITZ = True
except Exception:
    HAS_FITZ = False

def extract_text(pdf_file):
    """Extract text from uploaded PDF file-like object.

    If PyMuPDF (`fitz`) is unavailable, return a clear message so the
    Streamlit UI can show it instead of crashing the app.
    """
    if not HAS_FITZ:
        return (
            "[PDF parsing unavailable] PyMuPDF (fitz) is not installed in the "
            "runtime. Please add `pymupdf` to `requirements.txt` and redeploy, "
            "or use plain text inputs."
        )

    try:
        text = ""
        pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")
        for page in pdf:
            text += page.get_text()
        return text
    except Exception as e:
        return f"[PDF parsing error] {str(e)}"