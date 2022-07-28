def swap(s):
    size = len(s)

    temp = s[0]
    s[0] = s[len(s)-1]
    s[len(s)-1] = temp

    return s

s = [1,2,3,4,5,6,7]

print(f"Before swap is {s}")
a = swap(s)

print(f"After swap is {a}")


# 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

    
