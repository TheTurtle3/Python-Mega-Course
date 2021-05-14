phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for x in phone_numbers.values():
    x = "00" + x[1:]
    print(x)