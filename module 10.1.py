import time
from threading import Thread
from datetime import datetime


time_start = datetime.now()
def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1} \n ')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

#После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:

time_start_2 = datetime.now()

wite_first = Thread(target=wite_words, args=(10,  'example5.txt'))
wite_second = Thread(target=wite_words, args=(30, 'example6.txt'))
wite_third = Thread(target=wite_words, args=(200, 'example7.txt'))
wite_fourth = Thread(target=wite_words, args=(100, 'example8.txt'))

wite_first.start()
wite_second.start()
wite_third.start()
wite_fourth.start()

wite_first.join()
wite_second.join()
wite_third.join()
wite_fourth.join()

time_end_2 = datetime.now()
time_res_2 = time_end_2 - time_start_2
print(time_res_2)