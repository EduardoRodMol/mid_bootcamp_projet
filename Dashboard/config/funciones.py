def partidos_ganados(partidos,equipo):
    lstpartido = [0,0,0]
    for partido in partidos:
        if equipo in partido["team_name_home"]:
            if partido["team_home_score"] > partido["team_away_score"]:
                lstpartido[0] = lstpartido[0] +1
            if partido["team_home_score"] == partido["team_away_score"]:
                lstpartido[1] = lstpartido[1] +1
            if partido["team_home_score"] < partido["team_away_score"]:
                lstpartido[2] = lstpartido[2] +1

        else:
            if partido["team_away_score"] > partido["team_home_score"]:
                lstpartido[0] = lstpartido[0] +1
            if partido["team_away_score"] == partido["team_home_score"]:
                lstpartido[1] = lstpartido[1] +1
            if partido["team_away_score"] < partido["team_home_score"]:
                lstpartido[2] = lstpartido[2] +1

    return lstpartido
