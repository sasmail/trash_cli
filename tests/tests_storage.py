import pytest
from trash_cli.storage import generate_unique_filename
from pathlib import Path


def test_generate_unique_filename_returns_tuple():
    """Test that generate_unique_filename returns a tuple of 3 items"""
    result = generate_unique_filename("test.txt")

    assert isinstance(result, tuple)
    assert len(result) == 3


def test_generate_unique_filename_format():
    """Test that the generated filename has the right format"""
    new_filename, file_path, timestamp = generate_unique_filename("sample.txt")

    # Check new_filename is a string
    assert isinstance(new_filename, str)

    # Check it contains the original stem
    assert "sample" in new_filename

    # Check it has the .txt extension
    assert new_filename.endswith(".txt")

    # Check it contains a timestamp (underscore separates it)
    assert "_" in new_filename

    # Check file_path is a Path object
    assert isinstance(file_path, Path)

    # Check timestamp is a string
    assert isinstance(timestamp, str)

if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v", "--color=yes"])