
import math
# -*- coding: utf-8 -*-
def calculate_sum_and_product(number):
    """
    Обчислює суму та добуток цифр тризначного числа.

    Аргумент функції:
    number (int): Тризначне число.

    Повертає:
    tuple: Кортеж із сумою та добутком цифр.
    """
    # Перевірка, чи введене число є тризначним
    if 100 <= number <= 999:
         # Розбиваємо число на цифри
        firstnumber = number // 100
        secondnumber = (number % 100) // 10
        thirdnumber = number % 10
        
        # Обчислюємо суму і добуток цифр
        digit_sum = firstnumber + secondnumber + thirdnumber
        digit_product = firstnumber * secondnumber * thirdnumber

        return digit_sum, digit_product
    # Зробити виняток, якщо число не є тризначним
    else:
        raise ValueError("Введіть тризначне число")

def calculate_math_expression(x):
    """
    Обчислює математичний вираз.

    Аргумент функції:
    x (float): Числове значення.

    Повертає:
    float: Результат виразу.
    """
    # Обчислення математичного виразу
    try:
        y = (math.log2(abs(x)) * math.sin(math.radians(x + 35))**2) / \
            (3**(x - 1) * (2 * math.pi + math.cos(x) * 1/2)**(1/3))
        return y
    # Перевірка на нуль у знаменнику
    except ZeroDivisionError:
        raise ValueError("Знаменник не може бути нулем")
    # Уникнення інших помилок, наприклад введення невірних даних
    except Exception as e:
        raise ValueError(f"Помилка обчислення: {e}")

def check_isosceles_triangle(a, b, c):
    """
    Перевіряє, чи є трикутник рівнобедреним.

    Аргумент функції:
    a (float): Довжина сторони a.
    b (float): Довжина сторони b.
    c (float): Довжина сторони c.

    Повертає:
    bool: True, якщо трикутник рівнобедрений, False в іншому випадку.
    """
    return a == b or b == c or c == a

def main():
    #Відображення меню в консолі
    print("1. Обчислити суму та добуток цифр")
    print("2. Обчислити математичний вираз")
    print("3. Перевірити, чи є трикутник рівнобедреним")
    print("0. Вийти")
    #Вибір завдання завдяки вводу відповідного номеру
    choice = int(input("Оберіть завдання (0-3): "))
    #Відповідні випадки у разі вводу цифр 0-3
    if choice == 1:
        try:
            # Зчитуємо введене користувачем число
            user_input = int(input("Введіть тризначне число: "))
            #Виклик функції до 1-ого завдання
            result_sum, result_product = calculate_sum_and_product(user_input)
            print(f"Сума цифр: {result_sum}")
            print(f"Добуток чисел: {result_product}")
            #Відповідні винятки
        except ValueError as ve:
            print(f"Помилка: {ve}")
        except Exception as e:
            print(f"Виникла помилка: {e}")
    
    elif choice == 2:
        try:
            #Введення значення х для розрахунку виразу
            x = float(input("Введіть x: "))
            #Виклик функції другого завдання
            result = calculate_math_expression(x)
            print(f"Результат виразу: {result}")
            #Відповідні винятки
        except ValueError as ve:
            print(f"Помилка: {ve}")
        except Exception as e:
            print(f"Виникла помилка: {e}")

    elif choice == 3:
        try:
            #Введення сторін трикутника
            a = float(input("Введіть довжину сторони a: "))
            b = float(input("Введіть довжину сторони b: "))
            c = float(input("Введіть довжину сторони c: "))
            #Виклик функції до 3-ого завдання
            result = check_isosceles_triangle(a, b, c)
            print(f"Трикутник рівнобедрений: {result}")
            #Відповідні винятки
        except ValueError:
            print("Будь ласка, введіть правильні числові значення для довжин сторін.")
        except Exception as e:
            print(f"Виникла помилка: {e}")
            #Пункт меню для виходу з програми
    elif choice == 0:
        print("Вихід з програми.")
    #Опрацювання випадку якщо введено неіснуючий номер меню
    else:
        print("Невірний вибір. Оберіть ще раз.")

if __name__ == "__main__":
    main()
