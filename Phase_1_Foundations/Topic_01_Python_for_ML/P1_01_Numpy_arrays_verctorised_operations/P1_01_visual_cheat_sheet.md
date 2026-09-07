# P1_01 — NumPy Arrays & Vectorised Operations

> Mental Model: A NumPy array is a typed, contiguous block of memory with shape metadata. Vectorised ops = C-level loops on that block; Python loops = Python-level overhead on every element.

---

## Memory Layout

```
ndarray object
├── data pointer  →  [ f64 | f64 | f64 | f64 | f64 | f64 ]  (contiguous in RAM)
├── dtype         →  float64
├── shape         →  (2, 3)
├── strides       →  (24, 8)   ← bytes to skip per axis step
└── flags         →  C_CONTIGUOUS, WRITEABLE
```

Row-major (C order): row 0 fully laid out before row 1.  
Column-major (F order): column 0 first — set with `order='F'`.

---

## Shape & Strides Mental Model

```
shape  = (2, 3)
strides= (24, 8)   # float64 = 8 bytes

a[1, 2]  →  data + 1*24 + 2*8  =  data + 40
```

---

## Key Formulas

$$\text{element offset} = \sum_{i} \text{index}_i \times \text{stride}_i$$

$$\text{broadcast rule: shapes align right; size-1 dims expand}$$

---

## Broadcasting Rules

```
A: (3, 1, 4)
B:    (5, 4)
        ↑ align right
→  (3, 5, 4)   ← no copy; virtual expansion
```

> ⚠️ Gotcha: `(3,) + (3, 1)` → `(3, 3)`, not an error. Verify shapes before add.

---

## View vs Copy

| Operation | View or Copy? |
|-----------|--------------|
| `a[1:3]` slice | **View** |
| `a[[1,3]]` fancy index | **Copy** |
| `a.reshape(...)` | View if contiguous, else Copy |
| `a.T` | **View** (swaps strides) |
| `a.flatten()` | **Copy** |
| `a.ravel()` | View if possible |

Check with: `np.shares_memory(a, b)`

> ⚠️ Gotcha: Writing to a view mutates the original. `b = a[1:3]; b[:] = 0` zeroes `a[1:3]`.

---

## ufuncs vs Python loops

| | Python loop | NumPy ufunc |
|---|---|---|
| Loop location | Python interpreter | C / SIMD |
| Per-element overhead | ~100 ns | ~1 ns |
| Supports reduce/accumulate | No | Yes |

```python
# Slow  — Python loop
result = [x**2 for x in a]

# Fast  — vectorised
result = a ** 2        # calls np.power ufunc
```

---

## Axis Semantics

```
a.sum(axis=0)  →  collapse rows    → shape shrinks dim 0
a.sum(axis=1)  →  collapse columns → shape shrinks dim 1
a.sum(axis=-1) →  collapse last dim (same as axis=1 for 2-D)
```

---

## Common Pitfalls Table

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| int overflow | `np.int8` wraps at 127 | use `dtype=np.int32` |
| in-place on view | mutates original | `.copy()` first |
| float comparison | `a == 0.1` fails | `np.isclose(a, 0.1)` |
| shape `(n,)` vs `(n,1)` | broadcast surprise | `a[:, np.newaxis]` |
| concatenate list of arrays | slow loop | `np.stack` / `np.vstack` |

---

## Essential API Surface

```python
np.zeros(shape, dtype)    np.ones(...)   np.empty(...)
np.arange(start,stop,step)  np.linspace(start,stop,n)
np.eye(n)   np.random.default_rng(seed).standard_normal(shape)

a.shape  a.dtype  a.ndim  a.size  a.nbytes
a.reshape(new_shape)  a.T  a.squeeze()  a.expand_dims(axis)

np.dot(a,b)  a @ b  np.einsum('ij,jk->ik', a, b)
np.concatenate([a,b], axis=0)  np.stack([a,b], axis=0)

np.where(cond, x, y)   np.clip(a, lo, hi)
np.sort(a, axis)  np.argsort(a, axis)
np.unique(a, return_counts=True)
```

> ⚠️ Gotcha: `np.dot` on 2-D is matrix multiply; on 1-D is inner product. Use `@` for clarity.
