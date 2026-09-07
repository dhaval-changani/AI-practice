"""
P1_01 — NumPy Arrays and Vectorised Operations
================================================
Topic: NumPy arrays and vectorised operations
Phase: 1 (Foundations)

Instructions:
  Fill in every TODO block. Do NOT change function signatures.
  Run the file — each test prints PASS or FAIL.
  All operations must use NumPy vectorised calls; no Python for-loops
  inside the core logic functions.
"""

import numpy as np
from typing import Tuple


# ---------------------------------------------------------------------------
# 1. Array Creation
# ---------------------------------------------------------------------------

def create_arrays() -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Create and return four arrays:
      a) A 1-D array of floats from 0 to 9 (inclusive) using np.arange
      b) A 3×4 array of zeros with dtype float64
      c) A 5×5 identity matrix
      d) A 2×3 array filled with the value 7 (dtype int32)

    Returns
    -------
    Tuple of (a, b, c, d) as described above.
    """
    # TODO: create array a — 1-D arange 0..9
    a = NotImplemented
    # TODO: create array b — 3×4 zeros float64
    b = NotImplemented
    # TODO: create array c — 5×5 identity matrix
    c = NotImplemented
    # TODO: create array d — 2×3 filled with 7, dtype int32
    d = NotImplemented
    raise NotImplementedError("Fill in create_arrays()")


# ---------------------------------------------------------------------------
# 2. Reshaping and Indexing
# ---------------------------------------------------------------------------

def reshape_and_slice(arr: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Given a 1-D array of 24 elements, return:
      a) The array reshaped to (4, 6)
      b) The second row of the reshaped array (index 1)
      c) The sub-matrix spanning rows 1–2 (inclusive) and columns 2–4 (inclusive)
         of the reshaped array — shape should be (2, 3)

    Parameters
    ----------
    arr : np.ndarray  shape (24,)

    Returns
    -------
    Tuple of (reshaped, row, submatrix)
    """
    # TODO: reshape arr to (4, 6)
    reshaped = NotImplemented
    # TODO: extract second row (index 1)
    row = NotImplemented
    # TODO: extract sub-matrix rows 1:3, cols 2:5
    submatrix = NotImplemented
    raise NotImplementedError("Fill in reshape_and_slice()")


# ---------------------------------------------------------------------------
# 3. Vectorised Arithmetic and Broadcasting
# ---------------------------------------------------------------------------

def broadcasting_demo(matrix: np.ndarray, row_vector: np.ndarray) -> np.ndarray:
    """
    Add row_vector to every row of matrix using NumPy broadcasting.
    No loops allowed.

    Parameters
    ----------
    matrix    : np.ndarray  shape (M, N)
    row_vector: np.ndarray  shape (N,)

    Returns
    -------
    np.ndarray  shape (M, N) — element-wise sum
    """
    # TODO: broadcast-add row_vector to each row of matrix
    raise NotImplementedError("Fill in broadcasting_demo()")


def normalise_rows(matrix: np.ndarray) -> np.ndarray:
    """
    L2-normalise each row of matrix so that every row has unit norm.
    No loops. Handle zero-norm rows safely (leave them as zero).

    Parameters
    ----------
    matrix : np.ndarray  shape (M, N)

    Returns
    -------
    np.ndarray  shape (M, N)
    """
    # TODO: compute L2 norm of each row, shape (M, 1)
    norms = NotImplemented
    # TODO: divide each row by its norm; replace division by zero with 0
    normalised = NotImplemented
    raise NotImplementedError("Fill in normalise_rows()")


# ---------------------------------------------------------------------------
# 4. Aggregations and Axis Operations
# ---------------------------------------------------------------------------

