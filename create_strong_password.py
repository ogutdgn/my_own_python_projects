import random
password = []
for i in range(5):
    x = chr(random.randint(97,123))
    y = chr(random.randint(65,91))
    z = chr(random.randint(48,58))
    l = chr(random.randint(33,48))
    password.append(x)
    password.append(y)
    password.append(z)
    password.append(l)
    random.shuffle(password)
    password1 = "".join(password)
print(password1)