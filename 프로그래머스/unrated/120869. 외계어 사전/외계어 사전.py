def solution(spell, dic):
    answer = 0
    new_dic = []
    new_spell = ""
    for i in spell:
        new_spell += i
    new_spell = sorted(new_spell)
    
    
    for i in range(len(dic)):
        for j in dic[i]:
            new_dic += j
            new_dic = sorted(new_dic)
        if new_spell == new_dic:
            answer = 1
            break
        else:
            answer = 2
        print(new_dic)
        new_dic = []

    print(new_spell)

    return answer