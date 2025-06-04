import pygame

def load_image(name):
    path = f"assets/images/{name}.png"
    return pygame.image.load(path).convert_alpha()

def load_sound(name):
    path = f"assets/sounds/{name}.wav"
    return pygame.mixer.Sound(path)

def generate_partitions(target_sum, max_parts, value_limit):
    partitions = []
    dp = [[False] * (target_sum + 1)]
    
    def backtrack(remaining_sum, max_value, current_partition, parts_left):
        if remaining_sum == 0:
            partitions.append(current_partition[:])
            return
        if parts_left == 0 or remaining_sum < 0:
            return
        
        for value in range(min(value_limit, max_value), 0, -1):
            current_partition.append(value)
            backtrack(remaining_sum - value, value, current_partition, parts_left - 1)
            current_partition.pop()
    
    backtrack(target_sum, target_sum, [], max_parts)
    partitions.sort(key=len)
    return partitions

def generate_partitions_dp(target_sum, max_parts, value_limit):
    memo = {}

    def solve(current_target, parts_remaining, max_allowed_value):
        key = (current_target, parts_remaining, max_allowed_value)
        if key in memo:
            return memo[key]
        if current_target == 0:
            return [[]]
        if parts_remaining == 0 or current_target < 0:
            return []

        partitions = []
        for value in range(min(max_allowed_value, current_target, value_limit), 0, -1):
            sub_partitions = solve(current_target - value, parts_remaining - 1, value)
            for sp in sub_partitions:
                partitions.append([value] + sp)

        memo[key] = partitions
        return partitions
    result = solve(target_sum, max_parts, value_limit)
    result.sort(key=len)
    return result

if __name__ == "__main__":
    l = generate_partitions_dp(435, 7, 63)
    print(l)
