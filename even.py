
def main():
    evens = []
    for number in range(100):
        # mod 2 not divided by 2
        is_even = number % 2 == 0
        if is_even:
            evens.append(number)
    print(evens)

main()