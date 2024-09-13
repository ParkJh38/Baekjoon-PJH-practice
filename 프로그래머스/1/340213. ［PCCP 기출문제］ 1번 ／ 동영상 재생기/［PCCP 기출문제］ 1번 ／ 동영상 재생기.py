# 10초전, 10초후, 오프닝 건너뛰기
# 10초전: "prev" -> 현재위치에서 10초전으로 이동 / 10초 미만인 경우 영상의 처음 위치로 이동 0분0초
# 10초후: "next" -> 현재위치에서 10초후로 이동 / 남은시간 10초 미만인 경우 마지막 위치로 = 동영상 길이 
# 오프닝 건너뛰기: op_start ≤ 현재 재생 위치 ≤ op_end: 오프닝 끝나는 위치로 이동
# video_len: 동영상 길이 / pos: 기능 수행되기 전의 재생위치 문자열 / op_start: 오프닝 시작 시각 문자열 / op_end: 오프닝 끝나는 시각 문자열 / commands: 사용자의 입력을 나타내는 1차원 문자열 배열
# 사용자 입력 끝나고 동영상의 위치는 "mm:ss" 형식으로 반환
# video_len = pos = op_start = op_end의 길이 = 5
# 항상 디폴트로 현재 위치가 오프닝 구간 사이에 있는지 확인함 

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    mm, ss = map(int, pos.split(":"))
    end_mm, end_ss = map(int, video_len.split(":"))
    op_start_mm, op_start_ss = map(int, op_start.split(":"))
    op_end_mm, op_end_ss = map(int, op_end.split(":"))
    
    if (op_start_mm<mm==op_end_mm and ss<op_end_ss) or \
        (op_start_mm<mm<op_end_mm) or \
        (op_start_mm==mm==op_end_mm and op_start_ss<=ss<op_end_ss) or \
        (op_start_mm==mm<op_end_mm and op_start_ss<=ss):
            mm, ss = op_end_mm, op_end_ss

    for c in commands:
        if c == "prev":
            if (ss-10 < 0) and (mm>=1): 
                mm -= 1
                ss = 60+(ss-10)
            else:
                ss = max(0, ss-10)
        if c == "next":
            if (ss+10 >= 60) and (mm<end_mm): mm += 1
            
            if mm == end_mm:
                ss = min((ss+10) % 60, end_ss)
            else:
                ss = (ss+10) % 60

        if (op_start_mm<mm==op_end_mm and ss<op_end_ss) or \
        (op_start_mm<mm<op_end_mm) or \
        (op_start_mm==mm==op_end_mm and op_start_ss<=ss<=op_end_ss) or \
        (op_start_mm==mm<op_end_mm and op_start_ss<=ss):
            mm, ss = op_end_mm, op_end_ss
    
    return str(mm).zfill(2)+":"+str(ss).zfill(2)



