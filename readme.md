Commandsß
python app.py
------------------------------------------------------------------------------------------------------------------
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/cics/extract_cics
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/sql/extract_sql
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/sql/extract_sql_select
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/sql/extract_sql_insert
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/sql/extract_sql_update
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/sql/extract_sql_delete
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/copybook/extract_copybook
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/jcl_dsn/extract_jcl_dsn
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/jcl_dsn/extract_program_from_jcl
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/jcl_dsn/extract_program_only_from_jcl
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/jcl_dsn/extract_utility_only_from_jcl
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/jcl_dsn/extract_proc_from_jcl
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/bms_map/extract_bms_map

------------------------------------------------------------------------------------------------------------------
Use cbl.zip for:
cics
sql
copybook
bms_map
Use jcl.zip for:
cics

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
