# AI Tools and Applications Project

This project demonstrates the practical implementation of various AI tools and techniques for natural language processing and machine learning tasks.

## Project Overview

The project consists of three main tasks:
1. Text Classification using NLTK
2. Sentiment Analysis using TextBlob
3. Named Entity Recognition and Sentiment Analysis using spaCy

## Theoretical Understanding

### Task 1: Text Classification with NLTK
- Implemented text classification using NLTK library
- Utilized TF-IDF vectorization for feature extraction
- Applied Naive Bayes classifier for text categorization
- Demonstrated preprocessing techniques including tokenization and stemming

### Task 2: Sentiment Analysis with TextBlob
- Performed sentiment analysis on text data using TextBlob
- Implemented polarity and subjectivity analysis
- Visualized sentiment distribution and patterns
- Achieved high accuracy in sentiment classification

### Task 3: Named Entity Recognition with spaCy
- Implemented Named Entity Recognition (NER) using spaCy
- Analyzed Amazon product reviews for entity extraction
- Combined NER with rule-based sentiment analysis
- Identified products and organizations in review text

## Implementation Details

### Task 1 Implementation
![Task 1 Implementation](Practical_Implementation/Screenshots/Task1implemetation.PNG)

### Task 2 Implementation
![Task 2 Implementation](Practical_Implementation/Screenshots/task2implementation1.PNG)

### Task 2 Visualization
![Task 2 Visualization](Practical_Implementation/Screenshots/task2visualisation.PNG)

### Task 2 Accuracy
![Task 2 Accuracy](Practical_Implementation/Screenshots/Task2accuracy.PNG)

## Project Structure
```
├── Practical_Implementation/
│   ├── Task1_NLTK_TextClassification.ipynb
│   ├── Task2_TextBlob_SentimentAnalysis.ipynb
│   ├── Task3_spaCy_AmazonReviews.ipynb
│   ├── Screenshots/
│   │   ├── Task1implemetation.PNG
│   │   ├── task2implementation1.PNG
│   │   ├── task2visualisation.PNG
│   │   └── Task2accuracy.PNG
│   └── content/
│       └── amazon/
│           └── amazon_reviews.csv
```

## Requirements
- Python 3.8+
- NLTK
- TextBlob
- spaCy
- pandas
- numpy
- matplotlib
- seaborn

## Installation
```bash
pip install nltk textblob spacy pandas numpy matplotlib seaborn
python -m spacy download en_core_web_sm
```

## Usage
1. Clone the repository
2. Install the required dependencies
3. Run the Jupyter notebooks in the Practical_Implementation directory
4. Follow the implementation steps in each notebook

## Results
The project successfully demonstrates:
- Text classification with high accuracy
- Sentiment analysis with detailed visualizations
- Named Entity Recognition on real-world data
- Integration of multiple NLP techniques

## Author
Cpt. Njenga 
