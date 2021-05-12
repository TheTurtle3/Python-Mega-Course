def foo(temp):
    if temp > 25:
        return "Hot"
    elif temp <= 25 and temp >= 15:
        return "Warm"
    else:
        return "Cold"