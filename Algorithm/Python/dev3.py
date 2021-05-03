from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    dict_referral = defaultdict()
    dict_referral["-"] = "None"
    dict_profit = defaultdict(int)

    for i in range(0, len(enroll)):
        dict_referral[enroll[i]] = referral[i]

    for i in range(0, len(seller)):
        profit = amount[i] * 100
        profit_referral = int(profit * 0.1) #발생하는 이익에서 10% 를 계산하여 자신을 조직에 참여시킨 추천인에게 배분

        if profit_referral < 1:
            dict_profit[seller[i]] += profit
        else:
            dict_profit[seller[i]] += profit - profit_referral
            upper_person = dict_referral[seller[i]]
            while 1:
                if upper_person == "None":
                    break
                else:
                    upper_profit_referral = int(profit_referral * 0.1)
                    dict_profit[upper_person] += (profit_referral - upper_profit_referral)
                    profit_referral = upper_profit_referral
                    upper_person = dict_referral[upper_person]


    for i in range(0, len(enroll)):
        answer.append(dict_profit[enroll[i]])

    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]


print(solution(enroll, referral, seller, amount))

