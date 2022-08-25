'''
@Author: Wu Jiarui.
@e-mail: wu_jiarui@foxmail.com
@Topic:
    Given an integer list containing digits from [0,9], the task is to print all possible letter combinations that the numbers could represent. A mapping of digit to letters (just like on the telephone buttons) is being followed.Note that 0 and 1 do not map to any letters.All themapping are shown in the image below:

    ...(telephone buttons)

    Example:
        Input:  [2,3]
        Output: ad ae af bd be bf cd ce cf
        Input:  [9]
        Output: w x y z
'''

# Input Your Data Here:
input_data = [2, 3]

def toComb(input_data):
    '''
    将输入的数字，转换为可能的字符组合
    '''
    print('Input: ', input_data)

    # 数字-字符映射表
    numcode = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    input_count = [len(numcode[x]) for x in input_data]

    pointer = [0 for x in input_count]

    print('Output: ', end='')
    while pointer[0] < input_count[0]:
        # print a word.
        word = []
        for x in range(len(input_data)):
            if numcode[input_data[x]] != '':    # 改良，判断是否为空字符串。
                word.append(numcode[input_data[x]][pointer[x]])
        print(''.join(word), end=' ')

        pointer[-1] += 1
        # 进位检验
        for i in range(len(pointer)-1, 0, -1):
            if pointer[i] >= input_count[i]:
                pointer[i-1] += 1
                pointer[i] = 0

toComb(input_data)

input('\n\nPress any key to continue.')



# Deprecated code...

# numcode = {0:'', 1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'} #

# for x in numcode[input_data[0]]:
#     for y in numcode[input_data[1]]:
#         for z in numcode[input_data[2]]:
#             print(x, end='')
#             print(y, end='')
#             print(z, end='')
#             print('', end=' ')

# for i in range(len(input_data)):
#     # for x in numcode[input_data[i]]:
#     #     for y in numcode[input_data[i]]:
#             for j in numcode[input_data[i]]:
#                 print([0], end='')
#                 print(numcode[input_data[i]][1], end='')
#                 print(numcode[input_data[i]][2], end='')
#                 # print(y, end='')
#                 # print(z, end='')
#                 print('', end=' ')
