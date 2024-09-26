import streamlit as st
import pandas as pd
import easyocr
import numpy as np
import re 
from PIL import Image

# Display uploaded image
def display_image(image):
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Extract text using easyOCR
def extract_text_from_image(image):
    reader = easyocr.Reader(['en', 'hi'], gpu=False)
    results = reader.readtext(np.array(image))
    return results

# Concatenate extracted text for display
def concatenate_text(results):
    return " , ".join([detection[1] for detection in results])

# Search functionality for highlighting text with custom color and background
def search_and_highlight_text(text, keyword):
    if keyword:
        # Use re.sub() to highlight the matching keyword in the text, ignoring case
        # This applies inline CSS for custom color and background
        highlighted_text = re.sub(f"({keyword})", r"<span style='color: red; background-color: yellow;'>\1</span>", text, flags=re.IGNORECASE)
        return highlighted_text
    return text

# Streamlit app function
def run_ocr_app():
    st.title("Hindi-English OCR with Keyword Search")

    # Upload image
    file = st.file_uploader("Upload an Image (PNG/JPG/JPEG)", type=['png', 'jpg', 'jpeg'])
    
    if file:
        image = Image.open(file)
        display_image(image)

        # Extract text from image
        results = extract_text_from_image(image)

        # Concatenate extracted text into a single line
        extracted_text = concatenate_text(results)
        
        # Keyword search
        search_term = st.text_input("Search for a keyword:")
        
        # Highlight the keyword in the extracted text (if any)
        if search_term:
            extracted_text = search_and_highlight_text(extracted_text, search_term)

        # Display the extracted text with highlighted keyword
        st.write("### Extracted Text:")
        st.markdown(extracted_text, unsafe_allow_html=True)  # Display the extracted text with inline HTML

# Run the app
run_ocr_app()
