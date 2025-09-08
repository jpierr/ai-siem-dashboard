from src.parser import parse_log_line

def test_parse_log_line():
    sample = '{"event":"login"}'
    result = parse_log_line(sample)
    assert isinstance(result, dict)

    