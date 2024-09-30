import random


def main():
    data = [5, 6, 11, 7, 9, 4, 2]
    print(randomized_select(data, 0, len(data) - 1, 2))


def randomized_partition(data, start_index, end_idx):
    i = random.randint(start_index, end_idx)
    # Swap the first element with the random element
    data[start_index], data[i] = data[i], data[start_index]
    return partition(data, start_index, end_idx)


def partition(data, start_index, end_idx):
    x = data[start_index]  # Pivot
    i = start_index - 1
    for j in range(start_index + 1, end_idx + 1):
        if data[j] < x:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[end_idx] = data[end_idx], data[i + 1]
    return i + 1


def randomized_select(data, start_index, end_idx, i):
    if start_index == end_idx:
        return data[start_index]  # Base case
    pivot_idx = randomized_partition(data, start_index, end_idx)
    k = pivot_idx - start_index + 1
    if i == k:
        return data[pivot_idx]
    elif i < k:
        return randomized_select(data, start_index, pivot_idx - 1, i)
    else:
        return randomized_select(data, pivot_idx + 1, end_idx, i - k)


if __name__ == "__main__":
    main()
