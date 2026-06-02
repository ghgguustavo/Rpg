#Criando personagens
print( "=== Bem-vindo ao meu RPG === ")
nome= input ("Digite seu nome: ")

print()
print("Escolha sua classe:")
print("1 - ⚔️  Cavaleiro  (Vida: 120 | Ataque: 20 | Mana: 30)")
print("2 - 🔮 Mago        (Vida: 70  | Ataque: 10 | Mana: 100)")
print()

while True:
    escolha = input("Digite 1 ou 2: ")

    if escolha == "1":
        classe = "Cavaleiro"
        vida = 120
        ataque = 20
        mana = 30
        ouro = 0
        break
    elif escolha == "2":
        classe = "Mago"
        vida = 70
        ataque = 10
        mana = 100
        ouro = 0
        break
    else:
        print("❌ Opção inválida! Digite apenas 1 ou 2.")
        print()

print()
print(f"Herói '{nome}' o {classe} criado com sucesso!")
print(f"❤️  Vida:   {vida}")
print(f"⚔️  Ataque: {ataque}")
print(f"💙 Mana:   {mana}")

# Encontrando o monstro

import random

print()
print("=== VOCÊ ENTRA NA DUNGEON ===")
print()
print("O corredor está escuro e úmido...")
print("De repente, um inimigo aparece na sua frente!")
print()

monstro1_nome = "Goblin"
monstro1_vida = 50
monstro1_ataque = random.randint(5, 15)

print(f"💀 {monstro1_nome} apareceu!")
print(f"❤️  Vida do inimigo: {monstro1_vida}")
print()

# Batalha
while monstro1_vida > 0 and vida > 0:
    print("O que você quer fazer?")
    print("1 - ⚔️  Atacar")
    print("2 - 🏃 Fugir")
    print()

    acao = input("Digite 1 ou 2: ")

    if acao == "1":
        if classe == "Mago":
            if mana <= 0:
                print("💙 Você não tem mana suficiente para atacar!")
                continue

            dano_jogador = random.randint(ataque - 3, ataque + 8)
            mana = mana - 15
            print(f"🔮 Você lançou uma magia e causou {dano_jogador} de dano!")
            print(f"💙 Mana restante: {mana}")

        else:  # Cavaleiro
            dano_jogador = random.randint(ataque - 5, ataque + 5)
            print(f"⚔️  Você atacou o {monstro1_nome} e causou {dano_jogador} de dano!")

        monstro1_vida = monstro1_vida - dano_jogador

        # Monstro contra-ataca (se ainda estiver vivo)
        if monstro1_vida > 0:
            dano_monstro = random.randint(monstro1_ataque - 3, monstro1_ataque + 3)
            vida = vida - dano_monstro
            print(f"💀 O {monstro1_nome} contra-atacou e causou {dano_monstro} de dano!")

    elif acao == "2":
        print("🏃 Você fugiu da batalha!")
        break

    else:
        print("❌ Opção inválida!")
        continue

    # Status após cada rodada
    print()
    if classe == "Mago":
        print(f"❤️  Sua vida: {vida}  |  💙 Mana: {mana}  |  ❤️  Vida do {monstro1_nome}: {max(0, monstro1_vida)}")
    else:
        print(f"❤️  Sua vida: {vida}  |  ❤️  Vida do {monstro1_nome}: {max(0, monstro1_vida)}")
    print()

# Resultado da batalha
if monstro1_vida <= 0:
    ouro_ganho = random.randint(10, 15)
    ouro = ouro + ouro_ganho
    print(f"🏆 Você derrotou o {monstro1_nome}!")
    print(f"💰 Você ganhou {ouro_ganho} de ouro! Total: {ouro}")
elif vida <= 0:
    print("💀 Você foi derrotado... Game Over!")

# Passo 3: Loja de itens

if monstro1_vida <= 0:
    print()
    print("=== VOCÊ ENCONTROU UMA LOJA ===")
    print()
    print(f"💰 Ouro disponível: {ouro}")
    print()
    print("O que deseja comprar?")
    print("1 - 🧪 Poção de Vida     (+30 vida)   | Custo: 10 ouro")

    if classe == "Mago":
        print("2 - 💧 Poção de Mana     (+40 mana)   | Custo: 10 ouro")
    else:
        print("2 - 🛡️  Escudo reforçado  (+10 ataque) | Custo: 15 ouro")

    print("3 - 🚪 Sair da loja")
    print()

    while True:
        compra = input("Digite 1, 2 ou 3: ")

        if compra == "1":
            if ouro >= 10:
                vida = vida + 30
                ouro = ouro - 10
                print(f"🧪 Você bebeu a poção! ❤️  Vida: {vida} | 💰 Ouro: {ouro}")
            else:
                print("❌ Ouro insuficiente!")

        elif compra == "2":
            if classe == "Mago":
                if ouro >= 10:
                    mana = mana + 40
                    ouro = ouro - 10
                    print(f"💧 Mana restaurada! 💙 Mana: {mana} | 💰 Ouro: {ouro}")
                else:
                    print("❌ Ouro insuficiente!")
            else:
                if ouro >= 15:
                    ataque = ataque + 10
                    ouro = ouro - 15
                    print(f"🛡️  Escudo equipado! ⚔️  Ataque: {ataque} | 💰 Ouro: {ouro}")
                else:
                    print("❌ Ouro insuficiente!")

        elif compra == "3":
            print("🚪 Você saiu da loja. Boa sorte, aventureiro!")
            break

        else:
            print("❌ Opção inválida!")

        print()

    # Status final
    print()
    print("=== STATUS FINAL ===")
    print(f"🧙 Herói:   {nome} o {classe}")
    print(f"❤️  Vida:    {vida}")
    print(f"⚔️  Ataque:  {ataque}")
    print(f"💙 Mana:    {mana}")
    print(f"💰 Ouro:    {ouro}")

