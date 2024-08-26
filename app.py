from flask import Flask, jsonify
import json
from app import extract_data

app = Flask(__name__)

# Replace with the path to your JSON file
json_file_path = "data.json"

@app.route('/api_data')
def get_data():
    try:
        # Read the JSON data from the file
        with open(json_file_path, 'r') as f:
            data = json.load(f)
        # Return the JSON data as a response
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({'error': 'JSON file not found'}), 404
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON data'}), 400

@app.route('/api_data_fetch')
def get_data_trigger():
    status = extract_data()
    return jsonify({'status': status}), 200

if __name__ == '__main__':
    app.run(debug=True)