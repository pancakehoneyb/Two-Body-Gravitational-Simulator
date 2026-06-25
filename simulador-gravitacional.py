
import matplotlib.pyplot as plot


def fgrav(m2, dist):
    """Calcula a magnitude da aceleração gravitacional sobre o corpo em movimento.
    g = G * m2 / dist^2
    """
    G = 6.67408 * (10 ** -11)
    return G * (m2 / (dist ** 2))


def nova_posicao(pos_atual, vel, tempo, acel):
    """S = S0 + V0*T + A*T^2/2"""
    return pos_atual + (vel * tempo) + (acel * (tempo ** 2)) / 2


def nova_velocidade(vel, acel, tempo):
    """V = V0 + A*T"""
    return vel + acel * tempo


def ler_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Valor inválido, digite um número.")


def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Valor inválido, digite um número inteiro.")


def ler_sim_nao(msg):
    """Pergunta sim/não de forma mais tolerante a erro de digitação."""
    while True:
        resp = input(msg).strip().lower()
        if resp in ("1", "s", "sim", "y", "yes"):
            return True
        if resp in ("0", "n", "nao", "não", "no"):
            return False
        print("Digite 1 (sim) ou 0 (não).")


def salvar_arquivo(valores, prompt_nome):
    nome = input(prompt_nome).strip()
    if not nome:
        nome = "saida"
    nome += ".txt"
    texto = ", ".join(str(v) for v in valores)
    with open(nome, "w") as f:
        f.write(texto)
    print(f"Arquivo '{nome}' salvo com sucesso.")


def exibir_grafico(valores, titulo, ylabel):
    xpoints = list(range(len(valores)))
    plot.plot(xpoints, valores)
    plot.title(titulo)
    plot.xlabel("Instante")
    plot.ylabel(ylabel)
    plot.show()


def pos_e_salvar_grafico(valores, nome_grandeza):
    if ler_sim_nao(f"Digite 1 para baixar os valores de {nome_grandeza}: "):
        salvar_arquivo(valores, f"Defina o nome do documento para salvar os valores de {nome_grandeza}: ")
    if ler_sim_nao(f"Digite 1 para exibir o gráfico de {nome_grandeza}: "):
        exibir_grafico(valores, f"{nome_grandeza.capitalize()} x Instante", nome_grandeza)


def main():
    continuar = True

    while continuar:
        print("\n--- Nova simulação ---\n")

        # Massa do corpo parado
        while True:
            m2 = ler_float("Massa do corpo parado em Kg: ")
            expm2 = ler_int("Valor do expoente da massa do corpo parado em notação científica: ")
            m2 = m2 * (10 ** expm2)
            if m2 > 0:
                break
            print("A massa precisa ser maior que zero.")
        print("")

        # Distância inicial entre os corpos
        while True:
            ini_dist = ler_float("Insira a distância inicial entre os dois corpos: ")
            expdist = ler_int("Insira o valor do expoente da distância entre os dois corpos: ")
            ini_dist = ini_dist * (10 ** expdist)
            if ini_dist > 0:
                break
            print("A distância inicial precisa ser maior que zero (evita divisão por zero).")
        print("")

        # Deslocamento final
        pf = ler_float("Insira o deslocamento final do movimento: ")
        exppf = ler_int("Insira o valor do expoente do deslocamento final do movimento: ")
        pf = pf * (10 ** exppf)
        print("")

        # Velocidade inicial
        vel = ler_float("Insira a velocidade inicial do corpo em movimento em m/s: ")
        print("")

        # Resolução temporal
        while True:
            instantes_por_seg = ler_float("Insira a quantidade de instantes dentro de um segundo: ")
            if instantes_por_seg > 0:
                TI = 1 / instantes_por_seg
                break
            print("O valor precisa ser maior que zero.")
        print("")

        p1 = 0.0          # posição do corpo em movimento
        p2 = ini_dist      # posição do corpo fixo (referência de gravidade)
        acel = 0.0

        dists = []
        vels = []
        acels = []

        i = 0
        MAX_ITERACOES = 2_000_000  # proteção contra loop infinito
        DIST_MINIMA = 1e-6         # evita divisão por zero / singularidade

        # direção do movimento (para saber se vai se afastar ou se aproximar de pf)
        avancando = pf >= p1

        try:
            while (p1 < pf if avancando else p1 > pf):
                if i >= MAX_ITERACOES:
                    print("\nAVISO: número máximo de iterações atingido. "
                          "A simulação foi interrompida para evitar loop infinito.")
                    break

                dist_atual = p2 - p1  # mantém o sinal: positivo se p1 ainda não passou de p2
                if abs(dist_atual) < DIST_MINIMA:
                    print("\nAVISO: o corpo em movimento chegou muito perto do corpo fixo "
                          "(quase colisão). Simulação interrompida para evitar divisão por zero.")
                    break

                # magnitude da aceleração gravitacional
                acel_mag = fgrav(m2, abs(dist_atual))

                # sinal da aceleração: sempre aponta de p1 em direção a p2
                acel = acel_mag if dist_atual > 0 else -acel_mag

                p1 = nova_posicao(p1, vel, TI, acel)
                vel = nova_velocidade(vel, acel, TI)
                i += 1

                dists.append(p1)
                vels.append(vel)
                acels.append(acel)

                print(f"\nInstante {i}:"
                      f"\n\tPosição de p1 = {p1}"
                      f"\n\tTempo = {round(TI * i, 4)} seg"
                      f"\n\tDistância entre p1 e p2 = {abs(p2 - p1)}"
                      f"\n\tAceleração = {acel}"
                      f"\n\tVelocidade = {vel}")

        except KeyboardInterrupt:
            print("\nSimulação interrompida pelo usuário.")

        print("\n--- Fim da simulação ---\n")

        if dists:
            pos_e_salvar_grafico(dists, "espaço")
            pos_e_salvar_grafico(vels, "velocidade")
            pos_e_salvar_grafico(acels, "aceleração")
        else:
            print("Nenhum dado foi gerado nesta simulação.")

        continuar = ler_sim_nao("Digite 1 para continuar e 0 para sair: ")

    print("Encerrando o programa.")


if __name__ == "__main__":
    main()
