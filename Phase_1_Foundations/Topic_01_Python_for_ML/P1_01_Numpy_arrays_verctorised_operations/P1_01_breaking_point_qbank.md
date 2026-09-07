# P1_01 Breaking Point Q-Bank — NumPy Arrays and Vectorised Operations

*15 stress-test questions ordered from hard to hardest. No definition-level questions. Every answer is first-principles only.*

---

## Q1
**Question:** You have a (10000, 768) float32 NumPy array. You call `.copy()` on it. Exactly how much additional RAM is allocated, and why is that number not zero even though the data is identical?

**Gap exposed:** Confusing views with copies; not knowing memory layout implications.

**Ideal answer:** A `.copy()` allocates a fully independent contiguous block of memory — 10000 × 768 × 4 bytes = ~29.3 MB. It's not zero because a copy breaks the shared memory reference; any mutation to the original won't affect the copy. NumPy stores float32 as 4 bytes per element; the entire array is duplicated in RAM. A view would allocate near-zero additional memory but share the underlying buffer.

---

## Q2
**Question:** `a = np.zeros((3, 4))`. What is `a.strides`, and why does the second value differ from the first?

**Gap exposed:** Shallow understanding of C-order memory layout and how strides enable multidimensional indexing over flat memory.

**Ideal answer:** Strides will be `(16, 4)` for float32 (4 bytes per element). The second value is 4 because moving one column requires jumping 4 bytes (one element). The first value is 16 because moving one row requires jumping 4 columns × 4 bytes. NumPy stores arrays in row-major (C) order by default, so each entire row is contiguous in memory; strides encode how far to jump per dimension.

---

## Q3
**Question:** You do `b = a[:, ::2]` on a (1000, 1000) array. Is `b` a view or a copy? What happens to `b.strides` and why can't NumPy just store the data contiguously?

**Gap exposed:** Not understanding that non-contiguous slices produce views with modified strides, not reallocated memory.

**Ideal answer:** `b` is a view — no data is copied. `b.strides` doubles the column stride (e.g., from `(8000, 8)` to `(8000, 16)` for float64) because every other element is skipped. NumPy can't store it contiguously without copying because the elements are interleaved with skipped elements in the original buffer. The view mechanism encodes this by changing the stride, not the data.

---

## Q4
**Question:** You want to compute the pairwise Euclidean distance between every row of a (1000, 128) matrix. A naïve double for-loop runs in ~2 seconds. A vectorised implementation using broadcasting runs in ~5 ms. Derive the vectorised formula and explain which NumPy operations make it fast.

**Gap exposed:** Not knowing how to decompose $||a - b||^2 = ||a||^2 + ||b||^2 - 2a \cdot b^T$ into matrix ops.

**Ideal answer:** Expand $||x_i - x_j||^2 = x_i \cdot x_i + x_j \cdot x_j - 2 x_i \cdot x_j$. In NumPy: `sq = (X**2).sum(axis=1, keepdims=True)`, then `D = sq + sq.T - 2 * X @ X.T`. The speed comes from `@` (BLAS DGEMM) operating on contiguous memory in optimised C/Fortran, and the additions using broadcasting without explicit loops. The Python interpreter is called only a handful of times total instead of 10^6 times.

---

## Q5
**Question:** `np.dot(a, b)` vs `a @ b` vs `np.matmul(a, b)` — are these always equivalent? Give a concrete case where they differ.

**Gap exposed:** Treating them as identical without understanding the broadcasting and batching differences.

**Ideal answer:** For 2D arrays they are equivalent. They differ for higher dimensions: `np.dot` on ND arrays computes a sum product over the last axis of `a` and the second-to-last of `b` (not what you want for batch matmul). `np.matmul` and `@` broadcast over batch dimensions consistently. Example: `a.shape = (10, 3, 4)`, `b.shape = (10, 4, 5)` — `a @ b` gives `(10, 3, 5)` (10 independent matmuls); `np.dot(a, b)` gives `(10, 3, 10, 5)` (wrong shape).

---

