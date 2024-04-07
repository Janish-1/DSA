def countSub(s):
    Map ={}
    for i in range(len(s)):
        Map[s[i]] = -1
    allCount = 0
    levelCount = 0

    for i in range(len(s)):
        c =s[i]

        if (i==0):
            allCount = 1
            Map = 1
            levelCount = 1
            continue 
        levelCount = allCount + 1

        if(Map < 0):
            allCount = allCount + levelCount
        else:
            allCount = allCount + levelCount - Map
        Map = levelCount
    
    return allCount

List = ["abab","gfg"]

for s in List:
    cnt = countSub(s)
    withEmptyString = cnt + 1
    print("With empty string count for",s,"is",withEmptyString)
    print("Without empty string count for",s,"is",cnt)