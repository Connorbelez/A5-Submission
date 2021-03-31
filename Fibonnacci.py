def cachedfibonacci(n, cache={}):
    #basecases: 
    if n <= 2:
        cache[n] = 1 
        return 1
    else:
        f1 = n-1
        f2 = n-2
        if f1 in cache.keys():
            cache[n] = cache[f1] + cache[f2]
            return cache[f1] + cache[f2]
        else:
            return cachedfibonacci(n-1, cache) + cachedfibonacci(n-2, cache)



def test(val1,val2):
    if val1 != val2:
        print(f'Test Failed! \n\tActual: {val1} \n\tExpected: {val2}')
    else:
        print(f'Test PASSED! \n\tActual: {val1}  \n\tExpected: {val2}')

def main():
    test(cachedfibonacci(10,cache={}), 55)
    test(cachedfibonacci(5,cache={}), 5)
    test(cachedfibonacci(8,cache={}), 21)
    test(cachedfibonacci(-10,cache={}), 1)
    test(cachedfibonacci(100,cache={}), 354224848179261915075)
    test(cachedfibonacci(4,cache={}), 3)



if __name__ == "__main__":
    main()