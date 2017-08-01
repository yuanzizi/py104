# ------ex13 参数传递 ------------------
from sys import argv

script, user_name = argv
prompt = "$"

print("The script is called : {}".format(script))
print("Your name is : {}".format(user_name))
print("Do you like me, ?".format(user_name))
likes = input(prompt)

print("you said {} about liking me?".format(repr(likes)))
