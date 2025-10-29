from flask import Flask, render_template
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_FILE = os.path.join(BASE_DIR, 'content.json')

def load_content():
    with open(CONTENT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data.get("pages", [])

pages = load_content()

for page in pages:
    route = "/" if page.get("route") == "index" else f"/{page.get('route')}"

    def make_view(p):
        def view():
            template = 'images.html' if "images" in p else 'content.html'
            return render_template(template, content=p, pages=pages)
        return view

    app.add_url_rule(route, page.get("route"), make_view(page))

if __name__ == "__main__":
    app.run(debug=True)
