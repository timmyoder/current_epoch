"""microservice for returning current epoch"""
from flask import Flask
import time
import os

app = Flask(__name__)


@app.route('/current/')
def get_current_epoch():
    return str(time.time())


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
