# ========================================================
# 🚛 SISTEMA DE CONTROLE DE FROTA
# ==========================================================
 
# Lista que irá armazenar os caminhões
frota = []
 
# =========================================================
# FUNÇÃO: NORMALIZAR TEXTO
# ==========================================================
 
def normalizar(texto):
 
    texto = texto.strip().lower()
 
    texto de retorno
 
 
# =========================================================
# FUNÇÃO: NORMALIZAR ESTADO
# ==========================================================
 
def normalizar_estado(estado):
 
    estado = normalizar(estado)
 
    if estado == "são paulo" ou estado == "sp":
        return "SP"
 
    elif estado == "paraná" ou estado == "pr":
        return "PR"
 
    elif estado == "minas gerais" ou estado == "mg":
        return "MG"
 
    elif estado == "rio de janeiro" ou estado == "rj":
        return "RJ"
 
    elif estado == "santa catarina" ou estado == "sc":
        return "SC"
 
    elif estado == "rio grande do sul" ou estado == "rs":
        return "RS"
 
    elif estado == "bahia" ou estado == "ba":
        return "BA"
 
    elif estado == "goiás" ou estado == "go":
        return "GO"
 
    else:
        return estado.upper()
# =========================================================
# FUNÇÃO: CADASTRAR CAMINHÃO
# ==========================================================
 
