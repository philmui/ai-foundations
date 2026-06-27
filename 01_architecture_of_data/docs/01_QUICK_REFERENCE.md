# Module 01 Quick Reference

## Data Structure Comparison

| Feature | List | Dictionary |
|---------|------|------------|
| **Syntax** | `[1, 2, 3]` | `{"a": 1, "b": 2}` |
| **Access** | By index: `lst[0]` | By key: `dct["a"]` |
| **Lookup** | O(n) | O(1) ⚡ |
| **Insert** | O(1) append, O(n) insert | O(1) |
| **Delete** | O(n) | O(1) |
| **Ordered** | Yes | Yes (Python 3.7+) |
| **Mutable** | Yes | Yes |
| **Use for** | Sequences, iteration | Lookups, mappings |

## Big O Complexity (from fastest to slowest)

```
O(1)      ⚡ Constant    - Dict lookup, array index
O(log n)  ⚡ Logarithmic - Binary search
O(n)      ⚠️ Linear      - List search, single loop
O(n²)     ❌ Quadratic   - Nested loops
O(2ⁿ)     ❌ Exponential - Recursive fibonacci
```

## Mutability Quick Check

```python
# Immutable (creates new object)
id("hello")        # → 12345
id("hello".upper()) # → 67890 (different!)

# Mutable (modifies in-place)
lst = [1, 2, 3]
id(lst)            # → 11111
lst.append(4)
id(lst)            # → 11111 (same!)
```

## Common Operations

### Lists
```python
# Create
numbers = [1, 2, 3, 4, 5]

# Access
first = numbers[0]        # O(1)
last = numbers[-1]        # O(1)

# Search
if 3 in numbers:          # O(n) - slow!
    print("Found")

# Modify
numbers.append(6)         # O(1)
numbers.insert(0, 0)      # O(n)
numbers.remove(3)         # O(n)

# Iterate
for num in numbers:       # O(n)
    print(num)
```

### Dictionaries
```python
# Create
word_to_id = {"hello": 0, "world": 1}

# Access
token_id = word_to_id["hello"]              # O(1) - fast!
token_id = word_to_id.get("unknown", -1)    # O(1) with default

# Search
if "hello" in word_to_id:                   # O(1) - fast!
    print("Found")

# Modify
word_to_id["new"] = 2                       # O(1)
word_to_id.update({"foo": 3, "bar": 4})     # O(k) where k = keys added
del word_to_id["hello"]                     # O(1)

# Iterate
for word, idx in word_to_id.items():        # O(n)
    print(f"{word} → {idx}")
```

## Tokenizer Pattern

```python
# Step 1: Split text into words
text = "the quick brown fox"
words = text.lower().split()  # ["the", "quick", "brown", "fox"]

# Step 2: Build vocabulary (unique words)
vocab = sorted(set(words))

# Step 3: Create word-to-ID mapping (O(1) lookups!)
word_to_id = {word: idx for idx, word in enumerate(vocab)}
# {"brown": 0, "fox": 1, "quick": 2, "the": 3}

# Step 4: Create ID-to-word mapping (for decoding)
id_to_word = {idx: word for word, idx in word_to_id.items()}
# {0: "brown", 1: "fox", 2: "quick", 3: "the"}

# Step 5: Encode text to token IDs
token_ids = [word_to_id[word] for word in words]
# [3, 2, 0, 1]

# Step 6: Decode token IDs back to text
decoded = " ".join(id_to_word[token_id] for token_id in token_ids)
# "the quick brown fox"
```

## Word Frequency Counter

```python
# Method 1: Manual counting (educational)
text = "the quick brown fox jumps over the lazy dog"
words = text.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1  # O(1) increment
    else:
        freq[word] = 1   # O(1) insert

# Method 2: Using get() (cleaner)
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1  # O(1)

# Method 3: Using collections.Counter (best)
from collections import Counter
freq = Counter(words)  # O(n)

# Get most common words
most_common = freq.most_common(5)
# [('the', 2), ('quick', 1), ('brown', 1), ...]
```

## Nested Dictionary Navigation

```python
# Typical API response structure
response = {
    "model": "gpt-4",
    "usage": {
        "total_tokens": 45,
        "prompt_tokens": 15,
        "completion_tokens": 30
    },
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "Hello!"
            },
            "index": 0
        }
    ]
}

# Navigate nested structure
model = response["model"]                              # "gpt-4"
tokens = response["usage"]["total_tokens"]             # 45
message = response["choices"][0]["message"]["content"] # "Hello!"

# Safe navigation with .get()
tokens = response.get("usage", {}).get("total_tokens", 0)
```

