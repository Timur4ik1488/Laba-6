from pickletools import string1


def f(s):
    neg=[] #список отрицательных чисел
    pos=[] #список положительных чисел
    res=[] #здесь будет конечный список после преобразований
    k=0 #количество нулевых чисел
    for i in s: #перебор элементво исходного списка
        if i < 0:
            neg.append(i)
        elif i==0:
            k+=1
        else:
            pos.append(i)
    res=neg + [0] * k + pos
    return k, res

s=[-2, 4, 5, 6, 4, -1 , 0, 4, -1, -5, 0, 56, -78, 856]
k , s1 = f(s)
print("Количество элементов, равных 0:", k)
print("Отформатированный список:", s1)
