# Simple Tokenizer
# importing modules
import re # regular expression
import tiktoken # BPE implementations
import importlib # metadata of BPE

# Opening the file
with open("/home/akash/Downloads/the-verdict.txt","r",encoding="utf-8") as f :
    raw_text = f.read()

# checking original size of the book
original_text_size = len(raw_text)
print("Length of original book is : ",original_text_size)

# split the words and special characters
preprocessed = re.split(r'([,.:;?_!()\']|--|\s)', raw_text)
preprocessed = [item for item in preprocessed if item.strip()]
print(preprocessed[:199])
preprocessed_size = len(preprocessed)
print("Size after splitting all the words : ",preprocessed_size)

# converting tokens to tokenIDs
all_words = sorted(set(preprocessed))
all_words_size = len(all_words)
print("Size after sorting the tokens : ",all_words_size)

# assigned integer to the tokens
# key-value pairs are stored in vocab
vocab = {token:integer for integer, token in enumerate(all_words)}
print(vocab)

# assigned tokens to the integers
de_vocab = {integer:token for token,integer in vocab.items()}
print(de_vocab)

# tokenizer class
class SimpleTokenizer :
    def __init__(self,vocab,de_vocab):
        self.str_to_int = vocab
        self.int_to_str = de_vocab

    # encoding method
    def encode(self,text):
        data_preprocessed = re.split(r'[,.:;?!_()\']|--|\s',text)
        data_preprocessed = [item for item in data_preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in data_preprocessed]
        return ids

    # decoding method
    def decode(self,ids):
        text = " ".join(self.int_to_str[i] for i in ids)
        text = re.sub(r'\s+([,.:;?_!()\]])',r'\1',text)
        return text

# calling the class
tokenizer = SimpleTokenizer(vocab,de_vocab)
new_text = """It's the last he painted, you know," Mrs. Gisburn said with pardonable pride. "The last but one," she corrected herself--"but the other doesn't count, because he destroyed it."""
token_ids = tokenizer.encode(new_text)
print(token_ids)
normal_text = tokenizer.decode(token_ids)
print(normal_text)

# BPE tokens encodings
# BPE is also Sub-word tokenization
# BPE tokenization from GPT-2
tokenizer = tiktoken.get_encoding("gpt2")
bpe_text = (
    "Hello, do you like tea? <|endoftext|> In the sunlight terraces""of someunknownPlaces."
)
integers = tokenizer.encode(bpe_text, allowed_special={"<|endoftext|>"})
print(integers)