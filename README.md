# compiler-to-c
The python version used is 3.9

Code to convert python script to C executable or pyd module



To convert, you need to put a python script with any name in the compliler folder instead of example.py.
The next step is to run our build_c.py and wait for the build to complete.

# General information for building in exe #

## 1. To use python -> exe (pyinstaller) ##

We only need .pyd as a result of running build_c.py
Let's say our pyd file is example.cp39-win_amd64.pyd,
then we create start.py and write import example there
Next, we build through pyinstaller using start.py
>pyinstaller -F start.py --add-data "example.cp39-win_amd64.pyd ;."

Our code will be imported from pyd written in C


## 2. Using only C ##
There will be an .exe in the project folder after the build
Next, we need to download the embed python zip
For example for python 3.9 -> https://www.python.org/ftp/python/3.9.0/python-3.9.0-embed-win32.zip

Then you need to add the modules we need to the zip archive.
For example, if we used the requests module, we must put the requests folder in the zip
The requests folder is located in the 
>C:\Users\user\AppData\Local\Programs\Python\Python39\Lib\site-packages 

You also need to put the DLL in the python39.dll archive
The DLL is located here:
>C:\Users\user\AppData\Local\Programs\Python\Python39


## 3. Compile .c file ##

A more detailed article is here
https://docs.microsoft.com/ru-ru/cpp/build/walkthrough-compile-a-c-program-on-the-command-line


---------------------
Communication with me:

Telegram -> t.me/MrBonjur

Discord -> Bonjur#2002
