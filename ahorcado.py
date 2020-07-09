pbuscada=input("Dime una palabra para buscar:").upper()
buscada=[]
encontrada=[]
for c in pbuscada:
    buscada.append(c)
    encontrada.append("-")
print(buscada)
print(encontrada)
fallos=0
while buscada!=encontrada and fallos<7:
    for c in encontrada:
        print(c,end="")
    letra=input("\nDime una letra:")
    if letra in buscada:
        for x in range(len(buscada)):
            if(buscada[x]==letra):
                encontrada[x]=letra
    else:
        fallos=fallos+1
if fallos==7:
    print("Eres un paquete")
else:
    print("Muy bien, la has adivinado")
    
