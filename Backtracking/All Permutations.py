def permutations(n):
  def dfs(start, path, used, ans):
    if start == len(n):
      ans.append(''.join(path))
      return

    for i in range(len(n)):
      if used[i]:
        continue

      used[i] = True
      path.append(n[i])
      dfs(start + 1, path, used, ans)
      path.pop()
      used[i] = False

  ans = []
  dfs(0, [], [False] * len(n), ans)
  return ans
    
if __name__ == '__main__':
    letters = input("Enter a string: ")  # Prompt the user for input
    res = permutations(letters)
    for line in sorted(res):
        print(line)
