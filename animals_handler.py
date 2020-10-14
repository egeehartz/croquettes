from petting import Llama, Goat, Alpaca, Pony, Pig
from pond import Tadpole, Goldfish, Mallard, Goose, Frog
from tank import Snake, Turtle, Lizard, Viper, Boa
from attractions import PettingZoo


varmint_village = PettingZoo("Varmint Village")

############

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow" )
# print(miss_fuzz.feed())
mr_fuzz = Goat("Mister Fuzz", "mountain goat", "morning", "Goat Chow")
# print(mr_fuzz.feed())
baby_fuzz = Alpaca("Baby Fuzz", "domestic alpaca", "morning", "Alpaca Chow")
# print(baby_fuzz.feed())
fancy_fuzz = Pony("Fancy Fuzz", "miniature horse", "morning", "Pony Chow")
# print(fancy_fuzz.feed())
oink_fuzz = Pig("Oink Fuzz", "domestic pig", "morning", "Pig Chow")
#print(oink_fuzz.feed())

varmint_village.animals.append(miss_fuzz)
varmint_village.animals.append(mr_fuzz)
varmint_village.animals.append(baby_fuzz)


##########


sneky = Snake("Sneky", "copperhead", "morning", "Snake Chow")
print(sneky)
squirt = Turtle("Squirt", "turtle", "morning", "Turtle Chow")
# print(squirt.feed())
lizzie = Lizard("Lizzie", "lizard", "morning", "Lizard Chow")
# print(lizzie.feed())
veep = Viper("Veep", "viper", "morning", "Pig Chow")
# print(veep.feed())
boaz = Boa("Boaz", "boa constrictor", "morning", "Boa Chow")
# print(boaz.feed())


###############


thad = Tadpole("Thad", "frog", "morning", "Snake Chow")
# print(thad.feed())
nemo = Goldfish("Nemo", "fish", "morning", "Snake Chow")
# print(nemo.feed())
mallory = Mallard("Mallory", "duck", "morning", "Snake Chow")
# print(mallory.feed())
bonkers = Goose("Bonkers", "goose", "morning", "Snake Chow")
# print(bonkers.feed())
froggie = Frog("Froggie", "Frog", "morning", "Snake Chow")
# print(froggie.feed())

################

for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')