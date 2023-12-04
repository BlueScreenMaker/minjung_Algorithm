def bin_convert(s, zero, trying) :
    if len(s) == 1 :
        return [trying,zero]
    else :
        trying +=1
        zero += s.count('0')
        s = str(bin(s.count('1')))[2:]
        return bin_convert(s, zero, trying)

def solution(s):
    zero = 0
    trying = 0
    return bin_convert(s,zero,trying)