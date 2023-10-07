import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python btc_price.py <quantity>")

    quantity = sys.argv[1]

    try:
        quantity = float(quantity)
    except ValueError:
        sys.exit("Error: Invalid quantity provided")

    btc_value = fetch_btc_value(quantity)

    if btc_value is not None:
        print(f"${btc_value:,.4f}")
    else:
        sys.exit("Error: Unable to fetch BTC price")

def fetch_btc_value(quantity):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        price = data.get("bpi", {}).get("USD", {}).get("rate_float")
        return price * quantity if price is not None else None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    main()
