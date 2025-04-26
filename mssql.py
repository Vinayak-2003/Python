import pyodbc

# DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
# SERVER_NAME = 'CBLLAP0531\MSSQLVINAYAK'
# DATABASE_NAME = 'learn'
# USERNAME = 'sa'
# PASSWORD = '#Vinayak24042003'
#     UID = {USERNAME};
#     PWD = {PASSWORD};

# connection_string = f"""
#     DSN = {{{DRIVER_NAME}}};
#     SERVER = {SERVER_NAME};
#     DATABASE = {DATABASE_NAME};
#     Trusted_Connection = yes;
# """
# conn = pyodbc.connect(connection_string)
# print(conn)


try:
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=CBLLAP0531\\MSSQLVINAYAK;'
        'DATABASE=learn;'
        'UID=sa;'
        'PWD=#Vinayak24042003'
    )
    print("Connection successful")
except Exception as e:
    print("Error: ", e)

# conn = odbc.connect('DRIVER={SQL Server};SERVER={CBLLAP0531\MSSQLVINAYAK};DATABASE={learn};Trusted_Connection=yes;UID={sa};PWD={#Vinayak24042003}')
# print(conn)
# print(pyodbc.drivers())