def countSubstrs(s1,s2):
    ans = 0
    for i in range(len(s1)):
        s3 = ""
        # s3 stores all substrings of s1
        for j in range(i,len(s1)):
            # Store the sub string in s3
            s3+=s1[j]
            #check the presence of s3 in s2
            if s2.find(s3) != -1:
                ans += 1
    return ans


s1 = "aab"
s2 = "aaaab"
print(countSubstrs(s1,s2))