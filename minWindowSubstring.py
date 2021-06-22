def minWindowSubstring(s, t):
    
    target = defaultdict(int) # Counter for t
    for c in t:
        target[c] += 1
    missing = len(t) # number of valid chars to add
    i = I = 0 # initialize current and stored start index
    J = float('inf') # stored end index
    for j, c in enumerate(s, 1): # 1-indexing so that s[i:j] ends on c
        if target[c] > 0: # valid char to add
            missing -= 1 
        target[c] -= 1
        
        if missing == 0: # qualified substring got
            while target[(c_i := s[i])] < 0: # squeeze the left side as much as possible
                target[c_i] += 1
                i += 1
                
            # calculate the size of substring and update stored start/end indices
            if (j - i) < (J - I):
                I, J = i, j
            
            # break the qualification to search for new substring
            # by moving i to the right 
            target[s[i]] += 1
            missing += 1
            i += 1
    return s[I:J] if J != float('inf') else ''
                
                
    
        
