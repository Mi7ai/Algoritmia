dic = {"Name1": 18, "Name2": 18, "Name3": 18}

name = input("Name: ")

if name not in dic:
    print("No sé su edad!")
else:
    print(dic[name])
