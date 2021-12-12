#!/usr/bin/env python3
import os
import wx
import sqlite3


class Database:
    m_connection: sqlite3.Connection
    m_name: str

    def __init__(self):
        self.m_name = ""
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

    def _close_database(self):
        if self.m_connection is None:
            return
        self.m_connection.close()

    def __del__(self):
        self._close_database()
