# responses = [["good","ok","good","ok"],["ok","bad","ok","ok","good"],["good"],["bad"]]
responses = [["good", "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]]

# def findCommonResponse(responses: list[list[str]]) -> str:
#     response_count = {}
#     for reslist in responses:
#         resSet = set(reslist)
#         reslist = list(resSet)
#         for res in reslist:
#             response_count[res] = response_count.get(res, 0) + 1

#     print(response_count)
#     sorted_response = dict(sorted(response_count.items(), key=lambda item: (-item[1], item[0])))
#     return next(iter(sorted_response))


def findCommonResponse(responses: list[list[str]]) -> str:
    response_count = {}
    for reslist in responses:
        resSet = set(reslist)
        for res in resSet:
            response_count[res] = response_count.get(res, 0) + 1

    sorted_response = dict(sorted(response_count.items(), key=lambda item: (-item[1], item[0])))
    print(sorted_response)
    return min(sorted(response_count.items(), key=lambda item: (-item[1], item[0])))
        

ans = findCommonResponse(responses)
print(ans)