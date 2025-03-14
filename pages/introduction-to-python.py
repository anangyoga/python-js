import streamlit as st

st.set_page_config(page_title="Introduction to Python", page_icon="📝")

st.title("Introduction to Python")
st.page_link("main.py", label="Back to Homepage", icon="🏠")

st.divider()

st.write("I work with Javascript environment and I think that Python & Javascript has similar fundamental. The only different is the syntax. Here's the introduction to Python for those who already familiar with Javascript.")

st.write("### Variables")

st.write("Javascript uses :blue-background[let] and :blue-background[const] to declare a variable. In Python we don't need that. The conventions are:")
st.write("1. A variable shouldn't start with number.")
st.write("2. A variable can't contain a space.")
st.write("3. A variable can't be a kebab-case.")
st.write("4. A variable is case sensitive.")
st.write("5. A variable can't use reserved keyword in python.")

st.write("Best practice writing a variable:")
st.write("1. Use snake_case.")
st.write("2. Or PascalCase.")
st.write("3. UPPER_CASE is for constanta, in Js we use :blue-background[const].")

st.code(""" 
fruit = 'Durian'
favorite_fruit = 'Durian'
1favoritefruit = 'Durian' #error
favorite fruit = 'Durian' #error
favorite-fruit = 'Durian' #error

# constanta
APP_NAME = 'todolist'
API_KEY = '1312'
""")

st.write("### Print")

st.write(":blue-background[print()] is to Python as :blue-background[console.log()] to Javascript.")

st.code(""" 
# Javascript
const first_name = 'John Doe';
console.log(first_name);
        
# Python
her_name = 'Jane Doe'
print(her_name)
""")

st.write("### Data Types")

st.write("##### String")

st.code(""" 
# Javascript
const first_name = 'John Doe';
        
# Python
her_name = 'Jane Doe'
a_long_text = '''
roses are red
violets are blue
python is great
just like you
'''

""")

st.write("##### Boolean")

st.write("The only difference is that Python use Uppercase F & T for boolean's value, while Javascript uses false & true.")

st.code(""" 
# Javascript
const isActive = false;
const isAdmin = true;
        
# Python
is_admin = True
is_active = False
'''
""")

st.write("##### Number")

st.write("Python has numeric & float for number data types.")

st.code(""" 
# integer
blink = 182
        
# float
pie = 3.14
""")

st.write("##### None")
st.write("Python uses None while Javascript uses null.")

st.code(""" 
# Javascript
let placeholder = null;
        
# Python
my_state = None
""")

st.write("### Reference Types")

st.write("##### List")

st.write("List is just an array in Javascript. Both can contain different data types & mutable.")
st.code(""" 
# Javascript
let tasks = ['Eat', 'Sleep', 'Go to school'];
        
# Python
things_to_do = ['Eat', 'Sleep', 'Go to school']
random_list = ['Run', True, 182]
""")

st.write("##### Tuple")

st.write("Writing Tuple in Python & Javascript is totally different. In Python, the tuple wrapped in braces and the data is immutable. When we define only 2 data, we can't add or remove the data inside the tuple. In Javascript, tuple defined in an array and each element has type of data.")

st.code(""" 
# Javascript
let ourTuple: [number, boolean, string];

# initialize JS tuple correctly
ourTuple = [5, false, 'Coding God was here'];
        
# Python
direction = ("left", "right")
""")

st.write("##### Set")

st.write("Set is collection to store multiple items in a variable. It's unordered, unchangeable, and *do not allow duplicate values*. Honestly I have no idea what Set is in Javascript.")

st.write("We can define the Set in curly braces without key-values pairs.")

st.code(""" 
myset = {"lorem", "ipsum", "ipsum", "dolor"} 
# 'ipsum' is duplicated so when we print it only once appears
""")

st.write("##### Set")

st.write("We call it Object in Javascript. But the key is wrapped in double-quote, like json.")

st.code(""" 
student_information = {"name": "John", "age": 17, "is_student": True } 
""")

st.write("### F-Strings")

st.write("The F-Strings in Python is like template literal in Javascript.")

st.code(""" 
age = 19
txt = f"His age is {age} years old."
""")

st.write("I think that's all I got. Thanks!")

if st.button("Back to homepage"):
  st.switch_page("main.py")
