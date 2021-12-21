# Especificar tipo de cadena objeto u 
u = 'Chino'                 


# Codificar u con codificación gb2312 
# para obtener el objeto de tipo bytes
str1 = u.encode('gb2312') 
print(str1)
 
# Codifique u con codificación gbk 
# para obtener objetos de tipo bytes
str2 = u.encode('gbk') 
print(str2)

# Codifique u con codificación utf-8 
# para obtener objetos de tipo bytes
str3 = u.encode('utf-8')   
print(str3)

 
# Decodifique la cadena str con la 
# codificación gb2312 para obtener el 
# objeto de tipo cadena
u1 = str1.decode('gb2312') 
print(u1)
 

# Error, porque str1 está codificado por gb2312
# u2 = str1.decode('utf-8')  
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd6 in position 0: invalid continuation byte