#######################################################
# Exemplo
#######################################################
import numpy
my_array = numpy.array([0, 1, 2, 3, 4])
print(my_array)    #  [0  1 2 3 4]
print(type(my_array))  #<class 'numpy.ndarray'>
print("Máximo: " +
      str(my_array.max()) + ".")
print("Mínimo: " +
      str(my_array.min()) + ".")
print("Soma: " +
      str(my_array.sum()) + ".")
print("Média: " +
      str(my_array.mean()) + ".")
my_array = numpy.append(my_array,6)
print(my_array)
my_array = numpy.append(9,my_array)
my_array = numpy.insert(my_array,2,11)
print(my_array)
lista = my_array.tolist()
print(lista)



