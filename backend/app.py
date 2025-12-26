from analyzer import load_events, build_timeline
from detector import detect_disengagement
from explainer import generate_explanation

EVENTS_PATH = "data/events.json"

def run():
    events = load_events(EVENTS_PATH)
    timelines = build_timeline(events)

    for student_id, timestamps in timelines.items():
        disengaged, reasons, confidence = detect_disengagement(timestamps)

        print("\n==============================")
        print(f"Student: {student_id}")

        if disengaged:
            explanation = generate_explanation(student_id, reasons, confidence)
            print(explanation)
        else:
            print("No disengagement detected.")

if __name__ == "__main__":
    run()
