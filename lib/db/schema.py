create_table_backgrounds = """
CREATE TABLE IF NOT EXISTS backgrounds (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    filename TEXT NOT NULL,
    degree_offset INTEGER DEFAULT 0 NOT NULL,
    flip_horizontal BOOLEAN DEFAULT FALSE,
    flip_vertical BOOLEAN DEFAULT FALSE,
    mode TEXT DEFAULT "fit"
);"""
create_table_characters = """
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    filename TEXT NOT NULL,
    center_x INTEGER NOT NULL,
    center_y INTEGER NOT NULL,
    radius INTEGER NOT NULL
);"""
create_table_items = """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    filename TEXT NOT NULL,
    token BOOLEAN NOT NULL,
    center_x INTEGER DEFAULT 0 NOT NULL,
    center_y INTEGER DEFAULT 0 NOT NULL,
    radius INTEGER DEFAULT 0 NOT NULL,
    grid_width INTEGER DEFAULT 0 NOT NULL,
    grid_height INTEGER DEFAULT 0 NOT NULL
);"""
create_table_monsters = """
CREATE TABLE IF NOT EXISTS monsters (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    filename TEXT NOT NULL,
    center_x INTEGER DEFAULT 0 NOT NULL,
    center_y INTEGER DEFAULT 0 NOT NULL,
    radius INTEGER DEFAULT 0 NOT NULL,
    grid_diameter INTEGER DEFAULT 1 NOT NULL
);"""
create_table_players = """
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    filename TEXT NOT NULL,
    center_x INTEGER NOT NULL,
    center_y INTEGER NOT NULL,
    radius INTEGER NOT NULL,
    max_health INTEGER NOT NULL,
    current_heath INTEGER DEFAULT max_health
);"""
