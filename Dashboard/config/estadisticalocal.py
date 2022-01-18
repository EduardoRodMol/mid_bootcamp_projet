
def partidos_ganados(partidos : list,equipo: str):
    lstpartido = [0,0,0,0]#ganado,empatado,perdido,goles
    lst_partido_goles=[]#partido,goles
    p_jugado = 0
    for partido in partidos:
        p_jugado += 1
        if equipo in partido["team_name_home"]:
            lst_partido_goles.append([p_jugado, int(partido["team_home_score"]) ])
            lstpartido[3] = lstpartido[3] + int(partido["team_home_score"])
            if partido["team_home_score"] > partido["team_away_score"]:
                lstpartido[0] = lstpartido[0] +1
            if partido["team_home_score"] == partido["team_away_score"]:
                lstpartido[1] = lstpartido[1] +1
            if partido["team_home_score"] < partido["team_away_score"]:
                lstpartido[2] = lstpartido[2] +1

        else:
            lst_partido_goles.append([p_jugado, int(partido["team_away_score"])] )
            lstpartido[3] = lstpartido[3] + int(partido["team_away_score"])
            if partido["team_away_score"] > partido["team_home_score"]:
                lstpartido[0] = lstpartido[0] +1
            if partido["team_away_score"] == partido["team_home_score"]:
                lstpartido[1] = lstpartido[1] +1
            if partido["team_away_score"] < partido["team_home_score"]:
                lstpartido[2] = lstpartido[2] +1
        
    return lstpartido ,lst_partido_goles
