def swap_case(s):
    new_s = s.swapcase()
    return new_s 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
#String Split and Join

def split_and_join(line):
    # write your code here
    list = line.split(" ")
    string = "-".join(list)
    return string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
