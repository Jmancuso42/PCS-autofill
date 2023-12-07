import fitz  # PyMuPDF
import re 


def pdfscan():
    doc = pdf.open('Knapp.pdf')
    page = doc.load_page(0)
    widgets = list(page.widgets())
    text = widgets[0].get_text() 

    data_list.append(text)

    print(data_list[0])

def get_widget():
    doc = fitz.open('Knapp.pdf')
    page = doc.load_page(0)
    text = page.get_text("text")
    
    for line in text.splitlines():
        if line.startswith('3a. Client\'s First Name'):
            field_value = line.split('.', 1)[1].strip()
            print(field_value)
            break
    else:
        print(f'No field name found in {line}')

def get_field_content():
    doc = pdf.open('Knapp.pdf')
    page = doc[0]
    text = page.get_text("text")

    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith('3a. Client\'s First Name'):  # Adjust this to match your document
            field_value = lines[i + 1] if i + 1 < len(lines) else None
            print(field_value)
            break
    else:
        print('No matching field name found in the document.')



def get_field_content2():
    doc = fitz.open('Knapp.pdf')
    pattern = re.compile(r'\d+[a-z]\.')  # Pattern to match "number, letter, period"

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        lines = text.splitlines()

        for i, line in enumerate(lines):
            if pattern.match(line.strip().split(' ')[0]):  # If line starts with our pattern
                field_value = lines[i + 1] if i + 1 < len(lines) else None
                print(f'Field: {line.strip().split(" ", 1)[0]}, Value: {field_value}')


if __name__ == '__main__':
    # pdfscan()
    # get_widget()
    get_field_content2()