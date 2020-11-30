import sqlite3


class SQL:
    def __init__(self, db_file):
        self.file = db_file
        try:
            conn = sqlite3.connect(f"{self.file}.db")
        except Exception as e:
            print(f"Function 'init' - {e} ")
            return -1
        conn.execute('''
            CREATE TABLE IF NOT EXISTS RSS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title text NOT NULL,
                description text,
                link text
                
            );
        ''')
        conn.close()

    def insert(self, entry):
        try:
            conn = sqlite3.connect(f"{self.file}.db")
        except Exception as e:
            print(f"Function 'insert' - {e} ")
            return -1
        conn.execute('''
            INSERT INTO RSS(title, description, link)
            VALUES (?, ?, ?);
        ''', (entry.title, entry.summary, entry.link))
        conn.commit()
        conn.close()
        pass

    def get(self, skip, limit):
        try:
            conn = sqlite3.connect(f"{self.file}.db")
        except Exception as e:
            print(f"Function 'get' - {e} ")
            return -1
        result = [entry for entry in conn.execute('''
            SELECT * FROM RSS LIMIT ? OFFSET ?;
        ''', (limit, skip))]
        conn.close()
        return result

    def has(self, title):
        try:
            conn = sqlite3.connect(f"{self.file}.db")
        except Exception as e:
            print(f"Function 'has' - {e} ")
            return -1
        query = conn.execute('''
            SELECT * FROM RSS WHERE title = ?;
        ''', (title,))
        result = query.fetchone() is not None
        conn.close()
        return result
