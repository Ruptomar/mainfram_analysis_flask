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
    sql_queries = re.findall(r'EXEC SQL.*?END-EXEC', decoded_code, re.DOTALL)
    print("sql_queries analysis completed")
    return sql_queries

def process_cobol_file_for_select(cobol_file):
    cobol_code = cobol_file.read()
    encoding = detect_encoding(cobol_code)
    
    try:
        decoded_code = cobol_code.decode(encoding)
    except (UnicodeDecodeError, TypeError):
        decoded_code = cobol_code.decode('utf-8', errors='ignore')

    # Extract all EXEC SQL blocks
    all_sql_blocks = re.findall(r'EXEC SQL.*?END-EXEC', decoded_code, re.DOTALL | re.IGNORECASE)

    # Filter only SELECT queries
    select_queries = []
    for sql in all_sql_blocks:
        if re.search(r'\bSELECT\b', sql, re.IGNORECASE) and not re.search(r'\b(INSERT|UPDATE|DELETE|MERGE)\b', sql, re.IGNORECASE):
            select_queries.append(sql.strip())

    print("SELECT-only SQL query extraction completed")
    return select_queries

def process_cobol_file_for_insert(cobol_file):
    cobol_code = cobol_file.read()
    encoding = detect_encoding(cobol_code)
    
    try:
        decoded_code = cobol_code.decode(encoding)
    except (UnicodeDecodeError, TypeError):
        decoded_code = cobol_code.decode('utf-8', errors='ignore')

    # Extract all EXEC SQL blocks
    all_sql_blocks = re.findall(r'EXEC SQL.*?END-EXEC', decoded_code, re.DOTALL | re.IGNORECASE)

    # Filter only INSERT queries
    insert_queries = []
    for sql in all_sql_blocks:
        if re.search(r'\bINSERT\b', sql, re.IGNORECASE):
            insert_queries.append(sql.strip())

    print("INSERT-only SQL query extraction completed")
    return insert_queries
