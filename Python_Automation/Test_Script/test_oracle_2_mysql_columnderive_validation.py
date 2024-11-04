from sqlalchemy import create_engine
import cx_Oracle
import pandas as pd
import pytest
@pytest.fixture
def connect_oracle_db_SRC():
    engine= create_engine("oracle+cx_oracle://System:admin@localhost:1521/xe")
    connection_oracle = engine.connect()
    yield connection_oracle
    connection_oracle.close()

@pytest.fixture
def connect_mysql_db_TGT():
    engine= create_engine('mysql+pymysql://root:Iphone9%40@localhost:3306/etlautomation')
    connection_mysql=engine.connect()
    yield connection_mysql
    connection_mysql.close()

def test_derived_column_data_validation(connect_oracle_db_SRC,connect_mysql_db_TGT):
    query_oracle_src = 'select DNAME || \',\'|| LOC as address  FROM dept_src'
    #note: we are using here backward slash coz we have comma in between and we need the backward slash to handle this
    #or else the above line incorrectly splits the query into two parts that cause pandas.read_sql to misinterpret the input
    query_mysql_tgt = 'select address from dept_tgt'
    df_oracle_src = pd.read_sql(query_oracle_src, connect_oracle_db_SRC)
    df_mysql_tgt = pd.read_sql(query_mysql_tgt, connect_mysql_db_TGT)
    assert df_oracle_src.equals(df_mysql_tgt), "address column in target is not correctly derived from source columns: DNAME and LOC"
