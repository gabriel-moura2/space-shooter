import pygame

def load_image(name):
    path = f"assets/images/{name}.png"
    return pygame.image.load(path).convert_alpha()

def load_sound(name):
    path = f"assets/sounds/{name}.wav"
    return pygame.mixer.Sound(path)

def generate_partitions(target_sum, max_parts):
    partitions = []
    
    def backtrack(remaining_sum, max_value, current_partition, parts_left):
        if remaining_sum == 0:
            partitions.append(current_partition[:])
            return
        if parts_left == 0 or remaining_sum < 0:
            return
        
        for value in range(max_value, 0, -1):
            if value <= remaining_sum:
                current_partition.append(value)
                backtrack(remaining_sum - value, value, current_partition, parts_left - 1)
                current_partition.pop()
    
    backtrack(target_sum, target_sum, [], max_parts)
    partitions.sort(reverse=True, key=len)
    return partitions

if __name__ == "__main__":
    print(generate_partitions(10, 6))
