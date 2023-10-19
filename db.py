import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def posts_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM posts
        """
    ).fetchall()
    return [dict(row) for row in rows]

def posts_create(user, image_url, comment):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO posts (user, image_url, comment)
        VALUES (?, ?, ?)
        RETURNING *
        """,
        (user, image_url, comment),
    ).fetchone()
    conn.commit()
    return dict(row)

def posts_update_by_id(id, user, image_url, comment):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE posts SET user = ?, image_url = ?, comment = ?
        WHERE id = ?
        RETURNING *
        """,
        (user, image_url, comment, id),
    ).fetchone()
    conn.commit()
    return dict(row)

def posts_destroy_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        DELETE from posts
        WHERE id = ?
        """,
        id,
    )
    conn.commit()
    return {"message": "Post destroyed successfully"}

def posts_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM posts
        WHERE id = ?
        """,
        id,
    ).fetchone()
    return dict(row)

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