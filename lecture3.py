#%%
print("hello world")

# %%
x = 5
x
y = 100

# %%
students = ["harpreet", "shivam", "khushal",
            "vineet","vasu", "somya", "nadeem", "abhi",
            "arjun"]

# %%
type(students)

# %%  they are hetrogenous in nature
foo = ["goldy", 16, "hp"]
foo.pop(2)

# %%
foo[1]
# %% they are mutable
foo[1] = 17
# %%
foo
# %%
boo = ["parveen", 45, foo]

# %%
print(boo)
# %%
boo[2][1]
# %%
# syntax: var_name = (elements, )

# 1. Write a Python program to print a 
# specified list after remving the 0th, 4th and 5th
#  elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# 2. ask for a user input for his/her name with title and access the title
# sample: Mr. Rajesh Goldy
# output: Mr. 
user = input("Please enter your name: ")
user.split(" ")[0]


# 3. From the given string check whether the string is in title case or not?
# sample: This is a title case
# output: False

# 4. count 

#%%
x = [input("blah")]
# %%
sampl= "This is a title case"
sampl.istitle()
# %%
name = "goldy rana"
list(name)
# %%
name = [input("name"), "rana"]

# %%
name
# %%
