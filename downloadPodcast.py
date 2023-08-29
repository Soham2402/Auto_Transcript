import requests


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

async def downloadPodcast(link):
    response = requests.get(link,headers = headers,stream = True)
    with open("newfile.mp3",'wb') as f:
        for chunk in response.iter_content(chunk_size=300):
            f.write(chunk)