import chardet
import re

def detect_encoding(cobol_code: bytes):
    result = chardet.detect(cobol_code)
    return result['encoding']

def process_cobol_file_for_maps(cobol_file):
    cobol_code = cobol_file.read()
    encoding = detect_encoding(cobol_code)
    
    try:
        decoded_code = cobol_code.decode(encoding)
    except (UnicodeDecodeError, TypeError):
        decoded_code = cobol_code.decode('utf-8', errors='ignore')

    # Normalize case and remove line numbers if needed
    normalized_code = decoded_code.upper()
    print("getting bms maps from cobol code")
    # Match SEND MAP(mapname), RECEIVE MAP(mapname), or COPY mapname
    map_pattern = r'\b(?:SEND|RECEIVE)\s+MAP\s*\(\s*(\w+)\s*\)|\bCOPY\s+(\w+)\b'

    matches = re.findall(map_pattern, normalized_code)
    print("flatten duplicate")
    # Flatten and deduplicate map names
    map_names = set()
    for send_receive, copy in matches:
        if send_receive:
            map_names.add(send_receive)
        if copy:
            map_names.add(copy)

    print("bms map extraction completed")
    return list(map_names)
