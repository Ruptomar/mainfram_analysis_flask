from typing import List
import chardet
import re

# List of JCL utilities to search for
UTILITIES = [
    'IEFBR14', 'IEBGENER', 'IEBCOPY', 'IEBCOMPR', 'IEBEDIT',
    'IEBUPDTE', 'IEBDG', 'IEBISAM', 'IEBPTPCH',
    'IDCAMS', 'IEHPROGM', 'IEHLIST', 'IEHINITT', 'IEHMOVE',
    'ICKDSF', 'SPZAP', 'DFSORT', 'SYNCSORT', 'ICETOOL',
    'ICEGENER', 'IKJEFT01', 'IKJEFT1A', 'IKJEFT1B',
    'IRXJCL', 'ZOAU', 'SORT', 'SDSF', 'DFHCSDUP'
]

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

def process_jcl_file_for_program_only(jcl_file):
    jcl_bytes = jcl_file.read()
    encoding = detect_encoding(jcl_bytes)
    try:
        decoded_jcl = jcl_bytes.decode(encoding)
    except (UnicodeDecodeError, TypeError):
        decoded_jcl = jcl_bytes.decode('utf-8', errors='ignore')
    
    # Capture EXEC PGM=
    pattern = r'EXEC\s+PGM\s*=\s*([A-Z0-9$#@_-]+)'
    matches = re.findall(pattern, decoded_jcl, re.IGNORECASE)
    
    # Filter out utilities, dedupe & normalize
    programs = sorted({
        name.upper() for name in matches
        if name.upper() not in UTILITIES
    })
    
    print("Program only extraction completed.")
    return list(programs)
