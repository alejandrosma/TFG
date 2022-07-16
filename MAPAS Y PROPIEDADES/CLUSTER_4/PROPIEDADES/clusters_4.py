def clusters_4(doc1,doc2,doc3):

    from ase import Atoms
    from ase.io import read
    from ase.visualize import view
    import os

    #doc1 es el documento del que extraemos el numero de estructuras
    #con las que trabajamos de un cluster determinado (2_ENERGIA)

    fp1=open (doc1, 'r')

    #En un nuevo archivo 2_ENERGIA_NORM, se escriben las energías
    #de 2_ENERGIA, pero normalizadas

    fp=open ('4_ENERGIA_NORM', 'w')

    num_struc=0
    linea=fp1.readline()
    ref=float(linea)
    while linea:
        fp.write (str(float(linea)-ref)+'\n')
        num_struc=num_struc+1
        linea=fp1.readline()

    print (num_struc)
    fp1.close()
    fp.close()
    
    #En doc2 se encuentran los POSCARS de las estructuras. Cada estructura tiene:
    #Cluster1=35+8
    #Cluster2=70+8
    #Cluster3=44+8
    #Cluster4=44+8

    data_struc=44+8

    fp2=open (doc2, 'r')

    #En doc3 recogeremos las propiedades de las estructuras
    fp3=open (doc3, 'w')

    #Las propiedades individuales se recogen en los siguientes archivos:
    fp3_1=open ('4_DISTmin_Ca_Al', 'w')
    fp3_2=open ('4_DISTmed_Ca_Al', 'w')
    fp3_3=open ('4_DISTmin_Si_Al', 'w')
    fp3_4=open ('4_DISTmed_Si_Al', 'w')
    fp3_5=open ('4_DISTmin_Ca_Si', 'w')
    fp3_6=open ('4_DISTmed_Ca_Si', 'w')
    fp3_7=open ('4_COOR_Ca1', 'w')
    fp3_8=open ('4_COOR_Ca2', 'w')
    fp3_9=open ('4_COOR_Ca3', 'w')
    fp3_10=open ('4_COOR_Ca4', 'w')
    fp3_11=open ('4_COORmed_Ca', 'w')
    fp3_12=open ('4_COOR_Al1', 'w')
    fp3_13=open ('4_COOR_Al2', 'w')
    fp3_14=open ('4_COORmed_Al', 'w')
    fp3_15=open ('4_COOR_Si1', 'w')
    fp3_16=open ('4_COOR_Si2', 'w')
    fp3_17=open ('4_COORmed_Si', 'w')
    fp3_18=open ('4_H2O', 'w')
    fp3_19=open ('4_ENLACES_Ca-O-Al', 'w')
    fp3_20=open ('4_ENLACES_Ca-O-H-Al', 'w')
    fp3_21=open ('4_ENLACES_Si-O-Si', 'w')
    fp3_22=open ('4_ENLACES_Si-O-Al', 'w')
    fp3_23=open ('4_ENLACES_Al-O-Al', 'w')
    


    for i in range (num_struc):
        #Archivo auxiliar que se manda a ase_read con el POSCAR de una
        #determianda estructura
        fp4=open ('STRUCTURE', 'w')
        j=0
        for j in range (data_struc):
            linea=fp2.readline()
            #Si es la primera linea, guardamos además el nombre de la
            #estructura (P.ej:EA861)
            if j==0:
                linea_lista=linea.split()
                nombre=linea_lista[0]
            fp4.write(linea)
            
        fp4.close()
        POSCAR=read ('STRUCTURE', format='vasp')
        #Una vez tenemos el POSCAR de la estructura en cuestión
        #comenzamos a analizar las propiedades. En doc3 se guardan
        #todas las propiedades de las estructuras. Los datos de cada
        #una de las propiedades se guardan en archivos individuales
        fp3.write (nombre+'\n')

        #Distancias Ca-Al
        d_Ca1_Al=dist('Ca','Al',POSCAR,atom1_aux=0)
        d_Ca2_Al=dist('Ca','Al',POSCAR,atom1_aux=1)
        d_Ca3_Al=dist('Ca','Al',POSCAR,atom1_aux=2)
        d_Ca4_Al=dist('Ca','Al',POSCAR,atom1_aux=3)
        
        #Distancia min Ca-Al
        d_min_Ca_Al=min(d_Ca1_Al,d_Ca2_Al,d_Ca3_Al,d_Ca4_Al)
        fp3.write('Distancia min Ca-Al:'+str(d_min_Ca_Al)+'\n')

        fp3_1.write(str(d_min_Ca_Al)+'\n')

        #Distancia media Ca-Al
        d_med_Ca_Al=(d_Ca1_Al+d_Ca2_Al+d_Ca3_Al+d_Ca4_Al)/4
        fp3.write('Distancia media Ca-Al:'+str(d_med_Ca_Al)+'\n')

        fp3_2.write(str(d_med_Ca_Al)+'\n')


        #Distancias Si-Al
        d_Si1_Al1=dist('Si','Al',POSCAR,atom1_aux=0)
        d_Si2_Al1=dist('Si','Al',POSCAR,atom1_aux=1)
        
        d_min_Si_Al1=min (d_Si1_Al1,d_Si2_Al1)
        d_med_Si_Al1=(d_Si1_Al1+d_Si2_Al1)/2
        
        d_Si1_Al2=dist('Si','Al',POSCAR,atom1_aux=2,atom2_aux=1)
        d_Si2_Al2=dist('Si','Al',POSCAR,atom1_aux=2,atom2_aux=1)
        
        d_min_Si_Al2=min (d_Si1_Al2,d_Si2_Al2)
        d_med_Si_Al2=(d_Si1_Al2+d_Si2_Al2)/2

        #Distancia min Si-Al
        d_min_Si_Al=min(d_min_Si_Al1,d_min_Si_Al2)
        fp3.write('Distancia min Si-Al:'+str(d_min_Si_Al)+'\n')

        fp3_3.write(str(d_min_Si_Al)+'\n')

        #Distancia media Si-Al
        d_med_Si_Al=(d_med_Si_Al1+d_med_Si_Al2)/2
        fp3.write('Distancia media Si-Al:'+str(d_med_Si_Al)+'\n')

        fp3_4.write(str(d_med_Si_Al)+'\n')
    

        #Distancias Ca-Si
        d_Ca1_Si1=dist('Ca','Si',POSCAR,atom1_aux=0)
        d_Ca2_Si1=dist('Ca','Si',POSCAR,atom1_aux=1)
        d_Ca3_Si1=dist('Ca','Si',POSCAR,atom1_aux=2)
        d_Ca4_Si1=dist('Ca','Si',POSCAR,atom1_aux=3)

        d_min_Ca_Si1=min(d_Ca1_Si1,d_Ca2_Si1,d_Ca3_Si1,d_Ca4_Si1)
        d_med_Ca_Si1=(d_Ca1_Si1+d_Ca2_Si1+d_Ca3_Si1+d_Ca4_Si1)/4

        d_Ca1_Si2=dist('Ca','Si',POSCAR,atom1_aux=0,atom2_aux=1)
        d_Ca2_Si2=dist('Ca','Si',POSCAR,atom1_aux=1,atom2_aux=1)
        d_Ca3_Si2=dist('Ca','Si',POSCAR,atom1_aux=2,atom2_aux=1)
        d_Ca4_Si2=dist('Ca','Si',POSCAR,atom1_aux=3,atom2_aux=1)

        d_min_Ca_Si2=min(d_Ca1_Si2,d_Ca2_Si2,d_Ca3_Si2,d_Ca4_Si2)
        d_med_Ca_Si2=(d_Ca1_Si2+d_Ca2_Si2+d_Ca3_Si2+d_Ca4_Si2)/4

        
        #Distancia min Ca-Si
        d_min_Ca_Si=min(d_min_Ca_Si1,d_min_Ca_Si2)
        fp3.write('Distancia min Ca-Si:'+str(d_min_Ca_Si)+'\n')

        fp3_5.write(str(d_min_Ca_Si)+'\n')
        
        
        #Distancia media Ca-Si
        d_media_Ca_Si=(d_med_Ca_Si1+d_med_Ca_Si2)/2
        fp3.write('Distancia media Ca-Si:'+str(d_media_Ca_Si)+'\n')
        
        fp3_6.write(str(d_media_Ca_Si)+'\n')

        #Número de coordinación del Ca (Con O)
        cutoff_Ca=2.83062
        coor_Ca1=num_coor('Ca','O',POSCAR,cutoff_Ca,atom1_aux=0)
        coor_Ca2=num_coor('Ca','O',POSCAR,cutoff_Ca,atom1_aux=1)
        coor_Ca3=num_coor('Ca','O',POSCAR,cutoff_Ca,atom1_aux=2)
        coor_Ca4=num_coor('Ca','O',POSCAR,cutoff_Ca,atom1_aux=3)
        fp3.write('Coordinación Ca1 (cutoff='+str(cutoff_Ca)+'):'+str(coor_Ca1)+'\n')
        fp3.write('Coordinación Ca2 (cutoff='+str(cutoff_Ca)+'):'+str(coor_Ca2)+'\n')
        fp3.write('Coordinación Ca3 (cutoff='+str(cutoff_Ca)+'):'+str(coor_Ca3)+'\n')
        fp3.write('Coordinación Ca4 (cutoff='+str(cutoff_Ca)+'):'+str(coor_Ca4)+'\n') 
        fp3.write('Coordinación media Ca (cutoff='+str(cutoff_Ca)+'):'\
                  +str((coor_Ca1+coor_Ca2+coor_Ca3+coor_Ca4)/4)+'\n')

        fp3_7.write(str(coor_Ca1)+'\n')
        fp3_8.write(str(coor_Ca2)+'\n')
        fp3_9.write(str(coor_Ca3)+'\n')
        fp3_10.write(str(coor_Ca4)+'\n')
        fp3_11.write(str((coor_Ca1+coor_Ca2+coor_Ca3+coor_Ca4)/4)+'\n')

                
        #Número de coordinación del Al (Con O)
        cutoff_Al=2.1074
        coor_Al1=num_coor('Al','O',POSCAR,cutoff_Al,atom1_aux=0)
        coor_Al2=num_coor('Al','O',POSCAR,cutoff_Al,atom1_aux=1)
        fp3.write('Coordinación Al1 (cutoff='+str(cutoff_Al)+'):'+str(coor_Al1)+'\n')
        fp3.write('Coordinación Al2 (cutoff='+str(cutoff_Al)+'):'+str(coor_Al1)+'\n')
        fp3.write('Coordinación media Al(cutoff='+str(cutoff_Al)+'):'\
                  +str((coor_Al1+coor_Al2)/2)+'\n')
        
        fp3_12.write(str(coor_Al1)+'\n')
        fp3_13.write(str(coor_Al2)+'\n')
        fp3_14.write(str((coor_Al1+coor_Al2)/2)+'\n')

        #Número de coordinación del Si (Con O)
        cutoff_Si=1.99002
        coor_Si1=num_coor('Si','O',POSCAR,cutoff_Ca,atom1_aux=0)
        coor_Si2=num_coor('Si','O',POSCAR,cutoff_Ca,atom1_aux=1)

        fp3.write('Coordinación Si1 (cutoff='+str(cutoff_Si)+'):'+str(coor_Si1)+'\n')
        fp3.write('Coordinación Si2 (cutoff='+str(cutoff_Si)+'):'+str(coor_Si2)+'\n')
        fp3.write('Coordinación media Si (cutoff='+str(cutoff_Si)+'):'\
                  +str((coor_Si1+coor_Si2)/2)+'\n')

        fp3_15.write(str(coor_Si1)+'\n')
        fp3_16.write(str(coor_Si2)+'\n')
        fp3_17.write(str((coor_Si1+coor_Si2)/2)+'\n')
        
        #Número de moléculas de H2O
        H2O=num_agua(POSCAR)
        fp3.write('Número de moléculas de H2O:'+str(H2O)+'\n')
        
        fp3_18.write(str(H2O)+'\n')

        #Número de enlaces Ca-O-Al
        enlaces_Ca_O_Al=num_enlaces_Ca_O_Al(POSCAR)
        fp3.write('Número de enlaces Ca-O-Al:'+str(enlaces_Ca_O_Al)+'\n')
        
        fp3_19.write(str(enlaces_Ca_O_Al)+'\n')

        #Número de enlaces Ca-O-H-Al
        enlaces_Ca_O_H_Al=num_enlaces_Ca_O_H_Al(POSCAR)
        fp3.write('Número de enlaces Ca-O-H-Al:'+str(enlaces_Ca_O_H_Al)+'\n')
        
        fp3_20.write(str(enlaces_Ca_O_H_Al)+'\n')

        #Número de enlaces Si-O-Si
        enlaces_Si_O_Si=num_enlaces_Si_O_Si(POSCAR)
        fp3.write('Número de enlaces Si-O-Si:'+str(enlaces_Si_O_Si)+'\n')
        
        fp3_21.write(str(enlaces_Si_O_Si)+'\n')

        #Número de enlaces Al-O-Si
        enlaces_Al_O_Si=num_enlaces_Al_O_Si(POSCAR)
        fp3.write('Número de enlaces Al-O-Si:'+str(enlaces_Al_O_Si)+'\n')
        
        fp3_22.write(str(enlaces_Al_O_Si)+'\n')

        #Número de enlaces Al-O-Al
        enlaces_Al_O_Al=num_enlaces_Al_O_Al(POSCAR)
        fp3.write('Número de enlaces Al-O-Al:'+str(enlaces_Al_O_Al)+'\n')
        
        fp3_23.write(str(enlaces_Al_O_Al)+'\n')
        
        #destruimos el archivo temporal
        os.remove('STRUCTURE')
    
    fp2.close()
    fp3.close()
    fp3_1.close()
    fp3_2.close()
    fp3_3.close()
    fp3_4.close()
    fp3_5.close()
    fp3_6.close()
    fp3_7.close()
    fp3_8.close()
    fp3_9.close()
    fp3_10.close()
    fp3_11.close()
    fp3_12.close()
    fp3_13.close()
    fp3_14.close()
    

