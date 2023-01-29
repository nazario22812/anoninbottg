import sqlite3


class Database():
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

        try:
            # self.cursor.execute(""" create table if not exists users(id integer primary key, user_id integer not null unique, referrer_id integer) """)

            self.cursor.execute(""" create table if not exists messagers(id integer primary key, giver_id integer, sender_id integer, sender_name text, time text, message text) """)
        except Exception as ex:
            print(ex)
        finally:
            self.connection.commit()

    def user_exists(self, user_id):
        with self.connection:
            res = self.cursor.execute(f""" select * from users where user_id = '{user_id}' """).fetchall()
            return bool(len(res))
    
    
    def add_user(self, user_id, referrer_id=None):
        # self.cursor.execute(f""" insert into users values ('{user_id}', '{user_name}') """)
        # self.connection.commit()
        with self.connection:
            if referrer_id != None:
                return self.cursor.execute(f""" insert into users ('user_id', 'referrer_id') values ('{user_id}', '{referrer_id}') """)
            else:
                return self.cursor.execute(f""" insert into users ('user_id') values ('{user_id}') """)


    def dell_user(self, user_id):
        with self.connection:
            return self.cursor.execute(f""" delete from users where user_id = '{user_id}'""")
    
    
    def save_msg(self, giverid, senderid, sendername, tim, msg):
        with self.connection:
            return self.cursor.execute(f""" insert into messagers ('giver_id', 'sender_id', 'sender_name', 'time', 'message') values ('{giverid}', '{senderid}', '{sendername}', '{tim}', '{msg}') """)