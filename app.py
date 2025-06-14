from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API = "https://api.kanye.rest"

def format_quote(text):
    return {
        "name": "Kanye Quote",
        "quote": text,
        "author": "Kanye West",
        "year": "2024",
        "source": "Kanye REST API"
    }

@app.route("/")
def index():
    query = request.args.get("q", "").lower()

    try:
        response = requests.get(API)
        quote_text = response.json().get("quote", "?")
        quote = format_quote(quote_text)

        if query and query not in quote["quote"].lower():
            quotes = [] 
        else:
            quotes = [quote]

        return render_template("quote_list.html", quotes=quotes, search_query=query)

    except Exception as e:
        return f"Error occurred: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)


""" from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API = "https://api.kanye.rest"
cached_data = []

def format_quote(text, idx):
    return {
        "id": idx,
        "name": f"Kanye Quote #{idx + 1}",
        "quote": text,
        "author": "Kanye West",
        "year": "2024",
        "source": "Kanye REST API"
    }

@app.route("/")
def index():
    global cached_data
    query = request.args.get("q", "").lower()

    try:
        response = requests.get(API)
        quote_text = response.json().get("quote", "?")

        if not any(q["quote"] == quote_text for q in cached_data):
            new_quote = format_quote(quote_text, len(cached_data))
            cached_data.append(new_quote)

        quotes = cached_data
        if query:
            quotes = [q for q in cached_data if query in q["quote"].lower()]

        return render_template("quote_list.html", quotes=quotes, search_query=query)

    except Exception as e:
        return f"Error occurred: {e}", 500

@app.route("/quote/<int:idx>")
def quote_detail(idx):
    if 0 <= idx < len(cached_data):
        return render_template("quote_detail.html", quote=cached_data[idx])
    return "Quote not found", 404

if __name__ == "__main__":
    app.run(debug=True) """