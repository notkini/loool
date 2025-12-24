import json
from datetime import datetime
from collections import defaultdict

def load_events(path):
    with open(path, "r") as f:
        return json.load(f)

def build_timeline(events):
    timeline = defaultdict(list)

    for e in events:
        ts = datetime.fromisoformat(e["timestamp"])
        timeline[e["student_id"]].append(ts)

    for student in timeline:
        timeline[student].sort()

    return timeline
