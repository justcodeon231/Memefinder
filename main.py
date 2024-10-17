import os
import pytesseract
from PIL import Image
from tkinter import Tk, Label, Button, Listbox, filedialog, Scrollbar, Entry

# Initialize Tkinter app
root = Tk()
root.title("MemeFinder")

# Set Tesseract path for Windows (optional if not added to PATH)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Global variables to store folder path and extracted text data
meme_folder = "C:/Users/eduv4941540"
meme_text_data = {}

# Load memes from a directory and extract text
def load_memes():
    global meme_folder
    meme_folder = filedialog.askdirectory(title="Select Meme Folder")
    meme_files = [f for f in os.listdir(meme_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    listbox.delete(0, 'end')  # Clear previous items
    meme_text_data.clear()  # Clear previous text data
    for meme in meme_files:
        meme_path = os.path.join(meme_folder, meme)
        extracted_text = extract_text(meme_path)
        meme_text_data[meme_path] = extracted_text
        listbox.insert('end', meme)

# Function to extract text using Tesseract OCR
def extract_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()

# Search through memes based on user input
def search_memes():
    search_query = search_box.get().lower()
    listbox.delete(0, 'end')  # Clear current listbox
    for meme_path, text in meme_text_data.items():
        if search_query in text.lower():  # Match query with extracted text
            meme_name = os.path.basename(meme_path)
            listbox.insert('end', meme_name)

# Display selected meme
def display_meme(event):
    selected_meme = listbox.get(listbox.curselection())
    meme_path = os.path.join(meme_folder, selected_meme)
    img = Image.open(meme_path)
    img.thumbnail((400, 400))
    img = ImageTk.PhotoImage(img)
    meme_label.config(image=img)
    meme_label.image = img  # Keep reference

# GUI Setup
load_btn = Button(root, text="Load Memes", command=load_memes)
load_btn.pack()

search_box = Entry(root)
search_box.pack(pady=10)

search_btn = Button(root, text="Search", command=search_memes)
search_btn.pack()

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(root, yscrollcommand=scrollbar.set)
listbox.pack(fill="both", expand=True)
listbox.bind('<<ListboxSelect>>', display_meme)

scrollbar.config(command=listbox.yview)

meme_label = Label(root)
meme_label.pack(pady=20)

# Run the app
root.geometry("600x500")
root.mainloop()