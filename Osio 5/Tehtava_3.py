luku = int(input("Anna testattava kokonaisluku: "))

itr = luku-1

flag = True

while itr > 1:
    if luku%itr == 0:
        flag = False

    itr -= 1

if flag:
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")

