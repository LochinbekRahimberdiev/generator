import time


class CloneRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
            self.step = step
        else:
            self.start = start
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop and self.step > 0:
            raise StopIteration
        elif self.start <= self.stop and self.step < 0:
            raise StopIteration
        else:
            current = self.start
            self.start += self.step
            return current


# Test with float step
for i in CloneRange(2, 25, 2.5):
    print(i)

# Test with integer step
for i in CloneRange(2, 10, 2):
    print(i)

# Test with negative step
for i in CloneRange(10, 2, -2):
    print(i)

# Test with single argument
for i in CloneRange(10):
    print(i)
