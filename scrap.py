import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.geeksforgeeks.org/"
response = requests.get(url)

soup  = BeautifulSoup(response.content,'html.parser')

element = soup.find_all('a',target="_blank")

img_urls = []
for div in element:
    img = div.find('img')
    if img:
        img_url = img.get('src')
        img_urls.append(img_url)
with open('img_urls.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Image URL'])  # Write header
    for img_url in img_urls:
        writer.writerow([img_url])  # Write each image URL

print("Data saved to image_urls.csv")


