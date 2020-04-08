class Pokemon:
  def __init__(self, name, level, kind, max_health, cur_health, knocked_state,experience, hitpoints, attack_speed):
    self.experience = experience
    self.name = name
    self.level = level
    self.max_health = max_health
    self.kind = kind
    self.cur_health = cur_health
    self.knocked_state = knocked_state
    self.hitpoints = hitpoints
    self.attack_speed = attack_speed
    
  def knock_out(self):
    if self.cur_health == 0:
      self.knocked_state = True
      print("knocked out")
    
  def update_experience(self, state):
    if state == True:
      self.experience += 10
      if self.experience >= 50:
        self.level += 1
        self.experience = self.experience-50
        hitpoints += 2
        print("Level upppppp")
    else:
      self.experience -= 5
  def regain_health(self, points):
    self.cur_health += points
    print("health regained")

  def revive_pokemon(self):
    self.knocked_state = False
    print("Revived pokemon")
  
  def __repr__(self):
    print("{} now has {} health".format(self.name, self.cur_health))
      
  def pokemon_state(self, pokemon_2):
    if self.kind == 'fire' and pokemon_2.kind == 'grass':
      return 1
    elif self.kind == 'grass' and pokemon_2.kind == 'fire':
      return -1
    elif self.kind == 'fire' and pokemon_2.kind == 'water':
      return -1
    elif self.kind == 'water' and pokemon_2.kind == 'fire':
      return 1
    if self.kind == 'water' and pokemon_2.kind == 'grass':
      return -1
    elif self.kind == 'grass' and pokemon_2.kind == 'water':
      return 1
    
  def attack_pokemon(self, pokemon_2):
    if self.pokemon_state(pokemon_2) == 1:
      pokemon_2.cur_health -= self.hitpoints
      self.update_experience(True)
      print("VICTORY\nCurrent health1: {}".format(self.cur_health))
      print("Current Health2: {}".format(pokemon_2.cur_health))
    elif self.pokemon_state(pokemon_2) == -1:
      self.cur_health -= pokemon_2.hitpoints
      self.experience -= 5
      print("DEFEAT")
      print("Current health1: {}".format(self.cur_health))
      print("Current Health2: {}".format(pokemon_2.cur_health))
    else:
      print("NOTHING")
  
#pokemon definitions
charmander = Pokemon("Charmander", 1, 'fire', 100, 50, False,0, 10, 60)
bulbasur = Pokemon('Bulbasur', 1, 'grass', 100, 50, False,0, 7, 65)
squirtle = Pokemon('Squirtle', 1, 'water', 100, 50, False,0, 7, 55)
lapras = Pokemon('Lapras', 1, 'water', 100, 50, False,0, 8, 55)

class Trainer:
    
  def __init__(self, trainer_name, pokemon_list, potions_number, active_pokemon):
    self.pokemon_list = pokemon_list
    self.trainer_name= trainer_name
    self.potions_number = potions_number
    self.active_pokemon = active_pokemon

  def add_pokemon(self, adding_pokemon):
      for i in adding_pokemon:
        self.pokemon_list += i
      print("POKEMON ADDED")
    
  def attack(self, trainer_2):
    if self.active_pokemon.knocked_state == False:#attacks
      if trainer_2.active_pokemon.knocked_state == True:#returns unattacking because opponet is already knocked
        print("Opponent pokemon already knocked")
        return
      else:
        self.active_pokemon.attack_pokemon(trainer_2.active_pokemon)
        print("Attacked")
    else:#returns unattacking because it itself is knocked
      print("Cannot attack with knocked pokemon")
      return
    #knocks if health is 0
    trainer_2.active_pokemon.knock_out()
    self.active_pokemon.knock_out()
    
  def use_potion(self):
    if self.active_pokemon.cur_health < 100:
        if self.active_pokemon.cur_health > 90:
          self.active_pokemon.cur_health = 100
        else:
          self.active_pokemon.cur_health += 10
          print("health increased")
    else:
      print("Max health already")
  def switch_pokemon(self, switching_pokemon):
    if switching_pokemon.knocked_state == True:
      print("Cannot switch to knocked pokemon")
    else:
      self.active_pokemon = switching_pokemon
      print("Active pokemon now is {}".format(self.active_pokemon.name))

  def catch_pokemon(self, catching_pokemon):
    if len(self.pokemon_list) < 6:
      self.pokemon_list += catching_pokemon
    else:
      print("Cannot catch pokemon. Balls full. First remove one") 

  def remove_pokemon(self,removing_pokemon):
    spot = 100
    try:
      spot = self.pokemon_list.index(removing_pokemon)
    except ValueError:
      spot = 100
      print("You don\'t have {} to remove..".format(removing_pokemon.name))
    finally:
      if spot != 100:
        self.pokemon_list.pop(spot)
        print("Removed {}".format(removing_pokemon.name))

  def __repr__(self):
    return "Name: {}\nActive Pokemon:{}\nTotal Potions: {}".format(self.trainer_name, self.active_pokemon.name, self.potions_number)
    
yes = Trainer('Yesh', [charmander, bulbasur], 3, bulbasur)
no = Trainer('No', [squirtle, charmander], 5, squirtle)

def battleArena(master1, master2):
  current_player = 0
  won_by = 0

  #sets rival masters in turn
  if master1.active_pokemon.attack_speed > master2.active_pokemon.attack_speed:
    current_master = master1
    opponent_master = master2
  else:
    current_master = master2
    opponent_master = master1

  while(master1.active_pokemon.knocked_state != False or master2.active_pokemon.knocked_state != False):   #until one pokemon gets knocked out
    print("MOVES:........\n1) Attack\t2)Use potion\n3)Switch Pokemon")
    move = 3
    if move == 1:
      current_master.attack(opponent_master)
      current_master, opponent_master = opponent_master , current_master #swaps the attacking turn
    elif move == 2:
      current_master.use_potion()
    elif move == 3:
      print("Choose pokemon:\n")
      for i in current_master.pokemon_list:
        print(i)

battleArena(yes,no)
print(yes.pokemon_list[0].name)
print(yes)