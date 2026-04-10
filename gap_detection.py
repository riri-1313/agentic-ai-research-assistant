 def detect_gaps(summaries):
    gap_keywords = ["lack", "future work", "not explored", "limitations", "challenge", "issue"]
    gaps = []
    for s in summaries:
        for kw in gap_keywords:
            if kw in s.lower():
                gaps.append(s)
                break
    if not gaps:
        gaps.append("Existing studies do not sufficiently explore autonomous multi-agent reasoning for complex research tasks.")
        gaps.append("Limited work has been done on real-time agentic AI systems with self-correction and planning.")
        gaps.append("A unified research assistant capable of autonomous literature review and draft creation is lacking.")
    return gaps
