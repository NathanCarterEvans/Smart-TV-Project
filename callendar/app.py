from flask import Flask, request, jsonify
import subprocess
import shlex

app = Flask(__name__)

@app.route('/launch_app', methods=['POST'])
def launch_app():
    app_name = request.form['name']
    try:
        # Define your app launch commands here
        app_commands = {
            'Netflix': 'open -a Netflix',  # macOS example, replace with the actual command
            'Spotify': 'open -a Spotify',  # macOS example, replace with the actual command
            # Add other apps as needed
        }
        # Securely parse the command line string
        command = shlex.split(app_commands.get(app_name, ''))
        if command:
            # Launch the application
            subprocess.run(command, check=True)
            return jsonify({"status": "success", "message": f"{app_name} launched successfully!"})
        else:
            return jsonify({"status": "error", "message": "App command not found."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

