create_table_backgrounds = """
CREATE TABLE IF NOT EXISTS backgrounds (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    filename TEXT NOT NULL,
    degree_offset INTEGER DEFAULT 0 NOT NULL,
    flip_horizontal BOOLEAN DEFAULT FALSE,
    flip_vertical BOOLEAN DEFAULT FALSE,
    mode TEXT DEFAULT fit
);"""
create_table_pcs = """
CREATE TABLE IF NOT EXISTS pcs (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    filename TEXT NOT NULL,
    center_x INTEGER NOT NULL,
    center_y INTEGER NOT NULL
    radius INTEGER NOT NULL
);"""

