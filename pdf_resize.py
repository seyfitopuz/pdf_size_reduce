from pypdf import PdfWriter



import os

# Specify the directory path
directory = 'in'

# List to store filenames
filenames = []

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Construct full file path
    file_path = os.path.join(directory, filename)
    
    # Check if it's a file (not a directory)
    if os.path.isfile(file_path):
        filenames.append(filename)

# Count the number of files
file_count = len(filenames)

# Print the filenames and the count
print("Filenames:", filenames)
print("Number of files:", file_count)


for x in filenames:
    writer = PdfWriter(clone_from="in/"+x)

    for page in writer.pages:
        for img in page.images:
            img.replace(img.image, quality=100)

    with open("out/"+x, "wb") as f:
        writer.write(f)


"""
writer = PdfWriter(clone_from="example.pdf")

for page in writer.pages:
    for img in page.images:
        img.replace(img.image, quality=80)

with open("out.pdf", "wb") as f:
    writer.write(f)


writer = PdfWriter(clone_from="example.pdf")

for page in writer.pages:
    for img in page.images:
        img.replace(img.image, quality=80)

with open("out.pdf", "wb") as f:
    writer.write(f)"""