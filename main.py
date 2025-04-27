from ensurepip import version
from pickle import TRUE
from turtle import fillcolor
import qrcode
from qrcode.constants import ERROR_CORRECT_L

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=3,
    border=5
)
qr.add_data('https://www.google.com/')
qr.make(fit=TRUE)
img = qr.make_image(fill_color="black", back_color="white")
img.save('google.png')