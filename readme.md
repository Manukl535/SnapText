
# Image to Text Extractor

This is a Python script that uses the Tesseract OCR library to extract text from images. It is designed to be used with the Watchdog library to monitor a directory for new image files and extract text from them as they arrive.

## Installation

1. Install the python of latest version (version 3.11)
2. Install the Python packages required by the script using pip:
3. Install the Tesseract OCR library from the official website.
4. Install the Watchdog library from the official website.
5. Install the Pillow library from the official website.





```bash
pip install watchdog pillow pytesseract
```
```bash
pip install watchdog
pip install pillow
pip install pytesseract
```
## Usage

1. Create a directory to monitor for new image files.
2. Create a text file to store the extracted text.
3. Run the script:

```bash
python <filename>.py
py <filename>.py
python3 <filename>.py
```

The script will monitor the specified directory for new image files and extract text from them. The extracted text will be saved to the specified text file.

## Example

```bash
python <filename>.py
py <filename>.py
python3 <filename>.py
```

This will start monitoring the current directory for new image files and extract text from them.

## License

This script is released under the [MIT License](LICENSE).

## Author

[MANU K L](https://github.com/manukl535)

## Acknowledgments

- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- [Watchdog](https://github.com/gorakhargosh/watchdog)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

## Contact

If you have any questions or feedback, please contact [MANU K L](https://github.com/manukl535) on GitHub.

## Changelog

- 1.0.0 - Initial release

## Roadmap

- Add support for multiple image formats.
- Add support for multiple languages.
- Add support for custom configuration options.
- Add support for custom output formats.
- Add support for custom error handling.


## License

This script is released under the [MIT License](LICENSE).

## Acknowledgments

- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- [Watchdog](https://github.com/gorakhargosh/watchdog)
- [Pillow](https://pillow.readthedocs.io/en/stable/)


