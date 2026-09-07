# Problem Set — P1_01: NumPy Arrays and Vectorised Operations

**Phase:** 1 — Foundations  
**Topic:** NumPy arrays and vectorised operations  
**Problems:** 20  
**Format:** 5 Conceptual · 5 Math · 5 Coding · 3 Adversarial · 2 Debug

---

## Section A — Conceptual Edge Cases (no code)

**Q1** `[Medium]`  
You have two arrays: `a = np.zeros((3, 1))` and `b = np.zeros((1, 4))`. Broadcasting produces a `(3, 4)` result. Now consider `a = np.zeros((3, 2))` and `b = np.zeros((2, 4))`. Broadcasting fails. Explain precisely *why* the second case fails when the first succeeds, despite both involving a dimension mismatch. What is the exact rule NumPy applies, and what mental model do you use to predict broadcast compatibility without trial and error?

---

**Q2** `[Medium]`  
Consider this sequence:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a[0]       # row slice
c = a[[0]]     # fancy index
```

`b` and `c` contain identical values. However, mutating `b[0] = 99` changes `a`, while mutating `c[0] = 99` does not. Explain the mechanistic reason for this difference. Under what circumstances does NumPy return a view vs a copy, and what are the exact rules governing each case?

---

**Q3** `[Hard]`  
You compute `np.array([200], dtype=np.uint8) + np.array([100], dtype=np.uint8)`. The result is `44`, not `300`. Explain what happened, why NumPy does not raise an error, and describe two scenarios in an ML pipeline where silent integer overflow could corrupt your results without any warning. How do you defensively guard against this?

---

**Q4** `[Hard]`  
`np.nan != np.nan` evaluates to `True`. Explain why this is mathematically correct per IEEE 754, and describe the failure mode this creates when you use boolean masking to filter arrays containing NaN values. What is the correct NumPy idiom for NaN-aware filtering, and why does `array == np.nan` silently give wrong results?

---

**Q5** `[Expert]`  
NumPy stores arrays in either C-contiguous (row-major) or Fortran-contiguous (column-major) order. You are iterating over the columns of a large `(10000, 10000)` float64 matrix. Explain the performance implication of the memory layout on this operation, quantify the likely cache miss penalty, and describe the exact transformation you would apply to make column iteration cache-friendly. Why does this matter for ML operations like computing per-feature statistics?

---

## Section B — Mathematical Derivation / Proof

**Q6** `[Medium]`  
**Outer Product Derivation.**  
Given two vectors $\mathbf{u} \in \mathbb{R}^m$ and $\mathbf{v} \in \mathbb{R}^n$, the outer product $\mathbf{u} \otimes \mathbf{v}$ produces a matrix $M \in \mathbb{R}^{m \times n}$.

Formally define each element $M_{ij}$ in terms of $u_i$ and $v_j$. Then prove that the outer product is equivalent to the matrix multiplication $\mathbf{u}\mathbf{v}^T$ where $\mathbf{u}$ is treated as a column vector and $\mathbf{v}^T$ as a row vector. Show why `np.outer(u, v)` and `u[:, None] * v[None, :]` produce identical results by tracing the broadcasting shape computation step by step.

---

**Q7** `[Medium]`  
**Vectorised vs Loop Complexity.**  
You have a dataset $X \in \mathbb{R}^{n \times d}$ and want to compute the mean of each feature (column). 

Derive the exact number of arithmetic operations required by: (a) a Python-level double for-loop, (b) a Python for-loop over columns with NumPy sum, and (c) `X.mean(axis=0)`. Express each as a function of $n$ and $d$. Explain why the constant factor for (c) is dramatically smaller than (a) even though the asymptotic complexity $O(nd)$ is identical.

---

**Q8** `[Hard]`  
**L2 Norm Equivalence Proof.**  
Given a vector $\mathbf{x} \in \mathbb{R}^d$, prove algebraically that the following three expressions are mathematically equivalent:

$$\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^{d} x_i^2} = \sqrt{\mathbf{x} \cdot \mathbf{x}} = \sqrt{\mathbf{x}^T \mathbf{x}}$$

Then explain why `np.sqrt(np.sum(x**2))` may give a slightly different floating-point result than `np.linalg.norm(x)` for very large or very small values of $x$, and what numerical technique `linalg.norm` uses internally to mitigate this.

---

**Q9** `[Hard]`  
**Pairwise Euclidean Distance via Expansion.**  
Given a matrix $X \in \mathbb{R}^{n \times d}$ where each row is a data point, derive the formula for computing all $n^2$ pairwise squared Euclidean distances without any Python-level loops. Start from the identity:

$$\|x_i - x_j\|^2 = \|x_i\|^2 - 2x_i \cdot x_j + \|x_j\|^2$$

Show how each of the three terms maps to a vectorised NumPy operation, and specify the shape of each intermediate array. What is the memory cost in bytes for $n = 10000$ points in float32?

---

**Q10** `[Expert]`  
**Softmax Numerical Stability Derivation.**  
The softmax function is defined as:

$$\sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$$

Prove that subtracting $c = \max(\mathbf{z})$ from all logits before exponentiation produces an algebraically identical result:

$$\sigma(z)_i = \frac{e^{z_i - c}}{\sum_{j=1}^{K} e^{z_j - c}}$$

Show the step-by-step algebraic cancellation. Then explain what concretely happens (in terms of floating-point representation) when $z = [1000, 1001, 1002]$ without this trick vs with it, and why the naive formula fails.

---

## Section C — From-Scratch Coding (NumPy + Python stdlib only)

**Q11** `[Medium]`  
**Matrix Multiplication Without `np.dot` / `np.matmul`.**  
Implement a function `matmul(A, B)` that computes the matrix product of two 2D NumPy arrays. You may NOT use `np.dot`, `np.matmul`, `@`, `np.einsum`, or any scipy/sklearn function. You may only use element-wise operations, broadcasting, and `np.sum`. Your implementation must handle arbitrary shapes $(m \times k)$ and $(k \times n)$.

Verify correctness against `np.matmul` for a random $(50 \times 30) \times (30 \times 40)$ case.

---

**Q12** `[Medium]`  
**Softmax from Scratch.**  
Implement `softmax(X)` where `X` can be either a 1D vector or a 2D matrix of shape `(batch, classes)`. Requirements:
- When 2D, apply softmax independently to each row
- Must be numerically stable (subtract row-wise max before exponentiating)
- Must handle the edge case where an entire row is `-inf` (output should be uniform)
- No scipy, no sklearn

Verify that rows sum to 1.0 and that the output matches for input `X = np.array([[1000., 1001., 1002.], [-1., 0., 1.]])`.

---

**Q13** `[Medium]`  
**One-Hot Encoding from Scratch.**  
Implement `one_hot(labels, num_classes)` that converts an integer label array of shape `(n,)` into a float32 matrix of shape `(n, num_classes)`. Requirements:
- No loops over individual samples
- Handle out-of-range labels by raising a `ValueError` with a clear message
- The function must run in a single vectorised pass

Verify on `labels = np.array([0, 2, 1, 2])`, `num_classes = 3`.

---

**Q14** `[Hard]`  
**Sliding Window View.**  
Implement `sliding_windows(arr, window_size, step=1)` that takes a 1D array and returns a 2D array of shape `(num_windows, window_size)` containing all sliding windows. Requirements:
- No Python loops over elements
- Do NOT use `np.lib.stride_tricks.sliding_window_view` (implement the stride trick yourself using `np.lib.stride_tricks.as_strided`)
- Must not copy data (the returned array must be a view)
- Correctly compute `num_windows` as a function of `len(arr)`, `window_size`, and `step`

Verify on `arr = np.arange(10)`, `window_size=4`, `step=2`.

---

**Q15** `[Hard]`  
**Batch Normalisation — Forward Pass.**  
Implement `batch_norm(X, gamma, beta, eps=1e-8)` where:
- `X` has shape `(batch_size, num_features)`
- `gamma` and `beta` are learnable scale/shift parameters of shape `(num_features,)`
- Normalise each feature (column) to zero mean and unit variance across the batch
- Apply the affine transform: $\hat{X}_{norm} = \gamma \cdot X_{norm} + \beta$
- Return the normalised output and also the intermediate values `(mu, var, X_norm)` needed for the backward pass

No loops. Verify that after normalisation (before gamma/beta), each column has mean ≈ 0 and std ≈ 1.

---

## Section D — Adversarial Constraints

**Q16** `[Hard]`  
**Matrix Multiply in 4MB RAM.**  
You need to multiply two matrices $A \in \mathbb{R}^{2000 \times 2000}$ and $B \in \mathbb{R}^{2000 \times 2000}$ (float32). The full result matrix alone would require $2000 \times 2000 \times 4 = 16\text{MB}$. You are given a strict 4MB working memory budget (beyond storing the inputs, which are pre-allocated and read-only).

Implement a block/tiled matrix multiplication that computes the result incrementally, writing each block to disk (using `np.save`/`np.load`) rather than holding the full output in RAM. Specify the maximum tile size you can use within 4MB, and implement the tiling logic.

---

**Q17** `[Expert]`  
**Argmax Without `np.argmax`.**  
Implement `my_argmax(arr)` that returns the index of the maximum value in a 1D array. Constraints:
- You may NOT use `np.argmax`, `np.argsort`, `np.sort`, `np.where`, `list.index`, or Python's built-in `max()`
- You may use `np.max` (to find the value), boolean masks, and basic NumPy operations
- Must handle ties (return the first occurrence, matching NumPy's behaviour)
- Must work correctly when the array contains NaN values (treat NaN as less than all real values, matching `np.nanargmax` behaviour)

Explain your approach before coding it.

---

**Q18** `[Expert]`  
**Pairwise Cosine Similarity Without Materialising the Distance Matrix.**  
You have $n = 50000$ sentence embeddings of dimension $d = 768$ (float32). Computing the full $n \times n$ cosine similarity matrix requires $50000^2 \times 4 \approx 9.3\text{GB}$ — impossible on a 16GB machine.

Implement `top_k_similar(embeddings, query_idx, k=10)` that returns the indices of the top-$k$ most similar embeddings to a query row, processing the comparison in chunks of at most 1000 rows at a time to stay within 2GB. You must: (a) L2-normalise the embeddings first, (b) compute cosine similarity as a dot product after normalisation, (c) aggregate top-k results across chunks without ever holding more than one chunk in memory at once.

---

## Section E — Debugging

**Q19** `[Medium]`  
**The Silent Mutation Bug.**  
The following code is supposed to standardise each column of `X` to zero mean and unit variance, then return a copy safe to modify downstream. Find and fix all bugs. Explain why each bug is dangerous.

```python
import numpy as np

