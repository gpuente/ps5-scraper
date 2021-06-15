import json
import asyncio
import requests
from datetime import datetime
from scraper.scraper import SimpleScraper
from aiohttp import ClientSession, ClientTimeout


async def main():
    with open("src/config.json") as f:
        config = json.load(f)

    timeout = ClientTimeout(total=5)
    async with ClientSession(timeout=timeout) as session:
        scrapers = []

        for item in config["items"]:
            sc = SimpleScraper(
                item["url"],
                item["selector"],
                item["test_name"],
                session
            )

            scrapers.append((item["name"], sc))


        found = False
        while not found:
            for sc_name, sc in scrapers:
                now = datetime.now()
                print(now.strftime("[%H:%M:%S]"), "testing: ", sc_name)
                result = await sc.run_test()

                if result:
                    print("found in ", sc_name)
                    requests.post(config["notify_url"], json={"value1": config["notify_message"].replace("item_name", sc_name)})
                    found = True

            if not found:
                await asyncio.sleep(config["cycle"])




if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
