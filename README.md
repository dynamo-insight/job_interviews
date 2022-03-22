# job_interviews

A Python package to conduct live coding tests for interviewees. 
The package aims at supporting several exercises and is open to contributions.

## Installation

```
git clone https://github.com/dynamo-insight/job_interviews
pip install -e job_interviews
```

On Linux, the package must be installed on a virtual environment:
```
git clone https://github.com/dynamo-insight/job_interviews
python3 -m venv venv
source venv/bin/activate
pip install -e job_interviews
```

Installing the local package via ```pip``` installs the CLI ```job_interview``` that can be used by the interviewee to initialize its code and test it.

## Usage

```
job_interview -s [script] -e [exercise] -o [output_file] -i [input_file]
```

The ```job_interview``` command enables to perform 3 tasks with the ```-s``` option:
- ```init```: creates an output file with the expected function body
- ```run```: tests the interviewee code on simple unit tests
- ```submit```: tests the interviewee code on a full-battery of unit tests and performs speed tests

Each task must be executed for a specific exercise with the ```-e``` option. For now only the ```queens_attack``` exercise is available.
The ```-i```option aims at providing the path of the code to be tested with the tasks ```run``` and ```submit```.
The ```-o```option aims at providing the path of the file to be created by the ```init``` task.
