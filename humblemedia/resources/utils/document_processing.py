import magic
from PyPDF2 import PdfFileWriter, PdfFileReader

def _get_file_type(input_file):
    return magic.from_file(input_file, mime=True).decode()

def _write_page(pdf_output, pdf_input, num):
    page = pdf_input.getPage(num)
    pdf_output.addPage(page)

def _get_pdf_file_percentage(input_file, output_file, percentage):
    pdf_input  = PdfFileReader(open(input_file, 'rb'))
    pdf_output = PdfFileWriter()

    if pdf_input.getNumPages() == 1:
        raise Exception('Cannot convert single-page PDFs')

    count = round(pdf_input.getNumPages() * percentage / 100)
    if count < 1:
        _write_page(pdf_output, pdf_input, 0)
    else:
        for iter in range(0, count):
            _write_page(pdf_output, pdf_input, iter)

    output_stream = open(output_file, 'wb')
    pdf_output.write(output_stream)

def _get_txt_file_percentage(input_file, output_file, percentage):
    input_stream = open(input_file, 'rb')
    content = input_stream.read().decode()

    count = round(len(content) * percentage / 100)
    if count < 1:
        raise Exception('Cannot convert such small txt files')

    output_stream = open(output_file, 'wb')
    output_stream.write(content[:count].encode())

def get_document_file_percentage(input_file, output_file, percentage=10):
    file_type = _get_file_type(input_file)
    if file_type == 'application/pdf':
        _get_pdf_file_percentage(input_file, output_file, percentage)
    elif file_type == 'text/plain':
        _get_txt_file_percentage(input_file, output_file, percentage)
