from urllib.request import urlopen
from time import time
import concurrent.futures


def worker(url):
    html = urlopen(url).read().decode('utf-8')
    with open("file" + str(urls.index(url)) + ".txt", "w", encoding='utf-8') as file:
        file.write(html)


urls = [
    "https://www.wikipedia.org/",
    "https://www.youtube.com/",
    "https://miet.ru",
    "https://ya.ru",
    "https://google.com",
    "https://vk.com",
    "https://www.telegram.com/",
    "https://web.whatsapp.com/",
    "https://auto.ru/",
    "https://www.microsoft.com/ru-ru/"
]

start = time()
for url in urls:
    worker(url)
print("Время выполнения через 1 поток", time() - start)

start = time()
with concurrent.futures.ThreadPoolExecutor(10) as executor:
    data = {executor.submit(worker, url): url for url in urls}
    for future in concurrent.futures.as_completed(data):
        pass
print("Время выполнения через 10 потоков", time() - start)