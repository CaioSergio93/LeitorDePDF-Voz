import pyttsx3
import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer
#import PyPDF2 - biblioteca não mais usada

livro = open(r'C:\Users\caios\OneDrive\Documentos\Livros\Submundo - Oliver Bowden.pdf') # caminho do livro

for canvas in livro:
    page_images = canvas.images
    page_forms = canvas.forms    
    page_text = canvas.text_content
    page_inline_images = canvas.inline_images    
    page_strings = canvas.strings

pdf = pdfreader.PDFDocument(livro)

livro.canvas.inline_images == []
True

#paginas = pdf.numPages # solicita quantas paginas o livro possui

#print(paginas) # informa quantas pagians tem o livro

voz = pyttsx3.init(driverName='sapi5') # tom da voz
voz.setProperty ('rate', 200) # velocidade da voz

pagina = pdf.getPage(7)

texto = pagina.extractText(pagina)

voz.say(texto) # leitura da pag

voz.runAndWait()