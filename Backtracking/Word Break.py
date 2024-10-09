def wordBreak(target, words):
  def dfs(start_index):
    if start_index == len(target): # we have constructed the entire target
      return True

    for word in words:
      if target[start_index:].startswith(word):
        if dfs(start_index + len(word)):
            return True

    return False

  return dfs(0)
  
if __name__ == '__main__':
    target = "lemonade"
    words = ["lemon", "ade"]

    result = wordBreak(target, words)
    print(result)
