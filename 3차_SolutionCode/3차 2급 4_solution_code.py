def solution(words, word):              # 함수 만들기
    count = 0
    
    for comp in words:
        for x, y in zip(comp, word):
            if x != y:
                count = count + 1
                
    return count

words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)

print("solution 함수의 반환 값은", ret, "입니다.")