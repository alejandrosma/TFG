En cada uno de los 4 directorios, se recogen los princiaples archivos necesarios para la ejecucción del código USPEX, así como los principales
archivos de salida de la ejecucción del programa. Este tipo de resultados se dentigen en dos tipos de directorios

#################################################################    INPUTS   ######################################################################
Se recogen los principales archivos para la ejecución de porogrma

#INPUT.txt 

Es el archivo en el que se especifican todas las características referentes a parámetros del algoritmo evolutivo, que códigos externos se na a usar ...

#Directorio Submision

En este directorio se muestran los archivos necesarios para mandar cálculos al cluster de computación de la UPV/EHU, Arina

#Directorio Specific

En este directorio se muestran los archivos necesarios para la correcta ejecución de los códigos externos usados para el cálculo de energías y optimización
local, que en nuestro caso son SIESTA y GULP. SIESTA es el programa que más archivos necesita, puesto que hace uso de los llamdos pseudopotenciales

#######################################################################  OUTPUTS  #########################################################################
Se recogen los outputs más importantes tras la ejecuión de la simulación correspondiente.

#n_POSCARS_TOT

Recoge los POSCARS de todas las estructuras generadas en la simulación

#n_BEST_POSCARS

Recogen los POSCARS de las mejores estructuras de cada generación. Estas se pueden visualizar introduciendo este archivo en un visualizador como VESTA

#n_INDIVIDUALS

Información detallada de todos los dindividuos generados en una simulación
