import requests
def search_papers(topic, limit=5):
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={topic}&limit={limit}&fields=title,abstract,authors,year,url"
    response = requests.get(url)
    data = response.json()
    papers = data.get("data", [])
    results = []
    for p in papers:
        results.append({
            "title": p.get("title"),
            "abstract": p.get("abstract"),
            "year": p.get("year"),
            "url": p.get("url")
        })
     return results