def column_statistics(matrix: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Compute per-column mean, standard deviation, and max for a 2-D matrix.
    No loops.

    Parameters
    ----------
    matrix : np.ndarray  shape (M, N)

    Returns
    -------
    Tuple of (col_means, col_stds, col_maxes) each shape (N,)
    """
    # TODO: column means
    col_means = NotImplemented
    # TODO: column standard deviations (ddof=0)
    col_stds = NotImplemented
    # TODO: column maxima
    col_maxes = NotImplemented
    raise NotImplementedError("Fill in column_statistics()")


# ---------------------------------------------------------------------------
# 5. Boolean Masking and Fancy Indexing
# ---------------------------------------------------------------------------

def filter_and_replace(arr: np.ndarray, threshold: float) -> np.ndarray:
    """
    Return a copy of arr where all values strictly below `threshold`
    are set to 0.0. No loops; use boolean masking.

    Parameters
    ----------
    arr       : np.ndarray  any shape
    threshold : float

    Returns
    -------
    np.ndarray  same shape as arr
    """
    # TODO: create a copy of arr
    result = NotImplemented
    # TODO: build boolean mask of elements < threshold
    mask = NotImplemented
    # TODO: zero out masked positions
    raise NotImplementedError("Fill in filter_and_replace()")


def top_k_indices(arr: np.ndarray, k: int) -> np.ndarray:
    """
    Return the indices of the k largest values in a 1-D array,
    sorted in descending order of value. No loops.

    Parameters
    ----------
    arr : np.ndarray  shape (N,)
    k   : int

    Returns
    -------
    np.ndarray  shape (k,) — integer indices
    """
    # TODO: use np.argsort (or np.argpartition) to get top-k indices
    # Hint: np.argsort returns ascending order; think about reversing
    raise NotImplementedError("Fill in top_k_indices()")


# ---------------------------------------------------------------------------
# 6. Matrix Multiplication and Linear Algebra
# ---------------------------------------------------------------------------

def matrix_ops(A: np.ndarray, B: np.ndarray) -> Tuple[np.ndarray, np.ndarray, float]:
    """
    Given matrices A (shape M×K) and B (shape K×N), compute:
      a) Matrix product C = A @ B  shape (M, N)
      b) Element-wise square of A  shape (M, K)
      c) Frobenius norm of A (scalar)

    Parameters
    ----------
    A : np.ndarray  shape (M, K)
    B : np.ndarray  shape (K, N)

    Returns
    -------
    Tuple of (C, A_squared, frob_norm)
    """
    # TODO: matrix product
    C = NotImplemented
    # TODO: element-wise square of A
    A_squared = NotImplemented
    # TODO: Frobenius norm of A (single float)
    frob_norm = NotImplemented
    raise NotImplementedError("Fill in matrix_ops()")


# ---------------------------------------------------------------------------
# 7. Stacking and Concatenation
# ---------------------------------------------------------------------------

def stack_arrays(list_of_vectors: list) -> Tuple[np.ndarray, np.ndarray]:
    """
    Given a Python list of 1-D arrays each of shape (N,):
      a) Stack them as rows → shape (len(list), N)  using np.vstack or np.stack
      b) Concatenate them into one long 1-D vector  using np.concatenate

    Parameters
    ----------
    list_of_vectors : list of np.ndarray each shape (N,)

    Returns
    -------
    Tuple of (stacked_matrix, flat_vector)
    """
    # TODO: stack as row matrix
    stacked = NotImplemented
    # TODO: concatenate into single 1-D vector
    flat = NotImplemented
    raise NotImplementedError("Fill in stack_arrays()")


# ---------------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------------

def _check(name: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")


def run_tests() -> None:
    print("=" * 60)
    print("P1_01 — NumPy Arrays & Vectorised Operations — Test Suite")
    print("=" * 60)

    # --- Test 1: create_arrays ---
    print("\n[1] create_arrays()")
    try:
        a, b, c, d = create_arrays()
        _check("a shape (10,)",  a.shape == (10,))
        _check("a dtype float",  np.issubdtype(a.dtype, np.floating))
        _check("b shape (3,4)",  b.shape == (3, 4))
        _check("b all zeros",    np.all(b == 0))
        _check("c shape (5,5)",  c.shape == (5, 5))
        _check("c is identity",  np.allclose(c, np.eye(5)))
        _check("d shape (2,3)",  d.shape == (2, 3))
        _check("d all sevens",   np.all(d == 7))
        _check("d dtype int32",  d.dtype == np.int32)
    except NotImplementedError:
        print("  [SKIP] Not implemented yet")

    # --- Test 2: reshape_and_slice ---
    print("\n[2] reshape_and_slice()")
    try:
        src = np.arange(24, dtype=float)
        reshaped, row, submatrix = reshape_and_slice(src)
        _check("reshaped shape (4,6)", reshaped.shape == (4, 6))
        _check("row is index-1 row",   np.array_equal(row, reshaped[1]))
        _check("submatrix shape (2,3)", submatrix.shape == (2, 3))
        _check("submatrix correct values",
               np.array_equal(submatrix, reshaped[1:3, 2:5]))
    except NotImplementedError:
        print("  [SKIP] Not implemented yet")

    # --- Test 3: broadcasting_demo ---
    print("\n[3] broadcasting_demo()")
    try:
        M = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
        v = np.array([10, 20, 30], dtype=float)
        result = broadcasting_demo(M, v)
        expected = np.array([[11, 22, 33], [14, 25, 36]], dtype=float)
        _check("shape preserved",   result.shape == M.shape)
        _check("values correct",    np.allclose(result, expected))
    except NotImplementedError:
        print("  [SKIP] Not implemented yet")

    # --- Test 4: normalise_rows ---
    print("\n[4] normalise_rows()")
    try:
        M = np.array([[3.0, 4.0], [0.0, 0.0], [1.0, 0.0]])
        result = normalise_rows(M)
        _check("shape preserved",        result.shape == M.shape)
        _check("row 0 unit norm",         np.isclose(np.linalg.norm(result[0]), 1.0))
        _check("zero row stays zero",     np.allclose(result[1], [0, 0]))
        _check("unit row stays unit",     np.isclose(np.linalg.norm(result[2]), 1.0))
    except NotImplementedError:
        print("  [SKIP] Not implemented yet")

    # --- Test 5: column_statistics ---
    print("\n[5] column_statistics()")
    try:
        M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
        means, stds, maxes = column_statistics(M)
        _check("means shape (3,)",    means.shape == (3,))
        _check("means correct",       np.allclose(means, [4, 5, 6]))
        _check("stds correct",        np.allclose(stds,  np.std(M, axis=0)))
        _check("maxes correct",       np.allclose(maxes, [7, 8, 9]))
    except NotImplementedError:
        print("  [SKIP] Not implemented yet")

    # --- Test 6: filter_and_replace ---
    print("\n[6] filter_and_replace()")
    try:
        arr = np.array([1.0, 5.0, 3.0, 8.0, 2.0])
        result = filter_and_replace(arr, threshold=4.0)
        expected = np.array([0.0, 5.0, 0.0, 8.0, 0.0])
        _check("shape preserved",   result.shape == arr.shape)
        _check("values correct",    np.allclose(result, expected))
        _check("original unchanged", np.allclose(arr, [1, 5, 3, 8, 2]))
    except NotImplementedError:
        print("  [SKIP] Not implemented yet")

    # --- Test 7: top_k_indices ---
    print("\n[7] top_k_indices()")
    try:
        arr = np.array([3.0, 9.0, 1.0, 7.0, 5.0])
        idxs = top_k_indices(arr, k=3)
        _check("length is k",         len(idxs) == 3)
        _check("top-3 correct set",   set(idxs) == {1, 3, 4})
        _check("descending order",    arr[idxs[0]] >= arr[idxs[1]] >= arr[idxs[2]])
    except NotImplementedError:
        print("  [SKIP] Not implemented yet")

    # --- Test 8: matrix_ops ---
    print("\n[8] matrix_ops()")
    try:
        A = np.array([[1.0, 2.0], [3.0, 4.0]])
        B = np.array([[5.0, 6.0], [7.0, 8.0]])
        C, A_sq, frob = matrix_ops(A, B)
        _check("C correct",       np.allclose(C, A @ B))
        _check("A_sq correct",    np.allclose(A_sq, A ** 2))
        _check("frob correct",    np.isclose(frob, np.linalg.norm(A, "fro")))
    except NotImplementedError:
        print("  [SKIP] Not implemented yet")

    # --- Test 9: stack_arrays ---
    print("\n[9] stack_arrays()")
    try:
        vecs = [np.array([1.0, 2.0, 3.0]), np.array([4.0, 5.0, 6.0])]
        stacked, flat = stack_arrays(vecs)
        _check("stacked shape (2,3)", stacked.shape == (2, 3))
        _check("flat shape (6,)",     flat.shape == (6,))
        _check("flat values correct", np.allclose(flat, [1, 2, 3, 4, 5, 6]))
    except NotImplementedError:
        print("  [SKIP] Not implemented yet")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    run_tests()
