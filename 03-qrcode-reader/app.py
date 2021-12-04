from pyzbar.pyzbar import decode
from PIL import Image
import pyqrcode

print("Bienvenido al lector de Código QR")


msg = ("Python Bootcamp 2021")


cod = pyqrcode.create(msg)
cod.png('QRCODE.png', scale=5)

img = Image.open("QRCODE.png")

# Decodificando imagen
d = decode(img)

# Mostrar el resultado
print('QR Decodificado: '+d[0].data.decode())