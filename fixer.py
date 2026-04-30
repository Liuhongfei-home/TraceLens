def suggest_fix(root_cause):
    if root_cause == "TimeoutError":
        return "Increase retries, check network latency, adjust timeout settings"

    if root_cause == "ConnectionError":
        return "Check service discovery or node availability"

    return "Manual investigation required"

def generate_report(issues):
    for issue in issues:
        print("==== BUG REPORT ====")
        print(f"Trace ID: {issue['trace_id']}")
        print(f"Error Count: {issue['error_count']}")
        print(f"Affected Agents: {issue['agents']}")
        print(f"Root Cause: {issue['root_cause']}")
        print(f"Fix: {suggest_fix(issue['root_cause'])}")
        print()

if __name__ == "__main__":
    from analyzer import analyze
    issues = analyze()
    generate_report(issues)
