ML Algorithm Decision Support System (DSS)

Overview:
This project is an initial prototype of a Decision Support System (DSS) that helps a user choose
an appropriate machine learning algorithm based on their problem type and constraints.

The working:
- Asks the user a small set of questions (task type, dataset size, preferences)
- Uses a rule + scoring approach to rank candidate algorithms
- Prints the top 3 recommendations along with short “why” explanations

This is a rule-based DSS prototype intended to demonstrate the core decision logic and explainability.
It can be extended later with more criteria and a UI

Requirements:
- Python 3.10+ (3.12 works)
- No external libraries required

Instructions to run:
1) Open a terminal in the project folder (where ml_dss.py is located)

2) Run:
   python ml_dss.py

3) Answer the prompts in the console.

Example Run (sample):
=== ML Algorithm Decision Support System (Prototype) ===

What is your problem type?
  1) classification
  2) regression
  3) clustering
  4) anomaly_detection
Select an option number: 1

Approximate dataset size?
  1) small
  2) medium
  3) large
Select an option number: 3

Do you need high interpretability (easy to explain)? (y/n): n
Is maximum accuracy the top priority? (y/n): y
Is fast training important (limited compute / quick iteration)? (y/n): n

--- Top Recommendations ---

XGBoost (score: 8)
  - Often top performance for tabular classification
  - Often achieves top accuracy with proper tuning
  - Commonly used for larger tabular datasets

Random Forest (score: 6)
  - Strong general-purpose classifier, robust to noise
  - Typically strong accuracy on many real-world datasets
  - Scales reasonably for many large datasets

Decision Tree (score: 3)
  - Works for classification and is easy to interpret


Potential next improvements:
- add more decision factors: imbalanced data, missing values, latency constraints, non-linear patterns
- expand algorithm coverage: SVM, KNN, Naive Bayes, Neural Nets, etc.
- provide metric guidance: precision/recall/F1, RMSE/MAE, silhouette score, etc.
- add “data type” questions: text, time-series, images
- build a small UI (Streamlit) and/or export recommendations as a short report

Files:
- ml_dss.py : CLI-based DSS prototype (rule + scoring + explanations)
- README.txt : project overview and instructions
