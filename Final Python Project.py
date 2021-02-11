import random

IPS = {"str":10, "dex":10, "int":10, "lck":10,"AC":10,"MaxHP":10,"CHP":10} #IPS: Initial Player Stats
PS = IPS #PS - (Current) Player Stats
equipment = {"Armor":"Ragged Clothes","Weapon":"Fists","Ring":"Heirloom Ring","gold":50} #Equipment: Armor, Weapon, Ring
backpack = ["Health Potion"]
#Base Input Weapon_Name: {melee/ranged,Damage_Range,Attribute_Shift,Dictionary with stat effects}
item_types = {  #Weapons
                "Fists":{"item_type":"weapon", "dmg":"2d2"},
                "Sword":{"item_type":"weapon","dmg":"1d8","cost":12,"item_desc":"Basic melee weapon, good for slashing monsters. Deals 1d8 damage."},
                "Dagger":{"item_type":"weapon","dmg":"1d4","cost":8,"att_shift":{"dex":2}, "item_desc":"Weapon for apprentice rouges. Deals 1d4 damage and boosts dexterity by 2."},
                "Quarterstaff":{"item_type":"weapon","dmg":"1d6","cost":20,"att_shift":{"int":3},"item_desc":"Wizarding weapon for wizards. Deals 1d6 damage and boosts intelligence by 3."},
                "Executioner's Axe":{"item_type":"weapon","dmg":"1d20","cost":50,"att_shift":{"dex":-2,'str':3},"item_desc":"Abnormally large axe for executions. Handle with caution. Deals 1d20 damage and increases strength by 3, while reducing dexterity by 1."},
                "Dual Axes":{"item_type":"weapon","dmg":"2d5","cost":25,"att_shift":{'str':1,'int':-2},"item_desc":"Dually weld akes? Dualed wielded axis? Duality wueld axes? Just get out there and tear stuff up! Deals 2d6 damage and decreases intelligence by 2."},
                "Large Shield":{"item_type":"weapon","dmg":"1d4","cost":15,"att_shift":{"AC":2,'dex':-3},"item_desc":"A large shield. Good at soaking up damage. Deals 1d4 damage and gives a bonus 2 armor class at the cost of 2 dexterity."},
                "Halberd":{"item_type":"weapon","dmg":"1d10","cost":15,"att_shift":{"AC":1,'dex':-1},"item_desc":"A relic of war. Deals 1d10 damage and increases armor class by 1. Reduces dexterity by 1 given its awkward size."},
                #Potions
                "Health Potion":{"item_type":"potion","effect_type":"Instant","att_change":{"CHP":3},"cost":15,"item_def":"You feel a rush of vitality through your veins!","item_desc":"Heals 3 health on each use."},
                "Potion of giant strength":{"item_type":"potion","effect_type":"Instant","att_change":{"str":4},"cost":50,"item_def":"Everything around you feels... Weaker.","item_desc":"Increases strength by 4. Warning, does not work on sheep."},
                "Draught of Celerity":{"item_type":"potion","effect_type":"Instant","att_change":{"dex":4},"cost":20,"item_def":"Your step now feels exceptionally quick.","item_desc":"Increases dexterity by 4. Works as an energy drink as well."},
                "Potion of stone skin":{"item_type":"potion","effect_type":"Instant","att_change":{"AC":1, "dex":-1},"cost":45,"item_def":"You feel your skin harden","item_desc":"Increases armor class by 1 and decreases dexterity by 1. Good for tanking damage, not great for sprinting."},
                #Armor
                "Ragged Clothes":{"item_type":"armor","att_shift":{"AC":0},"cost":3,"item_desc":"Standard RPG starting clothes."},
                "Scale Mail":{"item_type":"armor","att_shift":{"AC":4},"cost":25,"item_desc":"Scalified mail. Like chain mail but with scales instead of metal. Armor class +4."},
                "Cloak":{"item_type":"armor","att_shift":{"AC":1,"dex":2},"cost":25,"item_desc":"A cloak that's suprisingly easy to move in. +1 Armor class. +2 Dexterity."},
                "Hide Armor":{"item_type":"armor","att_shift":{"AC":2,"dex":1},"cost":15,"item_desc":"Armor made from mountain wolf fur. +1 Armor class. +1 Dexterity."},
                "Chain Shirt":{"item_type":"armor","att_shift":{"AC":5,"dex":-1},"cost":30,"item_desc":"Plain heavy chains. Good for defense. +5 Armor Class. -1 Dexterity."},
                "Full Plate Armor":{"item_type":"armor","att_shift":{"AC":8, "dex":-3},"cost":75,"item_desc":"Extremely heavy armor. Don't try swimming in it. +8 Armor Class. -3 Dexterity."},
                "Scholarly Robes":{"item_type":"armor","att_shift":{'AC':1, "int":2},'cost':30,"item_desc":"Good for studying, not great for the battlefield. +1 Armor Class. +2 Intelligence."},
                "Merchant's Robes":{"item_type":"armor","att_shift":{'lck':5,'AC':-3},'cost':45,"item_desc":"You'll be the envy of the bazaar. If you make it back alive. +5 Luck -3 AC"},
                "Berserker's Armor":{"item_type":"armor","att_shift":{"AC":-3, "dex":1, "MaxHP":5},"cost":40,"item_desc":"Trades defense for manuverability and danger. -2 Armor Class. +1 Dexterity. +5 Max HP."},
                #Rings
                "Ring of Turtle":{"item_type":"ring","att_shift":{"AC":2,"MaxHP":5},"cost":100,"item_desc":"Grants bonus 2 Armor. Grants bonus 5 hp."},
                "Ring of Rabbit":{"item_type":"ring","att_shift":{"dex":2,"AC":-2,"MaxHP":5},"cost":100,"item_desc":"Grants bonus 2 Dexterity. Grants bonus 5 hp."},
                "Ring of Hermit":{"item_type":"ring","att_shift":{"AC":4,"dex":-4,"MaxHP":5},"cost":100,"item_desc":"Grants bonus 4 Armor. Takes away 2 Dexterity. Grants bonus 5 hp."},
                "Ring of Wolverine":{"item_type":"ring","att_shift":{"AC":1,"MaxHP":10},"cost":100,"item_desc":"Grants bonus 1 Armor. Grants bonus 10 hp."},
                "Ring of Fox":{"item_type":"ring","att_shift":{"int":2,"lck":1,"MaxHP":5},"cost":100,"item_desc":"Grants bonus 2 Intelligence and 1 Luck. Grants bonus 5 hp."},
                "Ring of Cat":{"item_type":"ring","att_shift":{"lck":3,"MaxHP":5},"cost":100,"item_desc":"Grants bonus 3 Luck. Grants bonus 5 hp."},
                "Heirloom Ring":{"item_type":"ring","att_shift":{"MaxHP":7},"cost":170,"item_desc":"Grants bonus 7 hp. May be worth selling."}
                }
