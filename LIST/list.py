list = ["a","c","d","b"]
list.sort()
print(list)

li = []

# print(type(li))

first = input("Enter 1 fevorite movie: ")
secoend = input("Enter 2 fevorite movie: ")
theird = input("Enter 3 fevorite movie: ")


li.append(first)
li.append(secoend)
li.append(theird)


print(li)



# PALIMDROM [1,2,3,2,1]

peli = [1, 2, 3, 2, 1]
copy_peli = peli.copy()
copy_peli.reverse()
print(copy_peli)

set = set()
print(type(set))

dicsnory = {
    "table" : ["A piece of furniture","List or=f facts & Figures"],
    "cat" : "A small animal"
}

print(dicsnory)

# you are given a list of subjects for students assume
# one classroom is required for 1 subject how many 
# classroom needed by students ?


set = {"python","java","C++","python","javascript","java","python","java","C++","C"}

print(len(set))


# # WAP to enter marks of 3 subjects
# from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one.
# Use subject name as key & marks as value.

dicsnory = {}
dicsnory.update({"chemistry":75})
dicsnory.update({"math":94})
dicsnory.update({"physics":79})
print(dicsnory)

set = {9, 9.0, 9.00}
print(set) #output: 9

