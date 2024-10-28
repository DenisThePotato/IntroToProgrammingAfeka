def f(weather="sunny", time=10):
    """
    param weather (str): can be either "sunny","cloudy", "rainy" or "snowy"
    default value is "sunny" (provided)
    param time (int):
    - default value is 10 (provided)
    - can be any value between 0 and 23
    return sport:
    - default value is "no sport"
    if time is before 6 sport is "too early to sport"
    if time is after 22 sport is "too late to sport"
    if weather is sunny and time is before 10 (including 10) sport is "running"
    if weather is sunny and time is before 14 (including 14) sport is "surfing"
    if weather is sunny and time is before 22 (including 22) sport is "gym"
    if weather is cloudy and time is within the permitted range (above), sport is "hiking"
    if weather is rainy and time is within the permitted range (above), sport is "indoor climbing"
    if weather is snowy and time is within the permitted range (above), sport is "skiing"
    """
    sport = "no sport"
    if time < 6:
        sport = "too early to sport"
    elif time > 22:
        sport = "too late to sport"
    elif weather == "sunny":
        if 6 < time <= 10:
            sport = "running"
        elif 10 < time <= 14:
            sport = "surfing"
        elif 14 < time <= 22:
            sport = "gym"
    elif weather == "cloudy":
        sport = "hiking"
    elif weather == "rainy":
        sport = "indoor climbing"
    elif weather == "snowy":
        sport = "skiing"
    return sport