def dist (atom1,atom2,atoms,atom1_aux=0,atom2_aux=0):
    #Distancia entre los átomos atom1 y atom2, pertenecientes a
    #atoms. En el caso de que haya más de un atom1/atom2 en atoms
    #se icluye atom1_aux/atom2_aux para especificar a que atomo1/atomo2
    #nos referimos
    
    atoms_symbols=atoms.get_chemical_symbols()
    atom1=atoms_symbols.index(atom1)
    #En el caso de que se especifique el atom1_aux
    atom1=atom1+atom1_aux

    atom2=atoms_symbols.index(atom2)
    #En el caso de que se especifique el atom2_aux
    atom2=atom2+atom2_aux

    d_atom1_atom2=atoms.get_distance(atom1,atom2)

    return d_atom1_atom2



def num_coor (atom1,atom2,atoms,cutoff,atom1_aux=0):
    # atom1 es el atomo de referencia, i.e. aquel cuyo num. de
    #coordinación queremos conocer. lista es la lista que contiene los
    #indices de los átomos con los que se coordina, denominados como atom2
    #Esta se construye a partir de atoms y atoms_symbol. En el caso de
    #que haya más de un atom1 en la estructura (P.ej Ca_2), para
    #especificar de que átomo queremos calcular el numero de coordinación
    #esta la entrada atom1_aux. 
    
    atoms_symbols=atoms.get_chemical_symbols()
    atom1=atoms_symbols.index(atom1)
    #En el caso de que se especifique el atom1_aux
    atom1=atom1+atom1_aux

    lista=[]
    
    for i in range (len(atoms_symbols)):
        if (atoms_symbols[i]==atom2):
            lista.append(i)
           
    d=atoms.get_distances(atom1,lista)

    #Una vez tenemos las distancias entre el atomo1 y los atomo2,
    #establecemos un cutoff para determianr el número de coordinación
    #Este es una entrada de la función y sus unidades son Angstrom

    num_coor=0
    
    for j in range (len(d)):
        if (d[j]<=cutoff):
            num_coor=num_coor+1
    
    return num_coor

