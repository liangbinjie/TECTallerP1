

def menuPolinomios():
    print("Has ingresado al modulo de polinomios, que deseas realizar?")
    print("1) Suma y resta de polinomios\n"+
        "2) Multiplicacion de polinomios\n"+
        "3) Grado de un polinomio\n"+
        "4) Polinomio Ordenado\n"+
        "5) Polinomio Incompleto\n"+
        "6) Salir")
    opcion = int(input("> "))
    corriendo = 1
    while corriendo != 0:
       
        if opcion == 1:
            sumres = input("Que desea hacer\n1) Restar\n2) Sumar\n> ")
            if sumres == "1":
                resta()
            elif sumres == "2":
                suma()
            input("Enter para continuar...")
            break

        elif opcion == 2:
            opcionM = int(input("Desea multiplicar\n1) Numero por polinomio\n2) Monomio por polinomio\n3) Polinomio por polinomio\n> "))
            if opcionM == 1:
                multiplicacionN()
            elif opcionM == 2:
                multiplicacionM()
            elif opcionM == 3:
                multiplicacionP()
            else:
                print("Opcion invalida")
            input("Enter para continuar...")
            break
        
        elif opcion == 3:
            gradoPolinomio()
            input("Enter para continuar...")
            break

        elif opcion == 4:
            esOrdenado()
            input("Enter para continuar...")
            break

        elif opcion == 5:
            esCompleto()
            input("Enter para continuar...")
            break
        
        elif opcion == 6:
            corriendo = 0

        else:
            print("Opcion invalida, ingrese nuevamente")
            opcion = int(input("> "))

def obtener(archivo): # funcion que convierte los polinomios del archivo en listas
    lista = []
    linea = archivo.readline().strip()
    while linea != '' or linea == '\n':
        lista.append(linea.replace('\n', '').split(';'))
        linea = archivo.readline().strip()
    for i in lista:
        i[0], i[2] = int(i[0]), int(i[2])
    
    return lista

# ordenamiento por medio de insercion
def ordenar(lista):
    for i in range(1, len(lista)):
        polinomio = lista[i]
        j = i - 1
        while j >= 0 and lista[j][2] > polinomio[2]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = polinomio

    return lista[::-1]

def suma():
    try:
        p1 = input("Ingrese el nombre del primer polinomio: ")
        p2 = input("Ingrese el nombre del segundo polinomio: ")
        a1 = open("Archivos"+f"\{p1}.txt", "r") # archivo 1
        a2 = open("Archivos"+f"\{p2}.txt", "r") # archivo 2
        poli1 = ordenar(obtener(a1))
        poli2 = ordenar(obtener(a2))
        aux = []
        for x in poli1:
            for y in poli2:
                if x[2] == y[2]:
                    x[0] = x[0] + y[0]
                    poli2.remove(y) # eliminamos esta lista, ya que no lo vamos a ocupar mas
                    aux.append(x) # agregamos la nueva suma a la lista

        for i in poli2: # agregamos los elementos que faltan y luego lo ordenamos
            aux.append(i)
        aux = ordenar(aux)
        res = ""
        for i in aux:
            operador = '+'
            if i[0] < 0:
                operador = ''
            res += f'{operador}{i[0]}{i[1]}{i[2]}'
        print(res[1:])


    except FileNotFoundError:
        print("No existe este archivo")
        
def resta():
    try:
        p1 = input("Ingrese el nombre del primer polinomio: ")
        p2 = input("Ingrese el nombre del segundo polinomio: ")
        a1 = open("Archivos"+f"\{p1}.txt", "r") # archivo 1
        a2 = open("Archivos"+f"\{p2}.txt", "r") # archivo 2
        # esOrdenado2(a1)
        # esOrdenado2(a2)
        poli1 = ordenar(obtener(a1))
        poli2 = ordenar(obtener(a2))
        aux = []
        for x in poli1:
            for y in poli2:
                if x[2] == y[2]:
                    x[0] = x[0] - y[0]
                    poli2.remove(y) # eliminamos esta lista, ya que no lo vamos a ocupar mas
                    aux.append(x) # agregamos la nueva suma a la lista

        for i in poli2: # agregamos los elementos que faltan y luego lo ordenamos
            aux.append(i)
        aux = ordenar(aux)
        res = ""
        for i in aux:
            operador = '+'
            if i[0] < 0:
                operador = ''
                y[0] = y[0] * -1
            res += f'{operador}{i[0]}{i[1]}{i[2]}'
        print(res[1:])

    except FileNotFoundError:
        print("No existe este archivo")

def multiplicacionN(): # Multiplicacion numero por polinomio
    try:
        p1 = input("Ingrese el nombre del primer polinomio: ")
        num = int(input("Ingrese el numero a multiplicar: "))
        a1 = open("Archivos"+f"\{p1}.txt", "r") # archivo 1
        # esOrdenado2(a1)
        poli1 = ordenar(obtener(a1))
        for polinomio in poli1:
            polinomio[0] *= num
        
        res = ""
        for i in poli1:
            operador = '+'
            if i[0] < 0:
                operador = ''
            res += f'{operador}{i[0]}{i[1]}{i[2]}'
        print(res[1:])

    except FileNotFoundError:
        print("No existe este archivo")

