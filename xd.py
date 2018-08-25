def insertar(lista,elemento):
    for i in range(len(lista)):
        if elemento < len(lista):
            lista.insert(i-1,elemento)
        if elemento > len(lista):
            lista.insert(i-1,elemento)
    print lista

listax=[2,3,4,5,7,8,9]
insertar(listax,50)
