## This will read what is written in the txt file
#my_file = open("/home/heroscampos/HC/Atividades/Arquivos/dados.txt", "r")
#file_content = my_file.read()
#my_file.close()
#
#print(file_content)
#
#
## This will write in the txt file but will delete the previous text
#user_name = input("Enter your name: ")
#my_file_writing = open("/home/heroscampos/HC/Atividades/Arquivos/dados.txt", "w")
#my_file_writing.write(user_name)
#
#my_file_writing.close()


# Atividade 
amigos = input("Digite o nome de três amigos, separados por vírgulas (sem espaço): ").split(',')

pessoas = open('/home/heroscampos/HC/Atividades/Arquivos/dados.txt', 'r')
pessoas_proximas = [line.strip() for line in pessoas.readlines()]
pessoas.close()

amigos_set = set(amigos)
pessoas_proximas_set = set(pessoas_proximas)

amigos_proximos_set = amigos_set.intersection(pessoas_proximas_set)


amigos_proximos_arquivo = open('/home/heroscampos/HC/Atividades/Arquivos/amigos_proximos.txt', 'w')

for amigo in amigos_proximos_set:
    print(f"{amigo} está perto.")
    amigos_proximos_arquivo.write(f"{amigo}\n") 

amigos_proximos_arquivo.close()

















