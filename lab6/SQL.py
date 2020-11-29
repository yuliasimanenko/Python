import sqlite3


class SQL:
    def __init__(self, db_file):
        self.file = db_file
        conn = sqlite3.connect(self.file)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS RSS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title text NOT NULL,
                description text,
                link text,
                website_name text NOT NULL
            );
        ''')
        conn.close()

    def insert(self, entry, website_name):
        conn = sqlite3.connect(self.file)
        conn.execute('''
            INSERT INTO RSS(title, description, link, website_name)
            VALUES (?, ?, ?, ?);
        ''', (entry.title, entry.summary, entry.link, website_name))
        conn.commit()
        conn.close()
        pass

    def get(self, website_name, skip, limit):
        conn = sqlite3.connect(self.file)
        result = [entry for entry in conn.execute('''
            SELECT * FROM RSS
            WHERE website_name = ? LIMIT ? OFFSET ?;
        ''', (website_name, limit, skip))]
        conn.close()
        return result

    def has(self, website_name, title):
        conn = sqlite3.connect(self.file)
        query = conn.execute('''
            SELECT * FROM RSS
            WHERE website_name = ?
            AND title = ?;
        ''', (website_name, title))
        result = query.fetchone() is not None
        conn.close()
        return result


