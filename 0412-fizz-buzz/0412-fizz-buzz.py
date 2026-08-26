class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        box = list()
        for i in range(1,n+1):
            if i % 3==0 and i % 5==0:
                box.append("FizzBuzz")
            elif i%3==0:
                box.append("Fizz")
            elif i%5==0:
                box.append("Buzz")
            else:
                box.append(str(i))
        return box        