import pyqrcode

print("Bienvenido al generador de códigos QR")


msg = input("Escribe un mensaje secreto:\n")


cod = pyqrcode.create(msg)

cod.png('new_cod.png', scale=5)

print("Código QR generado exitosamente.")
