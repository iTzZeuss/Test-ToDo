import sqlite3 as sql
import pyfiglet
import pandas as pd
import os
import glob, os

print(pyfiglet.figlet_format("db INTERFACE", justify="center", font="starwars", width=110))

print("Existing Data-Base files: ")
print("")

for file in glob.glob("*.db"):
    print(file)
print("")

current_db = input("Input paht to the existing DB or to create new ('example.db')> ")
conn = sql.connect(current_db)
db = conn.cursor()
print("Conneced successfully.\n")

print("Input sql command or write 'cmd' to view interface commands.")
cmd = ""

def table_info(db, conn):
    tables = db.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    for table_name in tables:
        table_name = table_name[0] # tables is a list of single item tuples
        table = pd.read_sql_query("SELECT * from {} LIMIT 0".format(table_name), conn)
        print(table_name)
        for col in table.columns:
            print('\t' + col)
        print()


while True:
    cmd = input("sql lite> ")
    show = True
    execute = True

    if cmd == "quit":
        conn.close()
        print("Quited.")
        exit()
    elif cmd == "cmd":
        print("")
        print("Commands -------------------------")
        print("cmd - view commands.")
        print("quit - quit.")
        print("vtable - view table.")
        print("dbtables - view all existing tables in the file.")
        print("commit - commit changes to db.")
        print("connect - connect to existing db or create new '.db' file.")
        print("cd - change directory.")
        print("delete - delete existing '.db' file.")
        print("vdb - View all existing databases in the current directory.")
        print("curdir - View current directory.")
        print("----------------------------------")
        print("")
        execute = False
        show = False
    elif cmd == "vtable":
        try:
            print(pd.read_sql_query("SELECT * FROM " + input("Input TABLE name> "), conn))
        except Exception as ex:
            print("ERROR: \n")
            print(ex)
            print("")
        execute = False
        show = False
    elif cmd == "commit":
        print("Commited changes successfully")
        conn.commit()
        execute = False
        show = False
    elif cmd == "connect":
        file = input("Input db name with extension 'example.db'> ")
        conn.commit()
        conn.close()
        conn = sql.connect(file)
        db = conn.cursor()
        print("Saved changes on previous db and connected to another successfully.")
        execute = False
        show = False
    elif cmd == "delete":
        print("To exit current directory write '..\your\other\db_file.db'")
        file = input("Input path to db file 'c:\your\db_file\database.db' > ")
        print("Are you shure that you want to delete " + file)
        answer = input("y or n> ")
        if answer == "y":
            if file == current_db:
                conn.commit()
                conn.close()
            try:
                os.remove(os.getcwd() + "\\" + file)
            except Exception as ex:
                print(ex)
            
            answer = input("do you want to connect to other db or you want to quit. y=connect, n=quit>")
            if answer == "y":
                current_db = input("Input path to the existing DB or to create new ('example.db') > ")
                conn = sql.connect(current_db)
            else:
                exit()

            show = False
            execute = False
        show = False
    elif cmd == "cd":
        os.chdir(input("Input directory> "))
        print()
        show =False
        execute = False
    elif cmd == "vdb":
        print("Existing Data-Base files: ")
        print("")

        for file in glob.glob("*.db"):
            print(file)
        print("")
        execute = False
        show = False
    elif cmd == "curdir":
        print("Current directory is: " + os.getcwd())
        execute = False
        show = False
    elif cmd == "dbtables":
        table_info(db,conn)
        execute = False
        show = False
    
    if execute == True:
        try:
            db.execute(cmd)
        except Exception as ex:
            print("ERROR: \n")
            print(ex)
            print("")
            show = False
        
    if show == True:
        if str(db.fetchall()) != "[]":
            print("OUTPUT: \n" + str(db.fetchall()) + "\n")
        else:
            print("\nCommand executed successfully.\n")