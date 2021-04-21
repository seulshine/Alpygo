from collections import deque
from collections import defaultdict


def solution(tickets):
    # 재귀 호출을 사용한 DFS
    def dfs(key, journey):
        if len(journey) == N + 1:
            return journey

        for idx, country in enumerate(airport_info[key]):
            airport_info[key].pop(idx)

            temp_journey = journey[:]  # deepcopy
            temp_journey.append(country)

            result_journey = dfs(country, temp_journey)

            if result_journey:
                return result_journey  # 모든 티켓을 사용해 통과한 경우

            airport_info[key].insert(idx, country)  # 통과 못했으면 티켓 반환

    airport_info = defaultdict(list)
    for key, value in tickets:
        airport_info[key].append(value)

    for airport in airport_info:
        airport_info[airport].sort()

    N = len(tickets)
    answer = dfs("ICN", ["ICN"])

    return answer


list_air = 	[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(list_air))

list_air2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

print(solution(list_air2))
