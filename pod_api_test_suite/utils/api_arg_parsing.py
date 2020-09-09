
import argparse


class CliArgParse():


    def get_args(self):
        parser = argparse.ArgumentParser(description='Passing cli arguments to test driver')
        parser.add_argument("--end_point_ip",default="localhost")
        parser.add_argument("--port",default="8080")
        parser.add_argument("--output_report_path",default=None)
        parser.add_argument("--input_file_path", default=None)
        parser.add_argument("--headers",default={"Content-Type": "application/json"})

        args = parser.parse_args()

        assert args.output_report_path is not None, "Output path can not be empty, please pass the folder path to save outputs"
        assert args.input_file_path is not None, "input file path can not be empty, please pass the test case file path"

        return args
