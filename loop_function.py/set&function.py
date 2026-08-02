my_set = {"ritik","rohan","sohan",75,"vishal","ritik"}

# # print(my_set[2]) ye error aayega bcoz set is rand

# print(my_set)
# print(len(my_set))

print(my_set.discard("ritik"))
print(my_set)

my_set.update(["ritik kumar"])
print(my_set)
# # print(reversed(my_set))  error! because set is unorderd

# for i in my_set:
#     print(i)
    
# seter = set()

# seter.add("ritik kumar")
# seter.add("Vishal")

# print(set)

# mera = ()
# mera1 = set()

my_cupoan = my_set.copy()

print(my_cupoan)