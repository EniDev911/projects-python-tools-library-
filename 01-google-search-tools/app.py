from googlesearch import search


print('Bienvenido a la herramienta de búsqueda en Google\n\n')

# Pidiendo la consulta
consulta = input("¿Qué quieres buscar en google?:\n")
print()
# Iterando en el rango de resultado
for i in search(consulta, start=0, stop=8):
	print(i)
print()
print()