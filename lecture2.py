#%%

# %%
x = 100
# %%
class  = 65
# %% asking for user name
name = "Goldy"


#%% asking for the user's input
name = input("enter your password")
# %% ------ Functions of strings
print(name)
# %% to capt...
name.upper()
# %% to title
diary = "My name is goldy and i belongs to hp"
print(id(diary))
diary = diary.title()
print(id(diary))

# %% lower
diary.lower()
# %%
number = input("Please enter your number: ")
number.isnumeric()

# %%
number = "2456 3456sfghdfgh"
number.isalnum()

# %% strip and split
name = "Rajesh Goldy"
name.split(" ")
# %%
name  = "       Python       "
name.lstrip()

# %% Question
#  seprate the input
info  = "Delhi,Mumbai"
info.split("M")
# %%
user = input("please enter your name: ")
#  Hello user_name
# >>Goldy
# >>>Hello Goldy
print("hello", user)
# >>> hello user_name, welcome to python 
print("Hello", user   ,"Welcome to python")

# %% Format string
print(f"Hello {user} welcome to python")

# %%
# Question
x = "      Python      "
# >>> this is  left strip *Python       *
print(f"This is left strip *{x.lstrip()}*")
# %%
var = "HELLO"
var[-3:-2]
# %%
var[0:7:2]
# %%
var[2:7:1]
# %%
var[::2]

# %%
number = "1234"
print(f"type of number is {type(number)}")
number = int(number)
print(f"type of number is {type(number)}")

# %%
ph_no = float(input("Please enter your number: "))

#%%
str(complex(3+5j))
# %%
b = str(true)
bool(b)
# %%
