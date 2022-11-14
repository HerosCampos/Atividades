
dados = open('/home/heroscampos/HC/Atividades/Arquivos/csv_dados.txt', 'r')
dados_un = [dado.strip().split(',') for dado in dados.readlines()]
dados.close()

for d in dados_un[1:]:
    print(f"{d[0].title()} tem {d[1]} anos e estuda na universidade {d[2].upper()} o curso {d[3].title()}")









