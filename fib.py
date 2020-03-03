def FIB(months, k):
    """Rabbits and Recurrence Relations"""
    babies = 1
    adults = 0
    for _ in range(months-1):
        adults_in_prev_month = adults
        adults += babies
        babies = adults_in_prev_month * k
    return adults + babies

if __name__ == "__main__":
    print(FIB(31, 4))