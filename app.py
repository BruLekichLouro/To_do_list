# Constante com as op��es do menu
MENU_OPTIONS = """
1. Adicionar tarefa
2. Remover tarefa
3. SAIR

"""

# Variável para armazenar a LISTA de tarefas
tasks = []

def add_task():
    task = input("Armazenar a tarefa: ")
    tasks.append(task)

def print_tasks():
    for task in tasks:
        print(task)
    
def menu():
    # Função principal do programa

    while True:
        
        print(tasks)
        
        option = input(MENU_OPTIONS)

        if option == "1":
            add_task()

        elif option == "2":
            ...

        elif option == "3":
            break


# Executa a função principal
menu()
