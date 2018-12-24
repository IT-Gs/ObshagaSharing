# Import sqlite3 module (in standart library - do not need to install)
import sqlite3


# Connect ot Database - in local file app.db
conn = sqlite3.connect('app_u.db')
# Create a cursor - a
c = conn.cursor()

c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Firstname TEXT,
    Lastname TEXT,
    Username TEXT,
    ObshagaAdress TEXT,
    Room TEXT,
    Password TEXT

)
''')

conn.commit()

# Adding some data (feel free to use you own data)
c.execute('''
    INSERT INTO users (Firstname, Lastname, Username, ObshagaAdress, Room, Password)
    VALUES ("Pavel", "Okop", "PashaOk", "Zaporozhskaya,21/A", "5", "1234567890")
''')
conn.commit()


c.execute('''
    ALTER TABLE users
    ADD COLUMN login TEXT
''')
conn.commit()


c.execute('''
    UPDATE users
    SET login = "paul"
    WHERE Lastname = "Okop"
''')
conn.commit()


c.execute('''
    ALTER TABLE users
    ADD COLUMN photo TEXT
''')
conn.commit()



# Our base data
users = [
    {
        'login': 'paul',
        'Firstname': 'Pavel',
        'Lastname': 'Okop',
        'Username': 'PashaOk',
        'ObshagaAddress': 'Zaporozhskaya,21/A',
        'Room': '5',
        'Password': '1234567890'
    },
    {
        'login': 'igor',
        'Firstname': 'Igor',
        'Lastname': 'Dashkov',
        'Username': 'IgirDa',
        'ObshagaAddress': 'Vitebskaya,14',
        'Room': '23',
        'Password': '11111111'
    }

]


# Adding it in the loop
for user in users:
    c.execute("INSERT INTO users "
              "(login, Firstname, Lastname, Username, ObshagaAddress, Room, Password)"
              "VALUES "
              "('{login}', '{Firstname}', '{Lastname}', '{Username}', '{ObshagaAddress}', '{Room}', '{Password}')".format(**user))
    conn.commit()

# Add second table
c.execute('''
    CREATE TABLE requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        conditions TEXT,
        time DATETIME,
        ObshagaAddress TEXT,
        bonuses TEXT
    )
''')
conn.commit()


c.execute('''
    INSERT INTO request (name, conditions, time, ObshagaAddress, bonuses)
    VALUES
    ("Pan for pancakes","clean, non-stick", "2 weeks", "Vitebskaya,14", "10 pancakes")
''')
conn.commit()

# Many to many connection
c.execute('''
    CREATE TABLE users_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        request_id INTEGER
    )
''')
conn.commit()


c.execute("INSERT INTO users_requests (user_id, request_id) VALUES (1, 1)")
conn.commit()
c.execute("INSERT INTO users_requests (user_id, request_id) VALUES (3, 1)")
conn.commit()


c.execute("SELECT u.* "
          "FROM users_requests ur "
          "JOIN users u ON (u.id=ur.user_id) "
          "WHERE ur.request_id=1")
conn.close()

