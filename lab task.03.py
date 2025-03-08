def WaterJugProblem(capacity1,capacity2,goal):
    stack= [(0 , 0 , [])]
    visited = set()


    while stack:
        jug1 , jug2, path = stack.pop()

        if jug1 == goal or jug2 == goal:
            print("Solution Founded:")
            for step in path:
                print(step)
            if jug1 == goal:
                print(f"jug 1 now has {jug1} liters.")
            else:
                print(f"jug 2 now has {jug2} liters.")
                return True
        if(jug1 , jug2) in visited:
            continue
        visited.add((jug1, jug2))

        rules = [
            (capacity1, jug2, "Fill Jug 1"),  
            (jug1, capacity2, "Fill Jug 2"),  
            (0, jug2, "Empty Jug 1"),  
            (jug1, 0, "Empty Jug 2"), 
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2), "Pour Jug 1 into Jug 2"),  
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1), "Pour Jug 2 into Jug 1"),  
            (0, jug2 + jug1, "Pour Jug 1 into Jug 2 until Jug 1 is empty"),  
            (jug1 + jug2, 0, "Pour Jug 2 into Jug 1 until Jug 2 is empty"), 
        ] 

        for state in rules:
            new_jug1, new_jug2, action = state
            if (new_jug1, new_jug2) not in visited:
                stack.append((new_jug1, new_jug2, path + [action]))
    print("No Solution Founded.")
    return False          

jug1Capacity = 4
jug2Capacity = 3
target = 2

WaterJugProblem(jug1Capacity, jug2Capacity, target)
