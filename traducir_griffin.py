# ---------------------------------------------------------------------------- #
#                            Leer resultados griffin                           #
# ---------------------------------------------------------------------------- #
import numpy as np
import pandas as pd
import os

# ---------------------------------------------------------------------------- #
#                  Guardar todas las redes en DataFrame redes                  #
# ---------------------------------------------------------------------------- #
filename = 'igual_a_tesis.out'
resultados = np.loadtxt(filename,dtype='str')

# Guardar todas las redes en una lista
lista_1 = []
for red in range(len(resultados)):
    todo = resultados[red]
    lista_1.append(todo.split(','))

# Obtener el máximo de attrs
max = max(int(k[5]) for k in lista_1)

# Guardar todos los attrs en una lista
lista_2 = []
for red in lista_1:
    no_attrs = int(red[5])
    attrs = [red[5+k] for k in range((no_attrs*2)+1)] # lista con attrs (total de estados, estados)
    for dif in range(max-no_attrs): # agregar ceros extra para que todas las listas tengan la misma longitud
        attrs.extend(['0','0'])
    lista_2.append(attrs)

# Guardar la info que me interesa en una lista
lista_3 = []
for red in range(len(lista_1)):
    nueva = []
    nueva.extend((lista_1[red][0],lista_1[red][3],lista_1[red][4])) #agregar 1ros valores de .out, pero los que me interesan
    nueva.extend(k for k in lista_2[red]) #agregar attrs
    nueva.extend(lista_1[red][-2:]) #agregar últimos valores de .out
    lista_3.append(nueva)

array_redes = np.array(lista_3)

# Crear DataFrame con toda la info que me interesa
redes = pd.DataFrame(array_redes,
                    columns=['red',
                             'bool_func',
                             'truth_t',
                             'total_attrs',
                             'len_attr_1','attr_1',
                             'len_attr_2','attr_2',
                             'len_attr_3','attr_3',
                             'len_attr_4','attr_4',
                             'len_attr_5','attr_5',
                             'len_attr_6','attr_6',
                            #  'len_attr_7','attr_7',
                             'total_reg',
                             'regulations'
                            ]
                    )

# Guardar el archivo
redes.to_csv("redes.csv", index=False)


# ---------------------------------------------------------------------------- #
#             Crear archivos .txt de cada red para leer en BoolNet             #
# ---------------------------------------------------------------------------- #
# En particular para analizar si los attrs de mutantes se están generando
cwd = os.getcwd()
os.chdir('redes_generadas')
nodos=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
for red in range(len(resultados)):
    arr = np.array([['targets,', 'factors']])
    rules = redes['bool_func'][red].split(';')
    for n in range(len(nodos)):
        arr = np.append(arr,[[nodos[n]+',',rules[n]]],axis=0)
    np.savetxt(str(red)+'.txt',arr,fmt='%s')
os.chdir(cwd)