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


def test_get_filename_full():
    # cleaning
    if os.path.exists(os.path.join(UNIT_TEST_PATH_OUTPUT, "test1.db")):
        os.remove(os.path.join(UNIT_TEST_PATH_OUTPUT, "test1.db"))
    db = bart.Database()
    assert db.get_filename_full() == ""
    assert db.open_database(name="test1.db", path_name=UNIT_TEST_PATH_OUTPUT) is False # database didn't exists
    assert db.get_filename_full() == ""
    assert db.create_new_database(name="test1.db", path_name=UNIT_TEST_PATH_OUTPUT)
    assert db.open_database(name="test1.db", path_name=UNIT_TEST_PATH_OUTPUT) # ok, database exists
    assert db.get_filename_full() == os.path.join(UNIT_TEST_PATH_OUTPUT, "test1.db")


@pytest.fixture(scope="module")
def create_test_database():
    db = bart.Database()
    # cleaning
    if os.path.exists(os.path.join(UNIT_TEST_PATH_OUTPUT, "unit_test.db")):
        os.remove(os.path.join(UNIT_TEST_PATH_OUTPUT, "unit_test.db"))

    # create and open new database
    assert db.create_new_database("unit_test.db", UNIT_TEST_PATH_OUTPUT)
    assert db.open_database("unit_test.db", UNIT_TEST_PATH_OUTPUT)

    # TODO: Add user here


def test_open_database(create_test_database):
    db = bart.Database()
    assert db.open_database("unit_test.db", UNIT_TEST_PATH_OUTPUT)