## Q6
**Question:** You have `arr = np.array([1, 2, 3])` and do `arr[arr > 1] = 0`. What is the memory model of `arr > 1`, and why does this in-place assignment not create a temporary array for the right-hand side?

**Gap exposed:** Not understanding boolean fancy indexing and in-place assignment semantics.

**Ideal answer:** `arr > 1` creates a boolean mask array of shape `(3,)`. Fancy indexing with a boolean mask selects elements but returns a *copy* on read. However, on the left side of an assignment, NumPy uses `__setitem__`, which writes directly into the selected positions of `arr` without creating an intermediate array for the result. The scalar `0` is broadcast to all selected positions in-place. The mask itself is a temporary `(3,)` bool array allocated and then garbage collected.

---

## Q7
**Question:** Why does `np.sum(a, axis=0)` on a (10000, 768) C-contiguous float32 array run faster than `np.sum(a, axis=1)` on the same array?

**Gap exposed:** Not connecting memory access patterns to cache efficiency.

**Ideal answer:** Summing along axis=0 means iterating down each column. For C-contiguous layout (rows are contiguous), accessing column elements requires jumping 768 × 4 = 3072 bytes between reads — this is strided, cache-unfriendly access. Wait — actually axis=0 is less cache-friendly. Summing axis=1 (across each row) reads contiguous memory. NumPy internally may transpose or use SIMD, but fundamentally: axis=1 sums contiguous row elements, keeping data in L1/L2 cache. Axis=0 strides across rows, causing cache misses per element, making it slower on large arrays.

---

## Q8
**Question:** `a = np.arange(10); b = a[2:5]; b[0] = 99`. What is `a[2]`? Now explain what breaks this when you do `a = np.array([1,2,3]); b = a[[0,1,2]]; b[0] = 99`. What is `a[0]`?

**Gap exposed:** Conflating basic slicing (view) with fancy indexing (copy).

**Ideal answer:** In the first case, `a[2]` is 99. Basic slices (`2:5`) return a view — `b` and `a` share the same buffer, so mutation propagates. In the second case, `a[0]` is still 1. Fancy indexing (integer array `[0,1,2]`) always returns a *copy*. The buffer of `b` is independent; writing to `b[0]` has no effect on `a`. This is a common source of bugs when developers expect views from index lists.

---

## Q9
**Question:** You have a (1M,) float32 array. You apply a custom element-wise function using `np.vectorize`. It runs in 4 seconds. Explain exactly why `np.vectorize` is not actually vectorised and how you'd fix it.

**Gap exposed:** Mistaking `np.vectorize` for a JIT/SIMD compiler when it's just a syntactic wrapper for a Python loop.

**Ideal answer:** `np.vectorize` is a Python-level loop over array elements — it calls the Python function once per element, incurring full interpreter overhead and no SIMD. It's equivalent to a for-loop with `dtype` handling added. The fix: express the computation using NumPy ufuncs or built-in operations (which call C-level loops with SIMD), or use `numba.jit` to compile the function to machine code. For example, `np.exp(arr) * np.sin(arr)` dispatches C functions; `np.vectorize(lambda x: math.exp(x)*math.sin(x))` does not.

---

## Q10
**Question:** What is the difference between `a.reshape(4, -1)` and `a.ravel()` then `a.reshape(4, -1)`? Under what conditions does reshape return a view vs a copy?

**Gap exposed:** Not knowing that reshape returns a view only for contiguous arrays and that ravel may copy for non-contiguous inputs.

**Ideal answer:** For a contiguous array, `reshape` returns a view — no data is moved; only shape and strides metadata changes. If the array is non-contiguous (e.g., result of a transpose), reshape must copy to create a contiguous layout before it can reshape. `ravel()` returns a flattened 1D view if the array is already contiguous; otherwise it returns a copy. Calling `ravel()` first forces contiguity, so the subsequent `reshape` is guaranteed to be a view of the contiguous flat array.

---

## Q11
**Question:** You do `c = a.T` on a (3, 4) array. `c.flags['C_CONTIGUOUS']` is False. Explain why, and explain what happens when you call `c @ d` for a compatible matrix `d`.

