import pytesseract
from PIL import Image, ImageEnhance
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# Specify the full path to the Tesseract executable (change this if needed)
# Update this path if Tesseract is not added to the PATH, or if you're using a custom installation
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    """
    Preprocess the image to improve OCR accuracy by converting to grayscale and enhancing contrast.
    """
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)  # Increase contrast
    return img

def extract_text_from_image(image_path):
    """
    Extract text from the given image using Tesseract OCR.
    """
    # Preprocess the image (optional but improves results in some cases)
    preprocessed_img = preprocess_image(image_path)

    # Use pytesseract to do OCR on the preprocessed image
    extracted_text = pytesseract.image_to_string(preprocessed_img)

    return extracted_text

def delete_image(image_path):
    """
    Delete the image file from the system after text extraction is complete.
    """
    try:
        os.remove(image_path)
        print(f"Successfully deleted the image: {image_path}")
    except Exception as e:
        print(f"An error occurred while deleting the image: {e}")

class Watcher(FileSystemEventHandler):
    def __init__(self, directory_to_watch):
        self.directory_to_watch = directory_to_watch

    def on_created(self, event):
        if not event.is_directory:
            image_path = event.src_path
            print(f"New file detected: {image_path}")
            try:
                # Extract text from the new image
                text = extract_text_from_image(image_path)

                # Print the extracted text
                print("\nExtracted Text:\n", text)

                # Delete the image after extraction
                delete_image(image_path)
            except Exception as e:
                print(f"An error occurred while processing the image: {e}")

def start_monitoring(directory_to_watch):
    """
    Start monitoring the directory for new image files.
    """
    event_handler = Watcher(directory_to_watch)
    observer = Observer()
    observer.schedule(event_handler, directory_to_watch, recursive=False)
    observer.start()
    print(f"Monitoring started on {directory_to_watch}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Main execution
if __name__ == '__main__':
    directory_to_watch = 'D:/Converter/'

    if not os.path.isdir(directory_to_watch):
        print(f"Error: The directory '{directory_to_watch}' does not exist.")
    else:
        # Start monitoring the directory
        start_monitoring(directory_to_watch)