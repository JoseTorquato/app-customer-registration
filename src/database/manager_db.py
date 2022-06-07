import sqlite3
from sqlite3 import Error


class __ManagerDataBase:
    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def create_table(self, conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
            rows = c.fetchall()
            print(rows)
        except Error as e:
            print(e)

    def migrate(self):
        database = "customer_registration.db"

        sql_create_persons_table = """ CREATE TABLE IF NOT EXISTS persons (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            age int,
                                            district text,
                                            profession text
                                        ); """

        conn = self.create_connection(database)

        if conn is not None:
            self.create_table(conn, sql_create_persons_table)

        else:
            print("Error! cannot create the database connection.")

    def get_all_persons(self):
        conn = sqlite3.connect(f'customer_registration.db')

        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM persons;")

        for row in cursor.fetchall():
            print(row)

        conn.close()

    def insert_person(self):
        conn = sqlite3.connect(f'customer_registration.db')
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO persons (id, name, age, district, profession) VALUES (1, 'José', 30, 'Guajuviras', 'developer');")
        conn.commit()
        conn.close()
    
    def update_person(self):
        conn = sqlite3.connect(f'customer_registration.db')
        cursor = conn.cursor()
        cursor.execute(f"""UPDATE persons 
                        SET age=31, district='Guaju', profession='desenvolvedor'
                        WHERE id=1;""")
        conn.commit()
        conn.close()
    
    def delete_person(self):
        conn = sqlite3.connect(f'customer_registration.db')
        cursor = conn.cursor()
        cursor.execute(f"""DELETE FROM persons WHERE id=1;""")
        conn.commit()
        conn.close()


manager_db  = __ManagerDataBase()