death = False
game = True

print("Welcome to Enchanted: Swords and Magic. This game centers around combat and strategy.")
while True:
    print("Choose your race from this list of types:\n1. Human: Decent all around character. +1 str, dex, int, lck\n2. High Elf: Highly intelligent and agile. +2 int +2 dex\n3. Half-Orc: Maintains the intelligence of a human with the strength of an orc. +3 str +1 AC\n4. Goblin: Quick and sneaky, a bit weak though. +4 dex, -1 AC\n5. Minotaur: Great for ramming, less great for thinking. +2 str +3 AC -1 int\n6. Occulist: Cyclopses born with one eye who focused on magic instead of strength. +3 int +1 lck")
    race = input()
    if race == "1":
        IPS['str'] += 1
        IPS['dex'] += 1
        IPS['int'] += 1
        IPS['lck'] += 1
        print("You've chosen the Human!")
        break
    elif race == '2':
        IPS['int'] += 2
        IPS['dex'] += 2
        print("You've chosen the High Elf!")
        break
    elif race == '3':
        IPS['str'] += 3
        IPS['AC'] += 1
        print("You've chosen the Half-Orc!")
        break
    elif race == '4':
        IPS['dex'] += 4
        IPS['AC'] -= 1
        print("You've chosen the Goblin!")
        break
    elif race == '5':
        IPS['str'] += 2
        IPS['int'] -= 1
        IPS['AC'] += 3
        print("You've chosen the Minotaur!")
        break
    elif race == '6':
        IPS['int'] += 3
        IPS['lck'] += 1
        print("You've chosen the Occulist!")
        break
    else:
      input("Sorry, invalid player type. (Be sure to type a number from 1-6)")

print("Your journey to gain gold, strength, and fortune starts now!\nHere are a few tips to get started:")
input("All stats if high or low enough are assigned 'modifier' scores. These range from boosting your damage in combat with strength, or recieving more gold from killing monsters with luck.")
input("Characters do not autoheal after combat. You must raise funds to buy health potions, or just not get hit.\nAlso, don't be afraid to run from combat, if you're fast, you won't lose any gold.")
input("Vanquish the 3 bosses in the game to win. The 'Jester', The 'Amethyst Dragon', and The 'Sleeping Giant'.")
input("And that's about it, there may be some more hidden features inside the game or loopholes, but just make sure to have fun and become 'Enchanted'!")
input("{Heirloom ring added to inventory}\n{Health Potion added to inventory}\n{Ragged Clothes added to inventory}\n")
def equip(item):
    global equipment
    global item_types
    global IPS

    if 'att_shift' in item_types[item]:
        for i in item_types[item]['att_shift']:
            IPS[i] += item_types[item]['att_shift'][i]
            if i == 'MaxHP':
                PS['CHP'] += item_types[item]['att_shift'][i]
equip("Heirloom Ring")

def de_equip(item):
    global equipment
    global item_types
    global IPS

    if 'att_shift' in item_types[item]:
        for i in item_types[item]['att_shift']:
            IPS[i] -= item_types[item]['att_shift'][i]
            if i == 'MaxHP':
                PS['CHP'] -= item_types[item]['att_shift'][i]
            
