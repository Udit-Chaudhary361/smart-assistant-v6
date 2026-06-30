import requests

def get_joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            setup = data["setup"]
            punch = data["punchline"]
            return f"{setup}\n{punch}"
        else:
            return f"Server Error Code - {response.status_code}"
    except Exception:
        return "Error Occured!"