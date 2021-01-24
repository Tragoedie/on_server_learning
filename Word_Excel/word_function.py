from docx import Document


def find_and_replace(document, find_line, replace_line):
    doc = Document(document)

    for paragraph in doc.paragraphs:
        if find_line in paragraph.text:
            text = paragraph.text.replace(find_line, replace_line)
            paragraph.text = text
    doc.save(document)






            #find_text = paragraph.runs
            #for i in range(len(find_text)):
                #if find_line in find_text[i].text:
                    #text = find_text[i].text.replace(find_line, replace_line)
                    #find_text[i].text = text


