import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.parser import parse_syslog_line, parse_json_line

def test_syslog_parser():
    line = "Sep  7 21:15:01 localhost CRON[1234]: (root) CMD (echo 'backup done')"
    result = parse_syslog_line(line)
    assert result["process"].strip() == "CRON"

def test_json_parser():
    line = '{"timestamp":"2025-09-07T21:15:01Z","event":"login"}'
    result = parse_json_line(line)
    assert result["event"] == "login"
