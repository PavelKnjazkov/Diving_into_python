# Семинар 6, задача 3.
# Напишите однострочный генератор словаря, который принимает на вход 
# три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии.
# Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров. 


import sys
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def create_salary_dict(names, rates, bonuses):
    return {name: rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}

def read_log_file():
    try:
        with open('log.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print('Файл log.txt не найден')

def display_new_logs():
    try:
        with open('log.txt', 'r') as file:
            logs = file.readlines()
            for log in logs[-1:]:
                print(log)
    except FileNotFoundError:
        print('Файл log.txt не найден')

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'log':
            read_log_file()
            return
        elif sys.argv[1] == 'newlogs':
            display_new_logs()
            return
        else:
            try:
                names = sys.argv[1].split(',')
                rates = [int(rate) for rate in sys.argv[2].split(',')]
                bonuses = [bonus.strip() for bonus in sys.argv[3].split(',')]
                if len(names) != len(rates) or len(names) != len(bonuses):
                    raise ValueError
                salary_dict = create_salary_dict(names, rates, bonuses)
                print(salary_dict)
                logging.info(salary_dict)
                display_new_logs()
            except (IndexError, ValueError):
                logging.error('Некорректные параметры. Введите три списка одинаковой длины.')
                print('Некорректные параметры. Введите три списка одинаковой длины.')
    else:
        while True:
            try:
                names = input('Введите имена (через запятую): ').split(',')
                rates = [int(rate) for rate in input('Введите ставки (через запятую): ').split(',')]
                bonuses = [bonus.strip() for bonus in input('Введите премии (через запятую с указанием процентов): ').split(',')]
                if len(names) != len(rates) or len(names) != len(bonuses):
                    raise ValueError
                break
            except ValueError:
                print('Некорректный ввод. Введите три списка одинаковой длины.')

        salary_dict = create_salary_dict(names, rates, bonuses)
        print(salary_dict)
        logging.info(salary_dict)
        display_new_logs()

if __name__ == '__main__':
    main()