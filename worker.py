from flask import Flask, jsonify
import time
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/task")
def task():
    start = time.time()

    time.sleep(random.uniform(0.3, 1.0))
    value = random.randint(1, 100)
    elapsed = round(time.time() - start, 3)

    result = {
        "message": "Worker działa OK",
        "generated_value": value,
        "processing_time_s": elapsed,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    print(f"[WORKER] Wygenerowano: {result}")
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
