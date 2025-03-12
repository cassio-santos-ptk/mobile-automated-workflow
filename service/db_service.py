import sqlite3

def search_for_data(path, sensitive_data):
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if tables:
            print("Tables in the db")
            for tb in tables:
                print(tb[0])
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