# This is:
#    *
#   * *
#  * * *
def triangle(number):
    sentence = ""
    for index in range (number):
        tempSentence = " " * (number - index - 1) + ("* " * (index + 1)) + "\n"
        sentence += tempSentence
    return sentence
print(triangle(10))

# This is:
#      *
#     **
#    ***
# for index in range(number):
#     tempSentence = " " * (number - index) + ("*" * (index + 1)) + "\n"
#     sentence += tempSentence
#-----------------------------------------------------------------------
# This is:
# *
# **
# ***
# for index in range(number):
#     tempSentence =("*" * (index + 1)) + "\n"
#     sentence += tempSentence