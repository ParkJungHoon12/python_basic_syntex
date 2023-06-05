def solution(array):
    answer = 0
    
    array = list(map(str, array))

    str1 = ''.join(array)
    

    answer = str1.count('7')
    
    return answer


array = [7, 77, 17]

print(solution(array))