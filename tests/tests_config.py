import pytest
import pathlib
from trash_cli.config import create_directory_structure


def test_config_directories_exit():
   result = create_directory_structure()

   assert result.exists()
   print(result)


