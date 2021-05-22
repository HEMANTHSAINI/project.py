 # art idea 
import random

simple = ["teddy bear", "flowers in a vase", "breakfast foods", "butterfly", "trees"]
hard = ["eyes", "ocean in a bottle", "car", "skeleton skull", "eiffel tower"]
landscape = ["waterfall", "sunset","field of flowers", "mountains", "space", "ocean", "forest"]
objects = ["cactus", "blossoms on trees", "portrait of a person", "fruit basket", "marbles"]
randoms = ["spill water, let dry and outline the shapes", "express emotions with random slashes", "pick three random colors and use your imagination", "distorted versions of nnormal things"]

print("I'm here to help you figure out an art idea!")
type1 = input("Would you like to draw or paint? ")

if type1 == "draw":
    type2 = input("Would you like to draw something simple or hard? ")

    if type2 == "simple":
        choice = random.choice(simple)
        print("Try painting: " + choice)
    elif type2 == "hard":
        choice = random.choice(hard)
        print("Try painting: " + choice)

elif type1 == "paint":
    type2 = input("Would you like to paint a landscape, an object, or random? ")

    if type2 == "landscape":
        choice = random.choice(landscape)
        print("Try painting: " + choice)
    if type2 == "object":
        choice = random.choice(objects)
        print("Try painting: " + choice)
    if type2 == "random":
        choice = random.choice(randoms)
        print("Try painting: " + choice)