def reverse_string(s):
    if s == "":
        return s
    else:
        return reverse_string(s[1:]) + s[0]
print(reverse_string("Hades"))