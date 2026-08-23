- There are many different chunking stratergies for RAG Applications

# All the stratergies:

## 1. *Fixed Size chunking:*
	We fix some amount of characters to split the documents at 
	- It is the simplest method
	- Only should be used for prototyping
	
	**Some Limitations**:
	- Loses symantic meaning
	- Cuts sentences in middle
	
	**Application methods:**
	- Maybe overlap some amount of characters between chunks
	
	*Key insights:*
	- Too small chunking = no context
	- Too large chunking = diluted context
	- Should be an average sized chunking like 200-800 for better context grabbing