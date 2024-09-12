def primes(limit):
    nums = list(range(2, limit + 1))
    for num in nums:
        print(num, end=" :  ")
        result = num + num
        while result <= limit:
            print(result, end=" ")
            if result in nums:
                nums.remove(result)
            result = result + num
        print("")
    return nums


print(primes(10))
