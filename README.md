Planetary CARE Research Library Builder
=======================================

Algorithms, Frameworks, and Libraries Used:
-------------------------------------------

1. Pyzotero (Python Zotero API Wrapper)
2. JSON
2. Pandas
<!-- 3. Pdf2txt
4. Numpy
5. Joblib (Parallel Processing)
6. TF-IDF (Custom Implementation)
7. Gensim (Stop Word Filter)
8. Dask
9. Docker
10. AWS (EC2)
11. GCS (Data Extraction)
 -->

Project Scope
-------------

The goal of this project was to collect URLs of scientific articles most relevant to the field of [Regenerative Agriculture](https://en.wikipedia.org/wiki/Regenerative_agriculture). These articles will be used as the beginning of a Knowledge Management System (KMS), in the form of a digital research library, for the [Planetary CARE](https://planetarycare.org) organization. A custom-built, TF-IDF based, Recommender System has been retooled to select the articles from the ArXiv repository which are most similar to a curated set of keywords. These keywords were extracted from the 'Tag' words associated with all the articles in the [PCARE Regenag.info](https://www.zotero.org/groups/pcare_regenag.info) Zotero citation collection at the time of writing (November 2021).

Stage 1 - Keyword Sourcing
--------------------------

The keywords used to find the most relevant articles were extracted using the [Pyzotero](https://pyzotero.readthedocs.io/en/latest/) Python wrapper, which can be used to retrieve metadata from any Zotero collection. The metadata was filtered to find the unique set of words used as tags for all the citations in the collection.
<!-- 7. Dask
8. Docker
9. AWS (EC2)
10. GCS (Data Extraction)

Here you can find the source project whose modules were modified to perform these tasks:

[Dataset Source and Extraction Tools](https://github.com/mattbierbaum/arxiv-public-datasets)

This is where to find my modified code, used to parse the PDFs:

[arxiv_public_data](https://github.com/christianspybrook/article_recommender/tree/master/arxiv_public_data)


Stage 2 - Document Selection and Text Preprocessing
---------------------------------------------------

After the raw text had been extracted from the full PDFs, preprocessing of the data could begin.

As the original dataset contained all of the draft stages of the articles, I created a filter to keep only the final version of each. I filtered out a small set of articles that gave encoding errors, as well.
To decide which stopwords to remove from the text, I wrote a script to identify which library would filter the greatest number of stopwords from a large sample of the dataset. The stopwords used by the Gensim library were chosen.
After some exploratory analysis of different cleaning methods, a final preprocessing pipeline was built.

This is the final script used:

[raw_text_cleaner.py](https://github.com/christianspybrook/article_recommender/blob/master/training/pdf_parsing/raw_text_cleaner.py)

The preprocessing methods used to clean the text data, before tokenization and embedding, can be found here :

[pdf_parsing](https://github.com/christianspybrook/article_recommender/tree/master/training/pdf_parsing)

Stage 3 - Word Embedding and Model Construction
-----------------------------------------------

Before beginning the tokenization process, I wrote a script to collect the file paths for either a random subset of the articles or the full set of nearly 1.5 million articles to use for the model's possible recommendations. After building this list of articles, I constructed a function designed to generate a word embedding of the data. Subsequently, the function can be used to remove tokens from the embedding based on specified minimum document appearances and desired maximum dictionary size. Finally, the function builds a dictionary mapping between the words and their index representations, a Term Frequency (TF) matrix, and an Inverse Document Frequency (IDF) matrix. The two matrices are combined to build the TF-IDF model. The final Numpy array holds over 7 trillion parameters.

The embedding and model construction scripts can be found here:

[tf_idf](https://github.com/christianspybrook/article_recommender/tree/master/training/tf_idf)
 -->
<!-- Project Workflow:
-----------------

[Data Preprocessing](https://github.com/christianspybrook/eluvio_coding_challenge/blob/master/data_preprocessing/preprocessing.ipynb):  
&nbsp;&nbsp;&nbsp;&nbsp;- [x] Determine Business Objective  
&nbsp;&nbsp;&nbsp;&nbsp;- [x] Reduce Memory Footprint  
&nbsp;&nbsp;&nbsp;&nbsp;- [x] Feature Engineering  
[Topic Modeling](https://github.com/christianspybrook/eluvio_coding_challenge/blob/master/modeling/topic_modeling.ipynb):  
&nbsp;&nbsp;&nbsp;&nbsp;- [x] Text Tokenization Pipeline  
&nbsp;&nbsp;&nbsp;&nbsp;- [x] Latent Dirichlet Allocation  
&nbsp;&nbsp;&nbsp;&nbsp;- [x] Topic Analysis & Visualization  
[Classifier Selection](https://github.com/christianspybrook/eluvio_coding_challenge/blob/master/modeling/classification_model_selection.ipynb):  
&nbsp;&nbsp;&nbsp;&nbsp;- [x] Cross Validation Pipeline  
&nbsp;&nbsp;&nbsp;&nbsp;- [x] Analysis & Model Selection  
[Random Forest Optimization](https://github.com/christianspybrook/eluvio_coding_challenge/blob/master/modeling/rf_classifier.ipynb):  
&nbsp;&nbsp;&nbsp;&nbsp;- [x] Bayesian Hyperparameter Search  
&nbsp;&nbsp;&nbsp;&nbsp;- [x] Analysis & Final Model Selection    
&nbsp;&nbsp;&nbsp;&nbsp;- [x] Test Performance  
Coming Soon:  
&nbsp;&nbsp;&nbsp;&nbsp;- [ ] Neural Network Regression  
&nbsp;&nbsp;&nbsp;&nbsp;- [ ] Out of Memory Modifications Using Dask

In Progress...  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;more coming, but ready for submission as is.
 -->