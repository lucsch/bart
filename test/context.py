#!/usr/bin/env python3
import os
import sys
import wx

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import bart  # noqa: F401,E402

# UNIT_TEST_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))
UNIT_TEST_PATH_OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "unit_test_output"))
if os.path.exists(UNIT_TEST_PATH_OUTPUT) is False:
    os.makedirs(UNIT_TEST_PATH_OUTPUT)

# send wx.Log to the console instead of GUI
my_log = wx.LogStderr()
wx.Log.SetActiveTarget(my_log)
