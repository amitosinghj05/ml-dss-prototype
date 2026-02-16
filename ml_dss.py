def add_score(scores, reasons, algo, points, reason_text):
    scores[algo] += points
    reasons[algo].append(reason_text)


def ask_choice(prompt, options):
    """
    Shows numbered options and forces a valid selection.
    Returns the selected option text.
    """
    while True:
        print(prompt)
        for i, opt in enumerate(options, start=1):
            print(f"  {i}) {opt}")
        choice = input("Select an option number: ").strip()

        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(options):
                return options[idx - 1]

        print("Invalid input. Please choose a valid option number.\n")


def ask_yes_no(prompt):
    """
    Forces a valid y/n answer and returns True/False.
    """
    while True:
        ans = input(f"{prompt} (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Invalid input. Please type y or n.\n")


ALGORITHMS = [
    "Logistic Regression",
    "Linear Regression",
    "Decision Tree",
    "Random Forest",
    "XGBoost",
    "K-Means",
    "DBSCAN",
    "Isolation Forest",
    "One-Class SVM"
]


def main():
    print("\n=== ML Algorithm Decision Support System (Prototype) ===\n")

    task = ask_choice(
        "What is your problem type?",
        ["classification", "regression", "clustering", "anomaly_detection"]
    )

    data_size = ask_choice(
        "Approximate dataset size?",
        ["small", "medium", "large"]
    )

    interpretability = ask_yes_no("Do you need high interpretability (easy to explain)?")
    accuracy = ask_yes_no("Is maximum accuracy the top priority?")
    fast_training = ask_yes_no("Is fast training important (limited compute / quick iteration)?")

    # Initialize scores + reasons
    scores = {algo: 0 for algo in ALGORITHMS}
    reasons = {algo: [] for algo in ALGORITHMS}

    # -------------------------
    # Task-based scoring rules
    # -------------------------
    if task == "classification":
        add_score(scores, reasons, "Logistic Regression", 3, "Fits classification tasks well (strong baseline)")
        add_score(scores, reasons, "Decision Tree", 3, "Works for classification and is easy to interpret")
        add_score(scores, reasons, "Random Forest", 3, "Strong general-purpose classifier, robust to noise")
        add_score(scores, reasons, "XGBoost", 3, "Often top performance for tabular classification")

    elif task == "regression":
        add_score(scores, reasons, "Linear Regression", 3, "Fits regression tasks well (interpretable baseline)")
        add_score(scores, reasons, "Decision Tree", 2, "Captures non-linear relationships in regression")
        add_score(scores, reasons, "Random Forest", 3, "Strong general-purpose regressor, robust")
        add_score(scores, reasons, "XGBoost", 3, "Often top performance for tabular regression")

    elif task == "clustering":
        add_score(scores, reasons, "K-Means", 3, "Fast clustering when k is known and clusters are compact")
        add_score(scores, reasons, "DBSCAN", 3, "Good when clusters are irregular and outliers exist")

    elif task == "anomaly_detection":
        add_score(scores, reasons, "Isolation Forest", 3, "Strong default for unlabeled anomaly detection")
        add_score(scores, reasons, "One-Class SVM", 3, "Useful for anomaly detection on smaller datasets")

    # -------------------------
    # Preference-based rules
    # -------------------------
    if interpretability:
        add_score(scores, reasons, "Logistic Regression", 2, "High interpretability (coefficients are explainable)")
        add_score(scores, reasons, "Linear Regression", 2, "High interpretability (coefficients are explainable)")
        add_score(scores, reasons, "Decision Tree", 2, "Decision paths are easy to explain to stakeholders")

    if accuracy:
        add_score(scores, reasons, "Random Forest", 2, "Typically strong accuracy on many real-world datasets")
        add_score(scores, reasons, "XGBoost", 3, "Often achieves top accuracy with proper tuning")

    if fast_training:
        add_score(scores, reasons, "Logistic Regression", 2, "Fast to train (good for quick iteration)")
        add_score(scores, reasons, "Linear Regression", 2, "Fast to train (good for quick iteration)")
        add_score(scores, reasons, "K-Means", 2, "Fast to train and run on many datasets")
        add_score(scores, reasons, "XGBoost", -1, "Can be slower to train compared to simpler models")

    # -------------------------
    # Data size heuristics
    # -------------------------
    if data_size == "small":
        add_score(scores, reasons, "Decision Tree", 1, "Often works well on smaller datasets")
        add_score(scores, reasons, "One-Class SVM", 1, "Often better suited for smaller datasets")
    elif data_size == "large":
        add_score(scores, reasons, "XGBoost", 1, "Commonly used for larger tabular datasets")
        add_score(scores, reasons, "Random Forest", 1, "Scales reasonably for many large datasets")

    # -------------------------
    # Ranking and output
    # -------------------------
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    print("\n--- Top Recommendations ---")
    shown = 0
    for algo, score in ranked:
        if score <= 0:
            continue
        print(f"\n{algo} (score: {score})")
        for r in reasons[algo][:4]:
            print(f"  - {r}")
        shown += 1
        if shown == 3:
            break

    if shown == 0:
        print("No strong recommendations found based on inputs. Try different constraints.")

    print("\n--- End ---\n")


if __name__ == "__main__":
    main()
