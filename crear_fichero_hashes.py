import hashlib
f = open("hashes.txt", 'w')
for n in range (5):
    nombre=input("Introduzca usuario:")
    password=input("Introduzca contraseña:")
    h=hashlib.md5(password.encode('UTF8')).hexdigest()
    print(h)
    f.write(nombre+":"+h+"\n")
f.close()
    
    

    
