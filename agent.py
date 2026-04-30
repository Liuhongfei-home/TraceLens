import time
import random
import requests
import uuid

COLLECTOR_URL = "http://localhost:5000/log"

def run_agent(agent_id):
    trace_id = str(uuid.uuid4())

    for step in range(5):
        log = {
            "agent_id": agent_id,
            "trace_id": trace_id,
            "step": step,
            "timestamp": time.time(),
            "status": "ok"
        }

        if random.random() < 0.2:
            log["status"] = "error"
            log["error"] = "TimeoutError"

        try:
            requests.post(COLLECTOR_URL, json=log)
        except Exception as e:
            print("Failed to send log:", e)

        time.sleep(random.uniform(0.5, 1.5))


if __name__ == "__main__":
    run_agent("agent-1")
