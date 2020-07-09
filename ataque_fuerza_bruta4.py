import hashlib
#cargo la lista de usuario con hash de contraseña
f_h = open("hashes.txt", 'r', encoding="utf8")
hashes=f_h.readlines()
f_h.close()
#recorro cada usuario con su hash
letras="abcdefghijklmnopqrstuvwxyz1234567890"
for linea in hashes:
    #quita saltos y divide en dos parte
    datos=linea.strip("\n").split(":")
    for letra1 in letras:
        for letra2 in letras:
            for letra3 in letras:
                for letra4 in letras:
                    palabra=letra1+letra2+letra3+letra4
                    hash_dicc=hashlib.md5(palabra.encode('utf8')).hexdigest()
                    #print(palabra)
                    if datos[1]==hash_dicc:
                        print("ENCONTRADA:",datos[0]+"->"+palabra)
                        break
        
