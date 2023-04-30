create_table_background = """
CREATE TABLE IF NOT EXISTS background (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    filename TEXT NOT NULL,
    degree_offset INTEGER DEFAULT 0 NOT NULL,
    flip_horizontal BOOLEAN DEFAULT FALSE,
    flip_vertical BOOLEAN DEFAULT FALSE,
    mode TEXT DEFAULT "fit"
);"""
create_table_character = """
CREATE TABLE IF NOT EXISTS character (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    filename TEXT NOT NULL,
    center_x INTEGER NOT NULL,
    center_y INTEGER NOT NULL,
    radius INTEGER NOT NULL
);"""
create_table_item = """
CREATE TABLE IF NOT EXISTS item (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    filename TEXT NOT NULL,
    token BOOLEAN NOT NULL,
    center_x INTEGER DEFAULT 0 NOT NULL,
    center_y INTEGER DEFAULT 0 NOT NULL,
    radius INTEGER DEFAULT 0 NOT NULL,
    grid_diameter INTEGER DEFAULT 1 NOT NULL
);"""
create_table_monster = """
CREATE TABLE IF NOT EXISTS monster (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    filename TEXT NOT NULL,
    center_x INTEGER DEFAULT 0 NOT NULL,
    center_y INTEGER DEFAULT 0 NOT NULL,
    radius INTEGER DEFAULT 0 NOT NULL,
    grid_diameter INTEGER DEFAULT 1 NOT NULL
);"""
create_table_player = """
CREATE TABLE IF NOT EXISTS player (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    filename TEXT NOT NULL,
    center_x INTEGER NOT NULL,
    center_y INTEGER NOT NULL,
    radius INTEGER NOT NULL,
);"""
