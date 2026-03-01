# PROJECT NAME : LANG LENS 


## Overview

 - This project is a simple Optical Character Recognition (OCR) tool that extracts text from images 
    and allows the user to search for keywords within the extracted text.
    The application supports both English and Hindi text recognition using the easyocr library.

## Table of contents
 - [Overview](#overview)
 - [Features](#Features)
 - [Tech Stack](#Tech-Stack)
 - [Implementation of LANGLENS](#Implementation-of-the-LANGLENS)
 - [Usage](#usage-of-LANG-LENS)
 - [Structure of directory](#Directory)
 - [Code overview](#Code-Overview)
## The Key Features  of this project are as listed below:
### Features
    - Image Upload: Users can upload image files in .jpg, .jpeg, or .png format.
    - OCR (Optical Character Recognition): The app processes the uploaded image to extract text, which can be in English or Hindi.
    - Text Search: Users can search for keywords within the extracted text, with matches being highlighted.
    - Text Download: Users can download the extracted text as a .json file.
    - Keyword Search Results: Search results display the number of matches and the specific lines containing the keyword.

## This project involves usage of different technologies to achieve its goal of extraction of text with search function:
### Tech Stack
    - Python: Backend logic and OCR functionality.
    - Streamlit: Frontend web framework to build the interactive UI.
    - EasyOCR: OCR engine for recognizing text in images.
    - PIL (Python Imaging Library): For handling and processing images.
    - Numpy: For handling image data as numpy arrays.

### Implementation of the LANG LENS:
- How to Install and Run Locally
        - Prerequisites
                Make sure you have Python 3.x installed on your machine.
```bash
            # clone command
            git clone https://github.com/Fawaz-devs/hindi-english-ocr.git
            cd hindi-english-ocr
 ```
- Installing Dependencies
            pip install -r requirements.txt
            You can find the requirements.txt file in the hindi-english-ocr folder.
            or you can refer to the below text :
            Dependencies :
                + streamlit
                + easyocr
                + pillow
                + numpy
#### After the completion of installation of the above Dependencies to Run the application use the command below :
 ```bash
        # streamlit
        streamlit run app.py 
        - Once the app is running, open your browser and go to http://localhost:8501 to access the web interface.
```
#### Usage of LANG LENS:
##Use this link to go to the LANG LENS : [LANGLENS](https://lang-lens.streamlit.app/)
- Upload an Image: Choose an image file by clicking the "Choose an image file" button.
- Perform OCR: Once the image is uploaded, click the "Perform OCR" button to extract the text from the image.
- View Extracted Text: The extracted text will be displayed in a text area for review.
- Search in Extracted Text: Enter a keyword in the search input to find and highlight specific terms in the extracted text.
- Download Extracted Text: Download the extracted text in .json format using the "Download JSON" button.

### Directory
 ##### The correct structure of directory is as below for the project to run efficiently:
       -  .
        - ├── app.py               + Main application script (Streamlit)
        - ├── ocr_model.py         + OCR Model (EasyOCR)
        - ├── requirements.txt     + Python dependencies
        - ├── README.md            + Project documentation

### Code Overview :
- app.py :-
         - Implements the Streamlit web interface.
         - Handles image upload, OCR processing, text search, and file download functionality.
         - Calls the OCRModel class to perform the text extraction using easyocr.
-  ocr_model.py :-
         - Contains the OCRModel class, which uses EasyOCR to read the text from an image.
         - Handles multi-language OCR processing for English and Hindi.

### The output will consist of :
- Extracted Text: The text extracted from the uploaded image will appear in the application for further processing.
- Search: The app highlights any matches of keywords in the extracted text, showing the number of occurrences and the corresponding lines.

#### This README provides a comprehensive overview of the project, installation instructions, and descriptions of key functionalities, as well as guidance for addressing issues encountered during development.
