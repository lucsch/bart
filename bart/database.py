#!/usr/bin/env python3
import os
import wx
import sqlite3


class Database:
    m_connection: sqlite3.Connection
    m_name: str

    def __init__(self):
        self.m_name = ""
        self.m_path = ""
        self.m_connection = None

    def create_new_database(self, name, path_name):
        if os.path.exists(path_name) is False:
            wx.LogError("'{}' didn't exists!".format(path_name))
            return False

        database_path_name = os.path.join(path_name, name)
        if os.path.exists(database_path_name):
            wx.LogError("'{}' exists already!".format(database_path_name))
            return False

        # create the new database
        my_sql_txt = """
        CREATE TABLE 'game' (
        'id' INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,
        'date' DATETIME DEFAULT (datetime('now','localtime')),
        'name' VARCHAR DEFAULT NULL
        );
        
        CREATE TABLE 'game_players' (
        'game_id' INTEGER NOT NULL  PRIMARY KEY REFERENCES 'game' ('id'),
        'player_id' INTEGER NOT NULL  REFERENCES 'players' ('id'),
        'player_visible' INTEGER DEFAULT NULL
        );
        
        CREATE TABLE 'players' (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'name' CHAR DEFAULT NULL,
        'picture' BLOB DEFAULT NULL
        );
        
        CREATE TABLE 'game_rounds' (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'game_id' INTEGER NOT NULL  REFERENCES 'game' ('id'),
        'player_id' INTEGER NOT NULL  REFERENCES 'players' ('id'),
        'score1' INTEGER DEFAULT NULL,
        'score2' INTEGER DEFAULT NULL,
        'score3' INTEGER DEFAULT NULL,
        'score_total' INTEGER DEFAULT NULL
        );
        """
        if self.m_connection is not None:
            self._close_database()

        self.m_connection = sqlite3.connect(database_path_name)
        self.m_connection.executescript(my_sql_txt)
        self.m_connection.commit()
        return True

    def open_database(self, name, path_name):
        database_path_name = os.path.join(path_name, name)
        if os.path.exists(database_path_name) is False:
            wx.LogError("'{}' didn't exists!".format(database_path_name))
            return False

        self._close_database()
        self.m_connection = sqlite3.Connection(database_path_name)
        self.m_name = name
        self.m_path = path_name
        return True

    def get_filename_full(self):
        return os.path.join(self.m_path, self.m_name)

    def _close_database(self):
        if self.m_connection is None:
            return
        self.m_connection.close()

    def is_open(self):
        if self.m_connection is None:
            return False
        return True

    def __del__(self):
        self._close_database()

    def create_new_user(self, user_name):
        if self.is_open() is False:
            return False

        cur = self.m_connection.cursor()
        cur.execute("insert into players (name) VALUES (:user_name)", {"user_name": user_name})
        self.m_connection.commit()
        return True
