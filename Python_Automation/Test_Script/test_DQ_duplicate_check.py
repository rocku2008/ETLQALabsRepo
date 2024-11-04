import pandas as pd
import pytest
@pytest.fixture()
def csv_file_path():
    return "../TGT/Employees.csv"

def test_duplicate_check(csv_file_path):
    df_tgt_csv=pd.read_csv(csv_file_path)
    duplicates=df_tgt_csv.duplicated()
    no_of_dup=duplicates.sum()
    print(f"The number of duplicate values are :",no_of_dup)
    assert  no_of_dup ==0, f"duplicate values are: {df_tgt_csv[duplicates]}"
    #assert no_of_dup == 0, f"duplicate values are:: {duplicates}"
