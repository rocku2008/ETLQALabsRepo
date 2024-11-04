import pandas as pd
import pytest
# for connecting mysql database
from sqlalchemy import create_engine
# for connecting oracle database
import cx_Oracle
@pytest.fixture
def connect_to_oracle_SRC():
    engine = create_engine("oracle+cx_oracle://System:admin@localhost:1521/xe")
    connection_oracle = engine.connect()
    yield connection_oracle
    connection_oracle.close()
def test_dataExtractionCheckInDatabase(connect_to_oracle_SRC):
    query_orcl_src = 'select DEPTNO,DNAME,LOC FROM dept_src'
    df_orcl_src = pd.read_sql(query_orcl_src,connect_to_oracle_SRC)
    expected_datatypes = {'deptno':'int64','dname':'object','loc':'object'}
    #expected_datatypes = {'DEPTNO': pd.Int64Dtype(), 'DNAME': 'object', 'LOC': 'object'}
    #print(df_orcl_src.dtypes)
    #print(df_orcl_src.dtypes.to_dict())
    #print(expected_datatypes)
    #assert df_orcl_src.dtypes.to_dict() == expected_datatypes," dataTypes not matching with expected"
    assert df_orcl_src.dtypes.rename(lambda x: x.lower()).to_dict() == expected_datatypes," dataTypes not matching with expected"