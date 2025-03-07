import os

# Define the file path
file_path = "output.bmp"

# Get file properties
file_properties = {
    "File Name": os.path.basename(file_path),
    "File Size (bytes)": os.path.getsize(file_path),
    "File Type": os.popen(f'file "{file_path}"').read().strip(),
    "SHA256 Hash:": os.popen(f'SHA256 checksum "{file_path}"').read().split()
}

for property in file_properties:
	print(property, file_properties[property])
