from random import choice

capital = "Topeka"
bird = "Western Meadowlark"
flower = "Sunflower"
song = "Home on the range"

def randomfact():
     funFacts = [
          "kansas is considered flat,but it does have mountains.",
          "Wichita is the largest city in the state, but many would guess that it is kansas city",
          "A considerable portion of kansas city is actually in Missouri",
          "Most Kansas are annoyed by Wizard of references from outside of Kansas."
     ]

     index = choice("0123")

     print(funFacts[int(index)])


if __name__ == "__main__":
     randomfact()