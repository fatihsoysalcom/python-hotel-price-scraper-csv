import csv
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

def scrape_hotel_prices(city, check_in_date, check_out_date):
    """
    Simulates scraping hotel prices for a given city and dates.
    In a real scenario, this would involve making an HTTP request to a travel site
    and parsing its response. For this example, we use a hardcoded HTML string
    to make it self-contained and robust.
    """
    print(f"Simulating scraping for {city} from {check_in_date.strftime('%Y-%m-%d')} to {check_out_date.strftime('%Y-%m-%d')}...")

    # --- Web scraping concept starts here ---
    # In a real application, you would typically fetch content from a URL:
    # import requests
    # url = f"https://example-travel-site.com/hotels?city={city}&checkin={check_in_date.strftime('%Y-%m-%d')}&checkout={check_out_date.strftime('%Y-%m-%d')}"
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'html.parser')

    # For this self-contained example, we use a hardcoded HTML string
    # to demonstrate the parsing logic without external network dependencies.
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Hotels in {city}</title></head>
    <body>
        <h1>Hotels in {city}</h1>
        <div class="hotel-list">
            <div class="hotel-card">
                <h3 class="hotel-name">Grand Pera Hotel</h3>
                <span class="hotel-price">2500 TRY</span>
                <p class="hotel-rating">4.5/5</p>
            </div>
            <div class="hotel-card">
                <h3 class="hotel-name">Sultanahmet Palace</h3>
                <span class="hotel-price">3200 TRY</span>
                <p class="hotel-rating">4.8/5</p>
            </div>
            <div class="hotel-card">
                <h3 class="hotel-name">Taksim Square Hotel</h3>
                <span class="hotel-price">1800 TRY</span>
                <p class="hotel-rating">4.0/5</p>
            </div>
            <div class="hotel-card">
                <h3 class="hotel-name">Bosphorus View Suites</h3>
                <span class="hotel-price">4100 TRY</span>
                <p class="hotel-rating">4.9/5</p>
            </div>
        </div>
    </body>
    </html>
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    hotels_data = []
    # Find all hotel cards using their class name
    hotel_cards = soup.find_all('div', class_='hotel-card')

    for card in hotel_cards:
        # Extract hotel name and price from each card
        name_tag = card.find('h3', class_='hotel-name')
        price_tag = card.find('span', class_='hotel-price')

        if name_tag and price_tag:
            hotel_name = name_tag.get_text(strip=True)
            hotel_price = price_tag.get_text(strip=True) # e.g., "2500 TRY"
            hotels_data.append({
                'city': city,
                'check_in': check_in_date.strftime('%Y-%m-%d'),
                'check_out': check_out_date.strftime('%Y-%m-%d'),
                'hotel_name': hotel_name,
                'price': hotel_price,
                'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
    # --- Web scraping concept ends here ---

    return hotels_data

def save_to_csv(data, filename="hotel_prices.csv"):
    """
    Saves the scraped hotel data to a CSV file.
    This demonstrates saving data to a spreadsheet format as mentioned in the article.
    """
    if not data:
        print("No data to save.")
        return

    # Define CSV headers based on the dictionary keys
    fieldnames = ['city', 'check_in', 'check_out', 'hotel_name', 'price', 'scraped_at']

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader() # Write the header row
            writer.writerows(data) # Write all data rows
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving to CSV: {e}")

if __name__ == "__main__":
    target_city = "Istanbul"
    # Define check-in and check-out dates for the scraping
    today = datetime.now()
    check_in = today + timedelta(days=30) # Example: 30 days from now
    check_out = check_in + timedelta(days=3) # Example: 3-day stay

    # Perform the scraping simulation
    scraped_data = scrape_hotel_prices(target_city, check_in, check_out)

    # Generate a dynamic filename for the CSV based on city and date
    csv_filename = f"hotel_prices_{target_city.lower().replace(' ', '_')}_{check_in.strftime('%Y%m%d')}.csv"

    # Save the scraped data to a CSV file
    save_to_csv(scraped_data, csv_filename)

    print("\nExample finished. Check the generated CSV file.")
