from flask import Flask
from extractors.cics import cics_bp
from extractors.sql import sql_bp
from extractors.copybook import copybook_bp
from extractors.jcl_dsn import jcl_dsn_bp
from extractors.bms_map import bms_map_bp

app = Flask(__name__)

app.register_blueprint(cics_bp, url_prefix='/api/v1/cics')
app.register_blueprint(sql_bp, url_prefix='/api/v1/sql')
app.register_blueprint(copybook_bp, url_prefix='/api/v1/copybook')
app.register_blueprint(jcl_dsn_bp, url_prefix='/api/v1/jcl_dsn')
app.register_blueprint(bms_map_bp, url_prefix='/api/v1/bms_map')

if __name__ == '__main__':
    app.run(debug=True)
