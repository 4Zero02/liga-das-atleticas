from unittest import result
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
            partida__etapa__in=[
                Partida.Etapa.FINAL,
                Partida.Etapa.TERCEIRO,
                Partida.Etapa.DESEMPATE56,
                Partida.Etapa.DESEMPATE78,
            ]
        ).prefetch_related("equipe")

        r = {
            Partida.Etapa.FINAL: [None, None],
            Partida.Etapa.TERCEIRO: [None, None],
            Partida.Etapa.DESEMPATE56: [None, None],
            Partida.Etapa.DESEMPATE78: [None, None],
        }

        for idx in range(0, len(partida_ranking), 2):
            if partida_ranking[idx].resultado > partida_ranking[idx + 1].resultado:
                r[partida_ranking[idx].partida.etapa] = [
                    partida_ranking[idx].equipe,
                    partida_ranking[idx + 1].equipe,
                ]
            else:
                r[partida_ranking[idx].partida.etapa] = [
                    partida_ranking[idx + 1].equipe,
                    partida_ranking[idx].equipe,
                ]

        for etapa, times in r.items():
            result_ranking.extend(times)

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
