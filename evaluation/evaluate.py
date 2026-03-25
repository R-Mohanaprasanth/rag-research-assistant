# evaluate.py
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from datasets import Dataset

def run_eval(pipeline, test_data):
    rows = []

    for item in test_data:
        ans, docs = pipeline(item["question"])
        rows.append({
            "question": item["question"],
            "answer": ans,
            "contexts": [d["content"] for d in docs],
            "ground_truth": item["ground_truth"]
        })

    dataset = Dataset.from_list(rows)

    return evaluate(dataset, metrics=[
        faithfulness,
        answer_relevancy,
        context_precision
    ])