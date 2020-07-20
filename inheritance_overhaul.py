from animals.walking.donkey import Donkey
from animals.walking.llama import Llama
from animals.swimming.fish import Fish
from animals.slithering.snake import Snake
from attractions.PettingZoo import PettingZoo
from attractions.SnakePit import SnakePit
from attractions.Wetlands import Wetlands

jack = Donkey('Jack', 'Irish', 'midday', 'kibles')
tina = Llama('Tina', 'Llama', 'morning', 'bits')
bruce = Snake('Bruce', 'Copperhead','mice')
gigi = Fish('Gigi', 'Clown', 'flakes')

pettingZoo = PettingZoo('Broncos Fun', 'Have a great time at the barn.')
snakePit = SnakePit('Slithering Substance', 'See the creepy crawlers')
wetlands = Wetlands('Moist place','Be immersed')

pettingZoo.addAnimals([jack, tina])
snakePit.addAnimals([bruce])
wetlands.addAnimals([gigi])