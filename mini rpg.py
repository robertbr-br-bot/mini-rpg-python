import random

vida = 10
pocao = 0
ouro = random.randint(3, 8)
vida_inimigo = 12
em_combate = False

while vida > 0:

    if em_combate:
        resposta = input('Escolha: Atacar | Fugir | Usar poção: ').strip().lower()
    else:
        resposta = input('Escolha: Esquerda | Direita | Usar poção | Voltar: ').strip().lower()

    vida_max = 10
    vida = min(vida, vida_max)
    print(f'Vida: {vida}/{vida_max} | Poções: {pocao} | Ouro: {ouro}')

    if resposta == 'direita':
        sorte = random.randint(1, 10)

        if sorte <= 5:
            dano = random.randint(1, 4)
            vida -= dano
            print(f'Você sofreu {dano} de dano ao explorar!')

        em_combate = True
        vida_inimigo = random.randint(5, 12)
        print('Um inimigo apareceu, o que você irá fazer?')

        while vida_inimigo > 0 and vida > 0:

            # ========COMBATE============
            acao = input('Atacar | Fugir | Usar poção: ').strip().lower()

            if acao == 'atacar':
                dano = random.randint(3, 6)

                # chance de crítico (20%)
                if random.random() < 0.2:
                    dano *= 2
                    print('DANO CRÍTICO!')

                vida_inimigo = max(0, vida_inimigo - dano)
                print(f'Você causou {dano} de dano!')

                if vida_inimigo > 0:
                    dano_inimigo = random.randint(1, 4)

                    if random.random() < 0.1:
                        dano_inimigo *= 2
                        print('VOCÊ SOFREU DANO CRÍTICO!')

                    vida = max(0, vida - dano_inimigo)
                    print(f'O inimigo te causou {dano_inimigo} de dano!')

                print(f'Sua vida: {vida}')
                print(f'Vida do inimigo: {vida_inimigo}')

            elif acao == 'usar poção':
                if pocao > 0:
                    pocao -= 1
                    cura = random.randint(2, 5)
                    vida += cura
                    vida = min(vida, 10)
                    print(f'Você usou uma poção e recuperou {cura} de vida!')
                else:
                    print('Você não tem poções!')

            elif acao == 'fugir':
                print('Você fugiu!')
                em_combate = False
                break

            else:
                print('Ação Inválida.')

        # vitória no lugar certo
        if vida_inimigo <= 0:
            print('Você derrotou o inimigo!')
            em_combate = False

            # ==========Exploração===========
    elif resposta == 'esquerda':
        print('Você encontrou um tesouro!')

        sorte = random.randint(1, 10)

        if sorte <= 4:
            print('Dentro do tesouro tinha uma poção!')
            pocao = pocao + 1
            print(f'Agora você tem {pocao} poção!')

        elif sorte <= 8:
            print(f'Você encontrou um saco de moedas!')
            ouro = ouro + random.randint(3, 15)
            print(f'Agora você tem {ouro} de ouro')

        elif sorte >= 9:
            print(f'Um objeto misterioso te cura por completo!')
            vida = 10

    elif resposta == 'usar poção':

        if pocao > 0:

            pocao -= 1

            cura = random.randint(2, 5)

            vida += cura

            vida = min(vida, 10)

            print(f'Você usou uma poção e recuperou {cura} de vida!')

        else:

            print('Você não tem poções!')

    elif resposta == 'voltar':

        print('Você voltou para a floresta, mas o que ela reserva para você?')
        break

    else:
        print('Tente novamente.')

    if vida <= 0:
        print('Você não resistiu...')
        break