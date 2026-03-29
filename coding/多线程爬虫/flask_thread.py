import flask
import json
import time
from concurrent.futures import ThreadPoolExecutor
from asyncio import as_completed

executor = ThreadPoolExecutor(max_workers=5)
app = flask.Flask(__name__)

@app.route("/long_task")
def long_task():
    f1 = executor.submit(get_date)
    f2 = executor.submit(get_api)
    f3 = executor.submit(get_model)
    return json.dumps({
        "getData": f1.result(),
        "getAPi": f2.result(),
        "getMode": f3.result()
    })

def get_date():
    time.sleep(1)
    return "getData"

def get_api():
    time.sleep(3)
    return "getAPi"

def get_model():
    time.sleep(5)
    return "getModel"

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
