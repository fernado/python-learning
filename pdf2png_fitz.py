import fitz  # PyMuPDF

# Path to the PDF file
pdf_path = r'C:\Users\fernando\Desktop\PMI_Certfication.pdf'

# Open the PDF
pdf_document = fitz.open(pdf_path)

# Iterate through each page
for page_number in range(len(pdf_document)):
    page = pdf_document.load_page(page_number)  # Load a specific page
    pix = page.get_pixmap()  # Render page to an image

    # Save the image as a PNG file
    pix.save(f'page_{page_number + 1}.png')

# Close the PDF document
pdf_document.close()