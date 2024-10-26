import random #Impotar librería para generar números random (aleatorios)

results=[] #Lista vacía para guardar resultados de suma de fracciones

def cifras(op): #Función para generar números con las cifras solicitadas
    #Variables globales para suma, resta y multiplicación
    global n1
    global n2
    
    
    cif=int(input("¿Con cuántas cifras deseas trabajar? \n(Ingresa el número de opción)\n" "[1]Una cifra\n[2]Dos cifras\n[3]Tres cifras\n[4]Cuatro cifras\n"))
    if cif==1:
        #Generará números aleatorios de 1 cifra
        n1=random.randint(1,9)
        n2=random.randint(1,9)
    if cif==2:
        #Generará números aleatorios de 2 cifras
        n1=random.randint(10,99)
        n2=random.randint(10,99)
    if cif==3:
        #Generará números aleatorios de 3 cifras
        n1=random.randint(100,999)
        n2=random.randint(100,999)
    if cif==4:
        #Generará números aleatorios de 4 cifras
        n1=random.randint(1000,9999)
        n2=random.randint(1000,9999)
        
    #Validar que en la resta el primer número sea mayor que el segundo, si no es así que cambie de posición ambos números  
    if op=="2":
        if n1<n2:
            n1, n2=n2, n1

                    
                

def validar(): #Función para validar en resta que un número sea mayor que otro
    global n1 #Variables globales
    global n2
    cifras() #Manda llamar la función de cifras()

    if n1<n2:
        while n1<n2: #Se generarán números aleatorios hasta que el primer número sea mayor que el segundo
            n1=random.randint(1,999)
            n2=random.randint(1,999)
            
#FUNCIONES DE FRACCIONES       
def fracc1(listnums, listdens, a): #Función para ingresar el resultado
    
    print("Ingrese el resultado de la suma de las siguientes fracciones: ")
    for i in range(a):
        num=listnums[i] #Lista donde acumula la cantidad de numeradores
        den=listdens[i] #Lista donde acumula la cantidad de denominadores
        print(num, "/", den) #Imprime las fracciones a calcular
     
    
        
    
def sumadefrac(listnums, listdens, a): #Función para calcular la suma de fracciones usando el método cruzado
    
    if a==2: #Si se elige 2 fracciones
        y=listnums[0]*listdens[1] #Multiplica el primer elemento de la lista de numeradores por el segundo elemento de la lista de denominadores
        z=listnums[1]*listdens[0] #Multiplica el segundo elemento de la lista de numeradores por el primer elemento de la lista de denominadores
        denres=listdens[0]*listdens[1] #Multiplica los denominadores
        
        res1=y+z #Resultado de la suma
        res2=denres
        
        
    if a==3:
        #Si se elige 3 fracciones
        y=listnums[0]*listdens[1] #Multiplica el primer elemento de la lista de numeradores por el segundo elemento de la lista de denominadores
        z=listnums[1]*listdens[0] #Multiplica el segundo elemento de la lista de numeradores por el primer elemento de la lista de denominadores
        denres=listdens[0]*listdens[1] #Multiplica los denominadores
        
        res1=((y+z)*listdens[2])+(listnums[2]*denres) #Suma el resultado de sumar dos fracciones y el nuevo elemento de la lista de numeradores se multiploca por el denominador de la otra fracción
        res2=denres*listdens[2] #Resultado de multiplicar los denominadores
        
    if a==4:
        #Si se elige 4 fracciones.
        #Primero se hace la suma de dos fracciones
        y=listnums[0]*listdens[1] #Multiplica numerador con denominador
        z=listnums[1]*listdens[0] #Multiplica numerador con denominador
        denres=listdens[0]*listdens[1] #Multiplica denominadores
        #Del resultado obtenido se calcula la suma de las otras dos fracciones
        w=listnums[2]*listdens[3] #Multiplica numerador con denominador
        w2=listnums[3]*listdens[2] #Multiplica numerador con denominador
        denres2=listdens[2]*listdens[3] #Multiplica denominadores
        
        k=(y+z)*(denres2) #Resultado de las primeras dos fracciones
        k2=(denres)*(w+w2) #Resultado de las siguientes dos fracciones
        
        res1=k+k2 #Suma de los numeradores
        res2=denres*denres2 #Multiplicación de los denominadores
        
    resultadosdiv=residuo(res1, res2) #El resultado va a ser igual a la fracción ya simplificada
    
    #print(resultadosdiv)
    
    return resultadosdiv
         
