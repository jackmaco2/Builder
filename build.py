import PyPDF2

pdf = input("Enter pdf file name: ")

bldsht = open(pdf, 'rb')
reader = PyPDF2.PdfFileReader(bldsht)

pone = reader.getPage(0)
ptwo = reader.getPage(1)
text = ptwo.extractText()

start = text.find("paint")
end = len(text)
todotog = text[start:end]
todo = todotog.split()

print(todo)

bldsht.close()