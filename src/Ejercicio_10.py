def processing_rounds(rounds):
    stats = {}
#Separo la cantidad de rondas y los puntajes-temas    
    for rounds_ids, val in enumerate(rounds):
        maxim = -1
#Por cada puntaje recorro juez para cada persona
        for person, scores in val["scores"].items():
            tot = 0
            for judge, score in scores.items():
                tot += score
            if tot > maxim:
                maxim = tot
                ganador = person
            if person in stats:
                stats[person]["points"] += tot
                
                if stats[person]["best_round"] < tot:
                    stats[person]["best_round"] = tot
            else:
                stats[person] = {"points": tot, "best_round": tot, "wins": 0, "prom": tot / (rounds_ids+1)}
        stats[ganador]["wins"] += 1
        
        print(f"\nRonda {rounds_ids} - {val["theme"]}: \n Ganador: {ganador} con {maxim} \n")
        
        in_order = sorted(stats.items(), key=lambda x: x[1]["points"], reverse = True)
        
        print("Progresion \n")
        
        for player, data in in_order:
            print(f"{player}: Puntos: {data["points"]} | Victorias: {data["wins"]}  | Mejor ronda:{data["best_round"]} |" 
                f" Un promedio de: {data["prom"]}\n")    

    print(f" {'Cocinero':<15} {'Puntaje':<15} {'Rondas ganadas':<20} {'Mejor ronda':<15} {'Promedio':<5}")
    print("-"*79)
    for player, values in stats.items():
        print(f" {player:<15} {values["points"]:<15} {values["wins"]:<20} {values["best_round"]:<15} {values["prom"]:<5}")
    print("-"*79)