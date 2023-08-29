# import requests
# from bs4 import BeautifulSoup

# from downloadPodcast import downloadPodcast
# rss_url_link = 'https://feeds.megaphone.fm/hubermanlab'
# page = requests.get(rss_url_link)
# soup = BeautifulSoup(page.content, 'xml')

# podcast_items = soup.find_all('item')
# soupType = type(podcast_items)

# def get_audio_links(podcast_items:soupType)->list:
#     audio_links:list = []
#     for i in podcast_items:
#         audio_links.append(i.find('enclosure')['url'])
#     return audio_links

# audio_links = get_audio_links(podcast_items)


# for i in audio_links:
#     downloadPodcast(i)

import asyncio
import aiofiles
import aiohttp
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

rss_url_link = 'https://lexfridman.com/feed/podcast/'
page = requests.get(rss_url_link)
soup = BeautifulSoup(page.content, 'xml')
podcast_items = soup.find_all('item')

def get_audio_links(podcast_items):
    audio_links = []
    for i in podcast_items:
        title = i.find('title').text
        url = i.find('enclosure')['url']
        audio_links.append({'title': title, 'url': url})
    return audio_links

async def download_file(session, title, url):
    async with session.get(url, headers=headers) as response:
        content = await response.read()
        async with aiofiles.open(f'./downloads/{title}.mp3', 'wb') as f:
            await f.write(content)
            print(f'File {title} written')

async def main():
    async with aiohttp.ClientSession() as session:
        audio_links = get_audio_links(podcast_items)
        tasks = []
        count = 0
        for file in audio_links:
            if count == 5:
                break
            title = file['title']
            url = file['url']
            task = asyncio.create_task(download_file(session, title, url))
            tasks.append(task)
            count = count + 1
        await asyncio.gather(*tasks)

asyncio.run(main())
