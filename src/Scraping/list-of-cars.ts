import { writeFileSync } from "fs";

export const getCarDetails = async (id: string) => {
  const response = await fetch(
    `https://api.hamrobazaar.com/api/Product/${id}`,
    {
      headers: {
        accept: "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "access-control-allow-origin": "*",
        apikey: "09BECB8F84BCB7A1796AB12B98C1FB9E",
        "cache-control": "no-cache",
        country_code: "null",
        deviceid: "2d426b8a-b97e-4b90-ad4e-f9244a18ed43",
        devicesource: "mobile",
        pragma: "no-cache",
        "sec-ch-ua":
          '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "strict-transport-security": "max-age=2592000",
        "x-content-type-options": "nosniff",
        "x-frame-options": "SAMEORIGIN",
        Referer: "https://hamrobazaar.com/",
      },
      body: null,
      method: "GET",
    }
  );

  const data = await response.json();

  return data.data.productAttributeValues
    .map((attr) => attr.value)
    .join(",");
};


const fetchPage = async (pageNumber: number) => {
  const response = await fetch(
    `https://api.hamrobazaar.com/api/Product?PageSize=27&CategoryId=59973AED-F03D-4985-9AEC-542831929081&IsHBSelect=false&PageNumber=${pageNumber}`,
    {
      headers: {
        accept: "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "access-control-allow-origin": "*",
        apikey: "09BECB8F84BCB7A1796AB12B98C1FB9E",
        "cache-control": "no-cache",
        country_code: "null",
        deviceid: "2d426b8a-b97e-4b90-ad4e-f9244a18ed43",
        devicesource: "mobile",
        pragma: "no-cache",
        "sec-ch-ua":
          '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "strict-transport-security": "max-age=2592000",
        "x-content-type-options": "nosniff",
        "x-frame-options": "SAMEORIGIN",
        Referer: "https://hamrobazaar.com/",
      },
      body: null,
      method: "GET",
    }
  );

  const data = await response.json();

  for (const car of data.data) {
    csv += `${car.name},${await getCarDetails(
      car.id.replace(/-/g, "")
    )}\n`;
  }

  return csv;
};

let csv =
  "Name,Used For,Warranty,Transmission,Colour,Make Year,Features,Mileage,Engine (CC),Fuel,Kilometer Run,Types\n";
let count = 0;
const pageNumbers = Array.from({ length: 250 }, (_, i) => i + 1);
console.log(`Fetching pages 1 to 20 in parallel...`);

const fetchPageWithCount = async (pageNumber: number) => {
  const result = await fetchPage(pageNumber);
  count++;
  console.log(`Fetched page ${count}`);
  return result;
};

const results = await Promise.all(
  pageNumbers.map(fetchPageWithCount)
);
csv += results.join("");

writeFileSync("current_bikes_scraped_hamrobazar.csv", csv);
console.log("CSV file written: cars.csv");


