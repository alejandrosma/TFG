#Programa para recoger todas las energías que han aparecido en un
#determinado cálculo, así como el nombre las estructuras con una
#determinada energía en un diccionario dict(tot). Se seleccionan las
#estructuras con una energía umbral por debajo de la mejor del cálculo
#y en doc4 se guardan sus POSCARS. En doc5 se guardan las energías de
#las estructuras seleccionadas


def energy(doc1,doc2,doc3,doc4,doc5):
    fp1=open(doc1,'r') #INDIVIDUALS (1_CaAlO_13H_20)
    fp2=open(doc2,'w') #ESTRUCTURAS SELECCIONADAS (1_E)
    fp5=open(doc5,'w') #ENERGÍA DE LAS ESTRUCTURAS SELECCIONADAS (1_ENERGIA)
    linea1=fp1.readline() #Leo linea 1
    linea2=fp1.readline() #Leo linea 2
    linea=fp1.readline() #Comenzamos leyendo la tercera linea
    tot=dict()
    
    while linea:
        linea=linea.split()
        e=linea[9] #Energía de la estructura (8 para Cluster1 y 9 para resto)
        e=float(e)
        e="{:.3f}".format(e) #3 decimales para la energia
        num='EA'+linea[1] #Número de la estructura
        if e in tot.keys():
            tot[e].append(num)#Si e ya es una clave, añade un nuevo valor
        else:
            tot[e]=[num]
        linea=fp1.readline()
        
    claves=list(tot.keys())
    valores=list(tot.values())
    claves.sort()
    claves.reverse() #En claves se guardan las energías de menor a mayor

    for i in range (len(claves)): 
        fp2.write(str(claves[i])+'\t'+tot[claves[i]][0]+'\n')
        
        #NOTA: Escogemos una estructura para "representar dicha energía"
        #mediante tot[claves[i]][0]

        
    fp1.close()
    fp2.close()

    fp3=open(doc3,'r') #POSCARS_TOTAL (1_POSCARS_TOTAL)
    fp4=open(doc4,'w') #POSCARS_SELECCIONADOS (1_POSCARS)

    
    x=44+8 #numero total de átomos de la estructura
            #Cluster1=35
            #Cluster2=70
            #Cluster3=44
            #Cluster4=44

    ev=4 #Energia umbral por debajo de la energía mínima
            #Cluster1=2eV => 856 estructuras
            #Cluster2=3eV => 766 estructuras
            #Cluster3=4eV => 802 estructuras
            #Cluster4=4eV => 886 estructuras

    #Determinamos cual es la energía más cercana a la umbral dentro de la lista

    diferencia=[]
    for m in range (len(claves)):
        diferencia.append(abs(float(claves[m])-(float(claves[0])+ev)))

    min_value=min(diferencia)
    print ('Minima energía:', claves[0])
    print ('Máxima energía:', claves[len(claves)-1])
    print ('Energia umbral:', float(claves[0])+ev)
    min_index=diferencia.index(min_value)
    print ('Energia umbral real:', claves[min_index])
    print ('Numero de estructuras seleccionadas:', min_index+1)

    #Escribimos en doc5 la energía de las estructuras seleccionadas (1_ENERGIA)

    for n in range (min_index+1):
        fp5.write(str(claves[n])+'\n')
    
    lineas=fp3.readlines()

    for j in range (min_index+1):
        pos=buscar (tot[claves[j]][0],doc3)
        for k in range (x):
            # Escribimos las lineas del poscar de la estructura
            fp4.write(lineas[pos+k])

    fp3.close()    
    fp4.close()
    fp5.close()
    
    return doc4

def buscar (string,doc):
    fp=open(doc,'r')
    linea=fp.readline()
    flag=0
    while linea:
        if string in linea:
            return flag
        else:
            flag=flag+1
            linea=fp.readline()

#Programa para tener en un fichero doc2, las energías de los mejores
#individuos de cada generación, para su posterior representación


def bestindividuals (doc1,doc2):
    #Función para Gráficas aux.
    
    fp1=open(doc1,'r') #BESTIndividuals
    fp2=open(doc2,'w') #Energia de Best individuals
    linea1=fp1.readline() #Leo linea 1
    linea2=fp1.readline() #Leo linea 2
    linea=fp1.readline() #Comenzamos leyendo la tercera linea

    gen=1
    while linea:
        linea=linea.split()
        e=linea[8] #Energía de la estructura (8 para Cluster1 y 9 para resto)
        e=float(e)
        e="{:.3f}".format(e)
        fp2.write(str(gen)+'\t'+str(e)+'\n')
        linea=fp1.readline()
        gen=gen+1
        
    fp1.close()
    fp2.close()

    return doc2
        


    
