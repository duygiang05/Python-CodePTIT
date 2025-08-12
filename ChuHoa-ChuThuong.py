def cnt(s) :
    res = 0
    for _ in s :
        if _.islower() : res += 1;
    
    if res >= len(s) - res : return True
    return False


s = input()

if cnt(s) == True :
    print(s.lower())
else :
    print(s.upper())