**Gap exposed:** Not understanding how transpose works without copying data and what NumPy does internally for non-contiguous matmul.

**Ideal answer:** `a.T` simply swaps the strides — the data buffer is unchanged; it's a zero-copy view. A (3, 4) C-contiguous array has strides (32, 8) for float64; the transpose has strides (8, 32), which is Fortran-order. Not C-contiguous. When you do `c @ d`, NumPy detects non-contiguous input and passes the Fortran-order flag to the underlying BLAS routine (e.g., dgemm with TRANSA='T'), which handles it efficiently without copying — BLAS natively supports transposed inputs via its CblasTrans flag.

---

## Q12
**Question:** `np.where(condition, a, b)` — what is its computational cost when `a` and `b` are large arrays with complex computations, and how does it differ from a masked assignment?

**Gap exposed:** Assuming `np.where` short-circuits like an `if` statement.

**Ideal answer:** `np.where(condition, a, b)` evaluates both `a` and `b` in their entirety before selecting elements — there is no short-circuit. If `a` and `b` are expressions involving large operations (e.g., `np.sin(big_array)`), both are fully computed regardless of the condition values. A masked assignment `out[mask] = expr` evaluates `expr` only for masked positions (if expressed as a Python-level filtered operation), but `np.where` is a merge, not a guard. Cost: O(N) for both branches always.

---

## Q13
**Question:** You have two arrays `a` shape (1000, 1) and `b` shape (1, 1000). You compute `a + b`. What is the resulting shape, how many additions actually occur, and how much memory does NumPy allocate for the output?

**Gap exposed:** Shallow understanding of broadcasting — thinking it always copies to full shape before operating.

**Ideal answer:** Result shape: (1000, 1000). NumPy does 1,000,000 additions — broadcasting is conceptual; the operation iterates over all output elements. The output is a full (1000, 1000) float64 array = 8 MB. NumPy does NOT materialise the broadcast copies of `a` and `b` into (1000, 1000) intermediate arrays; it virtually repeats them by adjusting iteration, but the output must be stored. Memory allocated: one (1000, 1000) output array. The input arrays stay at their original sizes.

---

## Q14
**Question:** Why is `np.einsum('ij,jk->ik', a, b)` sometimes faster than `a @ b`, and when is it not?

**Gap exposed:** Not knowing that einsum can fuse operations and reduce intermediate allocations, but may not leverage BLAS.

**Ideal answer:** `einsum` with a single contraction can be optimised by NumPy's backend (with `optimize=True`) to choose the best contraction path and potentially avoid intermediate allocations. For a simple matmul, `a @ b` dispatches to optimised BLAS DGEMM, which is typically faster than einsum's generic iteration. `einsum` wins when chaining multiple operations (e.g., `'ij,jk,kl->il'`) because it can find an optimal contraction order and reduce total FLOPs, whereas `@` chained naively (`a @ b @ c`) creates an intermediate matrix. Rule: prefer `@` for simple matmuls; use `einsum` with `optimize=True` for multi-tensor contractions.

---

## Q15
**Question:** You write `for i in range(len(arr)): result[i] = arr[i] ** 2` vs `result = arr ** 2`. Both produce the same output. Quantify the speedup source by tracing the Python interpreter call count in each approach.

**Gap exposed:** Not internalising *why* vectorisation is fast — attributing it vaguely to "C being fast" without understanding interpreter dispatch costs.

**Ideal answer:** The loop version calls the Python interpreter for: each `range` iteration (N calls), `len` (1), `__getitem__` on `arr` (N), `__pow__` as a Python method dispatch (N), `__setitem__` on `result` (N) — roughly 4N + overhead Python bytecode executions. Each Python dispatch is ~50–200 ns due to reference counting, type checking, and GIL acquisition. `arr ** 2` is one Python call dispatching to `np.power`, which runs a C loop with SIMD over all N elements with zero per-element interpreter overhead. Speedup is proportional to N × (Python dispatch overhead) / (C instruction overhead per element) — typically 10–100× for large N.
