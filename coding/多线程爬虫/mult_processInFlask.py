import flask
import time
import mult_process
from concurrent.futures import ProcessPoolExecutor
app=flask.Flask(__name__)
@app.route("/long_task/<numbers>")
def index(numbers):
    try:
        numbers_list = [int(i) for i in numbers.split(",")]
    except ValueError:
        return {"error": "请使用逗号分隔的数字，如 /long_task/1,2,3"}, 400
    with process_pool as executor:
        executor.map(mult_process.task1, numbers_list)
    return {"message": "任务完成", "numbers": numbers_list}
if __name__ == "__main__":
    process_pool=ProcessPoolExecutor()
    app.run(debug=True)