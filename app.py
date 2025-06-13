from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API = "https://api.kanye.rest"
cached_data = []

def Quote(Line):
       return {
        "Lines": Line.get("Quote", "?"),
    }

@app.route("/")
def index():
    global cached_data
    New_quote = request.arSgs.get("search", "").lower()

    try:
        response = requests.get(API)
        raw_data = response.json().get("items", [])  
        items = [Quote(i) for i in raw_data]

        if search:
            filtered = []
            for i in items:
                if search in i["Lines"].lower():
                    filtered.append(i)
            items = filtered

        items.sort(key=sort_key)
        cached_data = items

        return render_template("index.html", items=items, search_text=search)

    except: return "No", 500

@app.route("/item/<id>")
def item_detail(id):
    for item in cached_data:
        if item["id"] == id:
            return render_template("detail.html", item=item)
    return "Item not found", 404

if __name__ == "__main__":
    app.run(debug=True)

