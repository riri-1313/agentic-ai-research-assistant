from search import search_papers
from summarize import summarize_text
from gap_detection import detect_gaps
from draft_generator import generate_draft

topic = input("Enter your research topic: ")

print("\nSTEP 1: Searching papers...")
papers = search_papers(topic)
print(f"Found {len(papers)} papers.\n")

summaries = []

print("STEP 2: Summarizing papers...")
for p in papers:
    if p['abstract']:
        summary = summarize_text(p['abstract'])
        summaries.append(summary)
        print("\nSummary:", summary)

print("\nSTEP 3: Detecting research gaps...")
gaps = detect_gaps(summaries)
for g in gaps:
    print("- ", g)

print("\nSTEP 4: Generating draft...")
draft = generate_draft(topic, summaries, gaps)
print("\nDraft:\n")
print(draft)