def standardise(X):
    mu = X.mean(axis=0)
    std = X.std(axis=0)
    X -= mu          # in-place normalise
    X /= std         # in-place scale
    return X

# Usage
data = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
result = standardise(data)
print("Original data:", data)   # Expect: unchanged
print("Standardised:", result)
```

There are at least **3 distinct bugs or design flaws** in this code. Identify all of them.

---

**Q20** `[Hard]`  
**The Broadcasting Shape Trap.**  
The function below is supposed to compute the squared Euclidean distance between every pair of rows in matrices `A` (shape `m × d`) and `B` (shape `n × d`), returning a matrix of shape `(m, n)`. It runs without error but produces wrong results. Find the bug, explain the exact shape arithmetic that causes it, and provide the corrected implementation.

```python
import numpy as np

def pairwise_sq_dist(A, B):
    # ||a - b||^2 = ||a||^2 - 2a·b + ||b||^2
    sq_A = np.sum(A ** 2, axis=1)        # shape (m,)
    sq_B = np.sum(B ** 2, axis=1)        # shape (n,)
    dot   = A @ B.T                       # shape (m, n)
    return sq_A - 2 * dot + sq_B         # BUG IS HERE

A = np.random.randn(4, 3)
B = np.random.randn(5, 3)
D = pairwise_sq_dist(A, B)
print(D.shape)   # prints (4, 5) — looks right!
print((D >= 0).all())  # may print False — wrong!
```

Hint: think carefully about how `sq_A` (shape `(m,)`) and `sq_B` (shape `(n,)`) broadcast against `dot` (shape `(m, n)`).

---

*End of Problem Set — P1_01*
