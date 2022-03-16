EXERCISES = {
    "queens_attack": """
from job_interviews.timeit import timeit

@timeit 
def queens_attack(n, k, r_q, c_q, obstacles):
    # Read https://www.hackerrank.com/challenges/queens-attack-2/problem
    pass # Write your code here
    """
}

def init_exercise(exercise_name, output_file):
    
    text = EXERCISES[exercise_name]
    with open(output_file, "w") as text_file:
        text_file.write(text)