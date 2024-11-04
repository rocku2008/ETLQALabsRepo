import pandas as pd
import pytest
#for connecting to mysqldb#
from sqlalchemy import create_engine
@pytest.fixture()
def connect_to_mySQL():
    engine=create_engine("mysql+pymysql://root:Iphone9%40@localhost:3306/etlautomation")

    connection_mysql=engine.connect()
    yield connection_mysql
    connection_mysql.close()

@pytest.fixture()
def mySQL_address_datatype(connect_to_mySQL):
    #query_mysql ='''SELECT COLUMN_NAME,DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='etlautomation' AND TABLE_NAME='Address'
    #'''
    query_mysql = '''SELECT COLUMN_NAME,DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=%s AND TABLE_NAME=%s
    '''
    TABLE_SCHEMA='etlautomation'
    TABLE_NAME='Address'
    df=pd.read_sql(query_mysql,connect_to_mySQL,params=(TABLE_SCHEMA, TABLE_NAME))
    return df


def test_address_data_type(mySQL_address_datatype):
    """Test to check if the actual data types match expected data types for address table."""
    expected_data_types = {
        'addressId': 'int',
        'city': 'varchar',
        #'personId': 'int'
        'personId': 'int'
    }
#The above code Defines the expected data types for each column in the Address table. This dictionary maps each column name to its expected data type.#

#Compare actual data types from the Dataframe with expected data types
    for column, expected_type in expected_data_types.items():
        actual_type =mySQL_address_datatype.loc[
        mySQL_address_datatype['COLUMN_NAME'] == column,
        'DATA_TYPE'
        ].values #values extracts the matching data_type values as  a Numpy array#
        assert actual_type.size > 0, f"Column '{column}' not found in the address table."
        assert actual_type[0].lower() == expected_type.lower(), (
        f"Mismatch for column '{column}': Expected '{expected_type}', Found '{actual_type[0]}'"
        #The reason you access it with[0] is that actual_type is an array, and you want to retrieve the first ( and ideally only)
        #value from that array.
    )


