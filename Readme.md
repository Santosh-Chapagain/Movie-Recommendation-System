# Recommendation System

## Overview

This project is a **Content-Based Recommendation System** built using Python.  
It analyzes the textual features of items (such as movies) and recommends the most similar items based on their content.

The system uses:

- **CountVectorizer** for text vectorization  
- **Cosine Similarity** for similarity measurement  
- **Pandas** & **NumPy** for data handling  

---

## How It Works

1. Important text features (like genre, keywords, cast, etc.) are combined into a single string.  
2. `CountVectorizer` converts this text into a matrix of token counts.  
3. `cosine_similarity()` is applied to compute similarity between all items.  
4. Based on the similarity score, the system returns the **top recommended items**.
