# message = input("> ")
# words = message.split(" ")
# emoji ={
#     ":)" : "😁",
#     ":(" : "😑"
# }
# output = ("")
# for word in words:
#     output +=emoji.get(word,word) + " "
# print(output)


def emoji_convertor(message) :
    words = message.split(" ")
    emoji = {
        ":)": "😁",
        ":(": "😑"
    }
    output = ("")
    for word in words:
        output += emoji.get(word, word) + " "
    return output
message = input("> ")


print(emoji_convertor(message))
