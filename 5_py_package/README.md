# Collect_framework
### Installation
To use in your project just use your dependency manager to install it, with pip is like this:

`pip install collect-pkg`
### Short explanation
Program takes string or file(high priority if string too transferred) and return amount and characters which ar unique

call it from command line with this command

`python -m collect_pack --string <your string> --file <your file>`

The package has 4 functions
- amount_of_unique_char

takes string and return tuple amount of unique char in input string and list with them
- format_return

format the result of previous func 
- cli

add two arguments --file and --string and return parser with them
- work_with_args

parse arguments from command line and detect a priority if hand over two arguments

### How it works :new_moon_with_face:
Here a some examples

```
from collect_pack import amount_of_unique_char
print(amount_of_unique_char('qwerrr'))
# result (3,['q','w','e'])
```

```
from collect_pack import format_return, amount_of_unique_char
print(format_return('qwerrr'))
# before format format the result it call amount_of_unique_char in his body 
""" result "qwerrr" => 3
q,w,e are present once.
"""
```

```
from collect_pack import work_with_args
print(work_with_args(file="",string="qwerr"))
# result 'qwerr'
print(work_with_args(file="text.txt",string="qwerr"))
# result 'text from file like one string ' argument file has a higher priority
```