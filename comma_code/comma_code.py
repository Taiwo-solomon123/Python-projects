def comma_code(li):
    return ", ".join(li[:-1])+" and "+li[-1]
spam = ['apples', 'bananas', 'tofu', 'cats', "cakes", "mashmellows", "desert", "drinks", "friuts"]
print(comma_code(spam))