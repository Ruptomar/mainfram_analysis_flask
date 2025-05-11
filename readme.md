Commandsß
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/cics/extract_cics
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/sql/extract_sql
curl -X POST -F "file=@./path_to_your_file.zip" http://127.0.0.1:5000/api/v1/copybook/extract_copybook
python app.py

mainframe_analysis/
├── main.py
├── extractors/
│   ├── __init__.py
│   ├── cics.py
│   └── sql.py
├── utils.py
└── requirements.txt
