import sqlite3

# Establish a connection object instance
connection = sqlite3.connect("data.db")

# Establish a cursor object
cursor = connection.cursor()

# Query all data
cursor.execute("SELECT * FROM events WHERE date= '2088.10.15'")
rows = cursor.fetchall()
print(rows)

# Query certain columns based on conditions
cursor.execute("SELECT band, date FROM events WHERE date= '2088.10.15'")
rows = cursor.fetchall()
print(rows)

# INSERT new rows
new_rows = [('Cats', 'Cat city', '2088.10.17'), 
            ('Hens', 'Hen city', '2088.10.17')]

# We use the execute() method when we have a single row, and executemany method when we have multiple row
cursor.executemany("INSERT INTO events VALUES(?, ?, ?)", new_rows)

# Establish a  connection commit
connection.commit()

# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)