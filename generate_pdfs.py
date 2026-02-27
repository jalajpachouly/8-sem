"""
Generate PDFs from all HTML answer files using Microsoft Edge headless mode.
Then merge all individual PDFs into one combined PDF with bookmarks.
"""
import subprocess
import os
import time
from PyPDF2 import PdfMerger

# Config
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVER_URL = "http://localhost:8090"

# Files to convert (in order)
HTML_FILES = [
    ("index.html", "Index - DL Unit 2"),
    ("Q1.html", "Q1 - Perceptron & Training Steps"),
    ("Q2.html", "Q2 - Biological Neuron & Feed-Forward Network"),
    ("Q3.html", "Q3 - Activation Functions"),
    ("Q6.html", "Q6 - Hyperparameters"),
    ("Q7.html", "Q7 - Sentiment Analysis"),
    ("Q8.html", "Q8 - PyTorch & Google Colab"),
    ("Q9.html", "Q9 - Gradient Descent & Gradient Problems"),
]

PDF_DIR = os.path.join(BASE_DIR, "pdfs")
os.makedirs(PDF_DIR, exist_ok=True)


def html_to_pdf(html_file, pdf_path):
    """Convert an HTML file to PDF using Edge headless --print-to-pdf."""
    url = f"{SERVER_URL}/{html_file}"
    cmd = [
        EDGE,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        url,
    ]
    print(f"  Converting {html_file} -> {os.path.basename(pdf_path)}")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        print(f"    WARNING: Edge returned code {result.returncode}")
        if result.stderr:
            print(f"    stderr: {result.stderr[:200]}")
    # Edge sometimes needs a moment
    time.sleep(1)
    if os.path.exists(pdf_path):
        size = os.path.getsize(pdf_path)
        print(f"    OK ({size:,} bytes)")
        return True
    else:
        print(f"    FAILED - PDF not created")
        return False


def merge_pdfs(pdf_files_with_titles, output_path):
    """Merge multiple PDFs into one with bookmarks."""
    merger = PdfMerger()
    for pdf_path, title in pdf_files_with_titles:
        if os.path.exists(pdf_path):
            merger.append(pdf_path, outline_item=title)
            print(f"  Added: {title}")
    merger.write(output_path)
    merger.close()
    size = os.path.getsize(output_path)
    print(f"\n  Merged PDF: {output_path} ({size:,} bytes)")


if __name__ == "__main__":
    print("=" * 60)
    print("  HTML to PDF Converter - DL Unit 2")
    print("=" * 60)

    # Step 1: Generate individual PDFs
    print("\n[1/2] Generating individual PDFs...\n")
    pdf_files = []
    for html_file, title in HTML_FILES:
        pdf_name = html_file.replace(".html", ".pdf")
        pdf_path = os.path.join(PDF_DIR, pdf_name)
        success = html_to_pdf(html_file, pdf_path)
        if success:
            pdf_files.append((pdf_path, title))

    # Step 2: Merge all PDFs
    print(f"\n[2/2] Merging {len(pdf_files)} PDFs into one...\n")
    merged_path = os.path.join(PDF_DIR, "DL_Unit2_Complete.pdf")
    if pdf_files:
        merge_pdfs(pdf_files, merged_path)

    print("\n" + "=" * 60)
    print(f"  Done! {len(pdf_files)} PDFs generated in: {PDF_DIR}")
    print(f"  Combined PDF: {merged_path}")
    print("=" * 60)
