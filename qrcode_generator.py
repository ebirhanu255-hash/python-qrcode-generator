import qrcode

# Get user input
data = input('Enter the text or URL: ').strip()
file_name = input('Enter the output file name (without .png): ').strip()

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

# Add data and make the QR code
qr.add_data(data)
qr.make(fit=True)

# Generate the image
img = qr.make_image(fill_color='black', back_color='white')

# Save the image
img.save(f'{file_name}.png')

print(f'✅ QR code generated and saved as {file_name}.png')
