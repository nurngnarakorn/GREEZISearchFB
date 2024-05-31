import requests

def search_page_id(access_token, keyword):
    url = f"https://graph.facebook.com/v11.0/search"
    params = {
        "q": keyword,
        "type": "page",
        "access_token": access_token
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        pages = response.json().get('data', [])
        for page in pages:
            print(f"Page Name: {page['name']}, Page ID: {page['id']}")
    else:
        print(f"Failed to search pages: {response.status_code}")
        print(response.json())

# Replace with your actual Access Token with necessary permissions
access_token = "YOUR_ACCESS_TOKEN"
keyword = "ผับบาร์"  # Replace with your keyword

search_page_id(access_token, keyword)
