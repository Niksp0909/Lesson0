def all_variants(text):
    n = len(text)
    for size in range(1, n + 1):
        for i in range(n - size + 1):
            yield text[i:i + size]


a = all_variants("abc")
for i in a:
    print(i)
