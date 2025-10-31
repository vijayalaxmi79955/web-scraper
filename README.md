**What you built**

You built a Python web scraper that extracts the first 10 news headlines from the Times of India US section (https://timesofindia.indiatimes.com/us).

The program fetches the webpage HTML.

It parses the HTML to identify headline tags (h2 and h3).

It extracts the text of the headlines and removes duplicates.

The first 10 headlines are saved in a text file toi_us_top10.txt.

Headlines are also printed to the console.

Essentially, it automates the process of collecting the latest US news headlines from Times of India.

 **Why you built it**
 
The reasons for building this scraper:

Automation: Manually visiting the website and copying headlines is tedious.

Data collection: Useful for research, analytics, or personal news aggregation.

Learning purpose: It helps in understanding web scraping, HTML parsing, and handling real-world web page structures.

Filtering & storage: Collecting and saving only the top 10 headlines makes the data structured and easy to process.

This kind of tool is the foundation for larger projects like news dashboards, daily alerts, or sentiment analysis of headlines.

**How you built it**

Step-by-step explanation:

Choose the target URL

URL: https://timesofindia.indiatimes.com/us (US news section).

Fetch webpage content using Python

Used the requests library to download the HTML content.

Added a User-Agent header to mimic a browser and avoid blocking.

Parse HTML with BeautifulSoup

Used BeautifulSoup to navigate the HTML tree.

Targeted headline tags: <h2> and <h3> (most news headlines are wrapped in these).

Optional fallback: inside <article> tags for pages with different structures.

Extract and clean headlines

Extracted text from each tag.

Removed duplicates.

Limited to the first 10 headlines to keep it concise.

Handle non-ASCII characters

Used encoding='utf-8' when saving to the file.

Printed safely using .encode('utf-8', errors='replace') to avoid Unicode errors.

Save and display results

Wrote headlines to toi_us_top10.txt.

Printed the headlines to the console for quick verification.# web-scraper
