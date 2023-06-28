import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from pydub import AudioSegment
import os

def convert_pdf_to_mp3():
    convert_button["state"] = "disabled"
    completion_label["text"] = "Converting... Please wait."
    root.update()

    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        output_path = filedialog.asksaveasfilename(filetypes=[("MP3 Files", "*.mp3")])
        if output_path:
            # Check if the output_path ends with ".mp3"
            if not output_path.endswith(".mp3"):
                output_path += ".mp3"

            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                total_pages = len(reader.pages)
                text = ''
                for i, page in enumerate(reader.pages, start=1):
                    text += page.extract_text()
                    update_progress(i, total_pages)

            # Convert text to speech using pyttsx3
            engine = pyttsx3.init()
            engine.setProperty("rate", 150)  # Adjust the speech rate as needed
            engine.save_to_file(text, output_path)
            engine.runAndWait()

            completion_label["text"] = "Conversion completed successfully."
        else:
            completion_label["text"] = "Output path not selected."
    else:
        completion_label["text"] = "PDF file not selected."

    convert_button["state"] = "normal"
    progress_bar["value"] = 0

def update_progress(current_page, total_pages):
    progress = (current_page / total_pages) * 100
    progress_bar["value"] = progress
    root.update()

# User interface
root = tk.Tk()
root.title("MPDF")
root.geometry("500x350")  # Set the window size
root.resizable(False, False)  # Prevent window resizing

# Set the background to black with details of a blue headphone and a green book
root.configure(bg="black")
image_path = "C:/Users/caios/OneDrive/Documentos/PYTHON/Projeto Pessoal/AudioBook/Grafico/imagem/fone-azul.jpeg"  # Insert the desired image path

# Load the image using the Pillow library
image = Image.open(image_path)
image = image.resize((500, 300), Image.LANCZOS)  # Resize the image as needed
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
background_label = tk.Label(root, image=photo)
background_label.place(relwidth=1, relheight=0.85)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate")
progress_bar.place(relx=0.05, rely=0.9, relwidth=0.9, relheight=0.1)

# Button to convert PDF to MP3
convert_button = tk.Button(root, text="Convert PDF to MP3", command=convert_pdf_to_mp3)
convert_button.place(relx=0.4, rely=0.87, relwidth=0.2, relheight=0.08)

# Label to show completion status
completion_label = tk.Label(root, text="")
completion_label.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.05)

root.mainloop()
