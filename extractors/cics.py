from flask import Blueprint, request, jsonify
import zipfile
from utils import process_cobol_file

cics_bp = Blueprint('cics', __name__)

@cics_bp.route('/extract_cics', methods=['POST'])
def extract_cics():
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
                            cics_commands, _ = process_cobol_file(cobol_file)
                            if cics_commands:
                                results[filename] = cics_commands
                if results:
                    return jsonify(results), 200
                else:
                    return jsonify({"message": "No CICS commands found"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Invalid file format. Please upload a ZIP file."}), 400
