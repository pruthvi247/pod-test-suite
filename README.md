# POD-TEST-SUIT

> python scripts/super_script.py --ip=localhost --port=8081 --service=booking --basePath=/Users/pruthvi.kumar/Documents/workspace/eclipse-workspace/pod-test-suite/

> python scripts/super_script.py --ip=localhost --port=8081 --service=booking --basePath=/Users/pruthvikumar/Documents/workspace/pod-test-suite/

> python scripts/super_script.py --ip=localhost --port=8082 --service=parkingspot --basePath=/Users/pruthvikumar/Documents/workspace/pod-test-suite/
>
> python scripts/super_script.py --ip=localhost --port=8081 --service=booking --basePath=/Users/pruthvikumar/Documents/workspace/eclipse-work-space/pod-test-suite/


> python3 pod_api_test_suite/test_invoker.py --end_point_ip=192.168.0.177 --output_report_path=/Users/pruthvikumar/Desktop/rough/test_report.csv --port=8081 --input_file_path=/Users/pruthvikumar/Documents/workspace/eclipse-work-space/pod-test-suite/pod_user_service_suite/data/booking_service_test_cases.csv 

> python3 pod_api_test_suite/test_invoker.py --end_point_ip=192.168.0.177 --output_report_path=/Users/pruthvikumar/Desktop/rough/test_report.csv --port=8082 --input_file_path=/Users/pruthvikumar/Documents/workspace/eclipse-work-space/pod-test-suite/pod_user_service_suite/data/parkingspot_service_test_cases.csv

> seed_data command :  python pod_api_test_suite/utils/seed_data_prep.py
>
python3 -m venv env
source ./env/bin/activate
python -m pip install -- user pipenv

pip3 install -r requirement.txt


pytest examples/pytest_fixture_example.py -sv
        - s -> show prints
        -v  -> verbose
