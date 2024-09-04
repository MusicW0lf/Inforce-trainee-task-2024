import random
import string
import time
import matplotlib.pyplot as plt


def group_anagrams(strs):
    start_time = time.time()

    anagrams_map = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams_map:
            anagrams_map[sorted_word] = [word]
        else:
            anagrams_map[sorted_word].append(word)

    end_time = time.time()
    runtime = end_time - start_time
    return runtime


def generate_anagram_strs(size: int, length: int) -> [str]:
    return [''.join(random.choices(string.ascii_lowercase, k=length)) for _ in range(size)]


def measure_execution_time(size_values, lengths):
    execution_times = {length: [] for length in lengths}
    for length in lengths:
        for size in size_values:
            anagrams = generate_anagram_strs(size, length)
            execution_times[length].append(group_anagrams(anagrams))

    return execution_times


size_values = [100, 200, 500, 1000, 2000, 5000, 10000]
lengths = [3, 5, 10, 100, 1000, 2000, 5000]

execution_times = measure_execution_time(size_values, lengths)
transposed_hashmap = {size: [] for size in size_values}
for key, value in execution_times.items():
    for index, element in enumerate(value):
        transposed_hashmap[size_values[index]].append(element)

for length in lengths:
    plt.plot(size_values, execution_times[length], marker='o', label=f'Length {length}')
plt.title('Execution Time vs Number of Anagrams')
plt.xlabel('Number of Anagrams')
plt.ylabel('Execution Time (Seconds)')
plt.grid(True)
plt.legend()
plt.show()

for size in size_values:
    plt.plot(lengths, transposed_hashmap[size], marker='o', label=f'Size {size}')
plt.title('Execution Time vs Length of Anagrams')
plt.xlabel('Length of Anagrams')
plt.ylabel('Execution Time (Seconds)')
plt.grid(True)
plt.legend()
plt.show()
