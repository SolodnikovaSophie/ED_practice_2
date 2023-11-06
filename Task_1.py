import numpy as np
import json

matrix = np.load('matrix_95.npy')
#print(matrix)

size = len(matrix)
Matrix_summ = float(np.sum(matrix, axis = None)) #Сумма всех элементов матрицы
#print(Matrix_summ)
Matrix_avr = float(np.average(matrix)) #Cреднее арифметическое значение элементов матрицы
#print(Matrix_avr)
sumMd = np.trace(matrix) #Сумма всех элементов на главной диагонали
#print(sumMD)
sumSd = np.trace(matrix[::-1]) #Сумма всех элементов побочной диагонали
#print(sumSD)
avrMd = sumMd / size #Среднее арифметическое элементов главной диагонали матрицы
#print(avrMd)
avrSd = sumSd / size
#print(avrSd)
matrixMax = np.max(matrix)
#print(matrixMax)
matrixMin = np.min(matrix)
#print(matrixMin)

matrix_state = dict()
matrix_state['sum'] = Matrix_summ
matrix_state['avr'] = Matrix_avr
matrix_state['sumMD'] = sumMd
matrix_state['sumSD'] = sumSd
matrix_state['avrMD'] = avrMd
matrix_state['avrSD'] = avrSd
matrix_state['max'] = matrixMax
matrix_state['min'] = matrixMin

for key in matrix_state.keys():
    matrix_state[key] = float(matrix_state[key])

with open('matrix_state.json', 'w') as result:
    result.write(json.dumps(matrix_state))

norm_data = (matrix - matrixMin) / (matrixMax - matrixMin)
#print(norm_data)
np.save('norm_matrix', norm_data)

shape = norm_data.shape #Проверка размерности нормализованной матрицы
#print(shape)




