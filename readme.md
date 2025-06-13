Commandsß
python app.py
------------------------------------------------------------------------------------------------------------------
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/extract_bms_map/process_cobol_file_for_maps
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/extract_copybooks/process_cobol_file
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/

------------------------------------------------------------------------------------------------------------------
mainframe_analysis/
├── main.py
├── extractors/
│   ├── parsers
│   │   ├── parse_bms_map.py
│   │   ├── parse_copybook.py
│   │   ├── parse_jcl.py
│   │   └── parse_sql.py
│   ├── bms_map.py
│   ├── cics.py
│   ├── copybook.py
│   ├── jcl.py
│   └── sql.py
├── utils.py
├── app.py
├── readme.md
└── source (cbl.zip, jcl.zip)

------------------------------------------------------------------------------------------------------------------
