"""Test for my functions.
"""
import pytest
import mock
import builtins
from functions import tell_story

def test_tell_story():
    with mock.patch.object(builtins, 'input', lambda _: 'test_input'):
        assert tell_story('test') == 'This should be an adjective: test_input.'\
            ' This should be a noun: test_input. This should be a verb: test_input.'
test_tell_story()
