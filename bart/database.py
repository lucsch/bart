#!/usr/bin/env python3
import os

import wx


class Database:
    def __init__(self):
        self.m_name = None
        self.m_open = False

    def create_new_database(self, name, path_name):
        if os.path.exists(path_name) is False:
            wx.LogError("'{} didn't exists!".format(path_name))
            return False
        return True
