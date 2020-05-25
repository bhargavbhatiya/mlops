import os

acc = os.popen("cat /mlops/accuracy.txt")
acc1 = acc.read()
print(acc1)
acc2 = acc1.rstrip()
print(acc2)
acc3 = float(acc2)


if acc3<85:
    x = os.popen("cat /code/train.py | grep model.add | wc -l")
    x1 = x.read()
    x2 = x1.rstrip()
    x3 = int(x2)
    print(x3)
    if x3==2:
        y = 'model.add(Dense(units=23, activation=\"relu\"))'
    elif x3==3:
        y = 'model.add(Dense(units=16, activation=\"relu\"))'
    elif x3==4:
        y = 'model.add(Dense(units=8, activation=\"relu\"))'
    else:
        print("sorry not working!!!")
        exit()
    os.system("sed -i '/softmax/ i {}' /mlops/code.py".format(y))
    os.system("curl --user "bhargavbhatiya:323334" http://192.168.43.2:8080/job/mlops_job2/build?token=redhat")

    acc = os.popen("cat /mlops/accuracy.txt")
    acc1 = acc.read()
    print(acc1)
    acc2 = acc1.rstrip()
    print(acc2)
    acc3 = float(acc2)
else:
    print("congrats!!! your model's accuuracy is >85%")

