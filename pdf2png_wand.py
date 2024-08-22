from wand.image import Image

# Path to the PDF file
pdf_path = r'C:\Users\fernando\Desktop\PMI_Certfication.pdf'


# Open the PDF and convert each page to an image
with Image(filename=pdf_path, resolution=300) as pdf:
    for i, page in enumerate(pdf.sequence):
        with Image(page) as img:
            img.format = 'png'
            img.save(filename=f'page_{i + 2}.png')