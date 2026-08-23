- There are many different chunking stratergies for RAG Applications
### 1. *Fixed Size chunking:*

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


## 2. Structure Aware chunking:

- Creating symantically coherent chunks

*Application*:
- Use recursive text splitters to capture coherent sections like paragraphs or sentences. 

> Using things like '\n\n' and '\n' and maybe some headings for splitting chunks


## 3. Metadata-Enriched chunking

- Adding meta datas like page number, Headings, and all those to the documents itself.
- Adding Metadata increases context of the chunk.
- Easy to retrieve and filter


## 4. Parent-Child + (sliding Window)

- Smaller chunks are good for embedding (more context rich)
- but having many chunks increases search complexity during retrieval

*Key idea*:
- Having Parent chunk which is larger
  and having child chunks that come under the parent chunks
- The searching can happen with parent chunk's context
- and after a parent chunk is retrived, then smaller chunks can be used to get rich contextual meaning


## 5. Semantic chunking + Propositions

