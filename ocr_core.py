try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images
    We will use pillow's image class to open an image.
    We will use pytesseract to detect strings in an image.

    """
    text = pytesseract.image_to_string(Image.open(filename))

    print(ocr_core('images/ocr_example_1.png'))
