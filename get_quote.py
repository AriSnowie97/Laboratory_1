import requests

def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url, verify = False)
    if response.status_code == 200:
        data = response.json()  
        quote = data["content"]  
        author = data["author"]  
        return f'"{quote}" - {author}'
    else:
        return "Failed to fetch quote."
    
quote = get_random_quote()
print(quote)
with open("quote.txt", "w", encoding="utf-8") as file:
    file.write(quote)
