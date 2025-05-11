from flask import Blueprint, request, jsonify
import zipfile
from extractors.parsers.parse_copybooks import process_cobol_file

copybooks_bp = Blueprint('copybooks', __name__)

@copybooks_bp.route('/extract_copybooks', methods=['POST'])
def extract_copybooks():
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
                            copybooks = process_cobol_file(cobol_file)
                            if copybooks:
                                results[filename] = copybooks
                if results:
                    return jsonify(results), 200
                else:
                    return jsonify({"message": "No Copybooks found"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Invalid file format. Please upload a ZIP file."}), 400
