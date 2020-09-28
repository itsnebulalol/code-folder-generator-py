import os

print("|=============================|")
print("| Generating a code folder... |")
print("|=============================|")
print(" ")

# name
print(" - Please choose a project name:")
name = input()
print(" ")

print(" - Generating, please wait...")
os.mkdir(os.getcwd() + os.path.sep + name)
os.system("git init ." + os.path.sep + name)
os.system("echo # " + name + " > ." + os.path.sep + name + os.path.sep + "README.md")
print(" ")

print(" - Opening in Visual Studio Code...")
os.system("code ." + os.path.sep + name)
print(" ")
print(" ")

print("|===================|")
print("| Finished process! |")
print("|===================|")
