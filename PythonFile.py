s = input()
ans = s[len(s) - 3:]
if ans.lower() != '.py' : print("no")
else : print("yes")