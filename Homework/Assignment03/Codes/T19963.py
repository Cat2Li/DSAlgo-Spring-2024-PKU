import statistics

n = int(input())
location = [*map(eval, input().split())]
price = [*map(int, input().split())]

price_ratio = [sum(location[i]) / price[i] for i in range(n)]
price_ratio_median = statistics.median(price_ratio)

price_median = statistics.median(price)

mask = [False for _ in range(n)]
for i in range(n):
    if price[i] < price_median and price_ratio[i] > price_ratio_median:
        mask[i] = True

print(sum(mask))
