try:
    s=str(input("Введите строку:"))
    i=0
    res=''
    for i in range(len(s)):
        letter=s[i]
        if letter.upper()==letter:
            letter=letter.lower()
        else:
            letter=letter.upper()
        res+=str(letter)
    print(res)
except:
    print("Неверно введена строка")




