#cadastro de funcionarios

#estrutura dic
funcionario = {'Nome':'','salario':0.0,'ativo':False}

#entrada
print('\n\t\t\t -- Registro de Funcionario -- \n')
funcionario['nome'] = input('informe o nome: ')
funcionario['salario'] = float(input('informe o salario: '))


funcionario['Ativo'] = True

#saida
print(f'\n\nNome.......{funcionario["nome"]}')
print(f'salario.......{funcionario["salario"]}')
print(f'\n\t -funcionario ativo-') if funcionario['ativo'] else print('\n\t -funcionario inativo')
