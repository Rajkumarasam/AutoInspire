import requests
import os

def get_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    data = response.json()[0]
    quote = f"{data['q']} - {data['a']}"
    print("Fetched Quote:", quote)
    return quote

def generate_image(quote_text):
    api_key = os.getenv("DYNAPIC_API_KEY")
    template_id = os.getenv("TEMPLATE_ID")

    url = f"https://api.dynapictures.com/design/{template_id}/image"
    payload = {
        "modifications": {
            "quote": quote_text
        }
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        image_url = response.json()["url"]
        print("Image Generated:", image_url)
    else:
        print("Failed to generate image:", response.text)

def main():
    quote = get_quote()
    generate_image(quote)

if __name__ == "__main__":
    main()
