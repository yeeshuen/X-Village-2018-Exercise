import json

with open('SearchShowAction.json' , encoding="utf-8") as f:
    musicshow = json.load(f)
    musicshow_str = json.dumps(musicshow, indent = 4 , ensure_ascii = False)
    print(musicshow_str)