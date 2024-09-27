import streamlit as st
import pandas as pd
import easyocr
import numpy as np
from PIL import Image
import re

# Display uploaded image with a mobile-friendly size
def display_image(image):
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Resize the image for mobile performance
def resize_image(image, max_width=800):
    width_percent = (max_width / float(image.size[0]))
    height_size = int((float(image.size[1]) * float(width_percent)))
    resized_image = image.resize((max_width, height_size))
    return resized_image

# Extract text using easyOCR
def extract_text_from_image(image):
    reader = easyocr.Reader(['en', 'hi'], gpu=False)
    results = reader.readtext(np.array(image))
    return results

# Concatenate extracted text for display
def concatenate_text(results):
    return " ".join([detection[1] for detection in results])

# Search functionality for highlighting text using HTML
def search_and_highlight_text(text, keyword):
    if keyword:
        # Use re.split to handle case-insensitive keyword matching and splitting
        parts = re.split(f"({re.escape(keyword)})", text, flags=re.IGNORECASE)
        # Highlight the matched keyword using inline HTML for stronger emphasis
        highlighted_text = "".join([f"<span style='color:red; background-color:yellow;'>{part}</span>" 
                                    if part.lower() == keyword.lower() else part for part in parts])
        return highlighted_text
    return text

# Streamlit app function
def run_ocr_app():
    st.set_page_config(layout="centered")  # Mobile-friendly layout

    st.title("Hindi-English OCR with Keyword Search - Limit 200kb")

    # Upload image
    file = st.file_uploader("Upload an Image (PNG/JPG/JPEG)", type=['png', 'jpg', 'jpeg'])
    
    if file:
        image = Image.open(file)
        resized_image = resize_image(image)  # Resize image for mobile
        display_image(resized_image)

        # Extract text from image
        results = extract_text_from_image(resized_image)

        # Concatenate extracted text into a single line
        extracted_text = concatenate_text(results)
        
        # Keyword search
        search_term = st.text_input("Search for a keyword:")
        
        # Highlight the keyword in the extracted text (if any)
        if search_term:
            extracted_text = search_and_highlight_text(extracted_text, search_term)

        # Display the extracted text
        st.write("### Extracted Text:")
        st.markdown(extracted_text, unsafe_allow_html=True)  # Enable HTML rendering for custom styles

# Run the app
run_ocr_app()