def multiplicacionM(): # Multiplicacion monomio por polinomio
    try:
        p1 = input("Ingrese el nombre del archivo del polinomio: ")
        m1 = input("Ingrese el nombre del archivo del monomio: ")
        a1 = open("Archivos"+f"\{p1}.txt", "r") # abriendo archivo del polinomio
        m1 = open("Archivos"+f'\{m1}.txt', "r") # abriendo archivo del monomio
        # esOrdenado2(a1)
        poli1 = ordenar(obtener(a1))
        mono1 = m1.readline().split(";")
        for polinomio in poli1:
            polinomio[0] *= int(mono1[0])
            polinomio[2] += int(mono1[2])
        
        res = ""
        for i in poli1:
            operador = '+'
            if i[0] < 0:
                operador = ''
            res += f'{operador}{i[0]}{i[1]}{i[2]}'
        print(res[1:])

    except FileNotFoundError:
        print("No existe este archivo")

def multiplicacionP():
    try:
        p1 = input("Ingrese el nombre del archivo del polinomio: ")
        p2 = input("Ingrese el nombre del archivo del monomio: ")
        a1 = open("Archivos"+f"\{p1}.txt", "r") # abriendo archivo del polinomio
        a2 = open("Archivos"+f'\{p2}.txt', "r") # abriendo archivo del polinomio
        poli1 = ordenar(obtener(a1))
        poli2 = ordenar(obtener(a2))
        lista = []
        for poli_1 in range(len(poli1)):
            for poli_2 in range(len(poli2)):
                lista.append([poli1[poli_1][0]*poli2[poli_2][0],'x',poli1[poli_1][2]+poli2[poli_2][2]])
        similar = {}
        for term in lista:
            if term[2] in similar:
                similar[term[2]] += term[0]
            else:
                similar[term[2]] = term[0]
        res = []
        for term in lista:
            if term[2] in similar:
                res.append([similar[term[2]], term[1], term[2]])
                similar.pop(term[2])
        res = ordenar(res)
        out = ""
        for term in res:
            op = '+'
            if term[0] < 0:
                op = ''
            out += f'{op}{term[0]}x{term[2]}'

        if out[1] == '-':
            print(out)
        else:
            print(out[1:])

    except FileNotFoundError:
        print("No existe este archivo")

def gradoPolinomio():
    try:
        p1 = input("Ingrese el nombre del archivo del polinomio: ")
        a1 = open("Archivos"+f"\{p1}.txt", "r") # abriendo archivo del polinomio
        # esOrdenado2(a1)
        poli = ordenar(obtener(a1))
        grado = poli[0][2]
        print("El grado del polinomio seleccionado es: ", grado)

    except FileNotFoundError:
        print("No existe este archivo")
    
def esOrdenado():
    try:
        p = input("Ingrese el nombre del archivo del polinomio: ")
        p = open("Archivos"+f"\{p}.txt", "r") # abriendo archivo del polinomio
        polinomio = obtener(p)
        copia = ordenar(polinomio)
        grado = copia[0][2]
        polinomio = polinomio[::-1]
        lista = []
        for i in range(grado+1):
            lista = [i] + lista

        for i in range(len(polinomio)):
            if polinomio[i][2] == lista[i]:
                pass
            else:
                resultadoI()
                print(False)
                return False
        if len(lista) > len(polinomio):
            resultadoI()
            print(False)
            return False
        resultadoO()
        print(True)
        return True 

    except FileNotFoundError:
        print("No existe este polinomio")

def esCompleto(): # funcion para verificar si es completo el polinomio
    try:
        p = input("Ingrese el nombre del archivo del polinomio: ")
        p = open("Archivos"+f"\{p}.txt", "r") # abriendo archivo del polinomio
        polinomio = obtener(p)
        copia = ordenar(polinomio)
        grado = copia[0][2]
        polinomio = polinomio[::-1]
        lista = []
        for i in range(grado+1):
            lista = [i] + lista

        for i in range(len(polinomio)):
            if polinomio[i][2] == lista[i]:
                pass
            else:
                print(f'Falta x{i+1}')
                resultadoI()
                print(False)
                return False
        if len(lista) > len(polinomio):
            print("Falta x0")
            resultadoI()
            print(False)
            return False
        resultadoO()
        print(True)
        return True 

    except FileNotFoundError:
        print("No existe este polinomio")

def resultadoO(): # cantidad de polinomios ordenados
    a = open('resultados.txt', "r")
    linea = a.readline().strip().split(";")
    for i in range(len(linea)):
        linea[i] = int(linea[i])
    linea[2] = linea[2] + 1
    o = ""
    for i in linea:
        o += ";"+str(i)
    r = open("resultados.txt", "w")
    r.write(o[1::])
    r.close()

def resultadoI(): # cantidad de polinomios incompletos
    a = open('resultados.txt', "r")
    linea = a.readline().strip().split(";")
    for i in range(len(linea)):
        linea[i] = int(linea[i])
    linea[3] = linea[3] + 1
    o = ""
    for i in linea:
        o += ";"+str(i)
    r = open("resultados.txt", "w")
    r.write(o[1::])
    r.close()
