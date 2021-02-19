# -*- coding: utf-8 -*-
# Unittest for removing file
# author: Muztrizen

import unittest
from unittest.mock import patch
from remove_file import rm


class TestRemoveFile(unittest.TestCase):

  @patch('remove_file.os')
  def test_rm(self, mock_os):
    """
    Test case: Check if the Remove function 
    """
    # Input file path into Remove function
    rm("dir1/dir2/file.py")
    # Mock the Remove function
    mock_os.remove.assert_called_with("dir1/dir2/file.py")
