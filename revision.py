import json

default_data = {
    "counter": 0,
    "logs": []
}


def get_base():
    try:
        with open("counter.json") as counter_file:
            return json.loads(counter_file.read())
    except FileNotFoundError as err:
        return default_data
    except ValueError as err:
        return default_data

def save_base(counter_number, base):
    base["counter"] = counter_number
    base["logs"].append(counter_number)
    
    with open("counter.json", "w") as counter_file:
        counter_file.write(json.dumps(base, indent=4))

def counter(base, to_add):
    return base + to_add

base = get_base()

print(base)
while True:
    number = int(input("add number\n"))
    counter_number = counter(base["counter"], number)

    print("New number is ", base)
    save_base(counter_number, base)