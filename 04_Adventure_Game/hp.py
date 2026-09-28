player_hp=100 #at the start of the game
import random  
with open("hp_track.txt","w") as f:
    f.write(str(player_hp))

mob_encountered=True
if mob_encountered==True:
    with open("hp_track.txt","r") as f:
        hp=f.read()
    print(hp)

def player_damage():
    got_attacked=True
    if got_attacked==True:
        with open("hp_track.txt","r") as f:
                hp=int(f.read())
        hp-=round(random.randint(10,30)/10)*10
        if hp>0:
            with open("hp_track.txt","w") as f:
             f.write(str(hp))
        else:
            return 0
    print(hp)  

player_damage()
    





