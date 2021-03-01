import itertools
def solution(user_id, banned_id):
    items = []
    answer = 0
    set_id_num = set()
    for i in range(0, len(user_id)):
        items.append(i)

    perm = list(itertools.permutations(items,len(banned_id))) # 2개의 원소를 가지고 순열을 만든다

    for i in range(0, len(perm)):
        test = 0
        # print(perm[i])
        for j in range(0, len(perm[i])):
            name = user_id[perm[i][j]]
            depth = j
            #print(name + " : " + banned_id[depth])
            if len(name) != len(banned_id[depth]):
                continue
            passed = 0
            for k in range(0, len(name)):
                if banned_id[depth][k] == "*":
                    passed += 1
                elif banned_id[depth][k] == name[k]:
                    passed += 1

            if passed == len(name):
                # print(name + " : "  + banned_id[depth])
                test += 1

        if test == len(banned_id):
            sort_num = []
            for k in range(0, len(banned_id)):
                sort_num.append(perm[i][k])

            sort_num.sort()
            temp = ""
            for k in range(0, len(banned_id)):
                temp += str(sort_num[k])

            if temp not in set_id_num:
                answer += 1
                set_id_num.add(temp)


    return answer

user_id =["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))