from collections import Counter

n = input().lower()  #입력받은 문자열을 모두 소문자로 변환
tmp = Counter(n)  #collection의 Counter모듈로 각 원소의 개수를 count

max_count = max(tmp.values())  # 가장 많이 나온 알파벳 개수 찾기
most_common = [k for k, v in tmp.items() if v == max_count]  # 최빈 문자 리스트

if len(most_common) > 1:  # 최빈 문자가 여러 개라면
    print("?")
else:
    print(most_common[0].upper())  # 최빈 문자 대문자로 변환하여 출력
