import mysql.connector as msql

def creat_backup():
    db = input('Enter in database name:- ')
    connection = msql.connect(host='localhost', user='user',
                       password='P@ssW0rd', database=db)
    cur = connection.cursor()
    cur.execute('SHOW TABLES;')
    table_names = []
    for record in cur.fetchall():
        table_names.append(record[0])

    # print(table_names)

    backup_dbname = db + '_backup'
    try:
        cur.execute(f'CREATE DATABASE {backup_dbname}')
    except:
        pass


    cur.execute(f'USE {backup_dbname}')

    for table_name in table_names:
        cur.execute(
            f'CREATE TABLE {table_name} SELECT * FROM {db}.{table_name}')

    print(f'Back for {db} created as {backup_dbname}')

creat_backup()
