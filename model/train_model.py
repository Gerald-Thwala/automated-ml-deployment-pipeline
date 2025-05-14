import os
import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Sample synthetic dataset: 6 DNA sequences, labeled coding (1) or non-coding (0)
data = [
    ("ATGCGTACGTAG", 1),
    ("GCGTATATATCG", 0),
    ("ATGCCCGGGTTT", 1),
    ("TTATATATACCC", 0),
    ("ATGATGATGATG", 1),
    ("CGCGTATAAAAA", 0)
]

def kmer_counts(seq, k=3):
    """Convert DNA sequence into k-mer frequency vector."""
    counts = {}
    total = len(seq) - k + 1
    for i in range(total):
        kmer = seq[i:i+k]
        counts[kmer] = counts.get(kmer, 0) + 1
    # Normalize to frequency
    for k in counts:
        counts[k] /= total
    return counts

def vectorize(seqs, k=3):
    """Convert list of sequences into feature vectors based on k-mer frequencies."""
    all_kmers = set()
    for seq in seqs:
        all_kmers.update(kmer_counts(seq, k).keys())
    all_kmers = sorted(all_kmers)
    
    vectors = []
    for seq in seqs:
        counts = kmer_counts(seq, k)
        vec = [counts.get(kmer, 0) for kmer in all_kmers]
        vectors.append(vec)
    
    return np.array(vectors), all_kmers

def main():
    sequences, labels = zip(*data)
    X, feature_names = vectorize(sequences)
    y = np.array(labels)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Evaluation on test set:")
    print(classification_report(y_test, y_pred))

    os.makedirs("model", exist_ok=True)
    joblib.dump((model, feature_names), "model/model.pkl")
    print("Model saved to model/model.pkl")

if __name__ == "__main__":
    main()
