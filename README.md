# POD-TEST-SUIT

> python scripts/super_script.py --ip=localhost --port=8081 --service=booking --basePath=/Users/pruthvi.kumar/Documents/workspace/eclipse-workspace/pod-test-suite/

> python scripts/super_script.py --ip=localhost --port=8081 --service=booking --basePath=/Users/pruthvikumar/Documents/workspace/pod-test-suite/

> python scripts/super_script.py --ip=localhost --port=8082 --service=parkingspot --basePath=/Users/pruthvikumar/Documents/workspace/pod-test-suite/
>
> python scripts/super_script.py --ip=localhost --port=8081 --service=booking --basePath=/Users/pruthvikumar/Documents/workspace/eclipse-work-space/pod-test-suite/
>
> pytest pod_api_test_suite/drivers/parking_spot_service_driver.py -sv




python3 -m venv env
source ./env/bin/activate
python -m pip install -- user pipenv

pip3 install -r requirement.txt


pytest examples/pytest_fixture_example.py -sv
        - s -> show prints
        -v  -> verbose
