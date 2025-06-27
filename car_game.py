# cara-game
#
# >help
# start-to start the car
# stop-to stop the car
# quit-to exit

# asd- i don't understand

command = ""
started = False
while True:
    command = input("> " ).lower()
    if command == "start":
        if  started:
            print("car is already started ")
        else:
            started == True
            print("Car started ...")
    elif command == "stop":
        if not started:
            print("care is already stopped.")
        else:
            started == False
            print("Car stopped.")
    elif command == "help":
        print('''
start - car start to go
stop-car stop.
quiet-to quite''')
    elif command =="quit":
        break
    else:
        print("I don't understand!")

