import qrcode

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size  = 10,
    border =4
)

qr.add_data("https://www.linkedin.com/in/nikhil-gouda-1555491a1/")
qr.make(fit = True)

img = qr.make_image(fill_color = "blue", back_color = "White")

img.save("NikLinkdincolor.png")

print("Colored QR Generated Successfully")