import sqlite3


connection = sqlite3.connect("d7.db")
cursor = connection.cursor()


cursor.execute("""
    create table if not exists users(
        id integer primary key ,
        name varchar not null ,
        age integer
    )
""")

# create

# cursor.execute("insert into users (name, age) values (?,?)", ("Asadbek", 14))
# connection.commit()


# read

# users = cursor.execute("select id, name, age from users").fetchall()
# for user in users:
#     print(user)


#  update

# cursor.execute("update users set name=? where id=?", ("shohruh", 2))
# connection.commit()


#  delete

cursor.execute("delete from users where id=?", (3,))
connection.commit()