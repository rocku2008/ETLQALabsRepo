#from sqlalchemy import create_engine
from sqlalchemy import create_engine

def test_database_connection():
    engine = create_engine("oracle+cx_oracle://System:admin@localhost:1521/XE")
    connection = engine.connect()
    assert connection, "Connection failed"
    connection.close()

# try:
#     engine = create_engine("oracle+cx_oracle://System:admin@localhost:1521/XE")
#     connection = engine.connect()
#     print("Connection successful!")
#     connection.close()
# except Exception as e:
#     print(f"Error: {e}")
# from sqlalchemy import create_engine
# import pytest


# @pytest.fixture
# def connect_oracle_db_SRC():
#     try:
#         engine = create_engine("oracle+cx_oracle://System:admin@localhost:1521/xe")
#         connection_oracle = engine.connect()
#         yield connection_oracle
#     except Exception as e:
#         pytest.fail(f"Failed to connect to Oracle DB: {e}")
#     finally:
#         connection_oracle.close()
#
# @pytest.fixture
# def connect_mysql_db_TGT():
#     try:
#         engine = create_engine('mysql+pymysql://root:Iphone9%40@localhost:3306/etlautomation')
#         connection_mysql = engine.connect()
#         yield connection_mysql
#     except Exception as e:
#         pytest.fail(f"Failed to connect to MySQL DB: {e}")
#     finally:
#         connection_mysql.close()
