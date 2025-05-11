import chardet
import re

def detect_encoding(cobol_code: bytes):
    result = chardet.detect(cobol_code)
    return result['encoding']

def process_cobol_file(cobol_file):
    cobol_code = cobol_file.read()
    encoding = detect_encoding(cobol_code)
    try:
        decoded_code = cobol_code.decode(encoding)
    except (UnicodeDecodeError, TypeError):
        decoded_code = cobol_code.decode('utf-8', errors='ignore')
    copybooks = re.findall(r'(?:COPY|INCLUDE)\s+([\w\-\.]+)\.?', decoded_code)
    return copybooks
