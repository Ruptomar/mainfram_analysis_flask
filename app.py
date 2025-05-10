from flask import Flask
from extractors.cics import cics_bp
from extractors.sql import sql_bp

app = Flask(__name__)

app.register_blueprint(cics_bp, url_prefix='/api/v1/cics')
app.register_blueprint(sql_bp, url_prefix='/api/v1/sql')

if __name__ == '__main__':
    app.run(debug=True)
