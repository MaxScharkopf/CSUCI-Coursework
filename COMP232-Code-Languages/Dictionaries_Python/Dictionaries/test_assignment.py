#!/usr/bin/env python3

"""A unittest file to test student submissions."""

import importlib
import io
import itertools
import pathlib
import sys
import random
import unittest
import unittest.mock


class HwTestCase(unittest.TestCase):
    """The test case for student submissions."""
    INPUTS_DIR = "inputs"
    OUTPUTS_DIR = "outputs"

    # template filename for a given input case for a problem and its expected output
    IO_TEST_CASE_FILENAME_TEMPLATE = "problem{}_case*.txt"

    # the number of points that each problem is worth
    POINTS_PER_PROBLEM_FILENAME = "points_per_problem.txt"

    PROBLEM_SEPARATOR = "-" * 30

    # will hold the case number that each problem failed on. None = test passed for that problem.
    failed_test_case_nums = None
    total_score = 0

    @classmethod
    def _read_points_per_problem_file(cls):
        """Read the file that tells how many points each problem is worth."""
        cls.points_per_problem = [
            int(l) for l in
            (cls.test_dir / cls.POINTS_PER_PROBLEM_FILENAME).read_text().strip().split()
        ]

    @classmethod
    def _set_module_to_test(cls):
        """Suss out the module name that we will be testing."""
        for file_ in cls.test_dir.glob("*.py"):
            if not file_.stem.startswith(("test_", "template_", "exclude_")):
                cls.module_to_test_name = file_.stem
                break
        else:
            raise FileNotFoundError("Did not find a Python module to test.")

    @staticmethod
    def _sort_and_read_files(files):
        return tuple(f.read_text().strip("\r\n") for f in sorted(files))

    @classmethod
    def _set_inputs_and_outputs(cls):
        """Set the input and output files that the module will be tested against."""
        cls.inputs = []
        cls.outputs = []
        for problem_num in range(1, cls.num_problems + 1):
            cur_problem_input_glob = cls.IO_TEST_CASE_FILENAME_TEMPLATE.format(problem_num)

            input_files = (cls.test_dir / cls.INPUTS_DIR).glob(cur_problem_input_glob)
            cls.inputs.append(tuple(t.splitlines() for t in cls._sort_and_read_files(input_files)))

            output_files = (cls.test_dir / cls.OUTPUTS_DIR).glob(cur_problem_input_glob)
            cls.outputs.append(cls._sort_and_read_files(output_files))

    @classmethod
    def _make_input(cls, input_for_single_problem, problem_num):
        """Make an input to test a single problem.

        Make an input that randomly selects a a case's input for each problem
        with the aim of constructing a single valid input. Then, take the entire
        input and make a specified problem number's input the input for the
        case of the problem that we're testing. All of this is because we test
        one case of one problem at a time, but we still need a valid entire
        input because we have to run the entire program; we can't just take
        parts of the program to run individually.
        """
        input_ = [random.choice(i) for i in cls.inputs]
        input_[problem_num] = input_for_single_problem
        # flatten the list
        return list(itertools.chain.from_iterable(input_))

    @classmethod
    def setUpClass(cls):
        cls.test_dir = pathlib.Path(__file__).parent

        # i do this hack because importlib.import_module() looks in the directory of
        # the RESOLVED path of the calling file. currently there's a symlink model in
        # place for the testers.
        sys.path.insert(0, str(cls.test_dir))

        cls._read_points_per_problem_file()
        cls.num_problems = len(cls.points_per_problem)

        cls._set_module_to_test()
        cls._set_inputs_and_outputs()

        cls.failed_test_case_nums = [None] * cls.num_problems

    @classmethod
    def tearDownClass(cls):
        print("")

        for problem_num in range(cls.num_problems):
            # print(f"Problem #{problem_num + 1}: ", end="")
            print("Problem #{}: ".format(problem_num + 1), end="")
            cur_failed_test_case_num = cls.failed_test_case_nums[problem_num]
            if cur_failed_test_case_num is None:
                print("✅")
            else:
                # print("❌", f"(Test case #{cur_failed_test_case_num + 1})")
                print("❌", "(Test case #{})".format(cur_failed_test_case_num + 1))

        print("Total score:", cls.total_score)

    @staticmethod
    def _remove_trailing_whitespace(str_):
        """Remove trailing whitespace from each line in a string. Then, reassemble the string."""
        return "\n".join(l.rstrip() for l in str_.splitlines())

    # TODO: maybe i should reflect in a method for each problem being tested?
    # not sure if that's a good idea or not
    @classmethod
    def test_hw_correct(cls):
        """Check if all inputs match all outputs in all test cases."""
        # i use patch as a context manager instead of a decorator because we only want to patch
        # the builtins for a part of the function
        module_to_test = None

        # make sure we have an output for each problem we have an input for and vice versa
        assert (len(cls.inputs) == len(cls.outputs) == len(cls.points_per_problem) ==
                cls.num_problems)

        # cycle through the problems
        for problem_num in range(cls.num_problems):
            # make sure there's a 1-1 mapping of test cases for each input and output
            # in the current problem
            assert len(cls.inputs[problem_num]) == len(cls.outputs[problem_num])

            # cycle through the test cases for each problem
            for test_case_num in range(len(cls.inputs[problem_num])):
                with unittest.mock.patch(
                    "builtins.input",
                    side_effect=cls._make_input(cls.inputs[problem_num][test_case_num],
                                                problem_num)), \
                        unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
                    if module_to_test is None:
                        # module hasn't been imported yet
                        module_to_test = importlib.import_module(cls.module_to_test_name)
                    else:
                        # module has already been imported. regular import won't work
                        # we need to reload the module
                        importlib.reload(module_to_test)

                    # correct output files have excess preceding/trailing newlines stripped when
                    # they are read in, so we don't have to do a .strip("\n") here.
                    correct_output = cls._remove_trailing_whitespace(
                        cls.outputs[problem_num][test_case_num])
                    student_output = cls._remove_trailing_whitespace(mock_stdout.getvalue().split(
                        cls.PROBLEM_SEPARATOR)[problem_num]).strip("\r\n")
                    if correct_output != student_output:
                        cls.failed_test_case_nums[problem_num] = test_case_num
                        break
            else:
                cls.total_score += cls.points_per_problem[problem_num]


if __name__ == "__main__":
    unittest.main()
