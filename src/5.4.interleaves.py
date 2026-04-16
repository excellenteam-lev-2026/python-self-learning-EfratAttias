def interleave(*iterables):
    result = []
    for i in range(max(len(it) for it in iterables)):
        for it in iterables:
            if i < len(it):
                result.append(it[i])

    return result

if __name__ == "__main__":
    for item in interleave("abc", "123", "!@#"):
        print(item, end=" ")
