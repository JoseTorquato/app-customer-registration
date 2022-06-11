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

    def migrate(self, db_name):
        database = db_name

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

    def get_all_persons(self, db_name):
        conn = sqlite3.connect(db_name)

        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM persons;")
        records = cursor.fetchall()
        conn.close()

        if records:
            return [{"id":id, "name":name, "age":age, "district": district, "profession":profession} for id, name, age, district, profession in records]
        else:
            return {}
    
    def get_person_by_name(self, name, db_name):
        conn = sqlite3.connect(db_name)

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM persons WHERE name LIKE '{}'".format(name))
        records = cursor.fetchall()
        conn.close()
        if records:
            return [{"id":id, "name":name, "age":age, "district": district, "profession":profession} for id, name, age, district, profession in records][0]
        else:
            return {"message": "Não existe cliente com esse nome", "success": False}

    def insert_person(self, person, db_name):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        values = person.get_values()

        cursor.execute("INSERT INTO persons (name, age, district, profession, id) VALUES {};".format(values))
        
        if cursor.rowcount > 0:
            conn.commit()
            conn.close()
            return {'success':True, 'message': f'Cliente {person.name} criado com sucesso.'}
        else:
            return {'success':False,'message': 'Ocorreu um erro inesperado.'}
    
    def update_person(self, person, db_name):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE persons SET age={}, district='{}', profession='{}' WHERE id={} and name='{}';".format(
            person.age, person.district, person.profession, person.id, person.name
        ))
        conn.commit()
        conn.close()
        if cursor.rowcount > 0:
            return {'success':True, 'message': f'Dados do cliente {person.name} alterado com sucesso.'}
        else:
            return {'success':False,'message': 'Ocorreu um erro inesperado.'}
    
    def delete_person(self, person, db_name):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM persons WHERE id={} and name='{}';".format(person.id, person.name))
        conn.commit()
        conn.close()
        if cursor.rowcount > 0:
            return {'success':True, 'message': f'Cliente {person.name} deletado com sucesso.'}
        else:
            return {'success':False,'message': 'Ocorreu um erro inesperado.'}

manager_db  = __ManagerDataBase()
