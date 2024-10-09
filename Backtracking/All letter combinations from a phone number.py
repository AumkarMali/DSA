
#Hashmap
KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def letter_combinations_of_phone_number(digits):

    def dfs(start_index, path):
      #Once start value reaches the last digit entered the function stops
        if start_index == len(digits):
            res.append(''.join(path))
            return
        #Pointer of each nunber entered in list
        next_number = digits[start_index]
        for letter in KEYBOARD[next_number]:
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()

    res = []
    dfs(0, [])
    return res

if __name__ == '__main__':
    digits = input()
    print(letter_combinations_of_phone_number(digits))
    