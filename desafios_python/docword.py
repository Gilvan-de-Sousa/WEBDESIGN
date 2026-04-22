from docx import Document

documento = Document("C:\\Users\\F985712\\Downloads\\Trabalho.docx")
texto = " "
for par in documento.paragraphs:
    print(par.text)
    
