import csv
import time
def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()
slow_print("Введите значение температуры:")
temp=input("> ")
with open(r'database.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if float(row['temp_opt']) >= float(temp):
            print(row['species'])
