import time
import random

doors = [False, False, True]

right_count = 0
total_count = 1000000

def play_game() -> bool:
    # 随机选择一个下标0 1 2
    choice_index = random.randint(0, 2)

    # 主持人选择一个错误答案 选择0 除非玩家选择0 
    wrong_index = 0 if choice_index != 0 else 1

    # 考虑主持人帮我们排除了错误答案
    choice_index = ({0, 1, 2} - {choice_index, wrong_index}).pop()

    return doors[choice_index]

def play_game_v2() -> bool:
    # 打乱数组
    random.shuffle(doors)
    choice_index = random.randint(0, 2)

    # 主持人的备选集 排除掉玩家的选择
    wrong_index_set = {0, 1, 2} - {choice_index}

    # 先从备选集中随便选择一个
    wrong_index = wrong_index_set.pop()
    if doors[wrong_index]:
        # 如果选中了正确答案，则换一个即可
        wrong_index = wrong_index_set.pop()
    
    choice_index = ({0, 1, 2} - {choice_index, wrong_index}).pop()
    return doors[choice_index]



start = time.time()
for i in range(total_count):
    if play_game_v2():
        right_count += 1

print(f'right count = {right_count}, probability = {right_count / total_count}, cost time = {time.time() - start}')
