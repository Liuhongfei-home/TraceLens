import requests
from collections import defaultdict

COLLECTOR_URL = "http://localhost:5000/logs"

def fetch_logs():
    return requests.get(COLLECTOR_URL).json()

def analyze():
    logs = fetch_logs()
    trace_map = defaultdict(list)

    for log in logs:
        trace_map[log["trace_id"]].append(log)

    issues = []

    for trace_id, entries in trace_map.items():
        errors = [e for e in entries if e["status"] == "error"]

        if errors:
            issues.append({
                "trace_id": trace_id,
                "error_count": len(errors),
                "agents": list(set(e["agent_id"] for e in entries)),
                "root_cause": detect_root_cause(errors)
            })

    return issues

def detect_root_cause(errors):
    error_types = defaultdict(int)

    for e in errors:
        error_types[e.get("error", "unknown")] += 1

    return max(error_types, key=error_types.get)

if __name__ == "__main__":
    print(analyze())
