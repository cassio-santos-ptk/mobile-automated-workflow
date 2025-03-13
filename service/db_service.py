import sqlite3

def search_for(table, cursor):
    #check to prevent sql injection
    if not table.isidentifier():
        raise ValueError("Invalid table name")

    query = f"SELECT * FROM {table};"  

    cursor.execute(query)  
    return cursor.fetchall()

def has_sensitive_data(data, sensitive_data):
    # converts the db data to string and search for sensitive data
    data_str = " ".join(map(str, data))

    return sensitive_data in data_str

def search_for_data(path, sensitive_data):
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()

        # search for all the tables in de db
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if tables:
            for tb in tables:               
                tb_name = tb[0]
                content = search_for(tb_name, cursor)
                if content:
                    if has_sensitive_data(content, sensitive_data):
                        # format the evidence in a pretty format for github
                        evidence = f"// SELECT * FROM {tb_name}\n\n{content}"                       
                        return True, evidence                                
        else:
            print("No tables found in the db")

    except sqlite3.Error as e:
        print(f"[-] Database error:{e}")

    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        # Ensure the connection is closed properly
        if 'conn' in locals():
            conn.close()