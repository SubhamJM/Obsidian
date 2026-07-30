# 1. Trial (Using DistilBERT):

- Used LLMs to know more about the process of PII detecion.
- Used DistilBERT tokenizer to tokenize the tokens given and then extended the labels accordingly
- watched some youtube tutorials about the PII detection

### Key Takeaways:

1. How tokenizers work: Basically we want to have a general token structure so that we can convert that into embeddings for the model so we use tokenizers to further tokenize the tokens given.
2. splitting the words into sub tokens will create more input than there are labels, so we need to extend the labels list.
3. using -100 label in pytorch makes it so that during training that input and label gets ignored.
4. during tokenization, special characters get added which we want to avoid like [PAD], [UNK], etc. so we assign label to them as -100.
### Results and Conclusion

1. The prototype was unsuccessful, because somehow i messed up the tokenization part where we have to extend the labels. all the labels were either 5 or -100.
2. Learnt the process of the whole NLP thing from data preparing to model training.
3. Did some amount of [[EDA]]

---

# 2. Prototype2:


1. 2nd prototype was short, it failed early because i realised that normal CRF model is not good enough to capture the context of the whole sentence.
2. I 