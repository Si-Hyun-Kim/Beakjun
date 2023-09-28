def solution(my_string, overwrite_string, s):
    a = list(my_string)
    b = len(overwrite_string)
    a[s:s+b] = overwrite_string
    answer = ''.join(a)
    return answer