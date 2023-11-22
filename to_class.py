import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("d7.db")
        self.cursor = self.connection.cursor()
        self.create_user()

    def create_user(self):
        self.cursor.execute("""
        create table if not exists users(
            id integer primary key,
            name varchar not null,
            age integer
        )""")

    def add_user(self, name, age):
        self.cursor.execute("insert into users (name, age) values (?,?)",
                            (name, age))
        self.connection.commit()

    def get_user(self, id):
        self.cursor.execute("select * from users where id=?", (id,))
        return self.cursor.fetchone()

    def all_user(self):
        self.cursor.execute("select * from users")
        return self.cursor.fetchall()

    def edit_user(self, id, name, age):
        self.cursor.execute("update users set name=?, age=? where id=?",
                            (name, age, id))
        self.connection.commit()

    def delete_user(self, id):
        self.cursor.execute("delete from users where id=?", (id,))
        self.connection.commit()


