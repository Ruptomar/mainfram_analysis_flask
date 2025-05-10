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
    cics_commands = re.findall(r'\b(CALL|SEND|RECEIVE|START|WAIT)\b', decoded_code)
    sql_queries = re.findall(r'EXEC SQL.*?END-EXEC', decoded_code, re.DOTALL)
    return cics_commands, sql_queries