def cadastrar_caminhao():
 
    print()
    print("===================================")
    print(" CADASTRAR CAMINHÃO")
    print("==============================================)
 
    placa = input("Digite a placa: ")
    modelo = input("Digite o modelo: ")
    motorista = input("Digite o motorista: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    carga = str(input("Digite o tipo de carga: "))
 
    # Padronizando as informações
    placa = placa.strip().upper()
    modelo = modelo.strip()
    motorista = motorista.strip()
    cidade = cidade.strip()
    estado = normalizar_estado(estado)
    carga = carga.strip()
 
    # Verifique se a placa já está cadastrada
 
    placa_existe = False
 
    foro em frota:
 
        if caminhada["placa"] == placa:
 
            placa_existe = Verdadeiro
 
    se placa_existe:
 
        print()
        print("❌ Essa placa já está cadastrada!")
 
        retornar
 
    # Criando o caminhão
 
    caminhao = {
        "placa": placa,
        "modelo": modelo,
        "motorista": motorista,
        "cidade": cidade,
        "estado": estado,
        "carga": carga
    }
 
    #spotndo na frota
 
    frota.append(caminhao)
 
    print()
    print("✅ Caminhão cadastrado com sucesso!")
 
 
# =========================================================
# FUNÇÃO: LISTAR CAMINHÕES
# ==========================================================
 
def listar_caminhoes():
 
    print()
    print("===================================")
    print(" FROTA CADASTRADA")
    print("=========================================================================================================================================================================================")
 
    se len(frota) == 0:
 
        print("Nenhum caminhão cadastrado.")
 
        retornar
 
    para numero em range(len(frota)):
 
        ó = frota[número]
 
        print()
        print("Caminhão", numero + 1)
        print("----------------------------")
 
        print("Placa:", caminhao["placa"])
        print("Modelo:", caminhao["modelo"])
        print("Motorista:", caminhao["motorista"])
        print("Cidade:", caminhao["cidade"])
        print("Estado:", caminhao["estado"])
        print("Carga:", caminhao["carga"])
 
 
# =========================================================
# FUNÇÃO: PROCURAR POR PLACA
# ==========================================================
 
def procurar_placa():
 
    print()
    print("===================================")
    print(" PROCURAR CAMINHÃO")
    print("=====================================================================")
 
    placa = input("Digite a placa: ")
 
    placa = placa.strip().upper()
 
    encontrado = Falso
 
    foro em frota:
 
        if caminhada["placa"] == placa:
 
            print()
            print("✅ CAMINHÃO ENCONTRADO!")
            print("----------------------------")
 
            print("Placa:", caminhao["placa"])
            print("Modelo:", caminhao["modelo"])
            print("Motorista:", caminhao["motorista"])
            print("Cidade:", caminhao["cidade"])
            print("Estado:", caminhao["estado"])
            print("Carga:", caminhao["carga"])
 
            encontrado = Verdadeiro
 
    se encontrado == Falso:
 
        print()
        print("❌ Caminhão não encontrado.")
 
 
# =========================================================
# FUNÇÃO: PROCURAR POR MOTORISTA
# ==========================================================
 
def procurar_motorista():
 
    print()
    print("===================================")
    print("PROCURAR MOTORISTA")
    print("============================================)
 
    nome = input("Digite o nome do motorista: ")
 
    nome = normalizar(nome)
 
    encontrado = Falso
 
    foro em frota:
 
        motorista = normalizar(
            caminhao["motorista"]
        )
 
        se o médico for igual ao nome:
 
            print()
            print("Caminho encontrado:")
            print("----------------------------")
 
            print("Placa:", caminhada["placa"])
            print("Modelo:", caminhada["modelo"])
            print("Cidade:", caminhada["cidade"])
            print("Estado:", caminhada["estado"])
            print("Carga:", caminhada["carga"])
 
            encontrado = Verdadeiro
 
    se encontrado == Falso:
 
        print()
        print("❌ Nenhum caminhão encontrado.")
 
 
# =========================================================
# FUNÇÃO: PROCURAR POR CIDADE
# ==========================================================
 
def procurar_mesmo():
 
    print()
    print("===================================")
    print("PROCURAR POR CIDADE")
    print("===========================================")
 
    cidade = input("Digite a cidade: ")
 
    cidade = normalizar(il)
 
    encontrado = Falso
 
    foro em frota:
 
        cidade_caminhao = normalizar(
            caminhao["cidade"]
        )
 
        se cidade_caminhao == cidade:
 
            print()
            print("Placa:", caminhao["placa"])
            print("Modelo:", caminhao["modelo"])
            print("Motorista:", caminhao["motorista"])
            print("Estado:", caminhao["estado"])
            print("Carga:", caminhao["carga"])
 
            encontrado = Verdadeiro
 
    se encontrado == Falso:
 
        print()
        print("❌ Nenhum caminhão encontrado nessa cidade.")
 
 
# ========================================================
# FUNÇÃO: PROCURAR POR ESTADO
# ==========================================================
 
def procurar_estado():
 
    print()
    print("===================================")
    print("PROCURAR POR ESTADO")
    print("============================================")
 
    estado = input("Digite o estado: ")
 
    estado = normalizar_estado(estado)
 
    encontrado = Falso
 
    foro em frota:
 
        if caminhada["estado"] == estado:
 
            print()
            print("Placa:", caminhao["placa"])
            print("Modelo:", caminhao["modelo"])
            print("Motorista:", caminhao["motorista"])
            print("Cidade:", caminhao["cidade"])
            print("Carga:", caminhao["carga"])
 
            encontrado = Verdadeiro
 
    se encontrado == Falso:
 
        print()
        print("❌ Nenhum caminhão encontrado nesse estado.")
 
 
# =========================================================
# FUNÇÃO: PROCURAR POR CARGA
# ==========================================================
 
def procurar_carga():
 
    print()
    print("===================================")
    print(" PROCURAR POR CARGA")
    print("==========================================================================================================================================)
 
    carga = input("Digite o tipo de carga: ")
 
    carga = normalizar(carga)
 
    encontrado = Falso
 
    foro em frota:
 
        carga_caminhao = normalizar(
            caminhao["carga"]
        )
 
        se carga_caminhao == carga:
 
            print()
            print("Placa:", caminhada["placa"])
            print("Modelo:", caminhada["modelo"])
            print("Motorista:", caminhada["motorista"])
            print("Cidade:", caminhada["cidade"])
            print("Estado:", caminhada["estado"])
 
            encontrado = Verdadeiro
 
    se encontrado == Falso:
 
        print()
        print("❌ Nenhum caminhão encontrado.")
 
 
# =========================================================
# FUNÇÃO: ALTERAR CAMINHÃO
# ==========================================================
 
def alterar_caminhao():
 
    print()
    print("===================================")
    print("ALTERAR CAMINHÃO")
    print("=============================================================================================================================================================================)
 
    placa = input("Digite a placa do caminhão: ")
 
    placa = placa.strip().upper()
 
    encontrado = Falso
 
    foro em frota:
 
        if caminhada["placa"] == placa:
 
            encontrado = Verdadeiro
 
            print()
            print("Caminho encontrado!")
 
            print("Deixe vazio para manter a informação atual.")
 
            modelo = input(
                "Novo modelo: "
            )
 
            motorista = input(
                "Novo motorista: "
            )
 
            cidade = input(
                "Nova cidade: "
            )
 
            estado = input(
                "Novo estado: "
            )
 
            carga = input(
                "Nova carga: "
            )
 
            if modelo != "":
                caminhao["modelo"] = modelo.strip()
 
            if motorista != "":
                caminhao["motorista"] = motorista.strip()
 
            if cidade != "":
                caminhao["cidade"] = cidade.strip()
 
            if estado != "":
                caminhao["estado"] = normalizar_estado(
                    estado
                )
 
            if carga != "":
                caminhadao["carga"] = carga.strip()
 
            print()
            print("✅ Caminhão alterado com sucesso!")
 
    se encontrado == Falso:
 
        print()
        print("❌ Caminhão não encontrado.")
 
 
# =========================================================
# FUNÇÃO: REMOVER CAMINHÃO
# ==========================================================
 
def remover_caminhao():
 
    print()
    print("===================================")
    print(" REMOVEDOR CAMINHÃO")
    print("==================================================================================================================================================================================================)
 
    placa = input("Digite a placa: ")
 
    placa = placa.strip().upper()
 
    encontrado = Falso
 
    foro em frota:
 
        if caminhada["placa"] == placa:
 
            encontrado = Verdadeiro
 
            confirmacao = input(
                "Deseja realmente remover? (S/N): "
            )
 
            confirmacao = confirmacao.strip().upper()
 
            se a confirmação for igual a "S":
 
                frota.remove(caminhao)
 
                print()
                print("✅ Caminhão removido!")
 
            outro:
 
                print()
                print("Operação cancelada.")
 
            quebrar
 
    se encontrado == Falso:
 
        print()
        print("❌ Caminhão não encontrado.")
 
 
# =========================================================
# FUNÇÃO: ESTATÍSTICAS
# ==========================================================
 
def estatisticas():
 
    print()
    print("===================================")
    print(" ESTATÍSTICAS")
    print("===========================================)
 
    se len(frota) == 0:
 
        print("Nenhum caminhão cadastrado.")
 
        retornar
 
    total = len(frota)
 
    sp = 0
    pr = 0
    mg = 0
    rj = 0
    outros = 0
 
    foro em frota:
 
        estado =o["estado"]
 
        se estado == "SP":
 
            sp += 1
 
        elif estado == "PR":
 
            pr += 1
 
        elif estado == "MG":
 
            mg += 1
 
        elif estado == "RJ":
 
            rj += 1
 
        outro:
 
            outros += 1
 
    print()
    print("Total de tráfego:", total)
 
    print()
    print("Caminhos por estado:")
    print("SP:", sp)
    print("PR:", pr)
    print("MG:", mg)
    print("RJ:", rj)
    print("Outros:", outros)
 
 
# =========================================================
# FUNÇÃO: MENU
# ==========================================================
 
def menu():
 
    print()
    print("=========================================")
    print(" 🚛 CONTROLE DE FROTA")
    print("==================================================================)
 
    print("1 - Cadastrar caminhões")
    print("2 - Listar caminhões")
    print("3 - Procurar por placa")
    print("4 - Procurar por motorista")
    print("5 - Procurar por cidade")
    print("6 - Procurar por estado")
    print("7 - Procurar por carga")
    print("8 - Alterar caminhões")
    print("9 - Remover caminhões")
    print("10 - Estatísticas")
    print("0 - Sair")
 
    print("===========================================")