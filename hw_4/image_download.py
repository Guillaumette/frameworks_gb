"""Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения
программы."""

import os
import sys
from urllib.request import urlretrieve

import requests
import time
import threading
import multiprocessing
import asyncio
import urllib.parse


def download_image(url, folder):
    try:
        response = urlretrieve(url)
        # Извлечение имени файла из URL-адреса и корректировка имени, чтобы учесть URL-кодировку
        filename = os.path.join(folder, urllib.parse.unquote(os.path.basename(response[0])))
        # Перемещение файла в целевую папку с учетом корректного имени файла
        os.rename(response[0], filename)
        print(f"Скачано: {filename}")
    except Exception as e:
        print(f"Ошибка при скачивании {url}: {e}")


def download_images_threading(urls, folder):
    start_time = time.time()
    threads = []
    for url in urls:
        t = threading.Thread(target=download_image, args=(url, folder))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end_time = time.time()
    print(f"Всего времени затрачено (многопоточный подход): {end_time - start_time:.2f} секунд")


def download_images_multiprocessing(urls, folder):
    start_time = time.time()
    processes = []
    for url in urls:
        p = multiprocessing.Process(target=download_image, args=(url, folder))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    end_time = time.time()
    print(f"Всего времени затрачено (многопроцессорный подход): {end_time - start_time:.2f} секунд")


async def download_image_async(url, folder):
    try:
        response = await loop.run_in_executor(None, requests.get, url)
        if response.status_code == 200:
            filename = os.path.join(folder, url.split('/')[-1])
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Скачано: {filename}")
    except Exception as e:
        print(f"Ошибка при скачивании {url}: {e}")


async def download_images_async(urls, folder):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_image_async(url, folder))
        tasks.append(task)

    await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Всего времени затрачено (асинхронный подход): {end_time - start_time:.2f} секунд")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Введите в терминале: python image_download.py <folder_path> <url1> <url2> ...")
        sys.exit(1)

    folder_path = sys.argv[1]
    urls = sys.argv[2:]

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    print("Многопоточная загрузка изображений:")
    download_images_threading(urls, folder_path)

    print("\nМногопроцессорная загрузка изображений:")
    download_images_multiprocessing(urls, folder_path)

    print("\nАсинхронная загрузка изображений:")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_images_async(urls, folder_path))

# Пример работы:
# python image_download.py images https://img.freepik.com/free-photo/medium-shot-woman-wearing-headphones_23-2149818230.jpg
# Многопоточная загрузка изображений:
# Скачано: images\tmp8kbhqiyc
# Всего времени затрачено (многопоточный подход): 0.27 секунд
#
# Многопроцессорная загрузка изображений:
# Скачано: images\tmp45o96wrg
# Всего времени затрачено (многопроцессорный подход): 0.56 секунд
#
# Асинхронная загрузка изображений:
# C:\Users\User\PycharmProjects\FrameworksGB\hw_4\image_download.py:106: DeprecationWarning: There is no current event loop
#   loop = asyncio.get_event_loop()
# Скачано: images\medium-shot-woman-wearing-headphones_23-2149818230.jpg
# Всего времени затрачено (асинхронный подход): 0.69 секунд

