# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# # string concatenation (aka how to put strings together)
# # suppose we want to creat a stirng that says

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
animal = input("Animal: ")

madlib = f"Tractors are so {adj}! It makes me so excited all the time because\
I love to {verb1}.Stay hydrated and {verb2}like you are {animal}!"

print(madlib)