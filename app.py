from logging import makeLogRecord
import sqlite3

Connection = sqlite3.connect('project.db')
cursor = Connection.cursor()




# All of these commands only need to be run once & can be deleted which is why I have turned them into comments
# Creates First Table which stores Prayer names and the Primary Key in two columns (which we will use to join to the second table)
# Primary ID will be the same for both tables since we will use it to join the tables and pull an index from one table while calling an index on the other table

'''
sql_command = """CREATE TABLE emp (
Prayer_ID INTEGER PRIMARY KEY,
Pname VARCHAR(20));"""

cursor.execute(sql_command)
'''

# Inserts 5 rows which each have an index for the two columns we preciously created
''''
sql_command = """INSERT INTO emp VALUES (1, "Fajr");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO emp VALUES (2, "Dhuar");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO emp VALUES (3, "Asr");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO emp VALUES (4, "Maghrib");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO emp VALUES (5, "Isha");"""
cursor.execute(sql_command)

Connection.commit()

'''

# Creates second table which holds two columns: The primary ID and the prayer time


''''
sql_command = """CREATE TABLE time (
Time_ID INTEGER PRIMARY KEY,
Ptime VARCHAR(20));"""

cursor.execute(sql_command)

'''

# Inserts 5 new rows which hold entries for both the Primary key column and the prayer time column 

'''

sql_command = """INSERT INTO time VALUES (1, "6:30 AM");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO time VALUES (2, "2:10 PM");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO time VALUES (3, "5:15 PM");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO time VALUES (4, "8:36 PM");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO time VALUES (5, "9:15 PM");"""
cursor.execute(sql_command)

Connection.commit()
'''


print('Choose Prayer:')
print('1. Fajr')
print('2. Dhuar')
print('3. Asr')
print('4. Maghrib')
print('5. Isha')

userinput = input('enter prayer name: ')


# This code will take the user input (prayer name from table 1) then locate that index on table 1
# Next it will join the two tables using 

if userinput == 'Fajr':
    cursor.execute("SELECT Ptime FROM emp inner join time on emp.Prayer_ID = time.Time_ID WHERE emp.Pname = 'Fajr'  ")
    ans = cursor.fetchall()
    print(ans)

elif userinput == 'Dhuar':
    cursor.execute("SELECT Ptime FROM emp inner join time on emp.Prayer_ID = time.Time_ID WHERE emp.Pname = 'Dhuar'  ")
    ans = cursor.fetchall()
    print(ans)

elif userinput == 'Asr':
    cursor.execute("SELECT Ptime FROM emp inner join time on emp.Prayer_ID = time.Time_ID WHERE emp.Pname = 'Asr'  ")
    ans = cursor.fetchall()
    print(ans)

elif userinput == 'Maghrib':
    cursor.execute("SELECT Ptime FROM emp inner join time on emp.Prayer_ID = time.Time_ID WHERE emp.Pname = 'Maghrib'  ")
    ans = cursor.fetchall()
    print(ans)

elif userinput == 'Isha':
    cursor.execute("SELECT Ptime FROM emp inner join time on emp.Prayer_ID = time.Time_ID WHERE emp.Pname = 'Isha'  ")
    ans = cursor.fetchall()
    print(ans)

elif userinput == 'All':
    cursor.execute("SELECT * FROM emp, time  ")
    ans = cursor.fetchall()
    print(ans)
    
else :
    print( 'Incorrect prayer name. Please try again! ')

Connection.close()