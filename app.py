player_name = input("Welcome to GC Mini Golf! What is your name? ")
name_txt = f"Hi, {player_name}! "

while True:
    total_holes = input(name_txt + "Would you like to play 3 or 6 holes? ")
    if total_holes == "3" or total_holes == "6":
        par = int(total_holes) * 3
        break
    else:
        print(f"{total_holes} is not a valid response. Please enter 3 or 6 holes.")

hole_number = 1
total_score = 0

for i in range(int(total_holes)):
    ask_score = f"How many putts for hole {hole_number}? (par 3:) "
    hole_total = input(ask_score)
    hole_number += 1
    total_score += int(hole_total)

final_score = int(par) - int(total_score)
if int(total_holes) < 6:
    if int(total_score) > 9:
        print(f"Nice try, {player_name}... Your total score was: +{final_score}.")
    elif int(total_score) < 9:
        print(f"Great job, {player_name}! Your total score was: -{final_score}.")
    else:
        print(f"Good job, {player_name}. Your total score was: {final_score}.")
else:
    if int(total_score) > 18:
        print(f"Nice try, {player_name}... Your total score was: +{final_score}.")
    elif int(total_score) < 18:
        print(f"Great job, {player_name}! Your total score was: -{final_score}.")
    else:
        print(f"Good job, {player_name}. Your total score was: {final_score}.")