def dz0(dienum,t=False):#A play on classic d20, dz0 is a function that takes in string based a d20number and converts it into its final value. (ex. 1d20 = 1 to 20)
    num1 = []
    num2 = []
    iterations = ''
    max_num = ''
    final_num = 0
    for i in dienum:
        c = 0
        if not i == 'd':
            num1.append(i)
        else:
            break
        c += 1
    for i in range(len(num1)+1,len(dienum)):
        num2.append(dienum[i])
    for i in num1:
        iterations += i
    for i in num2:
        max_num += i
    iterations = int(iterations)
    max_num = int(max_num)
    for i in range(0,iterations):
        final_num += random.randint(1,max_num)
    if t:
        print(
          "  _________"+
        "\n /________/|"+
        "\n |        ||"+
        "\n |    "+str(final_num)+"   ||"+
        "\n |________|/")
    return final_num
def print_dice(num):
    print(
          "  _________"+
        "\n /________/|"+
        "\n |        ||"+
        "\n |    "+str(num)+"   ||"+
        "\n |________|/"
            )
def update_cps():
    global PS
    global IPS
    PS['dex'] = IPS['dex']
    PS['str'] = IPS['str']
    PS['int'] = IPS['int']
    PS['lck'] = IPS['lck']
    if PS['dex']<=1:
        PS['dex'] = 1
    if IPS['dex']<=1:
        IPS['dex'] = 1
    
def dice(maxnum, minnum=1,check=False,vs=0,mod=0,e=False):#Prints dice text art with a number, or returns true or false depending on the value of check and vs, takes in a minimum and maximum roll
    number = random.randint(minnum,maxnum)
    die =(
    "  _________"+
    "\n /________/|"+
    "\n |        ||"+
    "\n |    "+str(number)+"   ||"+
    "\n |________|/")
    if check == True:
        if e == False:
            if number+mod>vs:
                print("The task suceeds. " + str(number)+"+"+str(mod) + " vs " + str(vs)+'.')
                return True
            else:
                print("The task fails. " + str(number-1)+"+"+str(mod)+ " vs " + str(vs)+'.') #Basically negates ties
                return False
        if e == True:
            if number+mod>vs:
                print("The enemy is successful! " + str(number)+"+"+str(mod) + " vs " + str(vs)+'.')
                return True
            else:
                print("The enemy fails!" + str(number-1)+"+"+str(mod)+ " vs " + str(vs)+'.') #Basically negates ties
                return False
    else:
        print(die)

def main_c():#Main menu choice
    global game
    while True:
        a = input("1. Battle vs. Random monster\n2. Go to the shop\n3. View equipment/Player stats\n4. Use items\n5. Exit\n")
        if (a == '1') or (a == '2') or (a == '3') or (a == '4') or (a == '5'):
            return a
        else:
            print("Invalid Input.")
def modifier(stat):#Bonus points for high stats with negatives for low stats
    modif = 0
    if stat<=1:
        modif = -5
    elif 2<=stat<=3:
        modif = -4
    elif 4<=stat<=5:
        modif = -3
    elif 6<=stat<=7:
        modif = -2
    elif 8<=stat<=9:
        modif = -1
    elif 10<=stat<=11:
        modif = 0
    elif 12<=stat<=13:
        modif = 1
    elif 14<=stat<=15:
        modif = 2
    elif 16<=stat<=17:
        modif = 3
    elif 18<=stat<=19:
        modif = 4
    elif 20<=stat<=21:
        modif = 5
    elif 22<=stat<=23:
        modif = 6
    elif 24<=stat<=25:
        modif = 7
    elif 26<=stat<=27:
        modif = 8
    elif 28<=stat<=29:
        modif = 9
    elif 30<=stat:
        modif = 10
    return modif
