
# import the modules

from colorama import *
import random

# global variables start

# dictionary of npcs Key = name values = greeting, I am statement

npcs = {"Guy": ("Greetings", "I am"), "Aldith": ("Hello", "I am"), "Rowan": ("Good morning", "I am"),
        "Borin": ("Hi", "I am"), "Pierre": ("Bonjour", "je suis"), "Dora": ("Hola", "me llamo"),
        "Emperor Chu": ("Ni hao", "Wo jao"), "not important": ("Ah", "my name is"),
        "Aleixo-Defender of man": ("Olá", "meu nome é")}

# sword dictionary Key = name values = minimum damage, maxium damage, damage multiplier

weapons = {"sword": (1, 3, 1), "fists": (0, 2, 1), "axe": (0, 3, 2), "spear": (3,4,1), "hammer": (2, 8, 1), "tentacle":(0, 1, 10)}

# boss dictionary Key = name values = description, health

bosses = {"King of bananas": ("leader of the monkeys", 5, ["finds an opening and jumps on you", "you get squashed in the process"]), "Litius": ("pincher of men", 6, ["litius opens his pincer and grabs you","you have been crushed"]), "squid": ("creater of storms", 8, ["waves his tentacle and slaps you", "you fly into the sea unconscious"])}

# inventory (starting with fists)

inventory = ["fists"]

fires_lit = 0

# global variables end

# open a file called story.txt and write in it

myfile = open("story.txt", 'w')


# myprint function (substitue print with myprint and put it into the file)

def myprint(text):
    print(text)
    print(text, file=myfile, flush=True)


# pick function for creating menus and making them idiots proof

def pick(choices):
    myprint(Fore.WHITE + Style.BRIGHT)

    # while loop to make sure you enter a valid value

    valid = False
    while valid is False:

        # printing the options to choose from

        for i, option in enumerate(choices):
            myprint(f"\t{i + 1}) {option}")

        # getting the input

        x = input("select an option?\n")

        # is the input an integer?

        try:
            x = int(x)

            # is the input in the range of choices

            if x in range(1, len(choices) + 1):
                valid = True
            # if the input isn't valid but is an integer print...
            else:
                myprint(f"{x} is not a valid option, please try again")
                x = input()

        # if the input isn't an integer print...

        except:
            myprint(f"{x} is not a number, please select the numbers not their answers.")
            x = input()

    # return what you picked from the choices

    return choices[x - 1]


# function for printing areas

def area(title, descrip):
    myprint(Style.BRIGHT)
    myprint(f'{Fore.RED}{title.upper()}')
    myprint(f' {Fore.YELLOW}{descrip}')
    x = input()


# function for printing scenes

