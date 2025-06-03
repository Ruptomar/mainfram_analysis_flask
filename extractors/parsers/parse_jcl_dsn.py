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
    print(datasetnames)

    print("dataset name extraction completed")
    return datasetnames
