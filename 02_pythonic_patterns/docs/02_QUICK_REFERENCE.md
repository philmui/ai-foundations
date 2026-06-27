# Quick Reference: Pythonic Patterns

## List Comprehension Syntax

### Basic Pattern
```python
[expression for item in iterable]
```

### With Condition
```python
[expression for item in iterable if condition]
```

### Examples
```python
# Square all numbers
squares = [x**2 for x in range(10)]

# Filter and transform
positive = [x for x in numbers if x > 0]

# String processing
cleaned = [line.strip().lower() for line in file]

# With conditional expression
labels = ['even' if x % 2 == 0 else 'odd' for x in range(10)]
```

## Dict Comprehension Syntax

### Basic Pattern
```python
{key_expr: value_expr for item in iterable}
```

### With Condition
```python
{key_expr: value_expr for item in iterable if condition}
```

### Examples
```python
# Build vocabulary (word → frequency)
vocab = {word: words.count(word) for word in set(words)}

# Transform dictionary
squared = {k: v**2 for k, v in original.items()}

# Filter dictionary
filtered = {k: v for k, v in original.items() if v > 0}

# Invert dictionary
inverted = {v: k for k, v in original.items()}
```

## Set Comprehension

```python
# Unique values only
unique_words = {word.lower() for word in words}
```

## Nested Comprehensions

```python
# Flatten 2D list
flat = [item for row in matrix for item in row]

# Matrix transposition
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Reading: outer loop first, inner loop second
# Result: [matrix[0][i], matrix[1][i], matrix[2][i], ...]
```

## Generator Function Patterns

### Basic Generator with `yield`
```python
def generate_numbers(n):
    for i in range(n):
        yield i**2

# Usage
for square in generate_numbers(10):
    print(square)
```

### Batch Generator
```python
def batch_generator(data, batch_size):
    batch = []
    for item in data:
        batch.append(item)
        if len(batch) >= batch_size:
            yield batch
            batch = []
    if batch:  # Don't forget remaining items
        yield batch
```

### File Streaming Generator
```python
def stream_file(filename, chunk_size=1024):
    with open(filename) as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk
```

### `yield from` Pattern
```python
def flatten(nested_list):
    for sublist in nested_list:
        yield from sublist

# Equivalent to:
# for sublist in nested_list:
#     for item in sublist:
#         yield item
```

## Generator Expressions

### Syntax
```python
(expression for item in iterable)
```

### Examples
```python
# Lazy squares (no memory allocation until consumed)
squares = (x**2 for x in range(1000000))

# Use with next()
first = next(squares)  # 0
second = next(squares)  # 1

# Convert to list (defeats laziness)
all_squares = list(squares)

# Use in for loop (memory efficient)
for square in (x**2 for x in range(1000000)):
    if square > 1000:
        break
```

## Memory Comparison: List vs Generator

| Operation | List | Generator |
|-----------|------|-----------|
| Creation | `[x**2 for x in range(n)]` | `(x**2 for x in range(n))` |
| Memory | O(n) - all values stored | O(1) - one value at a time |
| Speed | Fast access after creation | Slower per-item (recomputes) |
| Reusable | Yes (can iterate multiple times) | No (exhausted after one pass) |
| Best for | Small datasets, random access | Large datasets, one-pass processing |

## Common Gotchas

### 1. Generator Exhaustion
```python
gen = (x for x in range(3))
list(gen)  # [0, 1, 2]
list(gen)  # [] - exhausted!

# Solution: recreate or convert to list first
data = list(gen)
```

### 2. Scope in Comprehensions
```python
# Variables in comprehension don't leak
[x for x in range(10)]
print(x)  # NameError! (in Python 3)
```

### 3. Nested Comprehension Order
```python
# WRONG intuition: "for each i, for each row"
# CORRECT: "for each row, extract column i"
[[row[i] for row in matrix] for i in range(cols)]
#  ^inner loop^              ^outer loop^
```

### 4. Mutable Default in Generator
```python
# WRONG: batch list is shared!
def batch_gen(data, batch=[]):  # DON'T DO THIS
    ...

# CORRECT: create new list each time
def batch_gen(data, batch_size=100):
    batch = []  # Fresh list
    ...
```

## Key Functions for Iteration

| Function | Purpose | Example |
|----------|---------|---------|
| `next(gen)` | Get next value from generator | `next(squares)` |
| `iter(obj)` | Create iterator from iterable | `it = iter([1,2,3])` |
| `enumerate(it)` | Get index + value | `for i, x in enumerate(data)` |
| `zip(it1, it2)` | Pair elements from iterables | `for x, y in zip(xs, ys)` |
| `itertools.islice()` | Slice generator (lazy) | `islice(gen, 10, 20)` |
| `itertools.chain()` | Chain generators | `chain(gen1, gen2)` |

## Performance Tips

1. **Use comprehensions for small datasets** (< 10,000 items)
   - Faster than equivalent for loops
   - More readable

2. **Use generators for large datasets** (> 100,000 items)
   - Memory efficient
   - Can process data larger than RAM

3. **Avoid repeated work in comprehensions**
   ```python
   # BAD: calls expensive_fn() many times
   [expensive_fn(x) for x in data if expensive_fn(x) > 0]
   
   # GOOD: compute once
   [result for x in data if (result := expensive_fn(x)) > 0]
   ```

4. **Generator for one pass, list for multiple passes**
   ```python
   # If you need the data multiple times, convert to list
   data = list(generate_data())
   
   # If you only iterate once, stay lazy
   for item in generate_data():
       process(item)
   ```

## Connection to PyTorch DataLoader

```python
# PyTorch's DataLoader is essentially:
def dataloader(dataset, batch_size):
    indices = list(range(len(dataset)))
    for i in range(0, len(indices), batch_size):
        batch_indices = indices[i:i+batch_size]
        yield [dataset[idx] for idx in batch_indices]

# Usage (lazy batching)
for batch in dataloader(dataset, batch_size=32):
    train(model, batch)
```

Key takeaway: Production AI systems use generators everywhere for memory efficiency.