def num_agua(atoms):
    #Dado un conjunto de atoms, determinamos el numero de moléculas de
    #H20 que hay en el. Para ello, nos situamos en 1 O determinado,
    #comprobamos si en su entorno hay 2 H a una distancia 0.7<d<1.2,
    #(teniendo en cuenta que la distancia entre O-H para una molécula
    #de H2O es d=0.95 Ang)

    atoms_symbols=atoms.get_chemical_symbols()

    #Construimos una lista con los índices en la que se encuentran los O

    lista_O=[]
    for i in range (len(atoms_symbols)):
        if (atoms_symbols[i]=='O'):
            lista_O.append(i)

    #Construimos una lista con los índices en la que se encuentran los H

    lista_H=[]
    for j in range (len(atoms_symbols)):
        if (atoms_symbols[j]=='H'):
            lista_H.append(j)

    #Para cada O, comprobamos si hay 2 H ceranos, en el rango de
    #distancias 0.7<d<1.2. Para ello, utilizamos 1 variable
    #booleana, ok1 (a encontrado un H a esa dist). Si ok1=true y 
    #a encontrado otro H a esa distancia, tenemos una molécula de
    #H2O)

    #número de moléculas de H2O
    H2O=0

    for k in range (len(lista_O)):
        l=0
        ok1=False
        for l in range (len(lista_H)):
            d=atoms.get_distances(lista_O[k],lista_H[l])
            #Condicional para activar ok1
            if (0.7<=d<=1.2) and (ok1==False):
                ok1=True
                continue
            #Condicional por si se encuentra otro H cercano al O
            if (0.7<=d<=1.2) and (ok1==True):
                H2O=H2O+1

    return H2O

