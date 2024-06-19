from typing import List

results = []


def dfs(record: List[int]):
    if len(record) == 8:
        results.append(record)
    for i in range(8):
        for j in range(len(record)):
            if record[j] == i or abs(record[j] - i) == len(record) - j:
                break
        else:
            dfs(record + [i])


def init_results():
    global results
    dfs([])
    results = [*map(lambda x: "".join([str(i + 1) for i in x]), results)]


def task(K: int):
    print(results[K])


if __name__ == "__main__":
    init_results()

    N = int(input())
    for _ in range(N):
        K = int(input())
        task(K - 1)
