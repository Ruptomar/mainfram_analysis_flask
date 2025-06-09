import chardet
import re

def detect_encoding(jcl_code: bytes):
    result = chardet.detect(jcl_code)
    return result['encoding']

def process_jcl_file(jcl_file):
    jcl_code = jcl_file.read()
    encoding = detect_encoding(jcl_code)
    try:
        decoded_jcl = jcl_code.decode(encoding)
    except (UnicodeDecodeError, TypeError):
        decoded_jcl = jcl_code.decode('utf-8', errors='ignore')
    
    # Extract dataset names using DSN= or DSNAME= patterns
    dsn_pattern = r'(?:DSN|DSNAME)\s*=\s*(?:\'|")?([^,\)\s\'"]+)'
    datasetnames = re.findall(dsn_pattern, decoded_jcl, re.IGNORECASE)

    print("dataset name extraction completed")
    return datasetnames

def process_jcl_file_for_program(jcl_file):
   
    jcl_code = jcl_file.read()
    encoding = detect_encoding(jcl_code)
    try:
        decoded_jcl = jcl_code.decode(encoding)
    except (UnicodeDecodeError, TypeError):
        # Fallback to utf-8 with error ignoring if detection fails or is incorrect
        decoded_jcl = jcl_code.decode('utf-8', errors='ignore')
    
    # Extract program names using EXEC PGM= pattern
    pgm_pattern = r'EXEC\s+PGM\s*=\s*([A-Z0-9$#@_-]+)'
    #program_names = re.findall(pgm_pattern, decoded_jcl, re.IGNORECASE)
    program_names = list(set(re.findall(pgm_pattern, decoded_jcl, re.IGNORECASE)))

    print("Program name extraction completed.")
    return program_names
