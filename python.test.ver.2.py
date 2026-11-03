import time
def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.04)
    print()

slow_print("Вас привествует цифровой помощник по экстремофилам.")
while True:
    slow_print("Чем я могу быть полезен?")
    print("1. Найти группу по названию.")
    print("2. Найти по условиям среды.")
    print("3. Найти по месту обитания.")
    print("4. Выход.")
    question=input("> ")
    if "1" in question or "назван" in question or "групп" in question:
        while True:
            slow_print("Введите название группы:")
            print("1. Термофилы.")
            print("2. Гипертермофилы.")
            print("3. Психрофилы (криофилы).")
            print("4. Ацидофилы")
            print("5. Алкофилы.")
            print("6. Галофилы.")
            print("7. Осмофилы.")
            print("8. Пьезофилы (барофилы).")
            print("9. Ксерофилы.")
            print("10. Металлофилы.")
            print("11. Радиорезистентные.")
            print("12. Полиэкстремофилы.")
            print("Назад.")
            name=input("> ").lower()
            if "1" == name or "термофил" in name:
                slow_print("Идет подбор данных...")
            elif "2" == name or "гипертермофил" in name:
                slow_print("Идет подбор данных...")
            elif "3" == name or "психрофил" in name or "криофил" in name:
                slow_print("Идет подбор данных...")
            elif "4" == name or "ацидофилы" in name:
                slow_print("Идет подбор данных...")
            elif "5" == name or "алкофил" in name:
                slow_print("Идет подбор данных...")
            elif "6" == name or "галофил" in name:
                slow_print("Идет подбор данных...")
            elif "7" == name or "осмофил" in name:
                slow_print("Идет подбор данных...")
            elif "8" == name or "пьезофил" in name or "барофил" in name:
                slow_print("Идет подбор данных...")
            elif "9" == name or "ксерофил" in name:
                slow_print("Идет подбор данных...")
            elif "10" == name or "металлофил" in name:
                slow_print("Идет подбор данных...")
            elif "11" == name or "радиорезистентные" in name:
                slow_print("Идет подбор данных...")
            elif "12" == name or "полиэкстремофил" in name:
                slow_print("Идет подбор данных...")
            elif "назад" in name:
                slow_print("Возвращаемся в главное меню...")
                break
            else:
                slow_print("Я не знаю такой группы. Попробуйте еще раз.")
    elif "2" in question or "условия" in question or "среда" in question:
        while True:
            slow_print("Введите температуру (или напишите 'назад' для возврата в главное меню):")
            temp=input("> ").lower()
            if "назад" in temp:
                slow_print("Возвращаемся в главное меню...")
                break
            slow_print("Введите кислотность (или 'назад'):")
            ph=input("> ").lower()
            if "назад" in ph:
                slow_print("Возвращаемся в главное меню...")   
                break
            slow_print("Введите соленость (или 'назад'):")
            sal=input("> ").lower()
            if "назад" in sal:
                slow_print("Возвращаемся в главное меню...")
                break
            slow_print("Введите давление (или 'назад'):")
            press=input("> ").lower()
            if "назад" in press:
                slow_print("Возвращаемся в главное меню...")
                break
            slow_print("Введите глубину (или 'назад'):")
            depth=input("> ").lower()
            if "назад" in depth:
                slow_print("Возвращаемся в главное меню...")
                break
            if "" == temp and "" == ph and "" == sal and "" == press and "" == depth:
                slow_print("Недостаточно данных для поиска. Введите параметры.")
                continue
            else:
                slow_print("Ищу по параметрам...")
    elif "3" in question or "мест" in question or "обитан" in question:
        while True:
            slow_print("Введите тип среды (или напишите 'назад' для возврата в главное меню):")
            print("1. Водная (океаны, моря, озера, реки).")
            print("2. Наземная (пустыни, почвы, скальные поверхности и другие).")
            print("3. Подземныая (пещеры, газовые месторождения, глубокие шахты и другие).")
            print("4. Ледниковыая (ледники, подледные озера, снежные поля и другие).")
            print("5. Атмосферная (тропосфера, верхняя тропосфера, стратосфера и другие).")
            print("6. Вулканическая (вулканические кратеры, геотермальные источники, вулканические почвы и другие).")
            print("7. Химически экстремальная (кислые, щелочные, гиперсоленые и другие).")
            print("8. Радиоактивная (урановые месторождения, радиоактивные шахты и другие).")
            print("9. Биологическая (симбионты и другие).")
            print("10. Глубоководная (океанические желоба, глубоководные трещины и другие).")
            print("11. Модельная внеземная (астробиология).")
            print("12. Смешанная.")
            print("Назад.")
            hab=input("> ").lower()
            if "назад" in hab:
                slow_print("Возвращаемся в главное меню...")
                break
            elif "1" in hab or "водн" in hab:
                slow_print("Идет подбор данных...")
            elif "2" in hab or "наземн" in hab:
                slow_print("Идет подбор данных...")
            elif "3" in hab or "подземн" in hab:
                slow_print("Идет подбор данных...")
            elif "4" in hab or "ледник" in hab:
                slow_print("Идет подбор данных...")
            elif "5" in hab or "атмосфер" in hab:
                slow_print("Идет подбор данных...")
            elif "6" in hab or "вулкан" in hab:
                slow_print("Идет подбор данных...")
            elif "7" in hab or "химич" in hab or "химия" in hab :
                slow_print("Идет подбор данных...")
            elif "8" in hab or "радио" in hab:
                slow_print("Идет подбор данных...")
            elif "9" in hab or "био" in hab:
                slow_print("Идет подбор данных...")
            elif "10" in hab or "глубоко" in hab or "глубоководн" in hab:
                slow_print("Идет подбор данных...")
            elif "11" in hab or "модель" in hab or "внеземн" in hab or "астробио" in hab:
                slow_print("Идет подбор данных...")
            elif "12" in hab or "смешан" in hab or "мультиэкстрим" in hab:
                slow_print("Идет подбор данных...")
            else:
                slow_print("Я не знаю такой среды обитания. Попробуйте еще раз.")
    elif "выход" in question:
        slow_print("Благодарим за использование цифрового справочника по экстремофилам.")
        slow_print("До свидания!")
        break

            









                
