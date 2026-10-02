import stats 
player=stats.Player_Stats()
def write_hp(content):
    with open("hp_track.txt","w") as f:
            f.write(str(max(0,content)))
def new_game():
    player_hp=player.player_health
    write_hp(player_hp)
    

def give_health():
    with open("hp_track.txt","r") as f:
         hp=f.read()
    return(int(hp))
    
def player_damage(damage):
    hp=give_health()
    hp-=player.get_damage(damage)
    write_hp(hp)
    if hp<=0:
        return 0
    return(int(hp))  


    





