import asyncio
import aiohttp
from bs4 import BeautifulSoup

URLS = [
    "https://example.com",
    "https://httpbin.org/html",
    # ... more urls
]

async def fetch(url, session):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        return soup.title.string.strip()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in URLS]
        titles = await asyncio.gather(*tasks)
        for url, title in zip(URLS, titles):
            print(f"{url} => {title}")

if __name__ == "__main__":
    asyncio.run(main())
