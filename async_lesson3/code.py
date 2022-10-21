import time
import aiofiles
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os


async def write_file(session, url, name_img):
    async with aiofiles.open(f'F:\\img\\{name_img}', mode='wb') as f:
        async with session.get(url) as response:
            async for file in response.content.iter_chunked(2048):
                await f.write(file)
        print(f'Изображение сохранено {name_img}')


async def main(url):
    schema = 'https://parsinger.ru/asyncio/aiofile/2/'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            all_page = [schema + x['href'] for x in soup.find_all('a')]
            all_url_image = []
            for x in all_page:
                async with session.get(x) as response2:
                    soup2 = BeautifulSoup(await response2.text(), 'lxml')
                    all_url_image.extend([x['src'] for x in soup2.find_all('img')])
            tasks = []
            for link in all_url_image:
                name_img = link.split('/')[6]
                task = asyncio.create_task(write_file(session, link, name_img))
                tasks.append(task)
            await asyncio.gather(*tasks)


path = 'zadacha1/'
start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
url = 'https://parsinger.ru/asyncio/aiofile/2/index.html'
asyncio.run(main(url))

print(f'Cохранено {len(os.listdir(path))} изображений за {round(time.perf_counter() - start, 3)} сек')


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size
print(f'Размер всех изображений {get_folder_size(path)} byte')