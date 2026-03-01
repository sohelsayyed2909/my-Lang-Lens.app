import easyocr
from PIL import Image
import numpy as np

class OCRModel:
    def __init__(self):
        self.reader = easyocr.Reader(['en', 'hi'])  # Initialize for English and Hindi

    def process_image(self, image: Image.Image) -> str:
        # Convert PIL Image to numpy array
        image_np = np.array(image)
        
        # Perform OCR
        result = self.reader.readtext(image_np)
        
        # Extract text from result
        text = ' '.join([item[1] for item in result])
        return text