import PyPDF2, pyttsx3

# Caminho do arquivo pdf
path = open(r'', 'rb')

pdf_reader = PyPDF2.PdfReader(path)

# Inicializa a biblioteca pyttsx3
speak = pyttsx3.init()

# Percorre todas as páginas do arquivo
for pages in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[pages].extract_text()
    speak.say(text)
    speak.runAndWait()

# Para o speak
speak.stop()