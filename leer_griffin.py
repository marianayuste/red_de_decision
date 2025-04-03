# ---------------------------------------------------------------------------- #
#                            Leer resultados griffin                           #
# ---------------------------------------------------------------------------- #
import numpy as np
import pandas as pd
from funciones import get_only_attrs
import os


# ---------------------------------------------------------------------------- #
#                        Leer los que están en redes.csv                       #
# ---------------------------------------------------------------------------- #
'''
# Abrir redes redes.csv (creado en traducir_griffin.grf, donde se tradujo lo generado por Griffin)
### NOTA ### debo checar cuántos attrs se guardaron (al correr traducir_griffin se imprime)
# y a mano poner todos como as_str:
as_str = lambda x: str(x) # función para guardar como str los attrs
redes = pd.read_csv('redes.csv',
                    sep=',',
                    # converters={'attr_1':as_str,'attr_2':as_str,'attr_3':as_str,'attr_4':as_str,'attr_5':as_str,'attr_6':as_str,'attr_7':as_str}
                    converters={'attr_0':as_str,'attr_1':as_str}
                    )
nodos=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']

# --------------------------- Sacar Reglas Lógicas --------------------------- #
reglas = []
for a in redes['bool_func']:
    reglas.append(a)
res=[]
for a in reglas:
    b = a.split(';')
    res.append(b)
tabla_reglas = pd.DataFrame(res, columns=nodos)

# Reglas de cada nodo 
total_reglas = {}
for a in tabla_reglas: # para cada nodo
    total_reglas[a] = []
    for b in tabla_reglas[a]:
        if b not in total_reglas[a]:
            total_reglas[a].append(b)
print('Reglas de cada nodo:\n')           
for a in total_reglas:
    print(a,len(total_reglas[a]))



# ------------------------------ Leer Atractores ----------------------------- #
# -------------------------- Checar tamaño de attrs -------------------------- #
# Obtener todos los totales de attrs: 
attrs = {}
attrs_len = dict.fromkeys(redes['total_attrs'],0) #generar diccionario con todas las ocurrencias de total de attrs
for a in range(len(redes['red'])): #para cada lista
    total = redes['total_attrs'][a]
    attrs[a]=[str(redes['attr_0'][a]),str(redes['attr_1'][a])] #guardar los attrs que salieron en la red
    attrs_len[total] += 1

print('Modelos con cada total de attrs:')
print(attrs_len)


# # ------------------ Checar los conjuntos de attrs que salen ----------------- #
conjuntos_attrs = {}
for a in attrs:
    # Poner todos los attrs en el mismo orden:
    ordenados = []
    for b in attrs[a]:
        separados = b.split(';') #separar estados
        separados.sort() # ordenar los estados
        ordenados.append(separados)
    ordenados.sort() # ordenar los attrs
    if str(ordenados) not in conjuntos_attrs:
        conjuntos_attrs[str(ordenados)] = 1
    else:
        conjuntos_attrs[str(ordenados)] += 1

print('Conjuntos de atractores:')
for a in conjuntos_attrs:
    print(a, '-', conjuntos_attrs[a], 'modelos')

# ------------------------ Leer atractores de mutantes ----------------------- #
# Para confirmar que se generan los attrs que estoy pidiendo en mutantes a griffin
# attrs_A_1 = {}
# for red in range(510):
#     rules = reglas[red]
#     attr_mut = get_only_attrs(nodos,rules,['A'],['1'])
#     attr_mut.sort()
#     # guardar attr generados en diccionario attrs_A_1: 
#     if str(attr_mut) not in attrs_A_1:
#         attrs_A_1[str(attr_mut)] = 1
#     else:
#         attrs_A_1[str(attr_mut)] += 1
#     # guardar attrs generados en documento:
#     cwd = os.getcwd()
#     os.chdir('redes_generadas')
#     with open(str(red)+'_A_1.txt', 'w') as f:
#         for line in attr_mut:
#             f.write(f"{line}\n")
#     os.chdir(cwd)

'''

# ---------------------------------------------------------------------------- #
#                                Leer el grn.log                               #
# ---------------------------------------------------------------------------- #
# Abrir bitácora grn.log:
cwd = os.getcwd()
os.chdir(cwd+'/combinaciones_opcionales/log')
f = open('grn.log','r')
grn_log = f.read().split('\n')
os.chdir(cwd)

max = len(grn_log)
#las líneas donde se guarda "INFO Griffin:428 - Total number of satisfying models found: ":
lines = [k+2 for k in range(max) if k%3==0][:-1]
    # mútliplo de 3
    # más 2 para que sea le línea correcta
    # quitando el último valor porque sobra

sat_models = []
for l in lines:
    line_with_info = grn_log[l]
    number = int(line_with_info[-2:])
    sat_models.append(number)

if all(k == 0 for k in sat_models):
    print('ninguno encontró modelo')
else:
    print('HAY MODELO!')