"""Tests for the 'add' command."""

import json
import unittest.mock as mock

import pytest

from localalias import commands
import shared


@pytest.fixture
def add_cmd(cmd_args):
    """Builds and returns 'add' command."""
    cmd = commands.Add(cmd_args.alias, color=cmd_args.color)
    return cmd


@mock.patch('localalias.commands.Edit.edit_alias')
def test_add(edit_alias, cleandir, add_cmd, alias_dict):
    """Tests add command."""
    alias_cmd_string = alias_dict[add_cmd.alias]
    edit_alias.return_value = alias_cmd_string
    add_cmd()
    loaded_aliases = shared.load_aliases()
    assert loaded_aliases == {add_cmd.alias: alias_cmd_string}
    assert len(loaded_aliases) == 1
