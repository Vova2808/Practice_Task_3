# pip install colorama
# Для подсветки текста
import colorama
from colorama import Fore
from colorama import Back
from colorama import Style
# Для работы с регулярными выражениями
import re

# Функция для анализа текста
def text_analyst():
    text = input("Введите текст: ")

    # Разделяем текст на слова с помощью билиотеки re - для работы с регулярными выражениями
    words = re.findall(r'\w+', text.lower())

    # Считаем колличество символов
    total_words = len(words)

    # Подсчитываем частоту слов
    word_freq = {}

    # вычисляет частоту каждого слова
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Частота слов в процентах
    # Создаём пустой словарь
    word_freq_percent = {}
    # Этот блок кода вычисляет процент частоты каждого слова по отношению к общему количеству слов
    for word, count in word_freq.items():
        word_freq_percent[word] = (count / total_words) * 100

    # Вывод результата total_words
    print(f"Общее количество слов: {Fore.BLUE}{total_words}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}------------------------------------{Style.RESET_ALL}")
    print("Частота слов:")
    for word, percent in word_freq_percent.items():
        if percent >= 80.00:
            print(f'- Слово "{Back.BLACK}{word}{Style.RESET_ALL}": Проценты - {Fore.GREEN}{percent:.2f}%{Style.RESET_ALL}')

        elif 40.00 <= percent <= 80.00:
            print(f'- Слово "{Back.BLACK}{word}{Style.RESET_ALL}": Проценты - {Fore.YELLOW}{percent:.2f}%{Style.RESET_ALL}')

        elif 0.00 <= percent <= 40.00:
            print(f'- Слово "{Back.BLACK}{word}{Style.RESET_ALL}": Проценты - {Fore.RED}{percent:.2f}%{Style.RESET_ALL}')

    print(f"{Fore.BLUE}------------------------------------{Style.RESET_ALL}")

# Запускаем функцию
# Это стандартный способ определения основной функции
if __name__ == "__main__":
    text_analyst()