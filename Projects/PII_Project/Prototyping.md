# 1. Trial (Using DistilBERT):

- Used LLMs to know more about the process of PII detecion.
- Used DistilBERT tokenizer to tokenize the tokens given and then extended the labels accordingly

### Key Takeaways:

1. How tokenizers work: Basically we want to have a general token structure so that we can convert that into embeddings for the model so we use tokenizers to further tokenize the tokens given.
2. splitting the words into sub tokens will create more input than there are labels, so we need to extend the labels list.
3. using -100 label in pytorch makes it so that during training that input and label gets ignored.
4. during tokenization, special characters get added which we want to avoid like [PAD], [UNK], []