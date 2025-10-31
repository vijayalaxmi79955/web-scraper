import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/us"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print("Failed to retrieve the webpage.")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

headlines = []

# Grab first 10 headlines from h2/h3 tags
for tag in soup.find_all(['h2', 'h3']):
    text = tag.get_text(strip=True)
    if text and text not in headlines:
        headlines.append(text)
    if len(headlines) >= 10:
        break

# Save to file using UTF-8
with open("toi_us_top10.txt", "w", encoding="utf-8") as f:
    for h in headlines[:10]:
        f.write(h + "\n")

# Print safely to console
print(f"✅ Scraped {len(headlines[:10])} headlines from Times of India US section.")
for i, h in enumerate(headlines[:10], 1):
    print(f"{i}. {h.encode('utf-8', errors='replace').decode('utf-8')}")
