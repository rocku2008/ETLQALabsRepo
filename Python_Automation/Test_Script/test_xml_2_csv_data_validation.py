import pandas as pd
import pytest
@pytest.fixture()
def xml_file_path():
    return "../SRC/Employees.xml"

@pytest.fixture()
def csv_file_path():
    return "../TGT/Employees.csv"

def test_xml_csv_extract_Validation(xml_file_path,csv_file_path):
    df_src_xml=pd.read_xml(xml_file_path)
    df_tgt_csv=pd.read_csv(csv_file_path)
    assert df_tgt_csv.equals(df_src_xml),"xml extraction failed- Please verify the root cause"