def scene(name, descrip, options=None):
    myprint(Style.BRIGHT)
    myprint(f'{Fore.BLUE}{name}')
    x = input()
    myprint(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{descrip}')
    print(Fore.WHITE + Style.BRIGHT)
            
    # if you specified options ask the user to pick one.

    if options is not None:
        return pick(options)


# function for printing and "making" bosses
# gets the values from the bosses dictionary

def boss(bossName):
    description, health, boss_losing = bosses[bossName]
    myprint(Style.BRIGHT)
    myprint(f'{Fore.LIGHTMAGENTA_EX}{bossName.upper()}')
    myprint(f'{Fore.MAGENTA}{description} - {health}hp')
    return description, health

def boss_fight(bossName):
  description, health, boss_losing = bosses[bossName]
  boss(bossName)
  for turn in range(3):
    answer = scene("", "What weapon do you attack with?", inventory)
    min, max, multiplier = weapons[answer]
    damage = random.randint(min, max) * multiplier
    health -= damage
    if health <=0:
      health = 0
    myprint(f'you did {damage} damage to  {bossName} with {answer}\n{health}hp left')
    if health <= 0:
      break
  if health <= 0:
    
    x = input()
    myprint(f'{bossName} fell to ground, he has been defeated')
  elif health > 0:
    for msg in boss_losing:
      x=input()
      myprint(msg)
     
    return False
  return True  


   
    


def monkey_forest(name, npc, npc2):
    global fires_lit

    greeting, im = npcs[npc]
    greeting2, im2 = npcs[npc2]
    answer = scene(npc + " vanishes and you find yourself before an archway leading to a forest", "Will you enter?",
                   ["yes", "no"])
    if answer == "yes":
        myprint("you slowly walk into the forest.")
    elif answer == "no":
        myprint("You stand still at the edge of the forest thinking of how you arrived here.")
        x = input()
        myprint("You turn around to see if there is an exit")
        x = input()
        answer = scene(
            "As you walk along the dirt leading away from the forest you notice a monkey engulfed by shadow emerge infront of you.",
            "How do you react?", ["Run back to the forest", "fight the monkey head on!"])
        if answer == "fight the monkey head on!":
            myprint("the monkey is faster than usual due to it's shadowed form")
            x = input()
            myprint("It swiftly climbs onto your head and bites you in neck!")
            x = input()

            return False
        elif answer == "Run back to the forest":
            myprint("you run into the forest and hide behind a tree hoping the monkey doesn't see you")
            x = input()
            myprint("the monkey jumps back into the trees leaving you alone")
            x = input()
    area("Monkey forest", "home of monkeys")
    answer = scene("you see someone leaning against a tree 20m away from you", "will you talk to them?", ["yes", "no"])
    if answer == "yes":
        myprint(f'{greeting2} {name}, {im2} {npc2}. nice to meet you.')
        x = input()
        myprint("You will need this sword, the monkeys in this forest are very aggresive since the land was engulfed.")
        x = input()
        myprint("You carry on through the forest")
        x = input()
        inventory.append("sword")
    elif answer == "no":
        myprint("You ignore the peron and carry on through the forest")

    answer = scene("whilst you are walking through the forest 5 monkeys drop down from the trees",
                   "how can you get past",
                   ["fight the monkeys", "carry on running through the forest", "surrender to the monkeys"])
    sword = "sword" in inventory
    if answer == "fight the monkeys":
        if sword is True:
            myprint("you fight off the monkeys with your sword and carry on through the forest!")

        elif sword is False:
            myprint("the monkeys swarm you and with no way of defending yourself you die.")
            return False
    elif answer == "carry on running through the forest":
        myprint("you carry on running but another group of monkeys falls infront of you.")
        x = input()
        myprint("You run through them also like the coward you are!")
        x = input()


    elif answer == "surrender to the monkeys":
        myprint("The monkeys tie you to tree and starve you.")
        return False
    myprint("after walking through the forest you find an oppening in the trees.")
    x = input()
    myprint("you enter the clearing...")
    x = input()

    bossName = "King of bananas"
    description, health = boss(bossName)
    for turn in range(3):
        answer = scene("", "What weapon do you attack with?", inventory)
        min, max, multiplier = weapons[answer]
        damage = random.randint(min, max) * multiplier
        health -= damage
        if health <= 0:
            health = 0
        myprint(f'you did {damage} damage to  {bossName} with {answer}\n{health}hp left')
        if health <= 0:
            break
    if health <= 0:
        x = input()
        myprint(f'{bossName} fell to ground, he has been defeated')
        x = input()
        answer = scene("At the end of the clearing you see a torch with a white flame and an eternal bonfire",
                       "Do you light it?", ["yes", "no"])
        if answer == "yes":
            fires_lit += 1
            myprint("you lit the Monkey forest's flame of light!")
        elif answer == "no":
            myprint("you didn't light the fire and the monkey forest remained in shadows")
        return True
    elif health > 0:
        x = input()
        myprint("The king of bananas saw an opening and jumped on you!")
        x = input()
        myprint("you were squashed in the process")

def black_sea(name, npc, npc2):
  global fires_lit

  greeting, im = npcs[npc]
  

  myprint("you follow a path from the bonfire until you find yourself on a beach.")

  area("The BEach of insanity", "where travellers lose their minds")

  answer = scene("There is a small wooden boat on the beach", "will you sail it or explore the coast some more?", ["sail", "explore"])  
  if answer == "explore":
    myprint("you turn left and walk along the beach.")
    x=input()
    myprint("while you are exploring the beach something scuttles out of the water...")
    x=input()
    if boss_fight("Litius") is False:
      return False  
        
    answer = scene("there is someone sitting on a rock behind the crab\'s corpse", "will you talk to them?", ["yes", "no"])
    if answer == "yes":
        myprint(f'{greeting} {name}, {im} {npc}. That\'s quite the feat you achieved. Killing that giant crab.')
        x = input()
        myprint("Thanks to you I can now get to my boat and sail to the island of treasure")
        x = input()
        myprint("legend has it a great knight got lost there and never returned home...")
        x = input()
        myprint("sorry for my waffling, take this axe as a token of my gratitude!")
        inventory.append("axe")
        x=input()
        myprint(f'you run back to the boat before {npc} gets there and you sail away')
    elif answer == "no":
        myprint("You ignore the person, return back to the boat and set sail!")
  
  elif answer == "sail":
    myprint("you set sail across...")
  x=input()
  area("The black sea", "an ocean, with no forgiveness")
  answer = scene("while you are sailing you see a shark circling you in the water", "how do you fend it off", ["try and sail faster", "stab it!", "punch it's nose then set sail again"])
  if answer == "try and sail faster":
    myprint("you pick up the pace but the shark can swim fast")
    x=input()
    myprint("it leaps out of the water and swallows you whole!")
    return False
  elif answer == "stab it!":
    if "sword" in inventory or "axe" in inventory:
      myprint("you stab the shark and it dies")
      x=input()
      myprint("you carry on sailing") 
    else:
      myprint("you have nothing to stab the sword with!")
      x=input()
      myprint("the shark bit off your head")
      return False
  elif answer == "punch it's nose then set sail again":
    myprint("you stop the boat, jump out and punch the shark in the nose!")
    x=input()
    myprint("it is stunned for just enough time and you sail away from the shark")
  
  answer = scene("You see a storm on the horrizon", "where do you go?", ["divert my course south", "divert my course north", "sail into the storm"])
  if answer == "sail into the storm":
    myprint("you sail directly into the storm")
    x=input()
    myprint("in the eye you find an island")
    x=input()
    myprint("and on it...")
    x=input()
    if boss_fight("squid") is False:
      return False
    myprint("the storm faded with the squid")
    x=input()
    answer = scene("the squid left behind one of his tentacles", "do you pick it up?", ["yes", "no"])
    if answer == "yes":
      myprint("you pick up the tentacle and sail on")
      inventory.append("tentacle")
    elif answer == "no":
      myprint("you carry on with your journey!")
  if answer == "divert my course south":
    myprint("you start sailing south and then go to sleep")
    x=input()
    myprint("after all you havent slept since you arrived here!")
    x=input()
    x=input()
    myprint("you wake up and you are on an island")
    x=input()
    area("The forgotten island", "a place of tranquillity")
    x=input()
    answer = scene("there is a lady lying down on the sand", "Will you talk to her or carry on sailing to the marked location?", ["talk","keep sailing"])
    if answer == "talk":
      myprint(f' hello {name} I am Spees, from Tenebrae (the city east of here)')
      x=input()
      myprint("I came here searching for my brother.")
      x=input()
      myprint("he was a very famous knight and he always strived to be better, more powerful")
      x=input
      myprint("because of this he went searching for an island called \"treasure island\"")
      x=input()
      myprint("it is said that an anccient sword is kept there called \"The great knight sword\"")
      x=input()
      myprint("it was named after a knight who used it to fight the king of shadows and stop the age of dark 1,000 years ago")
      x=input()
      myprint("my brother wanted to fight him (the king of shadows) but he never returned from his search")
      x=input()
      myprint("that is why I am here, to look for him so he can fight the king of shadows in Umbra castle.")
      x=input()
      answer = scene("", "will you help  me find him?", ["sure", "no thanks"])
      if answer == "sure":
        myprint("Thank you!")
        x=input()
        myprint("take this spear as a gift!")
        inventory.append("spear")
        x=input()
      elif answer == "no thanks":
        myprint("ok then")
        x=input()
      myprint("you get back in your boat and start sailing towards the marked location on your map")    





def story():
    # sys.stdout = open('story.text', 'w')

    if boss_fight == False:
      area("YOU die", "umbra will remain in shadow")

    npc = random.choice(list(npcs.keys()))
    npc2 = random.choice(list(npcs.keys()))
    # npc = list(npcs.keys())[-1]

    greeting, im = npcs[npc]

    mimick1 = random.randint(1, 3)
    myprint(Style.BRIGHT)
    name = input("What is your name?\n")
    myprint(f'{greeting} {name}, {im} {npc}. Welcome to...')
    x = input()
    area("umbra", "The land of shadows")
    myprint(Fore.WHITE + "This land is plagued with the curse of the shadows.")
    x = input()
    myprint("The shadows can only be destroyed by lighting each regions flame of light.")
    x = input()
    myprint("Your journey will be cruel and unforgiving, but I trust you can cure the curse.")
    x = input()


    if monkey_forest(name, npc, npc2) is True:
      x = input()
      myprint(Fore.LIGHTYELLOW_EX + "You survived the Monkey Forest")
      myprint(Fore.WHITE + Style.BRIGHT)
      x=input()

      if black_sea(name,npc , npc2) is True:
        x=input()
        myprint(Fore.LOGHTYELLOW_EX + "You survived the black sea")

      else:
       x = input()
      area ("You died", "Umbra will remain in shadow")


    else:
      x = input()
      area("You died", "Umbra will remain in shawdow")




init()
story()
myfile.close()
