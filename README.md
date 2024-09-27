
# Hindi-English OCR with Keyword Search - Documentation





## Project Overview

This application is a simple Optical Character Recognition (OCR) tool built with Streamlit for extracting and displaying text from images in both Hindi and English. Additionally, the application provides a keyword search functionality to highlight specific text in the extracted output. The app leverages EasyOCR to handle OCR processing.


## Features

- Image Upload: Users can upload images in PNG, JPG, or JPEG format.
- Text Extraction: Extracts text in Hindi and English from the uploaded image.
- Keyword Search: Users can input a keyword, which is then highlighted in the extracted text with custom styling (red text and yellow background).
- Real-time Interaction: A user-friendly interface using Streamlit for seamless interaction.


## Technologies Used

1) Streamlit: Web framework for building data applications.
2) EasyOCR: Optical Character Recognition (OCR) library for extracting text from images in multiple languages, including Hindi and English.
3) PIL (Pillow): Python Imaging Library for handling image uploads.
4) Regular Expressions (re): Used to search and highlight keywords in the extracted text.
5) Python: The core programming language for building the application.
## Application Flow

1) Upload Image: Users upload an image file (PNG, JPG, or JPEG) through the web interface.
2) Text Extraction: The app extracts text using EasyOCR and supports both Hindi and English.
3) Keyword Search: Users can search for specific words within the extracted text, and these words will be highlighted in the output.
4) Output Display: The extracted text, along with any highlights, is displayed in the app.

## Installation Guide

### Prerequisites
Ensure you have the following installed:

- Python 3.7+
- pip (Python package manager)
- virtualenv (for creating a virtual environment)

### Clone the Repository
First, clone the project repository from GitHub:

```bash
git clone https://github.com/Tushyen-Gotmare/OCR-WEB-APP.git
cd OCR-WEB-APP
```

### Create a Virtual Environment
After navigating to the project directory, it is recommended to create a virtual environment to isolate the project dependencies. To create and activate a virtual environment, follow these steps:

#### On Windows: 
```bash
python -m venv venv
venv\Scripts\activate
```

You should now see the virtual environment activated, indicated by (venv) at the beginning of your terminal prompt.

### Install Dependencies
With the virtual environment activated, install the required dependencies:

```bash 
pip install -r requirements.txt
```

If you don’t have a requirements.txt file, manually install the required packages:

```bash 
pip install streamlit easyocr pillow numpy
```

### Running the App
To run the application:

1) Ensure the virtual environment is activated.
2) Use the following command to start the app:

```bash 
streamlit run app.py
```
This will start a local web server, and the app will be accessible at http://localhost:8501.

![image](https://github.com/user-attachments/assets/6e330589-b693-48a2-81c6-97fe607b327a)

## Code Structure

```bash 
|-app.py  # Main Streamlit app
|-requirements.txt  # Dependencies
|-README.md  # Project documentation
```
## Additional Information

For further details, suggestions, or contributions, please reach out to the project maintainer at tushyengotmare@gmail.com .
