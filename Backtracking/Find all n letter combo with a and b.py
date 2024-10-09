
def letter_combination(n):
    def dfs(start_index, path):
        if start_index == n:
            res.append(''.join(path))
            return
        for letter in ['a', 'b']:
            path.append(letter)
            dfs(start_index+1, path)
            #Backtrack and delete
            path.pop()

    res = []
    dfs(0, [])
    return res

if __name__ == '__main__':
    n = int(input())
    res = letter_combination(n)

    #Printing output values 
    for line in sorted(res):
        print(line)
