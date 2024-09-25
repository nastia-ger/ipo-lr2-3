print ("Дан объем шара X куб. ед. "
"Найдите радиус фигуры.")
x = int (input ("Введите x" ))
import math
r = (3 * (int(x) ** (1/3))) / ( 4 * math.pi)
print ("Радиус равен", float(r))