import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS posts;
        """
    )
    conn.execute(
        """
        CREATE TABLE posts (
          id INTEGER PRIMARY KEY NOT NULL,
          user TEXT,
          image_url TEXT,
          comment TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    posts_seed_data = [
        ("Peter", "test.jpg", "comment"),
        ("Mason", "Test.jpg", "comment"),
        ("Jason", "test.jpg", "comment blah"),
    ]
    conn.executemany(
        """
        INSERT INTO posts (user, image_url, comment)
        VALUES (?,?,?)
        """,
        posts_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()