from PyPDF2 import PdfReader
from gtts import gTTS
from tkinter.filedialog import *

book_path = askopenfilename()
pdf_name = book_path.split("/")[-1]

# Get text from pdf
def get_text_from_pdf():
    full_text = ''
    read_pdf = PdfReader(book_path)
    number_of_pages = len(read_pdf.pages)
    print(number_of_pages)
    for i in range(0, number_of_pages):
        page = read_pdf.pages[i]
        page_content = page.extract_text()
        full_text += page_content
    print(full_text)
    return full_text

# Get Audio from text
def get_audio_from_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save(f"mp3s/{pdf_name}.mp3")

if __name__ == '__main__':
    text = get_text_from_pdf()
    get_audio_from_text(text)