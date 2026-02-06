#!/usr/bin/env python3

"""A unittest file to test student submissions."""

import ast
import importlib
import pathlib
import sys
import unittest
import unittest.mock


class FunctionTestResults:
    """Holds the test results of a function being tested."""
    def __init__(self, test_name, function_name, passed, input_=None,
                 expected_output=None, student_output=None, note=None):
        self.test_name = test_name
        self.function_name = function_name
        self.passed = passed
        self.input_ = input_
        self.expected_output = expected_output
        self.student_output = student_output
        self.note = note


class HwTestCase(unittest.TestCase):
    """The test case for student submissions."""
    FUNCTION_DATA_DIR = "function_data"

    # template filename for a file that describes how a function should be tested
    FUNCTION_DATA_FILENAME_TEMPLATE = "data_*.ast"

    # will hold instances of FunctionTestResults, which tell us if a function
    # passed its tests or not, which input it choked on, etc.
    function_test_results = []
    total_score = 0

    @classmethod
    def _set_module_to_test(cls):
        """Suss out the module name that we will be testing."""
        # needs to be a list b/c len() doesn't work w/ generators
        # no underscore in case people have a file like "answer XXX.py"
        answer_files = list(cls.test_dir.glob("answer*.py"))
        if len(answer_files) > 1:
            raise FileExistsError("Multiple answer files found.")
        elif len(answer_files) == 1:
            cls.module_to_test_name = answer_files[0].stem
        else:
            for file_ in cls.test_dir.glob("*.py"):
                if not file_.stem.startswith(("test_", "template_", "exclude_")):
                    cls.module_to_test_name = file_.stem
                    break
            else:
                raise FileNotFoundError("Did not find a Python module to test.")
        print("Testing this file:", cls.module_to_test_name + ".py")

    @classmethod
    def _set_function_data(cls):
        """Set the function data that the student's functions will be tested against."""
        cls.function_data = []
        for file_ in sorted((cls.test_dir / cls.FUNCTION_DATA_DIR).glob(
                cls.FUNCTION_DATA_FILENAME_TEMPLATE)):
            function_data_read = ast.literal_eval(file_.read_text())
            function_data_read["test_name"] = file_.stem[len("data_"):]
            cls.function_data.append(function_data_read)

    @classmethod
    def setUpClass(cls):
        cls.test_dir = pathlib.Path(__file__).parent

        # i do this hack because importlib.import_module() looks in the directory of
        # the RESOLVED path of the calling file. currently there's a symlink model in
        # place for the testers.
        sys.path.insert(0, str(cls.test_dir))

        cls._set_module_to_test()
        cls._set_function_data()

        # give driver program "None" for input in case it asks for it. we only test the functions
        # right now
        with unittest.mock.patch("builtins.input", side_effect=None):
            cls.module_to_test = importlib.import_module(cls.module_to_test_name)

    @classmethod
    def tearDownClass(cls):
        print("")

        for function_test_result in cls.function_test_results:
            # print(f"Problem #{problem_num + 1}: ", end="")
            print("{}: ".format(function_test_result.test_name), end="")

            if function_test_result.passed:
                print("✅")
            else:
                # print("❌", f"(Test case #{cur_failed_test_case_num + 1})")
                print("❌ ", end="")
                if function_test_result.note:
                    print("({})".format(function_test_result.note))
                else:
                    print("Expected {}({}) -> {}. Got: {}.".format(
                        function_test_result.function_name,
                        repr(function_test_result.input_),
                        repr(function_test_result.expected_output),
                        repr(function_test_result.student_output)))

        print("Total score:", cls.total_score)

    # TODO: maybe i should reflect in a method for each function being tested?
    # not sure if that's a good idea or not
    @classmethod
    def test_hw_correct(cls):
        """Check if all inputs match all outputs in all test cases."""
        # cycle through the problems
        for func_to_test_data in cls.function_data:
            test_name = func_to_test_data["test_name"]
            function_name = func_to_test_data["function_name"]
            try:
                func_to_test = getattr(cls.module_to_test, function_name)
            except AttributeError:
                cls.function_test_results.append(FunctionTestResults(
                    func_to_test_data["test_name"],
                    function_name,
                    passed=False,
                    note="This function wasn't found!"))
                continue

            # cycle through each test case
            # a tuple of IO pairs instead of a dictionary b/c some inputs can't be
            # hashed (e.g. sets), but we still want to be able to supply them as inputs
            for input_, correct_output in func_to_test_data["io_pairs"]:
                try:
                    student_output = func_to_test(*input_)
                except TypeError:
                    student_output = func_to_test(input_)

                if correct_output != student_output:
                    cls.function_test_results.append(FunctionTestResults(test_name,
                                                                         function_name,
                                                                         False,
                                                                         input_,
                                                                         correct_output,
                                                                         student_output))
                    break
            else:
                # don't store info about given input and student/correct output
                # if the function passes the test. that information is only needed
                # if a function fails its test(s)
                cls.function_test_results.append(FunctionTestResults(test_name,
                                                                     function_name,
                                                                     True))
                cls.total_score += func_to_test_data["num_points"]


if __name__ == "__main__":
    unittest.main()
