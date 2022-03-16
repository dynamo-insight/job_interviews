from job_interviews.timeit import timeit

def move_up(r_q, c_q):
    return r_q + 1, c_q

def move_down(r_q, c_q):
    return r_q - 1, c_q
    
def move_left(r_q, c_q):
    return r_q, c_q - 1

def move_right(r_q, c_q):
    return r_q, c_q + 1

def move_up_and_right(r_q, c_q):
    return r_q + 1, c_q + 1
    
def move_up_and_left(r_q, c_q):
    return r_q + 1, c_q - 1
    
def move_down_and_left(r_q, c_q):
    return r_q - 1, c_q - 1

def move_down_and_right(r_q, c_q):
    return r_q - 1, c_q + 1
    
def check_queen_in_bounds(n, r_q, c_q):
    if 1 <= r_q <= n and 1 <= c_q <= n:
        return True
    return False

def check_on_obstacle(r_q, c_q, obstacles):
    for obstacle in obstacles:
        if [r_q, c_q] == obstacle:
            return True
        if obstacle[0] > r_q:
            return False
        if obstacle[0] == r_q and obstacle[1] > c_q:
            return False
    return False    

@timeit 
def queens_attack(n, k, r_q, c_q, obstacles):
    moveFuncs = [
        move_up, 
        move_down, 
        move_left, 
        move_right, 
        move_up_and_left, 
        move_up_and_right, 
        move_down_and_left, 
        move_down_and_right
    ]
    nb_attacks = 0
    obstacles = sorted(obstacles)
    for func in moveFuncs:
        r_qi, c_qi = r_q, c_q
        inBound = check_queen_in_bounds(n, r_qi, c_qi)
        onObstacle = check_on_obstacle(r_qi, c_qi, obstacles)
        while inBound and not onObstacle:
            r_qi, c_qi = func(r_qi, c_qi)
            inBound = check_queen_in_bounds(n, r_qi, c_qi)
            if inBound:
                onObstacle = check_on_obstacle(r_qi, c_qi, obstacles)
            if inBound and not onObstacle:
                nb_attacks += 1
    return nb_attacks