import requests
from bs4 import BeautifulSoup
import csv
url = "https://geel.us/?srsltid=AfmBOor-qfCCAiWRzCL0PQFT4XEN5P-kxTlVSi5KJLpdIQM2Q4mtrKsu"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

element = soup.find_all('img', alt="Baxter Cardigan")

img_urls = []
for image in element:
    img = image.find('img')
    if image:
        img_url = image.get('src')
        img_urls.append(img_url)
with open('img_urls.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Image URL']) 
    for img_url in img_urls:
        writer.writerow([img_url])  
print("Data saved to image_urls.csv")