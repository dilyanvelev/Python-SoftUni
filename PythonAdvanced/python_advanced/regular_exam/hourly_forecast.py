def forecast(*tuples):
    for location, weather in tuples:
        print(location, sorted(weather))






print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
