import re
from watch import parse

def test_parse_with_youtube_iframe():
    # Sample HTML content with a YouTube iframe
    html = '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    result = parse(html)

    # Check that the result is the expected YouTube URL
    expected_result = 'https://youtu.be/xvFZjo5PgG0'
    assert result == expected_result

def test_parse_with_youtube_iframe_and_optionals():
    # Sample HTML content with a YouTube iframe
    html = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    result = parse(html)

    # Check that the result is the expected YouTube URL
    expected_result = 'https://youtu.be/xvFZjo5PgG0'
    assert result == expected_result

def test_parse_with_non_youtube():
    # Sample HTML content with a YouTube iframe
    html = '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
    result = parse(html)

    # Check that the result is the expected YouTube URL
    expected_result = 'https://youtu.be/xvFZjo5PgG0'
    assert result != expected_result