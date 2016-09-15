from flask import Flask

def run():
    app = Flask(__name__)

    #pylint: disable=unused-variable
    @app.route("/status")
    def status():
        return "Previews logging API running"

    app.run(host='0.0.0.0', port=8081)
