import random
import time


def main():
    data = [5, 6, 11, 7, 9, 4, 2, 2, 2, 2]
    print(select(data, 0, len(data) - 1, 5))

    test_data = [10000 - i for i in range(10000)]

    deterministic_start_time = time.time()
    select(test_data, 0, len(test_data) - 1, len(test_data) - 25)
    print(
        f'Deterministic Select Time: {(time.time() - deterministic_start_time) * 1_000_000:.2f} microseconds')

    randomized_start_time = time.time()
    randomized_select(test_data, 0, len(test_data) - 1, len(test_data) - 25)
    print(
        f'Randomized Select Time: {(time.time() - randomized_start_time) * 1_000_000:.2f} microseconds')

    test_data.clear()
    test_data.extend(range(10000))


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition_around(arr, start_idx, end_idx, pivot):
    pivot_index = arr.index(pivot)
    swap(arr, pivot_index, end_idx)
    store_index = start_idx

    for j in range(start_idx, end_idx):
        if arr[j] < pivot:
            swap(arr, store_index, j)
            store_index += 1
    swap(arr, store_index, end_idx)
    return store_index


def select(data, start_idx, end_idx, i):
    while (end_idx - start_idx + 1) % 5 != 0:
        for j in range(start_idx + 1, end_idx + 1):
            if data[start_idx] > data[j]:
                swap(data, j, start_idx)
        if i == 1:
            return data[start_idx]
        start_idx += 1
        i -= 1

    g = (end_idx - start_idx + 1) // 5
    for j in range(start_idx, start_idx + g):
        nested_list = []
        for k in range(5):
            nested_list.append(data[j + k * g])
        nested_list.sort()
        for k in range(5):
            data[j + k * g] = nested_list[k]

    x = select(data, start_idx + 2 * g, start_idx + 3 * g - 1, g // 2)
    q = partition_around(data, start_idx, end_idx, x)
    k = q - start_idx + 1

    if i == k:
        return data[q]
    elif i < k:
        # Search in the left partition
        return select(data, start_idx, q - 1, i)
    else:
        return select(data, q + 1, end_idx, i - k)


def randomized_select(data, start_idx, end_idx, i):
    if start_idx == end_idx:
        return data[start_idx]

    pivot_index = random.randint(start_idx, end_idx)
    pivot = data[pivot_index]
    swap(data, pivot_index, end_idx)
    q = partition_around(data, start_idx, end_idx, pivot)
    k = q - start_idx + 1

    if i == k:
        return data[q]
    elif i < k:
        # Search in the left partition
        return randomized_select(data, start_idx, q - 1, i)
    else:
        return randomized_select(data, q + 1, end_idx, i - k)


if __name__ == "__main__":
    main()
