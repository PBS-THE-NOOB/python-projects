import random
class Player_Stats():
     def __init__(self):
        #Player Stats
          self.player_health=100
          self.player_min_damage=10
          self.player_max_damage=40
          self.damage_boost=0
          self.defence_boost=0
          self.attack_level=1
     def damage_upgrade(self,increase):
         self.damage_boost+=increase
     def defence_upgrade(self,increase):
         self.defence_boost+=increase
     def attack_level_upgrade(self,increase):
         self.attack_level+=increase
     def health_boost(self,increase_in_10):
         self.player_health+=increase_in_10*10
     def get_player_attack(self):
        min_damage=self.attack_level*(self.player_min_damage+self.damage_boost)
        max_damage=self.attack_level*(self.player_max_damage+self.damage_boost)
        return (round(random.randint(min_damage,max_damage))/10)*10
     def get_damage(self,damage):
         return max(0,damage-self.defence_boost*10)
    
         
          

        