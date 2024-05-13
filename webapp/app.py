from flask import Flask, render_template

app = Flask(__name__)

# List of apps. Each app is a dictionary containing its name and the URL for its icon.
apps = [
    {"name": "App One", "icon": "/static/missing_image.png"},
    {"name": "App Two", "icon": "/static/missing_image.png"},
    {"name": "App Three", "icon": "/static/missing_image.png"}
]

@app.route('/')
def index():
    return render_template('index.html', apps=apps)

if __name__ == '__main__':
    app.run(debug=True)

