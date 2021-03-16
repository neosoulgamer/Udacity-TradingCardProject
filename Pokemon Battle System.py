class Pokemon:
  def __init__(self, name, level, element, max_health, cur_health, knocked_out):
    self.name = name
    self.level = level
    self.element = element
    self.max_health = max_health
    self.cur_health = cur_health
    self.knocked_out = knocked_out

  def __repr__(self):
    return "Pokemon Initialized."

  def lose_health(self, dmg):
    self.cur_health -= dmg
    print ("{} has lost {} health.".format(self.name, self.dmg))

  def gain_health(self, heal):
    self.cur_health += heal
    print ("{} has gained {} health.".format(self.name, self.dmg))

  def knock_out(self):
    if self.cur_health <= 0:
      self.knocked_out = True
      print ("{} has been Knocked Out!".format(self.name))
    else:
      print("{} has {} health remaining".format(self.name, self.cur_health))

  def revive(self):
    if self.knocked_out:
      self.knocked_out = False
      self.cur_health = 1
      print("{} has been revived! {} health remaining".format(self.name, self.cur_health))
    else:
      print("{} is still alive. {} health remaining".format(self.name, self.cur_health))

  def attack(self, Pokemon):
    if self.knocked_out:
      print("{} is currently knocked out! Cannot attack".format(self.name))
    else:
      dmg_done = self.level
      if self.element == "Water":
        if Pokemon.element == "Fire":
          dmg_done = self.level * 2
          Pokemon.cur_health -= dmg_done
        elif Pokemon.element == "Grass":
          dmg_done = self.level / 2
          Pokemon.cur_health -= dmg_done
        else:
          Pokemon.cur_health -= self.level
        print("{} has done {} damage to {}".format(self.name, dmg_done, Pokemon.name))
      elif self.element == "Fire":
        if Pokemon.element == "Grass":
          dmg_done = self.level * 2
          Pokemon.cur_health -= dmg_done
        elif Pokemon.element == "Water":
          dmg_done = self.level / 2
          Pokemon.cur_health -= dmg_done
        else:
          Pokemon.cur_health -= self.level
        print("{} has done {} damage to {}".format(self.name, dmg_done, Pokemon.name))
      else:
        if Pokemon.element == "Water":
          dmg_done = self.level * 2
          Pokemon.cur_health -= dmg_done
        elif Pokemon.element == "Fire":
          dmg_done = self.level / 2
          Pokemon.cur_health -= dmg_done
        else:
          Pokemon.cur_health -= self.level
        print("{} has done {} damage to {}".format(self.name, dmg_done, Pokemon.name))
      return dmg_done 




squirtle = Pokemon("Squirt", 5, "Water", 50, 50, False)
bulbasaur = Pokemon("Bulba", 5, "Grass", 50, 50, False)
charmander = Pokemon("Charm", 5, "Fire", 50, 50, False)

# squirtle.attack(bulbasaur)
#bulbasaur.attack(squirtle)

#print(squirtle)
#print(bulbasaur)

class Trainer:
  def __init__(self, name, potions, active_pokemon, pokemen):
    self.name = name
    self.potions = potions
    self.active_pokemon = active_pokemon
    self.pokemen = pokemen

  def __repr__(self):
    return "Trainer Initialized."

  def use_potion(self):
    amount_healed = 20
    if self.potions > 0:
      self.pokemen[self.active_pokemon].cur_health += amount_healed
      self.potions -= 1
    else:
      print("You do not have any potions.")

  def attack_other_trainer(self, Trainer):
    dmg_done = self.pokemen[self.active_pokemon].attack(Trainer.pokemen[Trainer.active_pokemon])
    print("{} has done {} damage to {}".format(self.pokemen[self.active_pokemon].name, dmg_done, Trainer.pokemen[Trainer.active_pokemon].name))

  def set_active(self, new_active_pokemon):
    self.active_pokemon = new_active_pokemon
    print("{} has been deployed".format(self.pokemen[self.active_pokemon].name))

Trainer1 = Trainer("Chance", 5, 0, [squirtle, charmander])
Trainer2 = Trainer("Devon", 3, 0, [squirtle, charmander])
#print(Trainer1)
#print(Trainer2)

# Testing functions below

#Trainer1.attack_other_trainer(Trainer2)
#Trainer1.set_active(0)
