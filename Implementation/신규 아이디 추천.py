def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    letter = ['-', '_', '.']
    temp = ''
    for c in new_id:
        if c.isdigit() or c.isalpha() or (c in letter):
            temp += c
    new_id = temp
    # 3단계
    while True:
        idx = new_id.find('..')
        if idx == -1: break
        new_id = new_id[:idx] + new_id[idx + 1:]
    # 4단계
    if len(new_id) != 0 and new_id[0] == '.': new_id = new_id[1:]
    if len(new_id) != 0 and new_id[-1] == '.': new_id = new_id[:-1]
    # 5단계
    if len(new_id) == 0: new_id = 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.': new_id = new_id[:-1]
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]

    return new_id