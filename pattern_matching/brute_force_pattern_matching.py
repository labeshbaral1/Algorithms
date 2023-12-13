def brute_force_pattern_match(P, T):

    for index in range(len(T)):
        l = 0
        p_index = 0

        while (index+p_index) < len(T) and p_index < len(P) and T[index+p_index] == P[p_index]:
            l+=1
            p_index+=1
        
        if l == len(P):
            return True
        
    return False

print(brute_force_pattern_match("na", "banana"))
