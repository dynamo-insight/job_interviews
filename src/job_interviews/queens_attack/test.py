import importlib.util
import os
from logzero import logger
import random

import job_interviews.queens_attack.fast_answer as fast_answer

TESTS = [
    [4, 0, 4, 4, []],
    [5, 3, 4, 3,[[5, 5], [4, 2], [2, 3]]],
    [1, 0, 1, 1, []],
    [50, 3],
    [50, 10],
    [500, 3],
    [500, 10],
    [5000, 30],
    [5000, 100],
    [9999, 30],
    [9999, 100],
]

def load_interviewee_module(code_filepath):
    code_filename = os.path.basename(code_filepath)
    spec = importlib.util.spec_from_file_location(code_filename, code_filepath)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo


def parse_test(test):
    if len(test) < 2:
        raise NotImplementedError(f"Cannot handle a test with less than 2 arguments")
    n, k = test[0], test[1]

    if len(test) < 4:
        r_q, c_q = random.randrange(1, n, 1), random.randrange(1, n, 1)
    else:
        r_q, c_q = test[2], test[3]

    if len(test) < 5:
        obstacles = []
        for _ in range(k):
            r_o, c_o = random.randrange(1, n, 1), random.randrange(1, n, 1)
            obstacles.append([r_o, c_o])
    else:
        obstacles = test[4]
    return n, k, r_q, c_q, obstacles


def test_interviewee(code_filepath, run_all=True):
    max_test = len(TESTS) if run_all is True else 3
    interviewee = load_interviewee_module(code_filepath)
    for i, test in enumerate(TESTS):
        n, k, r_q, c_q, obstacles = parse_test(test)
        interviewee_ret, interviewee_duration = interviewee.queens_attack(
            n, k, r_q, c_q, obstacles
        )
        ref_ret, ref_duration = fast_answer.queens_attack(n, k, r_q, c_q, obstacles)
        if (interviewee_ret != ref_ret) or (interviewee_duration > ref_duration * 1.3 and interviewee_duration > ref_duration + 0.1):
            if interviewee_ret != ref_ret:
                logger.critical(f"FAILED (Test {i}): expected output: {ref_ret}, received {interviewee_ret}")
            if interviewee_duration > ref_duration * 1.3 and interviewee_duration > ref_duration + 0.1:
                logger.warning(f"TIMEOUT (Test {i}): reference took: {ref_duration} s, interviewee took {interviewee_duration} s")
        else:
            logger.info(f"PASSED (Test {i})")
            logger.debug(f"reference took: {ref_duration} s, interviewee took {interviewee_duration} s")
        if i >= max_test - 1:
            break


if __name__ == "__main__":
    test_interviewee("slow_answer.py")
