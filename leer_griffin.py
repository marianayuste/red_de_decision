# ---------------------------------------------------------------------------- #
#                            Leer resultados griffin                           #
# ---------------------------------------------------------------------------- #
import numpy as np
import pandas as pd

# Abrir redes redes.csv (creado en traducir_griffin.grf, donde se tradujo lo generado por Griffin):
as_str = lambda x: str(x) # función para guardar como str los attrs
redes = pd.read_csv('redes.csv',
                    converters={'attr_1':as_str,'attr_2':as_str,'attr_3':as_str,'attr_4':as_str,'attr_5':as_str,'attr_6':as_str,'attr_7':as_str}
                    )

# ---------------------------------------------------------------------------- #
#                             Sacar Reglas Lógicas                             #
# ---------------------------------------------------------------------------- #
# reglas = []
# for a in redes['bool_func']:
#     reglas.append(a)
# res=[]
# for a in reglas:
#     b = a.split(';')
#     res.append(b)
# tabla = pd.DataFrame(res, columns=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'])

# # Reglas de cada nodo 
# total_reglas = {}
# for a in tabla: # para cada nodo
#     total_reglas[a] = []
#     for b in tabla[a]:
#         if b not in total_reglas[a]:
#             total_reglas[a].append(b)
# print('Reglas de cada nodo:\n')           
# for a in total_reglas:
#     print(a,len(total_reglas[a]))



# ---------------------------------------------------------------------------- #
#                                Leer Atractores                               #
# ---------------------------------------------------------------------------- #


# -------------------------- Checar tamaño de attrs -------------------------- #
attrs = {}
attrs_len = {6:0,7:0} # lo chequé con all(k==7 or k==6 for k in redes['total_attrs'])
for a in redes['red']:
    if redes['total_attrs'][a] == 6:
        attrs[a]=[str(redes['attr_1'][a]),str(redes['attr_2'][a]),str(redes['attr_3'][a]),str(redes['attr_4'][a]),str(redes['attr_5'][a]),str(redes['attr_6'][a])]
        attrs_len[6] = attrs_len[6] + 1
    elif redes['total_attrs'][a] == 7:
        attrs[a]=[str(redes['attr_1'][a]),str(redes['attr_2'][a]),str(redes['attr_3'][a]),str(redes['attr_4'][a]),str(redes['attr_5'][a]),str(redes['attr_6'][a]),str(redes['attr_7'][a])]
        attrs_len[7] = attrs_len[7] + 1
    else:
        print('cantidad de atractores:',redes['total_attrs'][a])

print('Modelos con 6 atractores: ', attrs_len[6], 'de', len(redes))
print('Modelos con 7 atractores: ', attrs_len[6], 'de', len(redes))


# ------------------ Checar los conjuntos de attrs que salen ----------------- #
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