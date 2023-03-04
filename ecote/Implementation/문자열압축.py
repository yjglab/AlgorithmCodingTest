def solution(s):
    answer = len(s)

    for n in range(1, (len(s) // 2) + 1):
        unit = n
        cnt = 1
        std = "".join(s[:unit]) # 기준 문자열
        result = ""
        while True:
            now = "".join(s[unit:unit + n]) # 단위 만큼 다음 문자열을 뽑아냄
            if not now: # 인덱스의 끝을 넘어갔으면
            	# 마지막에 남아있던 값을 넣어줌
                if cnt > 1:
                    result += str(cnt) + std
                else:
                    result += std
                break
            if std == now: # 현재 뽑아낸 문자열이 동일하면
                cnt += 1
                unit += n
            else:
                if cnt > 1:
                    result += str(cnt) + std
                else:
                    result += std
                std = now
                cnt = 1
                unit += n
        answer = min(answer, len(result)) # 결괏값의 길이 중 최솟값을 저장

    return answer