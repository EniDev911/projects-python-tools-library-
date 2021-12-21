import pyqrcode
import os

print("Bienvenido al generador de códigos QR")


msg = "Escribe un mensaje secreto:\n"


cod = pyqrcode.create(msg)

cod.png('new_cod.png', scale=5)
print(cod.terminal(quiet_zone=1))
print("Código QR generado exitosamente.")
