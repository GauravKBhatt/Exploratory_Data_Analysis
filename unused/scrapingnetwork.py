import requests
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

# API headers
HEADERS = {
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

# Get car details
def get_car_details(car_id: str) -> str:
    url = f"https://api.hamrobazaar.com/api/Product/{car_id}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    attributes = data.get("data", {}).get("productAttributeValues", [])
    return ",".join(attr.get("value", "") for attr in attributes)

# Fetch a page of cars
def fetch_page(page_number: int) -> list:
    url = (
        f"https://api.hamrobazaar.com/api/Product?PageSize=27&CategoryId=59973AED-F03D-4985-9AEC-542831929081&IsHBSelect=false&PageNumber={page_number}"
    )
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    cars = data.get("data", [])
    rows = []
    for car in cars:
        car_id = car.get("id", "").replace("-", "")
        details = get_car_details(car_id)
        rows.append([car.get("name", ""), *details.split(",")])
    return rows

# CSV header
header = [
    "Name",
    "Used For",
    "Warranty",
    "Transmission",
    "Colour",
    "Make Year",
    "Features",
    "Mileage",
    "Engine (CC)",
    "Fuel",
    "Kilometer Run",
    "Types",
]

# Fetch pages in parallel
page_numbers = list(range(1, 11))
all_rows = []

print("Fetching pages 1 to 250 in parallel...")
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(fetch_page, page): page for page in page_numbers}
    for future in as_completed(futures):
        page = futures[future]
        try:
            rows = future.result()
            all_rows.extend(rows)
            print(f"Fetched page {page}")
        except Exception as e:
            print(f"Error fetching page {page}: {e}")

# Write to CSV
output_file = "test.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(all_rows)

print(f"CSV file written: {output_file}")