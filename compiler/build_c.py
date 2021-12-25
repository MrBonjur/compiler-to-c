########################################################################
#                           Compiler to C                              #
#                      25.12.2021 create Bonjur                        #
#                To convert, put next to the py script                 #
#     To run .exe on other PCs, you need an archive with libraries     #
#                Download pure library for python 3.9                  #
# https://www.python.org/ftp/python/3.9.0/python-3.9.0-embed-win32.zip #
########################################################################
from getpass import getuser
import shutil
import sys
import os

user = getuser()

# Check the paths and, if different, replace with the desired one
name_project = "MyProject"
path_vcvarsall = r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat"
path_include = fr"C:\Users\{user}\AppData\Local\Programs\Python\Python39\include"
path_lib = fr"C:\Users\{user}\AppData\Local\Programs\Python\Python39\libs\python39.lib"


def compiler():
    build_file = None  # The name of the file to be compiled
    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename != os.path.basename(sys.argv[0]) and filename.endswith(".py"):
                build_file = filename

    os.rename(build_file, build_file + "x")  # You need a kind of file to compliment .pyx

    with open("setup.py", "w") as setup:  # Starter to convert to .c
        setup.write(f'''from distutils.core import setup\nfrom Cython.Build import cythonize\nsetup( name = '{name_project}', ext_modules = cythonize(["*.pyx"]))''')

    os.system("python setup.py build_ext --inplace")  # Compilation to .c

    with open("start.bat", "w") as setup:  # Starter to convert to .exe (No libraries)
        setup.write(f'cython {build_file + "x"} --embed\n'
        f'call "{path_vcvarsall}" x64\n' 
        fr'cl {build_file.replace("py", "c")} /MD /I "{path_include}" /link "{path_lib}" "%WindowsSdkDir%Lib\%WindowsSDKVersion%um\%VSCMD_ARG_HOST_ARCH%\User32.lib" "%WindowsSdkDir%Lib\%WindowsSDKVersion%um\%VSCMD_ARG_HOST_ARCH%\Kernel32.lib"')

    os.system("start.bat")
    os.rename(build_file + "x", build_file)
    os.remove("start.bat")
    os.remove("setup.py")
    os.remove(build_file.replace("py", "lib"))
    os.remove(build_file.replace("py", "exp"))
    os.remove(build_file.replace("py", "obj"))
    shutil.rmtree(os.path.dirname(__file__) + "\\build", ignore_errors=True)


if __name__ == "__main__":
    compiler()
