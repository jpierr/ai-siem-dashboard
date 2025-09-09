import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.parser import parse_syslog_line, parse_json_line

def test_syslog_parser():
    line = "Sep  7 21:15:01 localhost CRON[1234]: (root) CMD (echo 'backup done')"
    result = parse_syslog_line(line)
    assert result["process"].strip() == "CRON"

def test_syslog_parser_failed_ssh():
    line = "Sep  7 21:16:45 localhost sshd[2345]: Failed password for invalid user admin from 192.168.1.10 port 22 ssh2"
    result = parse_syslog_line(line)
    assert result["process"].strip() == "sshd"
    assert "Failed password" in result["msg"]

def test_json_parser():
    line = '{"timestamp":"2025-09-07T21:15:01Z","event":"login"}'
    result = parse_json_line(line)
    assert result["event"] == "login"

def test_json_parser_malformed():
    line = '{"timestamp": "2025-09-07T21:15:01Z", "event": "login"'  # missing closing brace
    result = parse_json_line(line)
    assert "raw" in result
