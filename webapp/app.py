from flask import Flask, render_template, request, jsonify

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

@app.route('/launch_app', methods=['POST'])
def launch_app():
    app_name = request.form['name']
    # You can add code here to do something with the app name, like launching the app
    print(f"Launching {app_name}")
    return jsonify({"status": "success", "message": f"{app_name} launched successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

