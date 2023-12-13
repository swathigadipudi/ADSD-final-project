import sqlite3

DATABASE_NAME = 'example.db'

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Create social_media table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS social_media (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT,
            username TEXT
        )
    ''')

    # Create event_management table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS event_management (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT,
            organizer TEXT
        )
    ''')

    conn.commit()
    conn.close()

def add_social_media(platform, username):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('INSERT INTO social_media (platform, username) VALUES (?, ?)', (platform, username))

    conn.commit()
    conn.close()

def add_event_management(event_name, organizer):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('INSERT INTO event_management (event_name, organizer) VALUES (?, ?)', (event_name, organizer))

    conn.commit()
    conn.close()

def get_combined_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT social_media.id, social_media.platform, social_media.username,
               event_management.event_name, event_management.organizer
        FROM social_media
        LEFT JOIN event_management ON social_media.id = event_management.id
    ''')

    result = cursor.fetchall()

    conn.close()
    return result
