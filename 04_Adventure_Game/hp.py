import random  
def new_game():
    player_hp=100
    with open("hp_track.txt","w") as f:
        f.write(str(player_hp))

def give_health():
    with open("hp_track.txt","r") as f:
         hp=f.read()
    return(int(hp))
    
    

def player_damage(damage):
    
    with open("hp_track.txt","r") as f:
            hp=int(f.read())
    hp-=damage
    if hp>0:
        with open("hp_track.txt","w") as f:
            f.write(str(hp))
    else:
        return 0
    return(int(hp))  


    





