# Copyright (C) 2020 Nebula
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os

print("|=============================|")
print("| Generating a code folder... |")
print("|=============================|")
print(" ")


print(" - Please choose a project name:")
name = input()  # project name
print(" ")

print(" - Generating, please wait...")
os.mkdir(os.getcwd() + os.path.sep + name)  # make folder
os.system("git init ." + os.path.sep + name)  # make git repo
os.system("echo # " + name + " > ." + os.path.sep + name + os.path.sep + "README.md")  # make readme
print(" ")

# open
print(" - Opening in Visual Studio Code...")
os.system("code ." + os.path.sep + name)  # open in vscode
print(" ")
print(" ")

print("|===================|")
print("| Finished process! |")
print("|===================|")
