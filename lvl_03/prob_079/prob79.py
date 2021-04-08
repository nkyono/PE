'''
A common security method used for online banking is to ask the user for three random characters from a passcode. 
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, 
analyse the file so as to determine the shortest possible secret passcode of unknown length.
'''
# tbh you can just look at the list and figure out the order really fast
# code below doesn't work because of the fact that a number could appear more than another leading to a higher value
# it ends up close but the 9 and 0 are swapped
def wrong(f, ans):
    for line in f.readlines():
        line = list(line.strip())
        for c in range(len(line)):
            ans[int(line[c])][0] = abs(ans[int(line[c])][0]) + c
    ans = sorted(ans)
    password = ""
    for x in range(len(ans)-1,-1,-1):
        if ans[x][0] == -1:
            ans.remove(ans[x])
        else:
            password = str(ans[x][1]) + password
    print(password)

# will implement something that works better, I think it will be a graph or something
def better():
    return

def main():
    f = open("./lvl_02/prob_079/p079_keylog.txt", "r")
    ans = [[-1,x] for x in range(10)]
    try:
        wrong(f, ans)
    finally:
        f.close()
        print(ans)

if __name__ == '__main__':
    main()