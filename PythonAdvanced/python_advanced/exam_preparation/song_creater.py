def add_songs(*tuples):
    songs = {}

    for t in tuples:
        song, lyrics = t

        if song not in songs:
            songs[song] = []

        songs[song].extend(lyrics)

    output = []

    for s_title, s_lyrics in songs.items():
        output.append("- " + s_title)
        output.extend(s_lyrics)

    return "\n".join(output)
