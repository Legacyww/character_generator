# file 
nav = [0,0,0,0]
suma = 30

a = int(input("""
      Для выхода нажмите 0.
      
      Что бы присвоить очко опыта способности выберите цифру от 1 - 4.
      1. Сила
      2. Ловкость
      3. Мудрость
      4. Здоровье
      
      Что бы убрать очко опыта нажмите 5, и выберите цифру с соответствующей способностью.
      Для того что бы обнулить все способности, нажмите на 6.
      """))

while a != 0:
    if a == 1:
        b = int(input("Введите сколько хотите отдать очков: "))
        if suma - b >= 0:
            suma -= b
            nav[0] += b
        print(nav,"Остаток:", suma)
        a = int(input())
    if a == 2:
        b = int(input("Введите сколько хотите отдать очков: "))
        if suma - b >= 0:
            suma -= b
            nav[1] += b
        print(nav,"Остаток:", suma)
        a = int(input())
    if a == 3:
        b = int(input("Введите сколько хотите отдать очков: "))
        if suma - b >= 0:
            suma -= b
            nav[2] += b
        print(nav,"Остаток:", suma)
        a = int(input())
    if a == 4:
        b = int(input("Введите сколько хотите отдать очков: "))
        if suma - b >= 0:
            suma -= b
            nav[3] += b
        print(nav,"Остаток:", suma)
        a = int(input())
    if a == 5:
        a = int(input())
        if a == 1:
            b = int(input("Введите сколько хотите забрать очков: "))
            if  nav[0] - b >= 0:
                suma += b
                nav[0] -= b
            print(nav,"Остаток:", suma)
            a = int(input())
        if a == 2:
            b = int(input("Введите сколько хотите забрать очков: "))
            if  nav[1] - b >= 0:
                suma += b
                nav[1] -= b
            print(nav,"Остаток:", suma)
            a = int(input())
        if a == 3:
            b = int(input("Введите сколько хотите забрать очков: "))
            if  nav[2] - b >= 0:
                suma += b
                nav[2] -= b
            print(nav,"Остаток:", suma)
            a = int(input())
        if a == 4:
            b = int(input("Введите сколько хотите забрать очков: "))
            if  nav[3] - b >= 0:
                suma += b
                nav[3] -= b
            print(nav,"Остаток:", suma)
            a = int(input())
    if a == 6:
        for i in range(0,len(nav)):
            nav[i] = 0
        suma = 30
        print(nav,"Остаток:", suma)
        a = int(input()) 