# программа для вычисления минимального расстояния между тремя точками (домом и двумя магазинами)
d1, d2, d3 = int(input()), int(input()), int(input())

var1 = d1 * 2 + d2 * 2
var2 = d1 + d3 + d2
var3 = d1 * 2 + d3 * 2
var4 = d2 * 2 + d3 * 2
print(min(var1, var2, var3, var4))
