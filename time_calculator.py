def getDayWeek(day, add):
    dia_semana = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6:"Sunday"}
    codigo_dia = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
    if isinstance(codigo_dia.get(day.lower()), int):
        return  dia_semana.get((codigo_dia.get(day.lower()) + add) % 7)


def mudaTurno(turno):
    conversor_turno = {"AM" : "PM", "PM": "AM"}
    return conversor_turno[turno]


def add_time(start_time: str, duration: str, week_day = None) -> str:
    turno = start_time.split()[1]
    stt = list(map(int, start_time.split()[0].split(":")))
    stt[0] = (stt[0] + 12) if turno == "PM" else stt[0]
    du = list(map(int, duration.split(":")))

    soma_minutos = stt[1] + du[1]
    soma_horas = stt[0] + du[0] + (soma_minutos // 60)

    novo_turno = mudaTurno(turno) if ((12 - (stt[0] % 12)) <= (soma_horas - stt[0]) % 24) else turno

    dias = soma_horas // 24

    if week_day:
        week_day = f", {getDayWeek(week_day, dias % 7)}"
    else:
        week_day = ""
    
    hora_final = soma_horas % 12 if (soma_horas % 12 != 0) else 12
    minutos_final = soma_minutos % 60

    if dias > 0:
        ending = " (next day)" if dias == 1 else f" ({dias} days later)"
    else:
        ending = ''

    # print(soma_horas , soma_minutos % 60, dias, week_day, getTurno(turno, soma_horas))
    return "{:01d}:{:02d} {}".format(hora_final, minutos_final, novo_turno) + week_day + ending



