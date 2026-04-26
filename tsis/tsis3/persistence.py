import json, os

DEFAULTS = {"sound": True, "car_color": "default", "difficulty": "normal"}

def load_settings():
    if os.path.exists("settings.json"):
        try:
            d = json.load(open("settings.json"))
            for k, v in DEFAULTS.items():
                d.setdefault(k, v)
            return d
        except: pass
    return DEFAULTS.copy()

def save_settings(s):
    json.dump(s, open("settings.json", "w"), indent=2)

def load_leaderboard():
    if os.path.exists("leaderboard.json"):
        try: return json.load(open("leaderboard.json"))
        except: pass
    return []

def save_score(name, score, distance, coins):
    board = load_leaderboard()
    board.append({"name": name, "score": score, "distance": distance, "coins": coins})
    board = sorted(board, key=lambda x: x["score"], reverse=True)[:10]
    json.dump(board, open("leaderboard.json", "w"), indent=2)
    return board