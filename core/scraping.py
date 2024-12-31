import requests
from bs4 import BeautifulSoup

def scrape_crypto_data(formatted_date):
    url = f"https://coincodex.com/historical-data/crypto/?date={formatted_date}T08:30:00Z"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Failed to retrieve data")

    soup = BeautifulSoup(response.content, 'html.parser')
    coins_data = []

    for row in soup.select('tr.coin'):
        index = row.select_one('td.rank')
        name = row.select_one('td.name .full-name')
        ticker = row.select_one('td.name .ticker')
        price = row.select_one('td.price')
        change_24h = row.select_one('td.change .price-change')
        market_cap = row.select_one('td.market-cap')
        volume = row.select_one('td.volume')
        circulating_supply = row.select_one('td.circulating-supply span')

        coins_data.append({
            "index": index.text.strip() if index else None,
            "name": name.text.strip() if name else None,
            "ticker": ticker.text.strip() if ticker else None,
            "price": price.text.strip() if price else None,
            "change_24h": change_24h.text.strip() if change_24h else None,
            "market_cap": market_cap.text.strip() if market_cap else None,
            "volume": volume.text.strip() if volume else None,
            "circulating_supply": circulating_supply.text.strip() if circulating_supply else None,
        })

    return coins_data