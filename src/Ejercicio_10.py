def processing_rounds(rounds):
    maxim = -1
    stats = {}
    for rounds_ids, val in enumerate(rounds):
        maxim = 0
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
                stats[person] = {"points": tot, "best_round": tot, "wins": 0, "prom": 0}
        stats[ganador]["wins"] += 1
        print(f"Ronda {rounds_ids} - {val["theme"]}: \n Ganador: {ganador} con {maxim}")

    for player in stats.values():
        player["prom"] = player["points"] / len(rounds)
    print(f" {'Cocinero':<15} {'Puntaje':<15} {'Rondas ganadas':<20} {'Mejor ronda':<15} {'Promedio':<5}")
    print("-"*79)
    for player, values in stats.items():
        print(f" {player:<15} {values["points"]:<15} {values["wins"]:<20} {values["best_round"]:<15} {values["prom"]:<5}")
    print("-"*79)