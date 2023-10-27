from flask import Flask, g
from views.web.routes import web
from views.errors.routes import errors
from datetime import timedelta
import json

def create_app():
    app = Flask(__name__)
    app.config.from_file(".config.json", load=json.load)
    app.config["TIMEZONE"] = "Europe/Madrid"
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSON_AS_ASCII'] = False
    app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
    app.register_blueprint(web, url_prefix="/")
    app.register_blueprint(errors)
    return app

app = create_app()
# CORS(app)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(debug=True, port=3000)
