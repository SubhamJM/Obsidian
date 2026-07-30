
![[Pasted image 20260729232116.png]]

---

> -> Number of normal words way too much exceeds the special entity words.
> -> Normal models like CRF and BiLSTM will struggle to capture the pattern
> -> Transformers is needed to capture the big picture here.

![[Pasted image 20260729232158.png]]

- _Some entities only have single or two digit occurances which will be extremely hard to capture the pattern for them._

![[Pasted image 20260729232508.png|686]]

---


![[Pasted image 20260729232436.png]]

*Most of the documents are in the range of 500 - 1000 range*
- Using a max_length of 512 for tokenization will be good for efficiency and performance purposes

