def count_substring(string, sub_string):
    
    stringlength = len(string)
    sub_stringlength = len(sub_string)
    stringlist = list(string)
    sub_stringlist = list(sub_string)
    count = 0
    sub_stringlist
    
    for i in range(stringlength-sub_stringlength+1):
        condition = True
        for j in range(sub_stringlength):
            if stringlist[i+j] != sub_stringlist[j]:
                condition = False
            else:
                pass
        if condition == True:
            count += 1
        else:
            pass
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
