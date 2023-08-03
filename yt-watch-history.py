import json
 
f = open("watch-history.json", encoding="utf8")
 
data = json.load(f)
pruned = {}
 
music = True
for entry in data:
    if "subtitles" in entry:
        #ENG VERSION (entry["title"] != "Visited YouTube Music")
        #entry["header"] == "YouTube" pro norm. videa "YouTube Music" pro ytmusic
        if ((entry["header"] == "YouTube Music") == music) and (entry["title"] != "Zhlédnutí videa, které bylo odstraněno") and ("https://www.youtube.com/watch?v=" not in entry["title"]) and (entry["title"] != "Watched a video that has been removed"):
            
            title = entry["title"][8::] 
            time = entry["time"]  

            if music:
                artist  = entry["subtitles"][0]["name"].replace(" - Topic", "")
                title = f'{title} - {artist}'.replace("jste video ","")
                #, last watched: {time}
    
            if title in pruned:
                pruned[title] = pruned[title] + 1
                pruned[time] = time
            else:
                pruned[title] = 1
                pruned[time] = time

total_plays = 0
 
for song, listens in dict(sorted(pruned.items(), key=lambda item: item[1])).items():
    total_plays += listens
    print(f'{song} [times listened: {listens}] [last watched: {time}]')
 
print(f'{total_plays} total plays across all tracks')