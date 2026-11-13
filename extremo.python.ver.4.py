import csv
import time
def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

slow_print("Вас привествует цифровой помощник по экстремофилам.")
while True:
    slow_print("Чем я могу быть полезен?")
    print("1. Найти группу по названию.")
    print("2. Найти по условиям среды.")
    print("3. Найти по месту обитания.")
    print("4. Открыть справочник определений.")
    print("Выход.")
    question=input("> ").lower()
    if "1" in question or "назван" in question or "групп" in question:
        while True:
            slow_print("Введите название группы (или напишите 'назад' для возврата в главное меню):")
            print("1. Термофилы.")
            print("2. Гипертермофилы.")
            print("3. Психрофилы (криофилы).")
            print("4. Ацидофилы")
            print("5. Алкалофилы.")
            print("6. Галофилы.")
            print("7. Осмофилы.")
            print("8. Пьезофилы (барофилы).")
            print("9. Ксерофилы.")
            print("10. Металлофилы.")
            print("11. Радиорезистентные.")
            print("12. Полиэкстремофилы.")
            print("Назад.")
            group=input("> ").lower()
            if "1" == group or "термофил" in group:
                with open(r'organism.csv', 'r', encoding='utf-8-sig') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['group'] == 'термофил':
                            print("Вид:", row['species'])
            elif "2" == group or "гипертермофил" in group:
                with open(r'organism.csv', 'r', encoding='utf-8-sig') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['group'] == 'гипертермофил':
                            print("Вид:", row['species'])
            elif "3" == group or "психрофил" in group or "криофил" in group:
                with open(r'organism.csv', 'r', encoding='utf-8-sig') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['group'] == 'психрофил':
                            print("Вид:", row['species'])
            elif "4" == group or "ацидофил" in group:
                with open(r'organism.csv', 'r', encoding='utf-8-sig') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['group'] == 'ацидофил':
                            print("Вид:", row['species'])
            elif "5" == group or "алкалофил" in group:
                with open(r'organism.csv', 'r', encoding='utf-8-sig') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['group'] == 'алкалофил':
                            print("Вид:", row['species'])
            elif "6" == group or "галофил" in group:
                with open(r'organism.csv', 'r', encoding='utf-8-sig') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['group'] == 'галофил':
                            print("Вид:", row['species'])
            elif "7" == group or "осмофил" in group:
                with open(r'organism.csv', 'r', encoding='utf-8-sig') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['group'] == 'осмофил':
                            print("Вид:", row['species'])
            elif "8" == group or "пьезофил" in group or "барофил" in group:
                with open(r'organism.csv', 'r', encoding='utf-8-sig') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['group'] == 'барофил':
                            print("Вид:", row['species'])
            elif "9" == group or "ксерофил" in group:
                with open(r'organism.csv', 'r', encoding='utf-8-sig') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['group'] == 'ксерофил':
                            print("Вид:", row['species'])
            elif "10" == group or "металлофил" in group:
                with open(r'organism.csv', 'r', encoding='utf-8-sig') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['group'] == 'металлофил':
                            print("Вид:", row['species'])
            elif "11" == group or "радиорезистентн" in group:
                with open(r'organism.csv', 'r', encoding='utf-8-sig') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['group'] == 'радиорезистентные':
                            print("Вид:", row['species'])
            elif "12" == group or "полиэкстремофил" in group:
                with open(r'organism.csv', 'r', encoding='utf-8-sig') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['group'] == 'полиэкстремофил':
                            print("Вид:", row['species'])
            elif "назад" in group:
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
    elif "4" in question or "справочник" in question or "определен" in question:
        while True:
            slow_print("Введите термин для поиска (или напишите 'назад' для возврата в главное меню):")
            search_term=input("> ").lower()
            if search_term == "назад":
                slow_print("Возвращаемся в главное меню...")
                break
            else:
                with open(r'glossary.csv', 'r', encoding='utf-8-sig') as file:
                    reader = csv.DictReader(file)
                    found = False
                    for row in reader:
                        user_root = search_term[:5].lower()
                        db_root = row['term'][:5].lower()
                        if user_root == db_root:
                            print(row['term'].capitalize() + " - ", end="")
                            slow_print(row['definution'])
                            print()
                            found = True
                    if not found:
                        print()
                        slow_print("Данного термина нет в глоссарии.")
    elif "5" in question or "выход" in question:
        slow_print("Благодарим за использование цифрового справочника по экстремофилам.")
        slow_print("До свидания!")
        break
    else:
        slow_print("Вариант не найден. Пожалуйста, выберете пункт из меню (1-5).")