def battle():
    global IPS
    global PS
    global equipment
    global item_types
    global backpack
    global death

    update_cps()
    
    if PS['CHP'] > PS["MaxHP"]:
        PS['CHP'] = PS["MaxHP"]
    
    #Monsters have key names:{armor_class, health, speed, gold drop, (thorns?,thorn_dmg), [battlemove1, battlemove2, battlemove(i)]}
    monster_types = {"Giant Rat":{"armor_class":10,"health":dz0("1d6")+3,"speed":8,"gold_drop":dz0('1d4'),"moveset":["rat_bite"]},
                     "Orc Bandit":{"armor_class":12, "health":dz0('1d5')+9, "speed":10,"gold_drop":dz0('2d10'),"moveset":["orc_bash","orc_bandit_block"]},
                     "Wolf":{"dmg_mod":0,"armor_class":11, "health":dz0("2d2")+3, "speed":14,"gold_drop":dz0('2d5'),"moveset":["howl","wolf_bite","wolf_bite","wolf_bite"]},
                     "Stone Golem":{"armor_class":14, "health":dz0('3d5')+20, "speed":8,"gold_drop":dz0('2d12'),"moveset":["golem_slam","golem_stoneskin","golem_recovery","golem_slam","golem_slam","golem_slam"]},
                     "Wind Sprite":{"armor_class":16, "health":dz0('5d2'), "speed":14, "gold_drop":dz0('1d20'),"moveset":["windsprite_speedup","windsprite_attack"]},
                     "Mind Eater":{"armor_class":11,"health":dz0("3d6"),"speed":12,"gold_drop":dz0('5d4'),"moveset":["mind_rot","dream_eat","brain_blast"]},
                     "Living Armor":{"armor_class":20,"health":dz0("3d6")+10,"speed":10,"gold_drop":dz0('5d9'),"moveset":["slam"]},
                     "Golden Scarab":{"armor_class":14,"health":dz0("2d6")+10,"speed":14,"gold_drop":70,"moveset":["bug_buzz"]},
                     "Sleeping Giant":{"armor_class":9,"health":dz0("4d10")+30,"speed":6,"gold_drop":dz0('20d4'),"moveset":["body_slam","sleep","sleep","sleep","sleep"]},
                     "Amethyst Dragon":{"armor_class":0,"health":dz0("6d5")+20,"speed":16,"gold_drop":dz0('15d10'),"moveset":["dragon_slash","dragon_slash","crystalize"]},
                     "Jester":{"armor_class":12,"health":30,"speed":30,"gold_drop":dz0('10d5'),"moveset":["double_slash","double_slash","double_slash","acrobatics"]}
                    }
    #Monsters spawn in different areas randomly, but you can choose which area to travel
    forest = ['Giant Rat',"Wolf","Orc Bandit"]
    city = ['Stone Golem', "Mind Eater"]
    temple = ['Wind Sprite',"Golden Scarab","Living Armor"]
    
    #The Sleeping giant attacks, then sleeps for 4 turns while recovering health.
    #The Amethyst Dragon starts at 0 AC, then raises every 2 turns as it recovers its scales.
    #The Jester has extremely high speed and attack with a low armor stat, he debuffs AC with acrobatics.
    bosses = ["Sleeping Giant","Amethyst Dragon","Jester"]
    #Enemy moves have a key name: [attack type, modifier, damage_roll,definition]
    enemy_moves = {"rat_bite":{"atk_type":"melee","atk_modif":-2,"e_dmg":"1d3","atk_def":"The rat bites down hard on your exposed foot!"},
                   "orc_bash":{"atk_type":"melee","atk_modif":3,"e_dmg":"1d10","atk_def":"The orc bandit bashes your body with a clobbering blow!"},
                   "orc_bandit_block":{"atk_type":"status_self","atk_duration":1,"status_type":"armor_class","modifier":5,"atk_def":"The bandit raises his buckler and takes a defensive stance. \nOrc Bandit's Armor Class rises!"},
                   "wolf_bite":{"atk_type":"melee","atk_modif":0,"e_dmg":"2d3","atk_def":"The wolf bites viciously into your arm!"},
                   "howl":{"atk_type":"status_self","atk_duration":2,"status_type":"dmg_mod","modifier":2,"atk_def":"The wolf howls, and begins to foam at the mouth!\nWolf's damage is raised!"},
                   "golem_slam":{"atk_type":"melee","atk_modif":-5,"e_dmg":"2d10","atk_def":"The golem bludgeons your body with its large arms..."},
                   "golem_stoneskin":{"atk_type":"status_self","atk_duration":2,"status_type":"armor_class","modifier":10,"atk_def":"The golem's rocky exterior appears to glow a deep gray. \nStone Golem's Armor Class rises!"},
                   "golem_recovery":{"atk_type":"status_self","atk_duration":3,"status_type":"speed","modifier":-3,"atk_def":"The golem's movements begin to slow.. \nStone Golem's speed falls"},
                   "windsprite_speedup":{"atk_type":"status_self","atk_duration":10,"status_type":"speed","modifier":2,"atk_def":"The wind sprite's speed rises!"},
                   "windsprite_attack":{"atk_type":"melee","atk_modif":6,"e_dmg":"1d2","atk_def":"The wind sprite's sand swirls then strikes you!"},
                   "mind_rot":{"atk_type":"p_debuff","atk_duration":3,"status_type":"int","modifier":-2,"atk_def":"You feel the Mind Eater generate an aching pain in your head!\nPlayer Intelligence lowered!"},
                   "dream_eat":{"atk_type":"perm_boost","status_type":"health","modifier":2,"atk_def":"The mind eater starts to eat away at your subconscious.\nMind  Eater health increased!"},
                   "brain_blast":{"atk_type":"perm_debuff","status_type":"MaxHP","modifier":-1,"atk_def":"You hear a sickening crunch from  your temple!\nPlayer Maximum HP permanently lowered!"},
                   "body_slam":{"atk_type":"melee","atk_modif":5,"e_dmg":"2d20","atk_def":"The Sleeping Giant wakes up, and rolls over!"},
                   "sleep":{"atk_type":"perm_boost","status_type":"health","modifier":5,"atk_def":"The giant snores...\nSleeping Giant health increased!"},
                   "crystalize":{"atk_type":"perm_boost","status_type":"armor_class","modifier":2,"atk_def":"The dragon's scales shift, revealing a deeper layer of carapace.\nAmethyst Dragon armor class increased!"},
                   "dragon_slash":{"atk_type":"melee","atk_modif":9,"e_dmg":"4d5","atk_def":"The dragon swipes at you with all 4 of its claws!"},
                   "double_slash":{"atk_type":"melee","atk_modif":6,"e_dmg":"2d10","atk_def":"The Jester quickly slices you twice with his daggers!"},
                   "acrobatics":{"atk_type":"status_self","atk_duration":3,"status_type":"armor_class","modifier":5,"atk_def":"The Jester begins to flip and turn!\nJester's speed is raised!"},
                   "slam":{"atk_type":"melee","atk_modif":0,"e_dmg":"2d4","atk_def":"The armor creaks, then uses its hands to strike you!"},
                   "bug_buzz":{"atk_type":"melee","atk_modif":-5,"e_dmg":"1d30","atk_def":"The scarab glitters, then flies into your spine!"}
                  }
    #Player moves have a key name: [attack type, attack modifier,attack definition]
    current_player_moves = {"strike":{"move_type":"melee","dmg_mod":0,"atk_modif":0,'atk_def':"Strikes the target with considerable power."},
                            "soul sacrifice":{"move_type":"enchantment",'atk_def':"Increase your main stats at the cost of 5 HP"},
                            "magic missle":{"move_type":"magic",'atk_def':"Shoot off missles based on your intelligence."},
                            "field bandages":{"move_type":"heal",'atk_def':"Crudely bandage your wounds."}
                            }
    while True:
        area = input("Which area would you like to travel?\n1. Forest\n2. City\n3. Temple\n4. Boss arena\n")
        if area == '1':
            enemy_index = random.choice(forest)
            input("Travelling to the Forest...")
            break
        elif area == '2':
            enemy_index = random.choice(city)
            input("Travelling to the City...")
            break
        elif area == '3':
            enemy_index = random.choice(temple)
            input("Travelling to the Temple...")
            break
        elif area == '4':
            enemy_index = random.choice(bosses)
            input("Travelling to the Boss Arena...")
            break
        else:
            print("Invalid Input.")
    
    enemy_name = enemy_index
    enemy = (monster_types[enemy_index])
    enemy_speed = monster_types[enemy_name]["speed"]
    player_speed = PS["dex"]
    enemy_effects = []
    player_effects = []
    
    turn = 'Player'
    b_loop = True
    win = "Neither yet"
    
    if player_speed > enemy_speed:
        turn = "Player"
        p = 1
        e = enemy_speed/player_speed
        gspeed = "Player"
    elif player_speed < enemy_speed:
        turn = "Enemy"
        e = 1
        p = player_speed/enemy_speed
        gspeed = "Enemy"
    else:
        r = random.randint(0,1)
        if r == 0:
            turn = "Player"
            p = 1
            e = 1
        else:
            turn = "Enemy"
            p = 1
            e = 1

    p_turn_c = p
    e_turn_c = e
    enemy_m = 0
    turn_counter = 0

    speed_update = False
    while b_loop:#b_loop: Battle loop
        if PS['dex']<=1:
            PS['dex'] = 1
        if IPS['dex']<=1:
            IPS['dex'] = 1
        if PS['CHP']>PS['MaxHP']:
            PS['CHP']= PS['MaxHP']
        if speed_update:
            enemy_speed = monster_types[enemy_name]["speed"]
            player_speed = PS["dex"]
            if player_speed > enemy_speed:
                turn = "Player"
                p = 1
                e = enemy_speed/player_speed
                gspeed = "Player"
            elif player_speed < enemy_speed:
                turn = "Enemy"
                e = 1
                p = player_speed/enemy_speed
                gspeed = "Enemy"
            else:
                r = random.randint(0,1)
                if r == 0:
                    turn = "Player"
                    p = 1
                    e = 1
                else:
                    turn = "Enemy"
                    p = 1
                    e = 1
            speed_update = False
        print("Turn: "+turn)
        if turn == 'Player':
            while turn == 'Player':
                                
                print("Player Health: "+str(PS["CHP"])+"/"+str(PS["MaxHP"]))
                print("Weapon: "+ str(equipment["Weapon"]))
                print("Enemy's Name: "+str(enemy_name) +"\nEnemy's Health: "+ str(enemy["health"]))
                a = input("1. Use a move.\n2. Use item/items.\n3. View Player Information\n4. Run away.\n")
                if a == '1':
                    while True:
                        print("1. Strike\n2. Soul Sacrifice\n3. Magic Missile\n4. Field Bandages")
                        b = input("Which move to use?\n")
                        if b == '1':
                            if dice(20,1,True,enemy["armor_class"],modifier(PS["str"]+current_player_moves['strike']['atk_modif'])):
                                temp_dmg = dz0(item_types[equipment["Weapon"]]["dmg"])
                                print_dice(temp_dmg)
                                enemy["health"] -= temp_dmg
                                print("Dealt ("+str(temp_dmg)+") damage with strike.")
                                break
                            else:
                                print("Attack Blocked by the "+enemy_name)
                                break
                        elif b == '2':
                            while True:
                                a = input("Which stat to modify?\n(str, dex, or int)")
                                if a == 'dex':
                                    PS[a] += 2
                                    PS['CHP'] -= 5
                                    print("The power of speed swells in your veins...\nYour heartbeat slows...")
                                    speed_update = True
                                    break
                                elif a == 'str':
                                    PS[a] += 2
                                    PS['CHP'] -= 5
                                    print("Your muscles are emboldened...\nYour heartbeat slows...")
                                    break
                                elif a == 'int':
                                    PS[a] += 2
                                    PS['CHP'] -= 5
                                    print("Your senses are awakened...\nYour heartbeat slows...")
                                    break
                                else:
                                    print("Invalid Input")
                            break
                        elif b == '3':
                            if PS['int'] < 0:
                                    print("Your head throbs, maybe try reading some more books...")
                                    break
                            else:
                                if dice(20,1,True,enemy["armor_class"]):
                                    temp_dmg = dz0(str(modifier(PS["int"]))+'d5')
                                    print_dice(temp_dmg)
                                    enemy["health"] -= temp_dmg
                                    print("Dealt ("+str(temp_dmg)+") damage with magic missle!")
                                    break
                                else:
                                    print("Attack Blocked by the "+enemy_name)
                                    break
                        elif b == '4':
                            temp_heals = 5 + modifier(PS["int"])
                            print("Upon patching yourself up you've recovered ("+str(temp_heals)+") health.")
                            PS['CHP'] += temp_heals
                            if PS['CHP'] > PS["MaxHP"]:
                                PS['CHP'] = PS["MaxHP"]
                            break
                        else:
                            print("Unknown Input.")
                    break
                if a == '2':
                    new_backpack = []
                    if len(backpack) <= 0:
                        input("{ Backpack is empty }")
                    else:
                        for i in range(0, len(backpack)):
                            print(str(i+1)+"."+backpack[i])
                        while True:
                            if len(backpack) <= 0:
                                input("{ Backpack is now empty }")
                                break
                            print("Type the same number twice in order to use a single item.")
                            c = input("Type the low bound of the items you want to use.\n('exit' to return to main loop)\n")
                            if c == 'exit':
                                input("Exiting item loop...")
                                break
                            d = input("Type the high bound of the items you want to use.\n('exit' to return to main loop)\n")
                            if d == 'exit':
                                input("Exiting item loop...")
                                break
                            if c == d:
                                try:
                                    c = int(c)-1
                                    if c in range(0,len(backpack)):
                                        for f in item_types[backpack[c]]["att_change"]:
                                            print(PS[f])
                                            print(item_types[backpack[c]]["att_change"][f])
                                            PS[f] += item_types[backpack[c]]["att_change"][f]
                                        print(item_types[backpack[c]]["item_def"])
                                        backpack.pop(c)
                                        break
                                    else:
                                        input("Item index out of range.")
                                except ValueError:
                                    input("Item doesn't exist in backpack.")
                            else:
                                try:
                                    c = int(c)-1
                                    d = int(d)-1
                                    if d <= len(backpack):
                                        if c >= 0:
                                            for items in range(c,d+1):
                                                print("Itemsvalue: "+str(items))
                                                for f in item_types[backpack[items]]["att_change"]:
                                                    PS[f] += item_types[backpack[items]]["att_change"][f]
                                                print(item_types[backpack[items]]["item_def"])
                                            for items in range(c,d+1):
                                                backpack[items] = ""
                                            for not_used in backpack:
                                                if not_used != "":
                                                    print("Not used item: "+str(not_used))
                                                    new_backpack.append(not_used)
                                            backpack = new_backpack
                                        else:
                                            input("Lower bound item index out of range.")
                                    else:
                                        input("Higher bound item index out of range.")
                                except ValueError:
                                    input("Invalid Input.")
                            
                    if PS['CHP'] > PS["MaxHP"]:
                        PS['CHP'] = PS["MaxHP"]
                if a == '3':
                    print("Player Stats: \nStrength: "+str(PS["str"])+" Modifier: ("+str(modifier(PS['str']))+')'+
                          "\nDexterity: "+str(PS['dex'])+" Modifier: ("+str(modifier(PS['dex']))+')'+
                          "\nIntelligence: "+str(PS["int"])+" Modifier: ("+str(modifier(PS['int']))+')'+
                          "\nLuck: "+str(PS["lck"])+" Modifier: ("+str(modifier(PS['lck']))+')'
                          )
                    print("Armor Class: "+str(PS["AC"])+"\nHealth: " + str(PS["CHP"])+"\nGold: "+str(equipment["gold"])+"\nBackpack Contents:")
                    print("Weapon: "+str(equipment['Weapon'])+"\nArmor: "+str(equipment['Armor'])+"\nRing: "+str(equipment['Ring']))
                if a == '4':
                    if PS['dex']>enemy["speed"]:
                        input("You manage to escape unscathed...")
                        b_loop = False
                        break
                    else:
                        if dice(20,1,True,10):
                            input("You manage to escape unscathed...")
                            b_loop = False
                            break
                        else:
                            escape_drop = equipment['gold']/2
                            input("You tried to escape, but instead you dropped "+str(escape_drop)+" gold.")
                            equipment['gold'] -= escape_drop
        if turn == "Enemy":
            if enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["atk_type"] == "melee":
                if dice(20,1,True,PS["AC"]+modifier(PS['dex']),enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["atk_modif"],True):
                    try:
                        temp_dmg = dz0(enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["e_dmg"])+enemy["dmg_mod"]
                        print_dice(temp_dmg)
                        PS["CHP"] -= temp_dmg
                    except KeyError:
                        temp_dmg = dz0(enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["e_dmg"])
                        print_dice(temp_dmg)
                        PS["CHP"] -= temp_dmg
                    print(str(enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["atk_def"]) + " The enemy has dealt ("+str(temp_dmg)+") damage.")
                else:
                    print("You manage to deflect the blow.")

            if enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["atk_type"] == "status_self":
                enemy_effects.append([enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["status_type"],enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["modifier"],enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["atk_duration"]])                
                enemy[enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["status_type"]] += enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["modifier"]
                if enemy[enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["status_type"]] == "speed":
                    speed_update = True
                    print("Updating speed")
                print(enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["atk_def"])
                
            if enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["atk_type"] == "p_debuff":
                player_effects.append([enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["status_type"],enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["modifier"],enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["atk_duration"]])                
                PS[enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["status_type"]] += enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["modifier"]
                if PS[enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["status_type"]] == "speed":
                    speed_update = True
                    print("Updating speed")
                print(enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["atk_def"])
                
            if enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["atk_type"] == "perm_boost":                
                enemy[enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["status_type"]] += enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["modifier"]
                if enemy[enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["status_type"]] == "speed":
                    speed_update = True
                    print("Updating speed")
                print(enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["atk_def"])
                
            if enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["atk_type"] == "perm_debuff":                
                IPS[enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["status_type"]] += enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["modifier"]
                if IPS[enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["status_type"]] == "speed":
                    speed_update = True
                    print("Updating speed")
                print(enemy_moves[monster_types[enemy_name]["moveset"][enemy_m]]["atk_def"])

        if enemy_m >= len(monster_types[enemy_name]["moveset"])-1:
            enemy_m = 0
        else:
            enemy_m += 1
        if len(enemy_effects)>0:
            c = 0
            for i in enemy_effects:
                if i[2]>0:
                    i[2] -= 1
                else:
                    enemy[i[0]] -= i[1]
                    enemy_effects.pop(c)
                c += 1
        if len(player_effects)>0:
            c = 0
            for i in player_effects:
                if i[2]>0:
                    i[2] -= 1
                else:
                    PS[i[0]] -= i[1]
                    player_effects.pop(c)
                c += 1
        if p == e:
            if turn == "Player":
                turn = "Enemy"
            else:
                turn = "Player"
        else:
            if gspeed == "Player":
                turn = "Player"
                if e_turn_c >= 1:
                    turn = "Enemy"
                    e_turn_c -= 1
                else:
                    e_turn_c += e
            else:
                turn = "Enemy"
                if p_turn_c >= 1:
                    turn = "Player"
                    p_turn_c -= 1
                else:
                    p_turn_c += p
        turn_counter += 1
        if enemy["health"] <= 0:
            win = "Player"
            break
        if PS["CHP"] <= 0:
            win = "Enemy"
            break
    if win == "Player":
        print("You win!")
        gold = monster_types[enemy_name]["gold_drop"]*(IPS['lck']/10)
        print("Gold Earned: " + str(gold))
        equipment["gold"] += gold
        if enemy_name in bosses:
            bosses.pop(enemy_name)
            print("You have successfully defeated "+str(3-len(bosses))+" boss(es)!")
        if len(bosses) == 0:
            input("The ground shakes beneath your feet.\nAfter defeating all the bosses, you have successfully vanquished all the evil from this world!\nGAME WIN!")
            death = True
    elif win == "Enemy":
        print("You've died.")
        input("Game Over.")
        death = True
