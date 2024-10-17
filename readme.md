## MemeFinder

### Overview

MemeFinder is a simple desktop application built using Python, Tkinter, and Tesseract OCR. This tool allows users to load a folder of meme images, extract text from the memes using OCR (Optical Character Recognition), and search for memes based on text content. The app is designed to help users quickly locate memes with specific wording or phrases.

### Features
- **Load Memes**: Choose a folder containing meme images, and the app will automatically extract any text from them using Tesseract OCR.
- **Search Memes**: Search for memes by entering keywords or phrases. The app will display any meme that matches the text content.
- **Display Meme**: Select a meme from the search results to preview the image in the app.

### Requirements
- Python 3.x
- Tkinter (usually included with Python)
- Tesseract OCR (Tesseract needs to be installed on your machine)
- Python libraries: `Pillow`, `pytesseract`

### Installation

1. **Install Python Libraries**:
   Install the necessary Python packages using pip:
   ```bash
   pip install pytesseract Pillow
   ```

2. **Install Tesseract OCR**:
   - **Windows**: Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract).
   - **Linux**: Install via package manager:
     ```bash
     sudo apt install tesseract-ocr
     ```
   - **Mac**: Install via Homebrew:
     ```bash
     brew install tesseract
     ```

   If Tesseract is not added to the system PATH, update the path in the code:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

### Usage

1. **Run the Application**:
   Execute the script to launch the MemeFinder GUI:
   ```bash
   python meme_finder.py
   ```

2. **Load Memes**:
   - Click the "Load Memes" button to select a folder containing meme images.
   - The supported file formats are `.png`, `.jpg`, `.jpeg`, and `.gif`.

3. **Search Memes**:
   - Enter a keyword or phrase in the search bar and click "Search".
   - The app will filter and display memes that contain the searched text.

4. **View Meme**:
   - Click on any meme in the results list to preview it.

### Notes

- Tesseract OCR may not be 100% accurate with all text, especially if the images have poor quality or complex backgrounds.
- You can tweak the OCR engine to improve accuracy by adjusting image pre-processing techniques (e.g., converting images to grayscale).

### Future Enhancements

- Add support for multiple languages in OCR.
- Implement advanced image filtering techniques to improve OCR text extraction.
- Add a feature to sort memes by relevance based on the search query.

### License

This project is open-source and free to use. Contributions are welcome to enhance the functionality.