import json
#ENG VERSION = json file in english 
f = open("watch-history.json", encoding="utf8")
 
data = json.load(f)
pruned = {}
 
music = True
for entry in data:
    if "subtitles" in entry:

        #FOR ALL YOUTUBE VIDS entry["header"] == "YouTube" 
        if ((entry["header"] == "YouTube Music") == music) and (entry["title"] != "Zhlédnutí videa, které bylo odstraněno") and ("https://www.youtube.com/watch?v=" not in entry["title"]) and (entry["title"] != "Watched a video that has been removed"):
        #ENG VERSION (entry["title"] != "Visited YouTube Music")
            title = entry["title"][8::] 

            if music:
                artist  = entry["subtitles"][0]["name"].replace(" - Topic", "")
                title = f'{title} - {artist}'.replace("jste video ","")
                #ENG VERSION no need for .replace("jste video ","")
    
            if title in pruned:
                pruned[title] = pruned[title] + 1
            else:
                pruned[title] = 1

total_plays = 0
 
for song, listens in dict(sorted(pruned.items(), key=lambda item: item[1])).items():
    total_plays += listens
    print(f'{song} [times listened: {listens}]')
 
print(f'{total_plays} total plays across all tracks')