def num_enlaces_Ca_O_Al (atoms):

    #Dado un objeto atoms(), determianmos el número de cadenas Ca_O_Al

    atoms_symbols=atoms.get_chemical_symbols()

    #cutoffs para los enlaces de diferentes parejas de átomos (VESTA)

    d_Ca_O=2.83062
    d_Al_O=2.1074

    #Identificamos los índices de los atomos de la cadena. lista es una
    #lista de listas. En la primera posición p.ej se guardan los índices
    #de los átomos que aparece en la primera posición de atoms_cadena
    #p.ej, 'Ca'

    lista=[[],[],[]]
    atoms_cadena=['Ca', 'O', 'Al']
    for i in range (3):
        j=0
        for j in range (len(atoms_symbols)):
            if (atoms_symbols[j]==atoms_cadena[i]):
                lista[i].append(j)


    #Una vez tenemos la lista de listas, vemos cuantos enlaces/cadenas
    #de átomos hay como la especificada en la entrada de la función.

    enlaces=0

    for k in range (len(lista[0])): #Recorremos todos los Ca (índice k)
        j=0
        for j in range (len(lista[1])): #Recorremos todos los O (índice j)
            l=0
            for l in range (len(lista[2])): #Recorremos todos los Al (índice l)
                if (atoms.get_distances(lista[0][k],lista[1][j])<=d_Ca_O) \
                and (atoms.get_distances(lista[2][l],lista[1][j])<=d_Al_O):
                    enlaces=enlaces+1
    

    return enlaces
                    
