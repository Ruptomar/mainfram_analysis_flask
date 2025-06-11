from flask import Blueprint, request, jsonify
import zipfile
from extractors.parsers.parse_jcl_dsn import process_jcl_file
from extractors.parsers.parse_jcl_dsn import process_jcl_file_for_program
from extractors.parsers.parse_jcl_dsn import process_jcl_file_for_program_only


jcl_dsn_bp = Blueprint('jcl_dsn', __name__)

@jcl_dsn_bp.route('/extract_jcl_dsn', methods=['POST'])
def extract_jcl_dsn():
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
                    if filename.endswith('.jcl'):
                        with zip_ref.open(filename) as jcl_file:
                            jcl_dsns = process_jcl_file(jcl_file)
                            if jcl_dsns:
                                results[filename] = jcl_dsns
                if results:
                    return jsonify(results), 200
                else:
                    return jsonify({"message": "No DSNs found"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Invalid file format. Please upload a ZIP file."}), 400

@jcl_dsn_bp.route('/extract_program_from_jcl', methods=['POST'])
def extract_program_from_jcl():
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
                    if filename.endswith('.jcl'):
                        with zip_ref.open(filename) as jcl_file:
                            jcl_pgms = process_jcl_file_for_program(jcl_file)
                            if jcl_pgms:
                                results[filename] = jcl_pgms
                if results:
                    return jsonify(results), 200
                else:
                    return jsonify({"message": "No Programs found"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Invalid file format. Please upload a ZIP file."}), 400

@jcl_dsn_bp.route('/extract_program_only_from_jcl', methods=['POST'])
def extract_program_only_from_jcl():
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
                    if filename.endswith('.jcl'):
                        with zip_ref.open(filename) as jcl_file:
                            jcl_pgms = process_jcl_file_for_program_only(jcl_file)
                            if jcl_pgms:
                                results[filename] = jcl_pgms
                if results:
                    return jsonify(results), 200
                else:
                    return jsonify({"message": "No Programs found"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Invalid file format. Please upload a ZIP file."}), 400
