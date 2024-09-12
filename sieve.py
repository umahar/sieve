def primes(limit):
    nums = list(range(2, limit + 1))
    for num in nums:
        result = num + num
        while result <= limit:
            if result in nums:
                nums.remove(result)
            result = result + num
    return nums


print(primes(10))
