#     Copyright (C) <year>  <name of author>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
