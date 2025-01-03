﻿### **Crypto API: a Django-based API to retrieve cryptocurrency data**


A Django-based API for scraping cryptocurrency data from [CoinCodex](https://coincodex.com) and providing it in a structured JSON format.

## Features

- Scrape live cryptocurrency data, including:
  - Rank
  - Name
  - Ticker
  - Price
  - 24-hour price change
  - Market cap
  - 24-hour trading volume
  - Circulating supply
- Fetch data for a specific date using a POST request.
- Fetch data for the current date using a GET request.
- Data validation and error handling for user input.
- API response formatted using Django REST Framework serializers.

---

## Endpoints

### 1. **GET `/api/get-crypto-data/`**
Fetch cryptocurrency data for the current date.

#### Example Request
```bash
curl -X GET http://127.0.0.1:8000/api/get-crypto-data/
```

#### Example Response
```json
[
  {
    "index": "1",
    "name": "Bitcoin",
    "ticker": "BTC",
    "price": "$30,000",
    "change_24h": "2.5%",
    "market_cap": "$600B",
    "volume_24h": "$40B",
    "circulating_supply": "19M BTC"
  },
  ...
]
```

---

### 2. **POST `/api/get-crypto-data/`**
Fetch cryptocurrency data for a specific date.

#### Request Body
| Parameter | Type   | Description                 |
|-----------|--------|-----------------------------|
| `date`    | string | Date in `YYYY-MM-DD` format |

#### Example Request
```bash
curl -X POST http://127.0.0.1:8000/api/get-crypto-data/ \
-H "Content-Type: application/json" \
-d '{"date": "2023-01-01"}'
```

#### Example Response
```json
[
  {
    "index": "1",
    "name": "Bitcoin",
    "ticker": "BTC",
    "price": "$30,000",
    "change_24h": "2.5%",
    "market_cap": "$600B",
    "volume_24h": "$40B",
    "circulating_supply": "19M BTC"
  },
  ...
]
```

#### Error Responses
- **400 Bad Request**: Missing or invalid date format.
- **500 Internal Server Error**: Unable to scrape data from the source.

---

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- Django 4.0 or higher
- Django REST Framework
- `requests` library
- `beautifulsoup4` library

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Amirreza-Jabbari/Crypto-API.git
   cd Crypto-API
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**
   ```bash
   python manage.py runserver
   ```

5. **Access the API**
   - Use [http://127.0.0.1:8000/api/get-crypto-data/](http://127.0.0.1:8000/api/get-crypto-data/) for GET requests.
   - Use the same URL with a POST request and a `date` parameter to fetch data for a specific date.

---

## Dependencies

- Django
- Django REST Framework
- requests
- beautifulsoup4

Install them with:
```bash
pip install django djangorestframework requests beautifulsoup4
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
