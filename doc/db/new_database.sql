CREATE TABLE 'game' (
'id' INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,
'date' DATETIME DEFAULT '(datetime('now','localtime'))',
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