#A module can be created by creating a .py file.
# hello.py
def say_hello():
 print("Hello!")

# Modules can be imported by other modules.
# greet.py
import hello
hello.say_hello()

#Specific functions of a module can be imported.
# greet.py
from hello import say_hello
say_hello()

#Modules can be aliased.
# greet.py
import hello as ai
ai.say_hello()

#A module can be stand-alone runnable script.
# run_hello.py
if __name__ == '__main__':
 from hello import say_hello
 say_hello()
#Run it! in cmd
#python run_hello.py