def num_enlaces_Ca_O_H_Al (atoms):

    #Dado un objeto atoms(), determianmos el número de cadenas Ca_O_H_Al

    atoms_symbols=atoms.get_chemical_symbols()

    #cutoffs para los enlaces de diferentes parejas de átomos (VESTA)

    d_Ca_O=2.83062
    d_Al_O=2.1074
    d_O_H=1.2

    #Identificamos los índices de los atomos de la cadena. lista es una
    #lista de listas. En la primera posición p.ej se guardan los índices
    #de los átomos que aparece en la primera posición de atoms_cadena
    #p.ej, 'Ca'

    lista=[[],[],[],[]]
    atoms_cadena=['Ca', 'O', 'H', 'Al']
    for i in range (4):
        j=0
        for j in range (len(atoms_symbols)):
            if (atoms_symbols[j]==atoms_cadena[i]):
                lista[i].append(j)


    #Una vez tenemos la lista de listas, vemos cuantos enlaces/cadenas
    #de átomos hay como la especificada en la entrada de la función.

    enlaces=0

    for k in range (len(lista[0])): #Recorremos todos los Ca (índice k)
        j=0
        for j in range (len(lista[1])): #Recorremos todos los O (índice j)
            l=0
            for l in range (len(lista[2])): #Recorremos todos los H (índice l)
                m=0
                for m in range (len(lista[3])): #Recorremos todos los Al (índice m)
                    if (atoms.get_distances(lista[0][k],lista[1][j])<=d_Ca_O) \
                    and (atoms.get_distances(lista[3][m],lista[1][j])<=d_Al_O)\
                    and (atoms.get_distances(lista[1][j],lista[2][l])<=d_O_H):
                        enlaces=enlaces+1
    

    return enlaces                 
        
