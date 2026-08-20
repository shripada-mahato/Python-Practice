# %%
print("hello world")

# %%
def odd_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
odd_even(10)

# %% [markdown]
# exception handling

# %%
try:
    num = 10 / 2
except ZeroDivisionError:
    print(f"can't devide by zero")
else:
    print(int(num))

# %%
try:
    print(10/2)
    print(10%2)
except ZeroDivisionError:
    print('error')
finally:
    print('program finished')

# %%
try:
    age = int(input("enter number:- "))
    print(age)
except ValueError:
    print('invalid number')


