import psycopg2 as postgre

# Заполнить свои данные
dbname = ""
user=""
host=''
password=''

def get_user(table_user,id_user):
    conn = postgre.connect(dbname=dbname, user=user, host=host, password=password)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {table_user} WHERE Id={id_user}")
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        user_gender = user[2] #Заменить индекс "2" на индекс гендера в БД
        return user_gender
    



