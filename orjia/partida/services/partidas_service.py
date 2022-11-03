from ..models import Partida, Competicao


def make_ranking(competicao: Competicao):
    competidores = Partida.equipes.through.objects.filter(
        partida__competicao=competicao
    )

    result_ranking = []

    # Modalidade mata-mata
    if competicao.modalidade.tipo_confronto == "0":
        # Busca as partida_competidores que estão nas etapas Final e TerceiroLugar
        # para a competição X
        partida_ranking = competidores.filter(
            partida__etapa__in=[Partida.Etapa.FINAL, Partida.Etapa.TERCEIRO]
        ).prefetch_related("equipe")

        # Itera sobre as partida_competidores que estão na Final e TerceiroLugar
        # O loop vai de 2 em 2, pois cada partida tem 2 equipes
        # O primeiro loop é da final e o segundo é para TerceiroLugar
        for idx in range(0, len(partida_ranking), 2):
            if partida_ranking[idx].resultado > partida_ranking[idx + 1].resultado:
                result_ranking.extend(
                    [partida_ranking[idx].equipe, partida_ranking[idx + 1].equipe]
                )
            else:
                result_ranking.extend(
                    [partida_ranking[idx + 1].equipe, partida_ranking[idx].equipe]
                )

    # Modalidade Todos-contra-Todos
    elif competicao.modalidade.tipo_confronto == "1":
        # Busca as 8 primeiras equipes da partida todos-contra-todos
        # ordenadas pela pontuação
        partida_ranking = competidores.order_by("-resultado")[:8].prefetch_related(
            "equipe"
        )

        result_ranking = [
            partida_competidor.equipe for partida_competidor in partida_ranking
        ]

    return result_ranking