# Passo 4: O Chefão Final

print()
print("=== A DUNGEON TREME SOB SEUS PÉS ===")
print()
print("Você avança pelo corredor e uma porta enorme se abre...")
print("Uma criatura colossal bloqueia sua saída!")
print()

chefao_nome = "Dragão das Sombras"
chefao_vida = 150
chefao_ataque = random.randint(15, 25)
chefao_turno = 0

print(f"🐲 {chefao_nome} rugiu! A batalha começa!")
print(f"❤️  Vida do chefão: {chefao_vida}")
print()

escudo_magico = False

while chefao_vida > 0 and vida > 0:
    chefao_turno += 1

    print("O que você quer fazer?")
    print("1 - ⚔️  Atacar")
    if classe == "Mago":
        if mana >= 30:
            print("2 - 💥 Magia Especial     (dano dobrado, gasta 30 de mana)")
        if mana >= 20:
            print("3 - 🛡️  Escudo Mágico     (reduz dano pela metade, gasta 20 de mana)")
    elif classe == "Cavaleiro":
        print("2 - 🛡️  Defender            (reduz dano pela metade neste turno)")
        print("3 - ⚡ Ataque Duplo        (ataca duas vezes, gasta 20 de vida)")
    print("4 - 🏃 Fugir")
    print()

    defendendo = False
    acao = input("Digite sua ação: ")

    if acao == "1":
        if classe == "Mago":
            if mana <= 0:
                print("💙 Sem mana! Você tenta um golpe físico fraco...")
                dano_jogador = random.randint(3, 8)
            else:
                dano_jogador = random.randint(ataque - 3, ataque + 8)
                mana -= 15
                print(f"🔮 Você lançou uma magia e causou {dano_jogador} de dano!")
                print(f"💙 Mana restante: {mana}")
        else:
            dano_jogador = random.randint(ataque - 5, ataque + 5)
            print(f"⚔️  Você atacou e causou {dano_jogador} de dano!")

        chefao_vida -= dano_jogador

    elif acao == "2":
        if classe == "Mago":
            if mana >= 30:
                dano_jogador = random.randint(ataque + 10, ataque + 25)
                mana -= 30
                print(f"💥 MAGIA ESPECIAL! Você causou {dano_jogador} de dano!")
                print(f"💙 Mana restante: {mana}")
                chefao_vida -= dano_jogador
            else:
                print("❌ Mana insuficiente para a magia especial!")
                continue
        else:  # Cavaleiro
            print("🛡️  Você assumiu postura defensiva!")
            defendendo = True

    elif acao == "3":
        if classe == "Mago":
            if mana >= 20:
                escudo_magico = True
                mana -= 20
                print(f"🛡️  Escudo Mágico ativado! Próximo dano será reduzido pela metade!")
                print(f"💙 Mana restante: {mana}")
            else:
                print("❌ Mana insuficiente para o escudo!")
                continue
        else:  # Cavaleiro - Ataque Duplo
            if vida > 20:
                dano1 = random.randint(ataque - 5, ataque + 5)
                dano2 = random.randint(ataque - 5, ataque + 5)
                dano_total = dano1 + dano2
                vida -= 20
                chefao_vida -= dano_total
                print(f"⚡ ATAQUE DUPLO! Primeiro golpe: {dano1} | Segundo golpe: {dano2}")
                print(f"💥 Dano total: {dano_total}! Você perdeu 20 de vida no esforço.")
            else:
                print("❌ Vida insuficiente para o ataque duplo!")
                continue

    elif acao == "4":
        print("🏃 Você fugiu do chefão! A dungeon permanece nas sombras...")
        break

    else:
        print("❌ Opção inválida!")
        continue

    # Chefão contra-ataca
    if chefao_vida > 0:
        if chefao_turno % 3 == 0:
            dano_monstro = random.randint(25, 40)
            print(f"🔥 O {chefao_nome} soltou FOGO! Dano massivo de {dano_monstro}!")
        else:
            dano_monstro = random.randint(chefao_ataque - 5, chefao_ataque + 5)
            print(f"🐲 O {chefao_nome} atacou causando {dano_monstro} de dano!")

        if defendendo or escudo_magico:
            dano_monstro = dano_monstro // 2
            print(f"🛡️  Proteção ativada! Dano reduzido para {dano_monstro}!")
            escudo_magico = False

        vida -= dano_monstro

    # Status após cada rodada
    print()
    if classe == "Mago":
        escudo_str = " | 🛡️  Escudo: ATIVO" if escudo_magico else ""
        print(f"❤️  Sua vida: {max(0, vida)}  |  💙 Mana: {mana}{escudo_str}  |  🐲 Vida do chefão: {max(0, chefao_vida)}")
    else:
        print(f"❤️  Sua vida: {max(0, vida)}  |  🐲 Vida do chefão: {max(0, chefao_vida)}")
    print()

# Resultado final
print()
if chefao_vida <= 0:
    print("=" * 40)
    print("🏆 VOCÊ DERROTOU O DRAGÃO DAS SOMBRAS!")
    print("A dungeon está salva. Você é uma lenda!")
    print("=" * 40)
elif vida <= 0:
    print("=" * 40)
    print("💀 O Dragão foi poderoso demais...")
    print("Sua jornada termina aqui. Game Over!")
    print("=" * 40)
