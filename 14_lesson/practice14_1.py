# 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#     Примечание: Списки фруктов создайте вручную в начале файла.

frut1 = ['яблоко', 'лимон', 'дыня']
frut2 = ['груша', 'яблоко', 'лимон', 'слива']

fruits = [frut for frut in frut1 if frut in frut2]
print(fruits)