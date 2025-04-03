# ---------------------------------------------------------------------------- #
#                     Editar documento busqueda_radial.grf                     #
# ---------------------------------------------------------------------------- #
# Para guardar las regulaciones opcionales requeridas para busqueda_radial.grf
# en una búsqueda radial al revés (ver nota Red decisión / 1er análisis / 10.)

import itertools
import os

#abrir documento 
f = open('busqueda_radial_base.grf', "r")
grn_original = f.read().split('\n')

# Guardar las regulaciones que siempre son mandatory:
MPU = '[A:A][A:B][B:C][B:D][C:D][B:E][B:F][E:F][J:F][F:G][N:G][F:H][L:H][F:I][H:I][L:J][Q:J][K:K][K:L][M:M][M:N][L:P][F:R][R:S][S:S][J:T]'
MNU = '[D:A][H:B][H:C][H:D][H:E][H:F][I:F][J:G][Q:G][B:I][J:I][O:I][F:J][N:J][H:L][N:M][F:P][J:P][R:P][P:R][E:T][G:T][S:T]'

# Guardar las que son opcionales:
OPU = [ '[A:C]','[C:F]','[N:F]','[P:L]','[F:O]','[J:Q]','[A:S]' ]
ONU = [ '[S:D]','[A:H]','[S:H]','[A:I]','[C:I]','[L:K]','[J:O]','[S:Q]','[D:R]','[T:R]','[D:S]','[S:I]','[N:L]','[I:N]' ]
O_all = OPU+ONU


# Generar todas las combinaciones y guardar un archivo por cada una
n_counter = 0
for comb in itertools.combinations(O_all,2): # Para cada posible combinación de OPU+ONU
    # Generar la línea de 'interactions':
    c1,c2 = comb[0],comb[1]
    if c1 in OPU and c2 in OPU:
        MPU_new = MPU.replace(c1,'').replace(c2,'')
        regulaciones = 'interactions = {MPU' + MPU_new + ',MNU'+ MNU + ',OPU' + c1 + c2 + '}'
    if c1 in OPU and c2 in ONU:
        MPU_new = MPU.replace(c1,'')
        MNU_new = MNU.replace(c2,'')
        regulaciones = 'interactions = {MPU' + MPU_new + ',MNU'+ MNU_new + ',OPU' + c1 + ',ONU' + c2 + '}'
    if c1 in ONU and c2 in OPU:
        MNU_new = MNU.replace(c1,'')
        MPU_new = MPU.replace(c2,'')
        regulaciones = 'interactions = {MPU' + MPU_new + ',MNU'+ MNU_new + ',ONU' + c1 + ',OPU' + c2 + '}'
    if c1 in ONU and c2 in ONU:
        MNU_new = MNU.replace(c1,'').replace(c2,'')
        regulaciones = 'interactions = {MPU' + MPU + ',MNU'+ MNU_new + ',ONU' + c1 + c2 + '}'

    # Modificar la línea de interactions original con la modificada:
    grn_modificado = grn_original.copy()
    grn_modificado[3] = regulaciones

    cwd = os.getcwd()
    # Guardar el nuevo documento con las regulaciones modificadas:
    os.chdir(cwd + '/combinaciones_opcionales')
    archivo = '2_' + str(n_counter) + '.grf'
    with open(archivo, 'w') as file:
        for k in grn_modificado:
            file.write(k+'\n')

    # Guardar el comando para correr con griffin ese documento en la terminal:
    out = '2_' + str(n_counter) + '.out'
    with open('comandos.txt','a') as file:
        file.write('griffin -f ' + archivo + ' -o ' + out + '\n')
    os.chdir(cwd)
    
    # Aumentar el contador, se usa para el título de los archivos guardados
    n_counter += 1

