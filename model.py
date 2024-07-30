import re
import openai
import arxiv
from tqdm import tqdm

def clean_query(query):
    # Use a simple function to clean the query
    return query.strip()

def get_relevant_research(cleaned_query):
    search = arxiv.Search(
        query=cleaned_query,
        max_results=8,
        sort_by=arxiv.SortCriterion.Relevance
    )
    results = [result for result in search.results()]
    return results, [result.pdf_url for result in results]

def summarize_papers(papers, openai_api_key):
    openai.api_key = openai_api_key
    summaries = []
    for paper in tqdm(papers):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Summarize the following research paper:\n\n{paper.summary}",
            max_tokens=200
        )
        summary = response.choices[0].text.strip()
        summaries.append(summary)
    return summaries

def make_paper_recommendation(summaries, query, openai_api_key):
    openai.api_key = openai_api_key
    prompt = "Based on the following summaries of research papers and their relevance to the query, provide a detailed recommendation including explanations and potential next steps for research:\n\n"
    for i, summary in enumerate(summaries):
        prompt += f"{i+1}. {summary}\n"
    prompt += f"\nQuery: {query}\n\nRecommendation:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=512
    )
    recommendation = response.choices[0].text.strip()
    return recommendation
