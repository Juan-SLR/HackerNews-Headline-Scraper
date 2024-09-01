"""
HackerNews-Headline-Scraper

A Python script to scrape headlines from Hacker News using requests and BeautifulSoup.

Copyright (c) 2024 Juan-SLR›

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

Non-Commercial Clause:
This program is licensed for non-commercial use only. You may not use,
distribute, or modify this program for commercial purposes without
express written permission from the copyright holder.
"""


import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the headlines within the <span class="titleline"> elements
        headlines = soup.find_all('span', class_='titleline')

        # Extract and print the text of each headline
        for i, headline in enumerate(headlines, 1):
            # The actual link (headline) is within an <a> tag inside the <span class="titleline">
            title = headline.find('a').get_text(strip=True)
            print(f"{i}. {title}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Use the actual URL of the webpage you want to scrape
    url = "https://news.ycombinator.com/"
    fetch_headlines(url)
