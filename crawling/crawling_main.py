from bs4 import BeautifulSoup
import pandas as pd


places_list =[]
places_list_1 = []
file_name = '/Users/pruthvikumar/Documents/workspace/a1m/pod-test-suite/pod_user_service_suite/data/crawling_data/blr_loc.htm'
output_file_name = "/Users/pruthvikumar/Documents/workspace/a1m/pod-test-suite/pod_user_service_suite/data/crawling_data/blr_locations.csv"
file_name_1 = '/Users/pruthvikumar/Documents/workspace/a1m/pod-test-suite/pod_user_service_suite/data/crawling_data/blr_loc.htm'
output_file_name_1 = "/Users/pruthvikumar/Documents/workspace/a1m/pod-test-suite/pod_user_service_suite/data/crawling_data/blr_locations_1.csv"
with open(file_name,'r') as html_file:
    html_content = html_file.read()
    # print(len(html_content.readlines()))
    # print(len(html_content))
    soup= BeautifulSoup(html_content,'lxml')
    course_card = soup.find_all('div',class_="col-md-6 col-sm-12")
    for course in course_card:
        print(str(course.a.text).replace("Rent your private space in",""))
        places_list.append(str(course.a.text).replace("Rent your private space in",""))

with open(file_name_1,'r') as html_file:
    html_content = html_file.read()
    # print(len(html_content.readlines()))
    # print(len(html_content))
    soup= BeautifulSoup(html_content,'lxml')
    course_card = soup.find_all('div',class_="col-md-6 col-sm-12")
    for course in course_card:
        print(str(course.a.text).replace("Rent your private space in",""))
        places_list_1.append(str(course.a.text).replace("Rent your private space in",""))

print(len(places_list_1))
print(len(places_list))

print(len(set(places_list_1) ^ set(places_list)))
print(len(set(places_list_1).intersection(set(places_list))))
# df = pd.DataFrame(list(set(places_list)) ,columns=["Banglore locations"])
# df.to_csv(output_file_name)
# df1 = pd.DataFrame(list(set(places_list_1)) ,columns=["Banglore locations"])
# df1.to_csv(output_file_name_1)

