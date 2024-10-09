def partition(n):

    def dfs(start, path, openBracketCtr, closedBracketCtr, ans):
        if start == n * 2:
            ans.append(''.join(path))
            return

        if openBracketCtr < n:
            path.append('(')
            openBracketCtr += 1
            dfs(start + 1, path, openBracketCtr, closedBracketCtr, ans)
            path.pop()
        if closedBracketCtr < openBracketCtr:
            path.append(')')
            closedBracketCtr += 1
            dfs(start + 1, path, openBracketCtr, closedBracketCtr, ans)
            path.pop()

    ans = []
    dfs(0, [], 0, 0, ans)
    return ans


if __name__ == '__main__':
    n = int(input("Enter n: "))
    res = partition(n)
    for row in res:
        print(row)
