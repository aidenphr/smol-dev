import sqlite3
from sqlite3 import Error
import config

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(config.DATABASE)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    try:
        sql = '''CREATE TABLE IF NOT EXISTS indices (
                    id integer PRIMARY KEY,
                    name text NOT NULL,
                    value real NOT NULL,
                    date text NOT NULL
                );'''
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def insert_index(conn, index):
    try:
        sql = '''INSERT INTO indices(name,value,date) VALUES(?,?,?)'''
        c = conn.cursor()
        c.execute(sql, index)
        return c.lastrowid
    except Error as e:
        print(e)

def close_connection(conn):
    try:
        conn.close()
    except Error as e:
        print(e)