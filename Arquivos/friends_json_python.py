import json

with open("/home/heroscampos/HC/Atividades/Arquivos/friends_json.txt", "r") as file:
    file_contents = json.load(file)


print(file_contents['friends'][0])


cars = [
    {"make": "Ford", "model": "Fiesta"},
    {"make": "Ford", "model": "Focus"}
]

with open("/home/heroscampos/HC/Atividades/Arquivos/cars_json.txt", "w") as file:
    json.dump(cars, file)


















