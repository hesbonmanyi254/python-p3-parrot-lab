# In the lib/testing/parrot_test.py file

import pytest
from lib.parrot import parrot

def test_prints_argument(capsys):
    '''prints the argument passed to it.'''
    parrot("Hello!")
    captured_out, _ = capsys.readouterr()
    assert captured_out.strip() == "Hello!"

def test_default_argument(capsys):
    '''prints the default argument when no argument is passed.'''
    parrot()
    captured_out, _ = capsys.readouterr()
    assert captured_out.strip() == "Squawk!"
