
#pip install pywebhdfs
from pywebhdfs.webhdfs import PyWebHdfsClient
import pandas as pd
import re

def getHourFileNames(base_path,date,duration):
    # print(type(date_list))
    # hdfs = PyWebHdfsClient(host='192.168.21.42', port='50070', user_name='livy')
    # hdfs_files = hdfs.list_dir('/ternium/ahai/raw/iba/')

    # print(date_list[1])
    hdfspathlst = list()

    if "hrs" in duration:
        if duration[0] == "+":
            time_duration = re.findall(r'\d+', duration)
            # pdlist = pd.date_range(start=date, periods=int(24/int(duration[1]))+1, freq='1H')
            pdlist = pd.date_range(start=date, periods=int(time_duration[0]), freq='1H')
            # print(pdlist)
        elif duration[0] == "-":
            time_duration = re.findall(r'\d+', duration)
            pdlist = pd.date_range(end=date, periods=int(time_duration[0]), freq='1H')
            # print(pdlist)
        for time in pdlist:
            # hdfspathlst.append(base_path+"date="+str(time).split(" ")[0].replace(" ","_").replace(":","_"))
            hdfspathlst.append(
                base_path + "date=" + str(time).split(" ")[0] + "/*_" + str(time).split(" ")[1].split(":")[0] + "_*")

        # print(hdfs_path)
    elif "days" in duration:
        if duration[0] == "+":
            time_duration = re.findall(r'\d+', duration)
            pdlist = pd.date_range(start=date, periods=int(time_duration[0]), freq='D')
            # print(pdlist)
        elif duration[0] == "-":
            time_duration = re.findall(r'\d+', duration)
            pdlist = pd.date_range(end=date, periods=int(time_duration[0]), freq='D')
            # print(pdlist)
        for time in pdlist:
            # hdfspathlst.append(base_path+"date="+str(time).split(" ")[0].replace(" ","_").replace(":","_"))
            hdfspathlst.append(
                base_path + "date=" + str(time).split(" ")[0] + "/*.parquet")

    print(hdfspathlst)




if __name__ =="__main__":
    date_list = list()
    with open('/Users/pruthvi.kumar/Desktop/hdfs_dfs_out_date.txt') as f:
        date_list = f.readlines()

    getHourFileNames(base_path="hdfs://192.168.21.42:8020/ternium/ahai/raw/iba/", date="2018-11-24",duration="-2hrs")
    getHourFileNames(base_path="hdfs://192.168.21.42:8020/ternium/ahai/raw/iba/", date="2018-11-24",duration="-6days")
