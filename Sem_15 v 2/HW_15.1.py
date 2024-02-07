# Семинар 1, задача 3.
# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу и на себя». 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
# Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров. 

import sys
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

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
            while True:
                try:
                    input_num = int(sys.argv[1])
                    if input_num < 0 or input_num > 100000:
                        raise ValueError
                    break
                except ValueError:
                    print('Некорректные параметры. Введите целое число.')
                    sys.argv[1] = input('Введите целое число: ')
            if is_prime(input_num):
                result = f'Число {input_num} является простым'
            else:
                result = f'Число {input_num} является составным'
            print(result)
            logging.info(result)
            display_new_logs()
    else:
        while True:
            try:
                input_num = int(input('Введите целое число: '))
                if input_num < 0 or input_num > 100000:
                    raise ValueError
                break
            except ValueError:
                print('Некорректный ввод. Введите целое число.')
        if is_prime(input_num):
            result = f'Число {input_num} является простым'
        else:
            result = f'Число {input_num} является составным'
        print(result)
        logging.info(result)
        display_new_logs()

if __name__ == '__main__':
    main()