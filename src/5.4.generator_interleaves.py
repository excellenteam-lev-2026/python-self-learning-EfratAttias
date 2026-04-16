def generator_interleave(*iterables):
    iterators = [iter(it) for it in iterables]
    while iterators:
        for it in iterators[:]:
            try:
                yield next(it)
            except StopIteration:
                iterators.remove(it)

if __name__ == "__main__":
    for item in generator_interleave("abc", "123", "!@#"):
        print(item, end=" ")
