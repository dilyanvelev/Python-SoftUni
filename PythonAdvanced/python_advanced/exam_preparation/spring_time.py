def start_spring(**data):
    spring_objects = {}
    result = []

    for value, key in data.items():
        if key not in spring_objects:
            spring_objects[key] = []

        spring_objects[key].append(value)

    spring_objects = sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0]))

    for spring_objects, values in spring_objects:
        result.append(f"{spring_objects}:")

        for value in sorted(values):
            result.append(f"-{value}")

    return "\n".join(result)
