from flask import Blueprint, request, jsonify
import zipfile
from extractors.parsers.parse_sql import process_cobol_file
from extractors.parsers.parse_sql import process_cobol_file_for_select
from extractors.parsers.parse_sql import process_cobol_file_for_insert

sql_bp = Blueprint('sql', __name__)

@sql_bp.route('/extract_sql', methods=['POST'])
def extract_sql():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and file.filename.endswith('.zip'):
        try:
            with zipfile.ZipFile(file, 'r') as zip_ref:
                results = {}
                for filename in zip_ref.namelist():
                    if filename.endswith('.cbl'):
                        with zip_ref.open(filename) as cobol_file:
                            sql_queries = process_cobol_file(cobol_file)
                            if sql_queries:
                                results[filename] = sql_queries
                if results:
                    return jsonify(results), 200
                else:
                    return jsonify({"message": "No SQL queries found"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Invalid file format. Please upload a ZIP file."}), 400

@sql_bp.route('/extract_sql_select', methods=['POST'])
def extract_sql_select():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and file.filename.endswith('.zip'):
        try:
            with zipfile.ZipFile(file, 'r') as zip_ref:
                results = {}
                for filename in zip_ref.namelist():
                    if filename.endswith('.cbl'):
                        with zip_ref.open(filename) as cobol_file:
                            sql_queries = process_cobol_file_for_select(cobol_file)
                            if sql_queries:
                                results[filename] = sql_queries
                if results:
                    return jsonify(results), 200
                else:
                    return jsonify({"message": "No SQL queries found"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Invalid file format. Please upload a ZIP file."}), 400
    
@sql_bp.route('/extract_sql_insert', methods=['POST'])
def extract_sql_insert():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and file.filename.endswith('.zip'):
        try:
            with zipfile.ZipFile(file, 'r') as zip_ref:
                results = {}
                for filename in zip_ref.namelist():
                    if filename.endswith('.cbl'):
                        with zip_ref.open(filename) as cobol_file:
                            sql_queries = process_cobol_file_for_insert(cobol_file)
                            if sql_queries:
                                results[filename] = sql_queries
                if results:
                    return jsonify(results), 200
                else:
                    return jsonify({"message": "No SQL queries found"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Invalid file format. Please upload a ZIP file."}), 400
