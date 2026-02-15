def generate_draft(topic, summaries, gaps):
    draft = f"Research Topic: {topic}\n\n"
    draft += "Summary of Existing Work:\n"
    for s in summaries:
        draft += f"- {s}\n"
    draft += "\nResearch Gaps:\n"
    for g in gaps:
        draft += f"- {g}\n"
    draft += "\nProposed Direction:\n"
    draft += "This research aims to explore the above gaps using agentic AI-based methods."
    return draft
