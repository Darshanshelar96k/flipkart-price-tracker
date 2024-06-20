# Price Tracker Script for Flipkart Product

## Overview
This Python script monitors the price of a product on Flipkart and sends an email notification when the price drops below a specified target price. It utilizes web scraping techniques with BeautifulSoup for data extraction and SMTP for email notifications.

### Skills Covered
- **Web Scraping**: Extracts price, description, highlights, and product image URL from a Flipkart product page using BeautifulSoup.
- **Email Notification**: Sends an email using SMTP when the product price drops below a specified threshold.
- **Regular Job Scheduling**: Uses the `schedule` library to run the price check job every 10 minutes.
- **Regex Handling**: Utilizes regular expressions to extract the product image URL from HTML content.

## How to Use
### Prerequisites
- Python 3.x installed on your system.
- Necessary Python libraries installed (`requests`, `beautifulsoup4`, `schedule`).

### Setup
1. Clone or download the script (`price_tracker.py`).
2. Install required libraries using pip:



### Configuration
1. Replace `"https://www.flipkart.com/motorola-edge-40-neo-black-beauty-128-gb/p/itm01cc46d96a79f"` with the URL of your desired Flipkart product.
2. Set `target_price` to the price threshold below which you want to receive notifications.
3. Replace `your_email@gmail.com` with your Gmail address and configure app password for SMTP authentication.

### Running the Script
1. Open a terminal or command prompt.
2. Navigate to the directory containing `price_tracker.py`.
3. Run the script:


