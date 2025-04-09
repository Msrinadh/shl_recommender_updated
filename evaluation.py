import numpy as np

def mapk(actual, predicted, k=10):
    def apk(a, p, k):
        p = p[:k]
        score, hits = 0.0, 0.0
        for i, pred in enumerate(p):
            if pred in a:
                hits += 1
                score += hits / (i + 1)
        return score / min(len(a), k)
    
    return np.mean([apk(a, p, k) for a, p in zip(actual, predicted)])

def recall_at_k(actual, predicted, k=10):
    return np.mean([len(set(p[:k]) & set(a)) / len(a) for a, p in zip(actual, predicted)])

if __name__ == "__main__":
    ground_truth = [
        {'query': 'sales executive', 'relevant': ['Sales Capability Test']},
        {'query': 'software engineer', 'relevant': ['Technical Skills Assessment']}
    ]
    predicted = [
        ['Sales Capability Test', 'Leadership Potential Test'],
        ['Technical Skills Assessment', 'Cognitive Ability Test']
    ]
    print("MAP@2:", mapk([g['relevant'] for g in ground_truth], predicted, k=2))
    print("Recall@2:", recall_at_k([g['relevant'] for g in ground_truth], predicted, k=2))