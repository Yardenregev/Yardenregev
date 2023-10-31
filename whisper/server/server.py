from flask import Flask

from models.models import ExcerptaModel

import configs.config as config


app = Flask(__name__)

excerpta_model = ExcerptaModel()

@app.route("/Record/Start",methods=["POST"])
def start_recording():
    return excerpta_model.start_recording()

@app.route("/Record/Stop",methods=["GET"])
def stop_recording():
    return excerpta_model.stop_recording()

if __name__ == "__main__":
    app.run(host=config.SERVER_HOST, port=config.SERVER_PORT,debug=True)
