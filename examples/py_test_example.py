
# import sys
# sys.path.append("../../../..")

from py_scale.init import pyscale_init
from py_scale.utils.common import connection
from py_scale.spark.ml import stat
from py_scale.tests.utils_test import util_functions
# from py_scale.tests.conf_test
import json
import pytest

prop = util_functions.load_properties_from_json("/conf_test/testing_configurations.json")

@pytest.mark.smoke
def test_corr():
    query = '''(SELECT * FROM Ds_training.dbo.Sensor_Data_ts)t'''

    pys = pyscale_init.Pyscale(host=prop['TESTING']['LIVY_HOST'], spark_submit_config=json.loads(prop['TESTING']['spark_submit_config']))
    pys.start_spark()

    # commenting below lines as we have depricated "DBDetailToFetchData" function, we will be using parquet files of ahai app

    # dbtype = prop['TESTING']['dbtype']
    # url = prop['TESTING']['sql_server_url']
    # user = prop['TESTING']['sql_server_user']
    # password = prop['TESTING']['sql_server_password']
    # condet = connection.DBDetailToFetchData(dbtype=dbtype, url=url, user=user, password=password)
    condet = connection.ParquetDetailToFetchData(url=prop['TESTING']['hdfs_url'], port=prop['TESTING']['hdfs_port'],
                                                 filepath=prop['TESTING']['parquet_file_path'],
                                                 sel_col='*')
    qa = stat.Correlation(condet)

    qa.corr(query)

@pytest.mark.regression
def test_sample():
    print("sample test case")


if __name__ == "__main__":
    # test_corr()
    prop = util_functions.load_properties_from_json("conf_test/testing_configurations.json")
    print(prop)

## Command to run py_scale test case : pytest -m “smoke” stats_correlation_tests.py