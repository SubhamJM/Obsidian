## Form of Data:

- Train dataset and test dataset both are in json format
![[Pasted image 20260729230144.png]]

_BIO Format:_ 
- B- means starting of an entity
- I- means ongoing entity text
- O- menas outside, not an entity


### Key takeaways:

- The tokenization into words is already given along with individual word's label
- labels correspond to each token
- using a transformer model for this will likely need another layer of tokenisation so might have to extend the labels for the new tokens. [[Prototyping]]
