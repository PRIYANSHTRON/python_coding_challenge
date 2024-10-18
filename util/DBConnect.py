import pyodbc

class DBConnUtil:
    @staticmethod
    def get_connection():

        connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DESKTOP-05PBHJ8\\SQLEXPRESS;"
            "DATABASE=InsuranceManagementDB;"
            "Trusted_Connection=yes;"
        )

        try:
            conn = pyodbc.connect(connection_string)
            print("Database connection established successfully.")
            return conn
        
        except pyodbc.InterfaceError as ie:
            print(f"Interface error: {ie}")
        
        except pyodbc.OperationalError as oe:
            print(f"Operational error: {oe}")

        except pyodbc.DatabaseError as de:
            print(f"Database error: {de}")

        except pyodbc.Error as e:
            print(f"Database connection failed: {e}")
        
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")

        finally:
            print("Attempted to connect to the database.")