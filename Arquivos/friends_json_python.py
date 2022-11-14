import json

file = open("/home/heroscampos/HC/Atividades/Arquivos/friends_json.txt", "r")
file_contents = json.load(file)

file.close()

print(file_contents['friends'][0])


cars = [
    {"make": "Ford", "model": "Fiesta"},
    {"make": "Ford", "model": "Focus"}
]

file = open("/home/heroscampos/HC/Atividades/Arquivos/cars_json.txt", "w")
json.dump(cars, file)

file.close()

















