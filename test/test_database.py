#!/usr/bin/env python3

import os
import shutil
from datetime import datetime

import pytest
import wx

from .context import UNIT_TEST_PATH_OUTPUT
from .context import bart


def test_new_database():
    db = bart.Database()

    # false, path didn't exists
    assert db.create_new_database(name="test", path_name="") is False

