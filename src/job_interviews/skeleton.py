"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = job_interviews.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``logger``...) of this file can
also be used as template for Python modules.

Note:
    This skeleton file can be safely removed if not needed!

References:
    - https://setuptools.readthedocs.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
import logzero
import sys

from job_interviews import __version__

__author__ = "Hugo Ehlinger"
__copyright__ = "Hugo Ehlinger"
__license__ = "MIT"

from logzero import logger

from job_interviews.init_exercise import init_exercise
from job_interviews.queens_attack.test import test_interviewee as queens_attack_test_interviewee

# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from job_interviews.skeleton import fib`,
# when using this Python module as a library.


def fib(n):
    """Fibonacci example function

    Args:
      n (int): integer

    Returns:
      int: n-th Fibonacci number
    """
    assert n > 0
    a, b = 1, 1
    for _i in range(n - 1):
        a, b = b, a + b
    return a


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Just a Fibonacci demonstration")
    parser.add_argument(
        "--version",
        action="version",
        version="job_interviews {ver}".format(ver=__version__),
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    parser.add_argument(
        "-s",
        "--script",
        dest="script",
        help="set script to launch",
    )
    parser.add_argument(
        "-e",
        "--exercise",
        dest="exercise",
        help="set exercise to launch",
    )
    parser.add_argument(
        "-i",
        "--input",
        dest="input",
        help="set input filepath",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        help="set output filepath",
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    loglevel = loglevel if loglevel else logging.INFO
    logzero.loglevel(loglevel)


def main(args):
    """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`fib`, it prints the result to the
    ``stdout`` in a nicely formatted message.

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    accepted_scripts = ["init", "run", "submit"]
    accepted_exercises = ["queens_attack"]
    if args.script not in accepted_scripts:
        raise NameError(f"Script {args.script} not accepted. Expected script should be one of {accepted_scripts}")
    if args.exercise not in accepted_exercises:
        raise NameError(f"Script {args.exercise} not accepted. Expected script should be one of {accepted_exercises}")

    if args.script == "init":
        init_exercise(args.exercise, args.output)
    elif args.script == "run":
        queens_attack_test_interviewee(args.input, run_all=False)
    elif args.script == "submit":
        queens_attack_test_interviewee(args.input, run_all=True)
    logger.info("Script ends here")


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m job_interviews.skeleton 42
    #
    run()
