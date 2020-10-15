from animals import Llama, Goat, Alpaca, Pony, Pig, Tadpole, Goldfish, Mallard, Goose, Frog, Snake, Turtle, Lizard, Viper, Boa
from attractions import PettingZoo, Wetlands




# fluffy_village = PettingZoo("Fluffy Village")
# varmint_village = PettingZoo("Varmint Village")
wet_village = Wetlands("Wet Village")
print(wet_village.description)


############

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow" )
mr_fuzz = Goat("Mister Fuzz", "mountain goat", "morning", "Goat Chow")
baby_fuzz = Alpaca("Baby Fuzz", "domestic alpaca", "morning", "Alpaca Chow")
fancy_fuzz = Pony("Fancy Fuzz", "miniature horse", "morning", "Pony Chow")
oink_fuzz = Pig("Oink Fuzz", "domestic pig", "morning", "Pig Chow")

# fluffy_village.add_to_list(miss_fuzz)
# fluffy_village.add_to_list(mr_fuzz)
# fluffy_village.add_to_list(baby_fuzz)
# fluffy_village.add_to_list(fancy_fuzz)
# fluffy_village.add_to_list(oink_fuzz)

##########

sneky = Snake("Sneky", "copperhead", "morning", "Snake Chow")
squirt = Turtle("Squirt", "turtle", "morning", "Turtle Chow")
lizzie = Lizard("Lizzie", "lizard", "morning", "Lizard Chow")
veep = Viper("Veep", "viper", "morning", "Pig Chow")
boaz = Boa("Boaz", "boa constrictor", "morning", "Boa Chow")

# varmint_village.add_to_list(sneky)
# varmint_village.add_to_list(squirt)
# varmint_village.add_to_list(lizzie)
# varmint_village.add_to_list(veep)
# varmint_village.add_to_list(boaz)

###############


thad = Tadpole("Thad", "frog", "morning", "Snake Chow")
nemo = Goldfish("Nemo", "fish", "morning", "Snake Chow")
mallory = Mallard("Mallory", "duck", "morning", "Snake Chow")
bonkers = Goose("Bonkers", "goose", "morning", "Snake Chow")
froggie = Frog("Froggie", "Frog", "morning", "Snake Chow", 123789)
print(froggie.chip_num)


wet_village.add_to_list(thad)
wet_village.add_to_list(nemo)

print(wet_village.last_critter_added)
# wet_village.add_to_list(mallory)
# wet_village.add_to_list(bonkers)
# wet_village.add_to_list(froggie)

################

# for animal in fluffy_village.animals:
#     print(f'You can find {animal.name} the {animal.species} in {fluffy_village.attraction_name}')

# for animal in varmint_village.animals:
#     print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

# for animal in wet_village.animals:
#     print(f'You can find {animal.name} the {animal.species} in {wet_village.attraction_name}')
