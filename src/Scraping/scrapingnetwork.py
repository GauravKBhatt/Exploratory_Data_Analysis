import asyncio
import aiohttp

car_id = 

async def get_car_details(session, car_id: str) -> str:
    """Fetch car details for a given ID."""
    url = f"https://api.hamrobazaar.com/api/Product/{car_id}"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "access-control-allow-origin": "*",
        "apikey": "09BECB8F84BCB7A1796AB12B98C1FB9E",
        "cache-control": "no-cache",
        "country_code": "null",
        "deviceid": "2d426b8a-b97e-4b90-ad4e-f9244a18ed43",
        "devicesource": "mobile",
        "pragma": "no-cache",
        "sec-ch-ua": '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "strict-transport-security": "max-age=2592000",
        "x-content-type-options": "nosniff",
        "x-frame-options": "SAMEORIGIN",
        "Referer": "https://hamrobazaar.com/",
    }
    
    async with session.get(url, headers=headers) as response:
        data = await response.json()
        values = [attr["value"] for attr in data["data"]["productAttributeValues"]]
        return ",".join(values)


async def fetch_page(session, page_number: int, csv_lines: list) -> None:
    """Fetch a single page of car listings."""
    url = (
        f"https://api.hamrobazaar.com/api/Product?"
        f"PageSize=27&CategoryId=F93D355F-CC20-4FFE-9CB7-6C7CDFF1DC50"
        f"&IsHBSelect=false&PageNumber={page_number}"
    )
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "access-control-allow-origin": "*",
        "apikey": "09BECB8F84BCB7A1796AB12B98C1FB9E",
        "cache-control": "no-cache",
        "country_code": "null",
        "deviceid": "2d426b8a-b97e-4b90-ad4e-f9244a18ed43",
        "devicesource": "mobile",
        "pragma": "no-cache",
        "sec-ch-ua": '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "strict-transport-security": "max-age=2592000",
        "x-content-type-options": "nosniff",
        "x-frame-options": "SAMEORIGIN",
        "Referer": "https://hamrobazaar.com/",
    }
    
    async with session.get(url, headers=headers) as response:
        data = await response.json()
        
        for car in data["data"]:
            car_id = car["id"].replace("-", "")
            details = await get_car_details(session, car_id)
            csv_lines.append(f'{car["name"]},{details}')


async def fetch_page_with_count(session, page_number: int, csv_lines: list, counter: dict) -> None:
    """Fetch a page and update counter."""
    await fetch_page(session, page_number, csv_lines)
    counter["count"] += 1
    print(f"Fetched page {counter['count']}")


async def main():
    """Main function to fetch all pages and write CSV."""
    csv_header = "Name,Used For,Warranty,Transmission,Colour,Make Year,Features,Mileage,Engine (CC),Fuel,Kilometer Run,Types\n"
    csv_lines = []
    counter = {"count": 0}
    
    page_numbers = list(range(1, 101))  # Pages 1 to 100
    print(f"Fetching pages 1 to 100 in parallel...")
    
    # Create session without SSL verification (if needed)
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_page_with_count(session, page_num, csv_lines, counter)
            for page_num in page_numbers
        ]
        await asyncio.gather(*tasks)
    
    # Write to CSV
    csv_content = csv_header + "\n".join(csv_lines) + "\n"
    
    with open("hamrobazaar_cars.csv", "w", encoding="utf-8") as f:
        f.write(csv_content)
    
    print("CSV file written: current_bikes_scraped_hamrobazar.csv")


if __name__ == "__main__":
    asyncio.run(main())