def num_enlaces_Si_O_Si (atoms):
    #Dado un objeto atoms(), determianmos el número de cadenas Si_O_Si

    atoms_symbols=atoms.get_chemical_symbols()

    #cutoffs para los enlaces de diferentes parejas de átomos (VESTA)

    d_Si_O=1.99002

    #Identificamos los índices de los atomos de la cadena. lista es una
    #lista de listas. En la primera posición p.ej se guardan los índices
    #de los átomos que aparece en la primera posición de atoms_cadena
    #p.ej, 'Si'

    lista=[[],[]]
    atoms_cadena=['Si', 'O']
    for i in range (2):
        j=0
        for j in range (len(atoms_symbols)):
            if (atoms_symbols[j]==atoms_cadena[i]):
                lista[i].append(j)


    #Una vez tenemos la lista de listas, vemos cuantos enlaces/cadenas
    #de átomos hay

    enlaces=0

    for k in range (len(lista[1])): #Recorremos todos los O (índice k)
        j=0
        for j in range (len(lista[0])): #Recorremos todos los Si (índice j)
                if (atoms.get_distances(lista[1][k],lista[0][j])<=d_Si_O):
                    for l in range (len(lista[0])): #Recorremos de nuevo los Si (índice l)
                        #Nos saltamos el caso de coger el mismo átomo de Si 2 veces
                        if (l==j):
                            continue
                        if (atoms.get_distances(lista[1][k],lista[0][l])<=d_Si_O):
                            enlaces=enlaces+1

    
    return enlaces                 

def num_enlaces_Al_O_Si (atoms):
    #Dado un objeto atoms(), determianmos el número de cadenas Al_O_Si

    atoms_symbols=atoms.get_chemical_symbols()

    #cutoffs para los enlaces de diferentes parejas de átomos (VESTA)

    d_Al_O=2.1074
    d_Si_O=1.99002

    #Identificamos los índices de los atomos de la cadena. lista es una
    #lista de listas. En la primera posición p.ej se guardan los índices
    #de los átomos que aparece en la primera posición de atoms_cadena
    #p.ej, 'Al'

    lista=[[],[],[]]
    atoms_cadena=['Al', 'O', 'Si']
    for i in range (3):
        j=0
        for j in range (len(atoms_symbols)):
            if (atoms_symbols[j]==atoms_cadena[i]):
                lista[i].append(j)


    #Una vez tenemos la lista de listas, vemos cuantos enlaces/cadenas
    #de átomos hay como la especificada en la entrada de la función.

    enlaces=0

    for k in range (len(lista[0])): #Recorremos todos los Al (índice k)
        j=0
        for j in range (len(lista[1])): #Recorremos todos los O (índice j)
            l=0
            for l in range (len(lista[2])): #Recorremos todos los Si (índice l)
                    if (atoms.get_distances(lista[0][k],lista[1][j])<=d_Al_O) \
                    and (atoms.get_distances(lista[1][j],lista[2][l])<=d_Si_O):
                        enlaces=enlaces+1
    

    return enlaces

def num_enlaces_Al_O_Al (atoms):
    #Dado un objeto atoms(), determianmos el número de cadenas Al_O_Al

    atoms_symbols=atoms.get_chemical_symbols()

    #cutoffs para los enlaces de diferentes parejas de átomos (VESTA)

    d_Al_O=2.1074

    #Identificamos los índices de los atomos de la cadena. lista es una
    #lista de listas. En la primera posición p.ej se guardan los índices
    #de los átomos que aparece en la primera posición de atoms_cadena
    #p.ej, 'Al'

    lista=[[],[]]
    atoms_cadena=['Al', 'O']
    for i in range (2):
        j=0
        for j in range (len(atoms_symbols)):
            if (atoms_symbols[j]==atoms_cadena[i]):
                lista[i].append(j)


    #Una vez tenemos la lista de listas, vemos cuantos enlaces/cadenas
    #de átomos hay

    enlaces=0

    for k in range (len(lista[1])): #Recorremos todos los O (índice k)
        j=0
        for j in range (len(lista[0])): #Recorremos todos los Al (índice j)
                if (atoms.get_distances(lista[1][k],lista[0][j])<=d_Al_O):
                    for l in range (len(lista[0])): #Recorremos de nuevo los Al (índice l)
                        #Nos saltamos el caso de coger el mismo átomo de Al 2 veces
                        if (l==j):
                            continue
                        if (atoms.get_distances(lista[1][k],lista[0][l])<=d_Al_O):
                            enlaces=enlaces+1

    
    return enlaces                 

