def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, start=1):
        print(f"{i}. {dwarf}")

def summon_captain_planet(fruits):
    return [fruit.capitalize() + '!' for fruit in fruits]

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

def find_the_cheese(cheeses):
    cheese_types = ["cheddar", "gouda", "brie"]  
    for cheese in cheeses:
        if cheese in cheese_types:
            return cheese
    return None
