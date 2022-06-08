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
        records = cursor.fetchall()
        conn.close()

        if records:
            a = [{"id":id, "name":name, "age":age, "district": district, "profession":profession} for id, name, age, district, profession in records]
            print(a)
            return a
        else:
            return {}

    def insert_person(self, person):
        conn = sqlite3.connect(f'customer_registration.db')
        cursor = conn.cursor()

        values = tuple(person.values())

        cursor.execute("INSERT INTO persons (name, age, district, profession, id) VALUES {};".format(values))
        
        if cursor.rowcount > 0:
            conn.commit()
            conn.close()
            return {'success':True, 'message': f'Cliente {person["name"]} criado com sucesso.'}
        else:
            return {'success':False,'message': 'Ocorreu um erro inesperado.'}
    
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
