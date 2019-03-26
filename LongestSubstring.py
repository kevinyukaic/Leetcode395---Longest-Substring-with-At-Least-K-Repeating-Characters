def LongestSubstring(input):
    try:
        SubstringCount = 0
        left = 0
        right = 0
        start = 0
        StartPos = 0
        EndPos = 0
        MaxCountandStartPos = [0,0]

        window = {'left':"",'right':""}
        for count,x in enumerate(input):
            #print("now:",count, x)
            

            if x not in window.values() and window['left'] == "":
                window['left'] = x
                
                StartPos = count
                
            elif x not in window.values() and window['right'] == "":
                window['right'] = x
                
                EndPos = count
            
            elif x not in window.values():
                
                EndPos = count
                while window['left'] in input[StartPos:EndPos]:
                    StartPos+=1
                window['left'] = window['right']
                window['right'] = x
                #print(window,StartPos,EndPos)
                
            elif x in window.values():
                if x == window['left'] and window['right']!="":
                    temp = window['left']
                    window['left'] = window['right']
                    window['right'] = temp
                    
                EndPos = count

            if EndPos - StartPos+1 > MaxCountandStartPos[1]:
                MaxCountandStartPos[1] = EndPos -StartPos+1
                MaxCountandStartPos[0] = StartPos
                #print(MaxCountandStartPos)
        

        #print(start)
        #return input[start:start+SubstringCount],SubstringCount
        return MaxCountandStartPos, input[MaxCountandStartPos[0]:MaxCountandStartPos[0]+MaxCountandStartPos[1]]

    except TypeError:
        print("Type Error")

#print(LongestSubstring(input))


print([LongestSubstring(test) for test in [None, "", "a", "ab", "aab",
                                                "bab", "babc", "bbbbcccac"]])
print([LongestSubstring(test) for test in ["eeeeebbbbb", "eeeeebbbbbc",
                                                "ceeeeebbbbb","abaccc"]])

print([LongestSubstring(test) for test in ["aaaaa", "edfraaaaaa", "baacba",
                                "babababababaaaabbbabz", "babc", "bbbbcccac"]])
print(LongestSubstring("abbaaaaeeeeeeeeee"))
