coins = [1,2,5]
amount = 11

def coinChange(coins, amount):
    sum = [0] + [amount + 1] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            sum[i] = min(sum[i], sum[i - coin] + 1)
    if sum[amount] == amount + 1:
        return -1
    return sum[amount]
print(coinChange(coins, amount))