import os
from PyPDF2 import PdfReader
from tkinter import Tk, filedialog

# Function to handle file upload
def upload_pdf(destination_folder="data"):
    # Open a file picker dialog
    root = Tk()
    root.withdraw()  # Hide the main Tkinter window
    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not file_path:
        raise FileNotFoundError("No file selected.")

    # Ensure destination folder exists
    os.makedirs(destination_folder, exist_ok=True)
    
    # Copy the file to the project directory
    filename = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, filename)
    with open(file_path, "rb") as src, open(destination_path, "wb") as dst:
        dst.write(src.read())

    return destination_path

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    pdf_text = ""
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            pdf_text += page.extract_text()
    return pdf_text

# Function to split text into chunks
def split_text(text, chunk_size=512):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
