import requests
from bs4 import BeautifulSoup
import smtplib

# Step 1 - Scrape the product price from Amazon
url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    'Accept-Language': 'en-US,en;q=0.5'
}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
price = soup.find('span', {'id': 'priceblock_ourprice'}).text.strip().replace(',', '').replace('$', '')
price = float(price)
print(f'Price: ${price:.2f}')

# Step 2 - Email alert when price is below preset value
target_price = 100
if price < target_price:
    # Set up email server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ashimshresthael@gmail.com', 'your_password ')

    # Send email
    subject = f'Amazon Product Price Alert: {url}'
    body = f'The price of the product is now ${price:.2f}, which is below your target price of ${target_price:.2f}.\n\nLink to buy: {url}'
    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail('your_email@gmail.com', 'recipient_email@gmail.com', msg)
    server.quit()

    print('Email sent successfully.')
else:
    print('Price is not below target price.')
