# arr의 각 원소는 0~9의 숫자
# 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
# 제거된 후 남은 수들을 반환할 때는 원래 순서를 유지

def solution(arr):
    answer = []

    # 정리한 코드
    for a in arr:
        if not answer or a != answer[-1]:
            answer.append(a)

    return answer