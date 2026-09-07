# NumPy Arrays & Vectorised Operations

> **80/20 Focus:** Arrays, broadcasting, and vectorisation are 80% of ML-relevant NumPy. Skip the rest until you need it.

---

## The Mental Model

Think of a Python list as a general-purpose shopping bag — it can hold anything but is slow for math. A NumPy array is a **fixed-type contiguous block of memory** — like a typed C array with a Python wrapper. Because every element is the same type and stored adjacently, the CPU can operate on entire rows/columns at once using SIMD instructions. That's why `np.sum(arr)` is 100× faster than `sum(arr)`.

**Vectorisation** = replacing explicit Python loops with NumPy operations that run in compiled C/Fortran under the hood.

---

## Core 20%

### 1. Array Creation

```python
import numpy as np

a = np.array([1, 2, 3])              # from list — dtype inferred (int64)
b = np.array([1.0, 2.0, 3.0])       # float64
c = np.zeros((3, 4))                 # 3×4 matrix of 0.0
d = np.ones((2, 3), dtype=np.int32)
e = np.arange(0, 10, 2)             # [0, 2, 4, 6, 8]
f = np.linspace(0, 1, 5)            # [0.0, 0.25, 0.5, 0.75, 1.0]
g = np.random.randn(3, 3)           # standard normal
```

### 2. Shape, Dtype, Rank

```python
arr = np.random.randn(100, 768)

arr.shape   # (100, 768) — tuple of dimension sizes
arr.ndim    # 2 — number of dimensions (rank)
arr.dtype   # float64
arr.size    # 76800 — total elements
```

**Key insight:** shape tells you everything about the array's structure. Most ML bugs come from shape mismatches.

### 3. Indexing & Slicing

```python
arr = np.arange(12).reshape(3, 4)
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])

arr[1, 2]       # 6 — row 1, col 2
arr[0, :]       # [0, 1, 2, 3] — entire row 0
arr[:, 1]       # [1, 5, 9] — entire col 1
arr[1:, :2]     # rows 1+, cols 0-1

# Boolean indexing
mask = arr > 5
arr[mask]       # [6, 7, 8, 9, 10, 11]
arr[arr > 5] = 0  # in-place modification
```

### 4. Reshaping & Axes

```python
arr = np.arange(24)
arr.reshape(4, 6)       # 4 rows, 6 cols
arr.reshape(2, 3, 4)    # 3D — 2 batches of 3×4
arr.reshape(-1, 6)      # NumPy infers first dim (=4)

# Transpose
mat = np.ones((3, 5))
mat.T               # shape (5, 3)
mat.transpose()     # same

# Adding dimensions (critical for broadcasting)
v = np.array([1, 2, 3])     # shape (3,)
v[np.newaxis, :]             # shape (1, 3)
v[:, np.newaxis]             # shape (3, 1)
```

### 5. Broadcasting

**Broadcasting rule:** Two shapes are compatible if, from the right, each dimension is either equal or one of them is 1.

```python
a = np.ones((3, 4))     # shape (3, 4)
b = np.array([1,2,3,4]) # shape (4,)  → treated as (1, 4)
a + b   # shape (3, 4) — b is broadcast across rows

# Real example: subtract mean from each column
data = np.random.randn(100, 10)  # 100 samples, 10 features
mean = data.mean(axis=0)         # shape (10,)
normalised = data - mean         # (100,10) - (10,) — broadcasts
```

### 6. Vectorised Math

```python
a = np.array([1.0, 4.0, 9.0])

np.sqrt(a)       # [1.0, 2.0, 3.0]
np.exp(a)        # element-wise e^x
np.log(a)        # element-wise ln
a ** 2           # [1.0, 16.0, 81.0]

# Aggregations
a.sum()          # scalar
a.sum(axis=0)    # sum along rows (collapse rows)
a.mean(axis=1)   # mean along cols (collapse cols)
a.max(), a.argmax()
np.cumsum(a)
```

### 7. Matrix Operations (ML-critical)

```python
A = np.random.randn(3, 4)
B = np.random.randn(4, 5)

C = A @ B           # matrix multiply → (3, 5)
C = np.dot(A, B)    # equivalent

v = np.array([1, 2, 3, 4])
A @ v               # matrix-vector → (3,)

# Element-wise vs matrix multiply
A * A               # element-wise square
A @ A.T             # proper matrix multiply (3,3)
```

### 8. Copies vs Views

```python
a = np.arange(10)
b = a[2:5]       # VIEW — shares memory with a
b[0] = 99        # mutates a!

c = a[2:5].copy()  # explicit copy — safe
```

**Why this matters:** PyTorch tensors follow the same pattern. Silently sharing memory causes bugs.

---

## Math Pillars

**L2 norm (vector length):**

$$\|v\|_2 = \sqrt{\sum_{i} v_i^2}$$

```python
np.linalg.norm(v)                  # L2 by default
np.linalg.norm(v, ord=1)           # L1
```

**Dot product:**

$$a \cdot b = \sum_i a_i b_i$$

```python
np.dot(a, b)    # or a @ b for 1D vectors
```

**Matrix multiply:**

$$C_{ij} = \sum_k A_{ik} B_{kj}$$

---

## Anki-Ready Highlights

- **NumPy array = contiguous, fixed-dtype block of memory** — enables SIMD vectorisation
- **`shape` is the most important array attribute** — always check it first when debugging
- **Slicing returns a VIEW, not a copy** — use `.copy()` to avoid mutation bugs
- **Broadcasting rule: align shapes from the right; dims must match or be 1**
- **`axis=0` collapses rows (result has fewer rows); `axis=1` collapses cols**
- **`@` = matrix multiply; `*` = element-wise multiply**
- **`reshape(-1, n)` lets NumPy infer one dimension** — use when batch size is unknown
- **`np.newaxis` adds a dimension of size 1** — essential for making shapes broadcast-compatible
- **`np.random.randn(m, n)` = standard normal; `np.random.rand(m, n)` = uniform [0,1]**
- **`dtype=np.float32` halves memory vs float64** — always use float32 in ML

---

## Common Pitfalls

| Mistake | Why It Fails | Fix |
|---|---|---|
| `a = arr[1:3]` then mutate `a` | It's a view — corrupts original | `a = arr[1:3].copy()` |
| `np.dot(A, B)` with wrong shapes | Shape mismatch error | Check `A.shape`, `B.shape` first |
| Using Python `sum()` on array | 100× slower | Use `arr.sum()` |
| `arr.shape` vs `arr.shape[0]` | Shape is a tuple, not an int | Index the tuple |
| `randn` vs `rand` confusion | Different distributions | `randn` = normal, `rand` = uniform |

---

## Quick Reference

```python
# Shape manipulation
arr.reshape(m, n)     arr.flatten()     arr.ravel()
arr.T                 arr.squeeze()     arr.expand_dims(axis=0)
np.concatenate([a,b], axis=0)          np.stack([a,b], axis=0)
np.hstack([a,b])      np.vstack([a,b])

# Math
np.dot(a,b)    a @ b    np.outer(a,b)    np.cross(a,b)
np.linalg.inv(A)        np.linalg.eig(A)    np.linalg.svd(A)

# Stats
arr.mean(axis)    arr.std(axis)    arr.var(axis)
np.percentile(arr, 95)    np.median(arr)

# Logical
np.any(arr > 0)    np.all(arr > 0)    np.where(cond, x, y)
```
