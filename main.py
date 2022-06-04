import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Hayvanlar14.'
)

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='Hayvanlar14.',
                                         database='MyNewDatabase')

    cursor = connection.cursor()
    # sql_Select = "select ID ,MovieName from Marvel where MCU_Phase='Phase1'"
    # sql_Select="select MovieName from Marvel where MCU_Phase='Phase3'"
    sql_Update = " UPDATE Marvel SET Date = 'November3,2017' WHERE Date = 'November3,2019'"
    cursor.execute(sql_Update)
    connection.commit()  # it is required to make the changes
    records = cursor.fetchall()
    print("Printing each row")
    for row in records:
        print(row)
    print(cursor.rowcount, "record(s) affected")
    # sql_Remove_Query="DELETE FROM Marvel where MovieName='TheIncredibleHulk'"
    # cursor.execute(sql_Remove_Query)
    # connection.commit()# it is required to make changes.
    # print('number of rows deleted', cursor.rowcount)

    # records = cursor.fetchall()
    # if len(records) == 0:
    #    print("Record Deleted successfully ")



except mysql.connector.Error as e:
    print("Failed to create table in MySQL:{}".format(e))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
