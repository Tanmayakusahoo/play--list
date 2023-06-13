play_list = ["a", "b", "c"]
while True:
    now = input("please enter a song or END :")
    if now == "END":
        print("You have Ended the task")
        break
    elif now not in play_list:
        play_list.pop(0)
        play_list.append(now)
        play_list
    elif now in play_list:
        index = play_list.index(now)
        play_list.pop(index)
        play_list.append(now)
        play_list
    print(play_list)