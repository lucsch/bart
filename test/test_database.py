#!/usr/bin/env python3

import os
import shutil
from datetime import datetime

import pytest
import wx

from .context import UNIT_TEST_PATH_OUTPUT
from .context import bart


def test_new_database_error():
    db = bart.Database()
    assert db.create_new_database(name="test", path_name="") is False # false, path didn't exists

    existing_path = os.path.join(UNIT_TEST_PATH_OUTPUT, "test_existing.wrongdb")
    with open(existing_path, 'w') as f:
        f.write("Dummy test file")
    # failed because file already exists
    assert db.create_new_database(name="test_existing.wrongdb", path_name=UNIT_TEST_PATH_OUTPUT) is False


def test_new_database():
    db = bart.Database()
    if os.path.exists(os.path.join(UNIT_TEST_PATH_OUTPUT, "test_new.db")):
        os.remove(os.path.join(UNIT_TEST_PATH_OUTPUT, "test_new.db"))
    assert db.create_new_database("test_new.db", path_name=UNIT_TEST_PATH_OUTPUT)


