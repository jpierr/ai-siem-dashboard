import json
import re

def parse_syslog_line(line: str) -> dict:
    """
    Parse a syslog line into components.
    """
    pattern = (
        r'^(?P<month>\w+)\s+(?P<day>\d+)\s+(?P<time>\S+)\s+'
        r'(?P<host>\S+)\s+'
        r'(?P<process>[^\[\s]+)\[(?P<pid>\d+)\]:\s+'
        r'(?P<msg>.+)$'
    )
    match = re.match(pattern, line)
    return match.groupdict() if match else {"raw": line}

def parse_json_line(line: str) -> dict:
    """
    Parse a JSON log line into a dictionary.
    """
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        return {"raw": line}
