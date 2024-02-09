def validate_month(month):
    try:
        month = int(month)
        if month < 1 or month > 12:
            return False
        else:
            return True
    except ValueError:
        return False
def validate_year(year):
    try:
        year = int(year)
        if year < 5 or year > 120:
            return False
        else:
            return True
    except ValueError:
        return False
def get_user_input():
    while True:
        name=input("Введіть ваше ім'я:")
        year=input('Введіть рік народження (5-120):')
        if not validate_year(year):
            print('Некоректний рік. Спробуйте ще раз.')
            continue
        month=input('Введіть місяць народження (1-12): ')
        if not validate_month(month):
            print('Некоректний місяць. Спробуйте ще раз.')
            continue
        return name, year, month
def create_test_file(name, year, month):
    with open('test_file.txt', 'w') as f:
        f.write(f'Прізвище: {name}\n')
        f.write(f'Рік народження: {year}\n')
        f.write(f'Місяць народження: {month}\n')
def main():
    name, year, month = get_user_input()
    create_test_file(name, year, month)
    print('Тестовий файл успішно створено!')
if __name__ == "__main__":
    main()