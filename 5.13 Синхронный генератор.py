def positive_integers(until: int):
    for integer in range(until):
        yield integer

positiv_iterator = positive_integers(2)

print(next(positiv_iterator))
print(next(positiv_iterator))