## Performance Tips

### ✅ DO
```python
# Use dict for lookups
vocab = {"hello": 0, "world": 1, ...}  # 50K words
if word in vocab:                       # O(1)
    token_id = vocab[word]

# Build dict once, reuse many times
word_to_id = build_vocabulary(corpus)
for sentence in sentences:
    tokens = encode(sentence, word_to_id)

# Use list comprehensions for transformations
token_ids = [word_to_id[w] for w in words]
```

### ❌ DON'T
```python
# Don't use list for lookups
vocab = ["hello", "world", ...]        # 50K words
if word in vocab:                      # O(n) - slow!
    token_id = vocab.index(word)       # O(n) again!

# Don't rebuild dict in loops
for sentence in sentences:
    word_to_id = build_vocabulary(sentence)  # Wasteful!
    tokens = encode(sentence, word_to_id)

# Don't use loops when comprehensions work
token_ids = []
for word in words:
    token_ids.append(word_to_id[word])  # Slower than comprehension
```

## Common Mistakes

### Mistake 1: Mutating Function Arguments
```python
# ❌ BAD: Modifies original
def add_word(vocab_list, word):
    vocab_list.append(word)  # Side effect!
    return vocab_list

original = ["hello", "world"]
new_vocab = add_word(original, "goodbye")
print(original)  # ["hello", "world", "goodbye"] - Oops!

# ✅ GOOD: Return new list
def add_word(vocab_list, word):
    return vocab_list + [word]  # Creates new list

original = ["hello", "world"]
new_vocab = add_word(original, "goodbye")
print(original)  # ["hello", "world"] - Unchanged!
```

### Mistake 2: Using List for Membership Testing
```python
# ❌ BAD: O(n) lookup repeated
valid_words = ["the", "quick", "brown", ...]  # 50K words
for word in document.split():                  # 10K words
    if word in valid_words:                    # O(n)
        process(word)
# Total: O(n × m) = O(50K × 10K) = 500M operations!

# ✅ GOOD: O(1) lookup repeated
valid_words = {"the", "quick", "brown", ...}  # 50K words (set or dict)
for word in document.split():                 # 10K words
    if word in valid_words:                   # O(1)
        process(word)
# Total: O(n + m) = O(50K + 10K) = 60K operations!
```

### Mistake 3: Forgetting Default Values
```python
# ❌ BAD: KeyError if word not in dict
token_id = word_to_id[unknown_word]  # Crashes!

# ✅ GOOD: Use .get() with default
token_id = word_to_id.get(unknown_word, 0)  # Returns 0 if not found

# ✅ BETTER: Use defaultdict
from collections import defaultdict
word_to_id = defaultdict(lambda: 0)
token_id = word_to_id[unknown_word]  # Returns 0 automatically
```

## Memory Management

```python
import sys

# Check object size
numbers = [1, 2, 3, 4, 5]
print(sys.getsizeof(numbers))  # ~120 bytes

word_dict = {"hello": 0, "world": 1}
print(sys.getsizeof(word_dict))  # ~232 bytes

# Check object identity
a = [1, 2, 3]
b = a          # Same object
c = a.copy()   # Different object

print(id(a) == id(b))  # True
print(id(a) == id(c))  # False
```

## Why This Matters for AI

| Scenario | List Approach | Dict Approach | Impact |
|----------|---------------|---------------|--------|
| GPT-4 vocabulary (100K tokens) | O(n) per lookup | O(1) per lookup | **10,000x faster** |
| Processing 1M tokens | O(n × m) = O(100B) ops | O(m) = O(1M) ops | Real-time vs. hours |
| API response parsing | Linear scan | Direct key access | Instant access |
| Embedding lookup | Sequential search | Hash table | **1000x faster** |

## Quick Wins

1. **Always use dict for vocabulary/token lookups** in AI applications
2. **Build dict once, reuse everywhere** - don't rebuild in loops
3. **Use `word_to_id.get(word, default)`** to handle unknown words
4. **Prefer immutable data** when possible to avoid side effects
5. **Profile with `timeit`** when optimizing - measure, don't guess!

---

**Need more details?** See `README.md` for comprehensive documentation.

© mui-group | AI Research Foundations Minicourse