def shop():
    global item_types
    global backpack
    global PS
    global item_types
    global equipment
    
    shop_items = []
    for i in item_types:
        if i != 'Fists':
            shop_items.append(i)
    print("Shopkeep: Hey there! Ready to buy something?\nItems for Sale:")
    print("Player Gold: " + str(equipment['gold']))
    for i in shop_items:
        print(i+" \n  Cost: "+str(item_types[i]['cost']))
        print('  Item Description: '+ item_types[i]['item_desc'])
    while True:
        item = input("Shopkeep: What would you like to buy?(type 'exit' to leave the shop)\n")
        if item == 'exit':
            break
        if item in shop_items:
            if item_types[item]['cost']<= equipment['gold']:
                if item_types[item]["item_type"] == 'weapon':
                    equipment['gold'] -= item_types[item]['cost']
                    print("Shopkeep: Thanks for the purchase!")
                    if equipment['Weapon'] != 'Fists':
                        print("Shopkeep: We've also bought back your old weapon!")
                        print("Gold added: "+str(item_types[equipment['Weapon']]['cost']))
                        equipment['gold'] += item_types[equipment['Weapon']]['cost']
                    de_equip(equipment['Weapon'])
                    equipment['Weapon'] = item
                    equip(equipment['Weapon'])
                    print("Remaining Gold: "+str(equipment['gold']))
                elif (item_types[item]["item_type"] == "potion"):
                    while True:
                        quantity = input("Shopkeep: How many would you like to buy?\n(type 'exit' to buy something else)\n")
                        if quantity == 'exit':
                            break
                        try:
                            quantity = int(quantity)
                            if quantity > 0:
                                if equipment['gold'] > (item_types[item]['cost']*quantity):
                                    for p in range(0,quantity):
                                        equipment['gold'] -= item_types[item]['cost']
                                        backpack.append(item)
                                    print("Shopkeep: Thanks for the purchase!")
                                    print("Remaining Gold: "+str(equipment['gold']))
                                    break
                                else:
                                    print("Shopkeep: Sorry, this isn't a charity!")
                            else:
                                print("Invalid quantity.")
                        except TypeError:
                            print("Invalid quantity.")
                elif item_types[item]["item_type"] == 'armor':
                    equipment['gold'] -= item_types[item]['cost']
                    print("Shopkeep: Thanks for the purchase!")
                    print("Shopkeep: We've also bought back your old armor!")
                    print("Gold added: "+str(item_types[equipment['Armor']]['cost']))
                    equipment['gold'] += item_types[equipment['Armor']]['cost']
                    de_equip(equipment['Armor'])
                    equipment['Armor'] = item
                    equip(equipment['Armor'])
                    print("Remaining Gold: "+str(equipment['gold']))
                    
                elif item_types[item]["item_type"] == 'ring':
                    equipment['gold'] -= item_types[item]['cost']
                    print("Shopkeep: Thanks for the purchase!")
                    print("Shopkeep: We've also bought back your old ring!")
                    print("Gold added: "+str(item_types[equipment['Ring']]['cost']))
                    equipment['gold'] += item_types[equipment['Ring']]['cost']
                    de_equip(equipment['Ring'])
                    equipment['Ring'] = item
                    equip(equipment['Ring'])
                    print("Remaining Gold: "+str(equipment['gold']))
            else:
                input("Shopkeep: Sorry, you don't have enough money for that...")
        else:
            print("Shopkeep: Sorry, we don't have that item right now.")
    input("Shopkeep: See you later!")
    
