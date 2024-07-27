

import pandas as pd

move_file = 'moves.csv'
moves_df = pd.read_csv(move_file)


file_content = f"""class Move:
    def __init__(self, pokemon, category, name, desc, move_type, power, accuracy, pp):
        self.pokemon = pokemon
        self.category = category
        self.name = name
        self.desc = desc
        self.move_type = move_type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp

    def use(self, actor, target):
        pass

move_dict = {{}}
"""

for _, row in moves_df.iterrows():
    class_name = row['Move Name'].replace(" ", "")
    name = row['Move Name']
    move_type = row['Move Type']
    power = row['Move Power']
    accuracy = row['Move Accuracy']
    pp = row['Move PP']
    desc = row['Move Effect']

    power = int(power) if power != '—' else None
    accuracy = int(accuracy) if accuracy != '—' else None
    pp = int(pp) if pp != '—' else None

    class_def = f"""class {class_name}(Move):
    def __init__(self, pokemon, category, name="{name}", desc="{desc}", move_type="{move_type}", power={power}, accuracy={accuracy}, pp={pp}):
        super().__init__(pokemon, category, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

move_dict["{name}"] = {class_name}(pokemon=[], category=None) 

"""

    file_content += class_def

file_path = 'move.py'
with open(file_path, 'w') as file:
    file.write(file_content)