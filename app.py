#!/usr/bin/env python
import argparse
import sys
from flask import Flask, jsonify, request
from pathlib import Path

FILE_NAME = "data.csv"

app = Flask(__name__)


@app.route('/data', methods=['GET'])
def read_data() -> str:
    try:
        with open(FILE_NAME, "r") as file:
            data = file.read()
        return jsonify({"data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def __write_lines(new_lines: list[str]):
    with open(FILE_NAME, "w") as file:
        [file.write(data + "\n") for data in new_lines]


@app.route('/upload', methods=['POST', 'PUT'])
def insert_data():
    new_data = request.json.get('new_data', '').strip()
    if not new_data:
        return jsonify({"error": "Data to insert is required"}), 400
    data, status_code = read_data()
    data = data.json
    if status_code == 200:
        data = data['data']
    else:
        return data, status_code
    lines = data.split()
    if new_data.strip() in lines:
        return jsonify({"error": f"'{new_data}' already in database"}), 400

    print(f"Writing '{new_data}' to '{lines}")
    try:
        with open(FILE_NAME, "a") as file:
            file.write(new_data + "\n")
            return jsonify({"new_data": new_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/update', methods=['PATCH'])
def update_data():
    old_data = request.json.get('old_data', '').strip()
    new_data = request.json.get('new_data', '').strip()
    lines = read_data().split()
    if old_data.strip() not in lines:
        return jsonify({"error": f"'{new_data}' not found in database"}), 404

    try:
        updated_lines = [new_data if line == old_data else line for line in lines]
        __write_lines(updated_lines)
        return jsonify({"new_data": new_data, "old_data": old_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/erase", methods=['DELETE'])
def delete_data():
    data_to_del = request.args.get('data', '').strip()
    if not data_to_del:
        return jsonify({"error": "Data to delete is required"}), 400
    data, status_code = read_data()
    data = data.json
    if status_code == 200:
        data = data['data']
    else:
        return data, status_code
    lines = data.split()
    if data_to_del.strip() not in lines:
        return jsonify({"error": f"'{data_to_del}' not found in database"}), 404
    try:
        updated_lines = [line for line in lines if line.strip() != data_to_del]
        __write_lines(updated_lines)
        return jsonify({"data": data_to_del}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def main():
    # Make sure database file exists
    try:
        with open(FILE_NAME, "a"):
            pass
    except:
        print("Unexpected error.")


if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", debug=True, port=8080)
