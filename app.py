""" from flask import Flask, render_template, request
import requests
app = Flask(__name__, template_folder='template')

@app.route("/")
def index():
    return render_template("quote_list.html")

if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)
API = "https://api.kanye.rest"

def get_kanye_quotes(n):
    quotes = []
    seen = set()
    while len(quotes) < n:
        try:
            response = requests.get(API)
            quote = response.json().get("quote")
            if quote and quote not in seen:
                seen.add(quote)
                quotes.append({
                    "quote": quote,
                    "author": "Kanye West",
                    "year": "2024",
                    "source": "Kanye REST API"
                })
        except Exception as e:
            # Return partial list on API failure
            break
    return quotes

@app.route("/")
def index():
    query = request.args.get("q", "").lower()
    all_quotes = get_kanye_quotes(8)
    if query:
        quotes = [q for q in all_quotes if query in q["quote"].lower()]
    else:
        quotes = all_quotes
    return render_template("quote_list.html", quotes=quotes, search_query=query)

if __name__ == "__main__":
    app.run(debug=True) """


from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='template')

API = "https://api.kanye.rest"

def get_kanye_quotes(n):
    quotes = []
    seen = set()
    tries = 0
    while len(quotes) < n and tries < n * 2:
        try:
            response = requests.get(API, timeout=5)
            quote = response.json().get("quote")
            if quote and quote not in seen:
                seen.add(quote)
                quotes.append({
                    "quote": quote,
                    "author": "Kanye West",
                    "year": "2024",
                    "source": "Kanye REST API"
                })
        except Exception as e:
            print("Error fetching quote:", e)
        tries += 1
    return quotes

@app.route("/")
def index():
    query = request.args.get("q", "").lower()
    quotes = get_kanye_quotes(31)
    if query:
        quotes = [q for q in quotes if query in q["quote"].lower()]
    return render_template("quote_list.html", quotes=quotes, search_query=query)

if __name__ == "__main__":
    app.run(debug=True)