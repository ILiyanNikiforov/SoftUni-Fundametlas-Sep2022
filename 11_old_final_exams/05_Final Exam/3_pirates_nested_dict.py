targets = {}

while True:
    target = input()
    if target == "Sail":
        break

    cmd = target.split("||")
    city, population, gold = cmd[0], int(cmd[1]), int(cmd[2])

    if city not in targets.keys():
        targets[city] = {}
        targets[city]["population"] = population
        targets[city]["gold"] = gold
    else:
        targets[city]["population"] += population
        targets[city]["gold"] += gold

while True:
    current_command = input()
    if current_command == "End":
        if len(targets) > 0:
            print(f'Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:')
            for towns, people_gold in targets.items():
                print(f'{towns} -> Population: {people_gold["population"]} citizens, Gold: {people_gold["gold"]} kg')
        else:
            print('Ahoy, Captain! All targets have been plundered and destroyed!')
        break

    command = current_command.split("=>")
    town = command[1]

    if command[0] == "Plunder":
        people, gold = int(command[2]), int(command[3])
        targets[town]['population'] -= people
        targets[town]['gold'] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        if targets[town]['population'] <= 0 or targets[town]['gold'] <= 0:
            print(f'{town} has been wiped off the map!')
            del targets[town]

    elif command[0] == "Prosper":
        gold = int(command[2])
        if gold < 0:
            print(f'Gold added cannot be a negative number!')
        else:
            targets[town]['gold'] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {targets[town]["gold"]} gold.')
