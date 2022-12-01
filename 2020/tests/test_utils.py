"""Tests for utility functions."""
from pathlib import Path
from aoc_2020.utils import daily_input, lines

def test_daily_input():
    """Test the daily_input() utility function."""
    assert daily_input(1).exists()

def test_lines(tmp_path: Path):
    """Test the lines() utility function."""
    file = tmp_path / "temp.txt"
    file.write_text("foo bar\nbaz")

    assert list(lines(file)) == ["foo bar", "baz"]

    file = tmp_path / "numbers.txt"
    file.write_text("1\n99999\n-99")

    assert list(lines(file, int)) == [1, 99999, -99]
