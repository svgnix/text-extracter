# utils.py
import re
import pytesseract
from PIL import Image

# Configure Tesseract (specify path if needed)
# For example: pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'

def extract_text(image_path):
    """Extracts raw text from an image using Tesseract OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_document_data(text):
    """Extracts name, document number, and expiration date from OCR text."""
    # Adjust regex patterns based on the specific format of your passport or license
    name_pattern = r"Name:\s*([A-Z\s]+)"       # Example pattern for name
    number_pattern = r"Document No:\s*(\w+)"   # Example pattern for document number
    expiry_pattern = r"Expires:\s*(\d{2}/\d{2}/\d{4})"  # Example pattern for expiration date

    name = re.search(name_pattern, text)
    document_number = re.search(number_pattern, text)
    expiration_date = re.search(expiry_pattern, text)

    return {
        "name": name.group(1) if name else None,
        "document_number": document_number.group(1) if document_number else None,
        "expiration_date": expiration_date.group(1) if expiration_date else None
    }
