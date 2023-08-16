candidates = [2,3,5]
target = 8

answer = []


def backtracking(level, res):

    if sum(res) > target:
        return

    if level == len(candidates):
        return

    if sum(res) == target:
        print(res)
        answer.add(tuple(sorted(res)))
        return

    for i in range(len(candidates)):
        backtracking(level+1, res + [candidates[i]])
        backtracking(level+1, res)




n = len(candidates)

def dfs(cur, cur_sum, idx):  # try out each possible cases

    if cur_sum > target:
        return  # this is the case, cur_sum will never equal to target

    if cur_sum == target:
        answer.append(cur)
        return  # if equal, add to `ans`

    for i in range(idx, n):
        dfs(cur + [candidates[i]], cur_sum + candidates[i], i)  # DFS


dfs([], 0, 0)

print(answer)
