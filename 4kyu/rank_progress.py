
# More details on this kata
# https://www.codewars.com/kata/51fda2d95d6efda45e00004e

# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method
class User:

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, act):
        assert act in range(-8, 0) + range(1, 9)
        diff = act - (act > 0) - self.rank + (self.rank > 0)
        self.progress += (0, 1, 3, diff * diff * 10)[(diff > 0) + (diff >= 0) + (diff >= -1)]
        while self.progress >= 100:
            self.rank += 1 + (self.rank == -1)
            self.progress -= 100
        if self.rank >= 8:
            self.rank, self.progress = 8, 0


if __name__ == "__main__":
    user = User()
    print(user.rank)
    user.inc_progress(2)
    print(user.rank)
    
