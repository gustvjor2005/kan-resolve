from inspect import stack
import json
import re


def parse_log(log):
    try:
        # Parse JSON log
        log_data = json.loads(log)
        severity = log_data.get("severity", "UNKNOWN")
        message = log_data.get("message", "")
        stack_trace = log_data.get("stack_trace", "")

        # Generalized error detection patterns
        errors = re.findall(r'Exception.*?: (.*?)(:|\n|$)', message)
        stack_trace = re.findall(r'Exception.*?: (.*?)(:|\n|$)', stack_trace)
        unresolved_placeholders = re.findall(
            r"Could not resolve placeholder '(.*?)'", message)
        bean_creation_issues = re.findall(
            r"Error creating bean with name '(.*?)'", message)

        info = {
            "severity": severity,
            "message": message,
            "stack_trace": [e[0] for e in stack_trace],
            "errors": [e[0] for e in errors],
            "unresolved_placeholders": unresolved_placeholders,
            "bean_creation_issues": bean_creation_issues
        }

    except json.JSONDecodeError:
        # Log parsing failure
        info = {
            "severity": "ERROR",
            "message": f"Invalid log format: {log}"
        }

    if info["severity"] == "ERROR":
        print(f"Severity: {info['severity']}")
        if "message" in info:
            print("Message:")
            print(f"  {info['message']}")
        if "stack_trace" in info:
            print("Stack Trace:")
            for line in info['stack_trace']:
                print(f"  - {line}")
        if info.get('errors'):
            print("Errors Detected:")
            for error in info['errors']:
                print(f"  - {error}")
        if info.get('unresolved_placeholders'):
            print("Unresolved Placeholders:")
            for placeholder in info['unresolved_placeholders']:
                print(f"  - {placeholder}")
        if info.get('bean_creation_issues'):
            print("Bean Creation Issues:")
            for bean in info['bean_creation_issues']:
                print(f"  - {bean}")
        print()
