import base64

base64_data = """base64 here"""

zip_data = base64.b64decode(base64_data)

#replace the file name with something different. I just did this because the file at the time had header PK
with open("reconstructed.zip", "wb") as f:
    f.write(zip_data)

