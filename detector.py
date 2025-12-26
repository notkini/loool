def detect_disengagement(timestamps):
    if len(timestamps) < 3:
        return False, [], 0.0

    gaps = []
    for i in range(1, len(timestamps)):
        gaps.append((timestamps[i] - timestamps[i - 1]).days)

    recent_gap = gaps[-1]
    avg_gap = sum(gaps[:-1]) / max(len(gaps[:-1]), 1)

    reasons = []
    confidence = 0.0

    if recent_gap > avg_gap * 1.5:
        reasons.append(
            f"Engagement gap increased from an average of {avg_gap:.1f} days to {recent_gap} days"
        )
        confidence = min(recent_gap / (avg_gap + 1), 1.0)

    disengaged = len(reasons) > 0
    return disengaged, reasons, round(confidence, 2)
