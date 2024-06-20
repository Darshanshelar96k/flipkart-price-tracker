import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import re,time
from email.mime.image import MIMEImage

url = "https://www.flipkart.com/motorola-edge-40-neo-black-beauty-128-gb/p/itm01cc46d96a79f"
target_price = 22000


def get_price_data(url):
    data_dict = {}
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_tag = soup.find('div', class_='CxhGGd')
        if price_tag:
            price = price_tag.text
            data_dict["price"] = int(price[1:].strip().replace(',', ''))
            Description = soup.find('div', class_='_4gvKMe').text
            data_dict["discription"] = Description
            highlights =soup.find('div', class_='xFVion').text
            data_dict["highlight"] = highlights
            img =soup.find('img', class_="jLEJ7H")
            src_pattern = r'src="([^"]+)"'
            src_match = re.search(src_pattern, str(img))
            if src_match:
                src_url = src_match.group(1)
                print(src_url)
                data_dict["img"] = src_url 
            print(f"Price: {price[1:].strip().replace(',', '')} RS")
            return data_dict
        else:
            print("Price tag not found")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Function to send an email notification
def send_email(from_email,to_email,data_dict): 
    
    subject = 'Price Drop Alert for Flipkart Product'
    body = f"""The price has dropped to ${data_dict["price"]}. Check it out!
        Highlights :
            {data_dict["highlight"].replace("|","\n          ")}
        
        Description :
            {data_dict["discription"]}
    """
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with open(data_dict["img"], 'rb') as fp:
        img = MIMEImage(fp.read())
    
    # Add image attachment to email
    img.add_header('Content-Disposition', 'attachment', filename='image.png')
    msg.attach(img)


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, 'your_app_password')
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')


def main(target_price,url):
    from_email ="your_email@gmail.com"
    to_email =  "recipient_email@gmail.com"
    data_dict =  get_price_data(url)
    price = data_dict["price"]
    print(price)
    if price and target_price >= price:
        send_email(from_email,to_email,price)

def job():
    main(target_price,url)

# Schedule the job every 10 minutes
schedule.every(10).minutes.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)

