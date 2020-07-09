import hashlib
#cargo la lista de usuario con hash de contraseña
f_h = open("hashes.txt", 'r', encoding="utf8")
hashes=f_h.readlines()
f_h.close()
#cargo las palabras del diccionario
f_d = open("diccionario.txt", 'r', encoding="utf8")
palabras=f_d.readlines()
f_d.close()
#recorro cada usuario con su hash
for linea in hashes:
    #quita saltos y divide en dos parte
    datos=linea.strip("\n").split(":")
    for palabra in palabras:
        palabra=palabra.strip("\n")
        hash_dicc=hashlib.md5(palabra.encode('utf8')).hexdigest()
        #print(datos[1],palabra,hash_dicc)
        if datos[1]==hash_dicc:
            print("ENCONTRADA:",datos[0]+"->"+palabra)
        






