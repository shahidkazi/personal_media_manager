#=======================================================================
# Description:
# Data Access Layer implementation for the application to interact with
# the backend SQLite database
#=======================================================================
import sqlite3
import pandas as pd
import utils.constants as constants

#=======================================================================
def execute_query(query : str) -> bool:
    """
    Executes a given SQL query on the default database.

    Parameters:
    query (str): The SQL query to be executed.

    Returns:
    bool: True if the query was executed successfully and committed, False if an error occurred.

    Exceptions:
    sqlite3.Error: Raised if there is an error executing the query, in which case the transaction is rolled back.
    """
    connection = sqlite3.connect(constants.DEFAULT_DB_PATH)
    cursor     = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print(error)
        connection.rollback()
        return False
    finally:
        if connection:
            connection.close()
    
    return True


def execute_read(query : str) -> pd.DataFrame:
    """
    Executes a read operation on a SQLite database using the provided SQL query.

    Parameters:
    query (str): A SQL query string to be executed on the database.

    Returns:
    pd.DataFrame: A DataFrame containing the results of the SQL query.

    Exceptions:
    Raises an Exception if there is an error during the execution of the SQL query, 
    which is caught and printed to the console. The database connection is closed 
    in the 'finally' block to ensure resources are released.
    """
    connection = sqlite3.connect(constants.DEFAULT_DB_PATH)
    result_df  = pd.DataFrame()
    
    try:
        result_df  = pd.read_sql_query(query, connection)
    except Exception as error:
        print(error)
    finally:
        if connection:
            connection.close()

    return result_df

#=======================================================================