import requests
from bs4 import BeautifulSoup
import time
import os

def scrape_news():
    os.system('clear')
    print("\033[92m" + "="*60)
    print("       🔥 LIVE NEWS SCRAPER - by Jatin")
    print("="*60 + "\033[0m")
    
    url = "https://news.ycombinator.com"
    print(f"\n\033[93mFetching data from {url}...\033[0m\n")
    time.sleep(1)
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    stories = soup.find_all('span', class_='titleline')
    
    print("\033[96m📰 TOP TECH NEWS RIGHT NOW:\033[0m\n")
    for i, story in enumerate(stories[:15], 1):
        link = story.find('a')
        if link:
            print(f"\033[92m[{i:02d}]\033[0m {link.text}")
            print(f"     \033[90m🔗 {link.get('href', 'N/A')}\033[0m\n")
    
    print("\033[92m" + "="*60 + "\033[0m")
    print("\033[93mScraping complete! Data fetched in real time.\033[0m")

scrape_news()
