from flask import Blueprint, request, jsonify
import zipfile
from extractors.parsers.parse_bms_map import process_cobol_file_for_maps

bms_map_bp = Blueprint('bms_map', __name__)

@bms_map_bp.route('/extract_bms_map', methods=['POST'])
def extract_bms_map():
    print("extracting bms map")
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
                            bms_maps = process_cobol_file_for_maps(cobol_file)
                            if bms_maps:
                                results[filename] = bms_maps
                if results:
                    return jsonify(results), 200
                else:
                    return jsonify({"message": "No SQL queries found"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Invalid file format. Please upload a ZIP file."}), 400