def boss_battle():
    pass
def equipment_view():
    print("Player Stats: \nStrength: "+str(IPS["str"])+" Modifier: ("+str(modifier(IPS['str']))+')'+
          "\nDexterity: "+str(IPS['dex'])+" Modifier: ("+str(modifier(IPS['dex']))+')'+
          "\nIntelligence: "+str(IPS["int"])+" Modifier: ("+str(modifier(IPS['int']))+')'+
          "\nLuck: "+str(IPS["lck"])+" Modifier: ("+str(modifier(IPS['lck']))+')'
          )
    print("Armor Class: "+str(IPS["AC"])+"\nHealth: " + str(PS["CHP"])+"/"+str(PS["MaxHP"])+"\nGold: "+str(equipment["gold"])+"\nBackpack Contents:")
    print("  Weapon: "+str(equipment['Weapon'])+"\n  Armor: "+str(equipment['Armor'])+"\n  Ring: "+str(equipment['Ring']))
    if len(backpack) <= 0:
        input("{ Backpack is empty }")
    else:
        print("  Potions:")
        for i in backpack:
            print("    "+str(i))
        print('')
def use_items():
    global backpack
    global IPS
    global PS
    global item_types
    
    new_backpack = []
    if len(backpack) <= 0:
        input("{ No potions availible! }")
    else:
        for i in range(0, len(backpack)):
            print(str(i+1)+"."+backpack[i])
        while True:
            if len(backpack) <= 0:
                input("{ Backpack is now empty }")
                break
            print("Type the same number twice in order to use a single item.")
            c = input("Type the low bound of the items you want to use.\n('exit' to return to main loop)\n")
            if c == 'exit':
                input("Exiting item loop...")
                break
            d = input("Type the high bound of the items you want to use.\n('exit' to return to main loop)\n")
            if d == 'exit':
                input("Exiting item loop...")
                break
            if c == d:
                try:
                    c = int(c)-1
                    if c in range(0,len(backpack)):
                        for f in item_types[backpack[c]]["att_change"]:
                            print(PS[f])
                            print(item_types[backpack[c]]["att_change"][f])
                            PS[f] += item_types[backpack[c]]["att_change"][f]
                        print(item_types[backpack[c]]["item_def"])
                        backpack.pop(c)
                        break
                    else:
                        input("Item index out of range.")
                except ValueError:
                    input("Item doesn't exist in backpack.")
            else:
                try:
                    c = int(c)-1
                    d = int(d)-1
                    if d <= len(backpack):
                        if c >= 0:
                            for items in range(c,d+1):
                                print("Itemsvalue: "+str(items))
                                for f in item_types[backpack[items]]["att_change"]:
                                    PS[f] += item_types[backpack[items]]["att_change"][f]
                                print(item_types[backpack[items]]["item_def"])
                            for items in range(c,d+1):
                                backpack[items] = ""
                            for not_used in backpack:
                                if not_used != "":
                                    print("Not used item: "+str(not_used))
                                    new_backpack.append(not_used)
                            backpack = new_backpack
                        else:
                            input("Lower bound item index out of range.")
                    else:
                        input("Higher bound item index out of range.")
                except ValueError:
                    input("Invalid Input.")
            
    if PS['CHP'] > PS["MaxHP"]:
        PS['CHP'] = PS["MaxHP"]

while not death:
    update_cps()
    choice = main_c()
    if choice == '1':
        battle()
    elif choice == '2':
        shop()
    elif choice == '3':
        equipment_view()
    elif choice == '4':
        use_items()
    elif choice == '5':
        l = input("Are you sure? ('Y' to exit)")
        if l == 'Y':
            input("See you later!")
            break
        else:
            print("Alright!")
    else:
        print("Invalid Input.")