def residuo(res1, res2): #Función para simplificar fracción
    global results
    results=[] #Lista vacía
    
    primos=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101] #Lista de números primos
    
    for n in primos:
        while res1%n==0 and res2%n==0: #Mientras el residuo de simplificar los resultados sea cero:
            res1=res1/n #Divide el resultado 1 entre cada número de la lista de números primos que sea divisible
            res2=res2/n #Divide el resultado 2 entre cada número de la lista de números primos que sea divisible
    #Acaba el ciclo
    v1=res1
    v2=res2
    #Se añaden los resultados a la lista "results"     
    results.append(int(v1)) 
    results.append(int(v2))
    
    return results


   #Función para contar respuestas correctas e incorrectas, total de operaciones realizadas y número de intentos en cada operación
def programa(cont,correctas,incorrectas,intentos): #Función para ejecutar todo el programa
    op=0
    
    cont=cont+1 #Contar número de operaciones
    #Imprime el menú
    print("Menú: \n" "[1]Suma\n[2]Resta\n[3]Multiplicación\n[4]División\n[5]Suma de fracciones")

    op=str(input("\n"+"Ingresa la operación a realizar:"+"\n"))
    
    #Si elige la opción "Suma"
    if op=="1" or op=="Suma" or op=="suma" or op=="SUMA" or op=="+": 
        cifras(op) #Manda llamar la función de cifras(op)
        s=n1+n2 #Realiza la operación
        answer=s-1
        intentos=0
        
        #Mientras la respuesta sea incorrecta contará el número de intentos y mostrará la operación para corregirla
        while answer!=s:
            if intentos<3:
                intentos=intentos+1 #Suma el número de intentos
                answer=int(input( "\n"+ str(n1)+ "+"+ str(n2)+ "= "+"\n")) #Mostrar de la operación
                if answer==s: #Si la respuesta es correcta
                    print("¡Muy bien! :D")
                    correctas=correctas+1 #Cuenta el número de respuestas correctas
                else:
                    if intentos<3:
                        print("Intenta otra vez")
                    else: #Si se acaban los tres intentos
                      print("Lo siento, ya no tienes más intentos")
                      incorrectas=incorrectas+1 #Suma respuestas incorrectas
                      answer=s
                      
    #Si elige la opción: "Resta"
    if op=="2" or op=="Resta" or op=="resta" or op=="RESTA": 
        cifras(op) #Manda llamar la función cifras (op)
        resta=n1-n2 #Se realiza la operación
        answer=resta-1
        intentos=0
        
        while answer!=resta: #Mientras la respuesta sea diferente al resultado correcto
             if intentos<3: #Si el número de intentos es menor que 3:
                intentos=intentos+1 #Cuenta el número de intentos
                answer=int(input("\n"+ str(n1)+ "-"+ str(n2)+ "= "+"\n")) #Muestra la operación
                if answer==resta: #Si la respuesta es correcta
                    print("¡Muy bien! :D")
                    correctas=correctas+1 #Suma número de respuestas correctas
                else:
                    if intentos<3: #Si el número de intentos es menor que 3
                        print("Intenta otra vez")
                    else:
                    #Si se acaban los tres intentos
                      print("Lo siento, ya no tienes más intentos")
                      incorrectas=incorrectas+1 #Suma número de respuestas incorrectas
                      answer=resta

     #Si elige la opción: "Multiplicación"            
    if op=="3" or op=="Multiplicación" or op=="Multiplicacion" or op=="MULTIPLICACION" or op=="multiplicacion" or op=="multiplicación":  
        cifras(op) #Manda llamar la función de cifras(op)
        m=n1*n2 #Realiza la operación
        answer=m-1
        intentos=0
        
        while answer!=m: #Mientras la respuesta sea incorrecta
            if intentos<3: #Si el número de intentos es menor que 3
                intentos=intentos+1 #Suma el número de inetntos
                answer=int(input("\n"+ str(n1)+ "x"+ str(n2)+ "= "+"\n")) #Mostrar la operación
                if answer==m: #Si la respuesta es correcta
                    print("¡Muy bien! :D")
                    correctas=correctas+1 #Suma número de respuestas correctas
                else:
                    if intentos<3: #Si el número de intentos es menor que 3
                        print("Intenta otra vez")
                    else:
                    #Si ya no hay más intentos
                      print("Lo siento, ya no tienes más intentos")
                      incorrectas=incorrectas+1 #Suma número de respuestas incorrectas
                      answer=m
    #Si elige la opción: "División"
    if op=="4" or op=="Division" or op=="division" or op=="División" or op=="división": 
        #Genera números aleatorios de 2 cifras tanto para el divisor como para el dividendo
        divisor=random.randint(0,99)
        dividendo=random.randint(0,99)
        
        while divisor>dividendo: #Mientras el divisor sea mayor que el dividendo
            #Generará nuevos números aleatorios
            divisor=random.randint(0,99)
            dividendo=random.randint(0,99)
            
        div=dividendo//divisor #Realiza la operación
        res1=dividendo%divisor #Calcula el residuo
        cociente=div-1
        intentos=0
        
        while cociente!=div or residuo!=res1: #Mientras el cociente y el residuo sean diferentes
            if intentos<3:#Si el número de intentos es menor que 3
                intentos=intentos+1 #Cuenta el número de intentos
                print(" \n"+ str(dividendo)+ "/"+ str(divisor)+ "= "+"\n") #Muestra la operación
                cociente=int(input("Escriba el cociente:"))
                residuo=int(input("Escriba el residuo:"))
             
                if cociente==div and residuo==res1: #Si los resultados son correctos
                    print("¡Muy bien! :D")
                    correctas=correctas+1 #Suma número de respuestas correctas
                else:
                    if intentos<3: #Si el número de intentos es menor que 3
                        print("Intenta de nuevo")
                    else:
                        #Si se acaba el número de intentos
                        print("Lo siento, ya no tienes más intentos")
                        incorrectas=incorrectas+1 #Suma número de respuestas incorrectas
                        cociente=div
                        residuo=res1
                        
    #Si elige la opción: "Suma de Fracciones"       
    if op=="5" or op=="Suma de fracciones" or op=="suma de fracciones" or op=="fracciones": 
        #cantfracc(cont,correctas,incorrectas,intentos)
        listnums=[] #Lista de numeradores dependiendo de la cantidad de fracciones
        listdens=[] #Lista de denominadores dependiendo de la cantidad de fracciones
    
        a=int(input("¿Con cuántas fracciones desea trabajar? (+2): "))
        x=a
        
        #Ciclo para generar números aleatorios para el numerador y el denominador
        for i in range(a):
            numerador=random.randint(1,10)
            denominador=random.randint(1,10)
            
            while numerador>denominador: #Mientras el numerador sea mayor que el denominador, generará nuevos números aleatorios
                numerador=random.randint(1,10)
                denominador=random.randint(1,10)
            #Acaba el ciclo while  
            listnums.append(numerador) #Añadirá a la lista los numeradores de acuerdo al número de fracciones
            listdens.append(denominador) #Añadirá a la lista los denominadores de acuerdo al número de fracciones
        #Acaba el ciclo for   
        fracc1(listnums, listdens, a) #Manda llamar la función fracc1(listnums,listdens,a)
        
        results=sumadefrac(listnums, listdens, a) #El resultado es igual a lo que se genere en la función de suma de fracciones
        
        respnum=results[0]-1
        intentos=1
           
        while respnum!=results[0] or respden!=results[1]: #Mientras el numerador y el denominador sean diferentes
              respnum=int(input("Ingrese el numerador (simplificado): "))
              respden=int(input("Ingrese el denominador (simplificado): "))
              if respnum==results[0] and respden==results[1]:#Si el numerador y el denominador son correctos
                   print("¡Muy bien! :D")
                   correctas=correctas+1 #Suma número de respuestas correctas
              else:
                if intentos<=2: #Si el número de intentos es menor o igual a 2
                    intentos=intentos+1 #Suma número de intentos
                    print("Intenta otra vez")
                    
                else:
                    #Si se acaba el número de intentos
                    print("Lo siento, ya no tienes más intentos")
                    incorrectas=incorrectas+1 #Suma número de respuestas incorrectas
                    respnum=results[0]
                    respden=results[1]
            


    #Acaba el ciclo
    rep=input("¿Quieres practicar otra operación? \nSí o No\n") #Corrobora si el usuario quiere seguir practicando
    if rep=="Sí" or rep=="Si" or rep=="si" or rep=="sí": #Si elige la opción "Sí"
        #Se repite todo el programa
        programa(cont,correctas,incorrectas,intentos) #Manda llamar la función de programa() para repetir
    else:#Si elige la opción "No"
        #Muestra en pantalla
        print("\nTotal de operaciones: ",cont)
        print("Correctas:",correctas)
        print("Incorrectas:",incorrectas)
        print("Muchas gracias por utilizar el programa,",nombrej.title(),",vuelve pronto :)")
        #Finaliza el programa
                
#PROGRAMA PRINCIPAL
global correctas #Variables globales
global incorrectas
global intentos
global nombrej
#Bienvenida
print("¡Bienvenido al programa PISITA!") 
nombrej=str(input("¿Cuál es tu nombre? "))
print("\n"+"¡Hola "+nombrej+"! ¿Qué deseas practicar hoy? ")
#Variables para los contadores
cont=0
correctas=0
incorrectas=0
intentos=0
programa(cont,correctas,incorrectas,intentos) 