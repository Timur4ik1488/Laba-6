def f(s):
    #здесь будет так называемый маппинг для латинских букв
    u={
        'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F',
        'g':'G', 'h':'H', 'i':'I', 'j':'J', 'k':'K', 'l':'L',
        'm':'M', 'n':'N', 'o':'O', 'p':'P', 'q':'Q', 'r':'R',
        's':'S', 't':'T', 'u':'U', 'v':'V', 'w':'W', 'x':'X',
        'y':'Y', 'z':'Z'
    }
    #здесь будет маппинг для русских букв
    y={
        'а': 'А', 'б': 'Б', 'в': 'В', 'г': 'Г', 'д': 'Д', 'е': 'Е', 'ё': 'Ё',
        'ж': 'Ж', 'з': 'З', 'и': 'И', 'й': 'Й', 'к': 'К', 'л': 'Л', 'м': 'М',
        'н': 'Н', 'о': 'О', 'п': 'П', 'р': 'Р', 'с': 'С', 'т': 'Т', 'у': 'У',
        'ф': 'Ф', 'х': 'Х', 'ц': 'Ц', 'ч': 'Ч', 'ш': 'Ш', 'щ': 'Щ', 'ъ': 'Ъ',
        'ы': 'Ы', 'ь': 'Ь', 'э': 'Э', 'ю': 'Ю', 'я': 'Я'
    }

    res="" #сюда будет приплюсовываться результат после преобразиований
    for i in s: #перебор элементов в строке
        if i in u:
            res+=u[i]
        elif i in y:
            res+=y[i]
        else:
            res+=i
    return res

s='Это будет чисто пример, but i do not know, будет он работать or not' #исходная строка
output_s=f(s) #строка, полученная уже после изменения регистра исходной строчки
print(output_s)
