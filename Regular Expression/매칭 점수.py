import re

def solution(word, pages):
    answer = 0
    n = len(pages)  # 웹페이지 개수
    domain_info = {}  # 웹페이지의 domain: index 정보
    basic_score = [0] * n  # 기본 점수
    external_links = [0] * n  # 외부 링크수
    link_pages = [[] for _ in range(n)]  # i번째 웹페이지로 링크가 걸린 페이지 리스트
    
    # 기본 점수 계산
    for i in range(n):
        page = pages[i]
        # 도메인 이름 저장
        domain = re.compile('<meta property="og:url" content="(.*?)"/>').search(page).group(1)
        domain_info[domain] = i
        # 기본 점수 계산
        include = len(re.compile(word, re.I).findall(page))  # word가 나타나는 횟수
        front = len(re.compile('[a-z]' + word, re.I).findall(page))  # word 앞에 문자가 있을 경우(단어취급 X)
        rear = len(re.compile(word + '[a-z]', re.I).findall(page))  # word 뒤에 문자가 있을 경우(단어취급 X)
        basic_score[i] = include - front - rear

    # 외부 링크수 계산
    for i in range(n):
        page = pages[i]
        links = re.compile('<a href=.*?>').finditer(page)
        for link in links:
            external_links[i] += 1
            href = link.group()[9:-2]
            if href in domain_info.keys():
                link_pages[domain_info[href]].append(i)
    
    # 최종 점수 계산
    max_score = -1
    for i in range(n):
        link_score = 0
        # j번째 페이지가 i번째 페이지를 참조함
        for j in link_pages[i]:
            link_score += (basic_score[j] / external_links[j])
        total_score = basic_score[i] + link_score
        if total_score > max_score:
            max_score = total_score
            answer = i
    
    return answer