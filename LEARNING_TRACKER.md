# FinSight AI/ML Learning Tracker

> **How to use this file:**
> At the start of each study session, open this file and check `## 📍 Current Position`.
> That tells you exactly which file to open and what to do with it.
> At the end of your session, paste your notes/answers here and I will update this file.
> Every Sunday we create a weekly summary.
>
> **Updated 2026-08-19** — added three fixes from a pre-mortem review (see `learning_ai_premortem_2026-08` in project memory for the full reasoning): a daily spaced-review habit that no longer waits for phase-end, a minimum-viable-day rule so a busy day still counts, and a daily 7:00 AM IST check-in nudge. None of this changes the curriculum content — only how it's paced day to day.

---

## 🔁 Daily Spaced Review (Anki) — do this every day, no matter what phase you're in

**One-time setup:** import `AI_Engineering_Spaced_Review.apkg` (in this same folder) into the free [Anki](https://apps.ankiweb.net/) app. It contains all 1,467 flashcards from every `anki_*.md` file in this curriculum, organized as one `AI Engineering` deck with a subdeck per phase. You only do this once.

**Every day:** open Anki, click into the `AI Engineering` deck, hit **Study Now**, and clear whatever cards it says are due. That's it — Anki's own spaced-repetition algorithm decides which cards to show you based on how well you knew them last time, so this naturally covers Phase 1 material even while you're deep into Phase 4. This replaces the old approach of reviewing Anki cards only inside a sub-topic session and once more at the end of the phase — reviewing a card twice, close together, isn't actually spaced repetition; the forgetting curve does most of its damage in the days *between* those two reviews, which is exactly the gap this fixes.

Typical daily review time: 5–15 minutes once the deck settles into a steady state (it'll be a bit more in the first couple of weeks while new cards are still being introduced — Anki caps new cards at 20/day by default, which paces that automatically).

---

## ✅ Minimum Viable Day

The full 5-step protocol below (~95 minutes) is the **target** for a day with a real time block. It is not the **minimum**. The minimum, non-negotiable action for any day — including a day with only 10–15 minutes — is: **clear the Anki due queue.** Nothing else is required to log the day as done.

Do the full protocol when you have the time. On a day you don't, do the Anki review only, log it in the Session Log below with Type = `Minimal`, and move on without guilt. A logged minimal day keeps the habit and the tracker's own record intact; a skipped, unlogged day is what turns into a multi-week gap (see the 2026-06-28 → 2026-08-19 gap this file already had on record before this update).

---

## 📍 Current Position

```
Phase   : Phase 1 — Foundations
Topic   : Topic 01 — Python for ML
Sub-topic: P1_01 — NumPy Arrays and Vectorised Operations
Step    : 1 of 5 → Read Power Doc
Status  : NOT STARTED
```

**Next action:** Open `Phase_1_Foundations/Topic_01_Python_for_ML/P1_01_numpy_arrays_vectorised_operations.md` and study it offline.

---

## 📅 Daily Session Protocol

Every session follows this exact sequence. Do not skip steps.

### Per sub-topic (repeat for each sub-topic in a topic)

| Step | Action | File | Time |
|------|--------|------|------|
| 0 | Clear today's Anki due queue (see Daily Spaced Review above). Do this first, every day, regardless of what else you have time for. | Anki app → `AI Engineering` deck | 5–15 min |
| 1 | Read the Power Doc offline. Build the mental model. | `PX_NN_<topic>.md` | 25 min |
| 2 | Review the Visual Cheat Sheet. Check what you missed. | `PX_NN_visual_cheat_sheet.md` | 10 min |
| 3 | ~~Go through Anki Cards from the markdown file~~ — superseded by Step 0. The `PX_NN_anki_*.md` files were the *source* the flashcard deck was generated from; you don't need to re-read them separately. | — | 0 min |
| 4 | Answer the Breaking Point QBank questions. Write answers. Bring them to me. | `PX_NN_breaking_point_qbank.md` | 20 min |
| 5 | Complete the Code Skeleton. Implement from scratch. Share code for review. | `PX_NN_code_skeleton.py` | 30 min |

### At the end of a topic group (after all sub-topics done)

| Step | Action | File | Time |
|------|--------|------|------|
| 6 | Complete the full Problem Set. Submit all solutions. | `PhaseX_TopicNN_*_ProblemSet.md` | 90 min |

### At the end of each phase

| Step | Action | File |
|------|--------|------|
| 7 | Review the Phase Connection Map to see how all concepts link together. | `PX_connection_map.md` |
| 8 | ~~Review the Anki batch file for the phase. Do full recall pass.~~ — no longer needed as a separate step; the daily Anki habit (Step 0) already keeps this phase's cards in rotation continuously. Optional: check this phase's tag in Anki's stats to confirm retention looks healthy. | `anki_cards_topics_*.md` |

### End of each week

Paste a short summary of what you covered and your scores. I will generate the weekly progress report.

A daily check-in nudge fires at 7:00 AM IST as a push notification — it's there so a busy week doesn't quietly turn into a silent month like the one this file already has on record. It's a nudge, not a guilt trip; a `Minimal` day logged below is a full success by this tracker's own rules.

---

## 📊 Session Log

| # | Date | Type | Sub-topics Covered | BPQ Score | Code Quality | Notes |
|---|------|------|--------------------|-----------|--------------|-------|
| — | — | — | No sessions yet | — | — | — |

`Type` is `Full` (all 5 steps) or `Minimal` (Anki due queue only, per the Minimum Viable Day rule above). Both count — log every day you touch this, even a Minimal one.

---

## 📆 Weekly Summaries

*No weeks completed yet.*

---

## 🗂 Full File Index

Legend: `[ ]` = not started · `[>]` = in progress · `[x]` = complete

---

### PHASE 1 — Foundations

Phase files: `Phase_1_Foundations/P1_connection_map.md` · `Phase_1_Foundations/anki_cards_topics_01_10.md`

---

#### Topic 01 — Python for ML
`Phase_1_Foundations/Topic_01_Python_for_ML/`

**Sub-topic P1_01 — NumPy Arrays and Vectorised Operations**
- [ ] `P1_01_numpy_arrays_vectorised_operations.md` ← Power Doc
- [ ] `P1_01_visual_cheat_sheet.md`
- [ ] `P1_01_breaking_point_qbank.md`
- [ ] `P1_01_code_skeleton.py`
- [ ] `P1_01_ProblemSet_NumPy.md` ← standalone NumPy problem set

**Sub-topic P1_02 — pandas DataFrames and Data Manipulation**
- [ ] `P1_02_pandas_dataframes_data_manipulation.md` ← Power Doc
- [ ] `P1_02_visual_cheat_sheet.md`
- [ ] `P1_02_breaking_point_qbank.md`
- [ ] `P1_02_code_skeleton.py`

**Sub-topic P1_03 — Python Type Hints and Data Classes**
- [ ] `P1_03_python_type_hints_dataclasses.md` ← Power Doc
- [ ] `P1_03_visual_cheat_sheet.md`
- [ ] `P1_03_breaking_point_qbank.md`
- [ ] `P1_03_code_skeleton.py`

**Sub-topic P1_04 — Exception Handling and Logging**
- [ ] `P1_04_exception_handling_logging.md` ← Power Doc
- [ ] `P1_04_visual_cheat_sheet.md`
- [ ] `P1_04_breaking_point_qbank.md`
- [ ] `P1_04_code_skeleton.py`

**Sub-topic P1_05 — Virtual Environments and Dependency Management**
- [ ] `P1_05_virtual_environments_dependency_management.md` ← Power Doc
- [ ] `P1_05_visual_cheat_sheet.md`
- [ ] `P1_05_breaking_point_qbank.md`
- [ ] `P1_05_code_skeleton.py`

**Topic 01 Problem Set**
- [ ] `Phase1_Topic1_Python_ML_ProblemSet.md` ← do after all 5 sub-topics above

---

#### Topic 02 — Embeddings and Vector Search
`Phase_1_Foundations/Topic_02_Embeddings_Vector_Search/`

**Sub-topic P1_06 — Word Embeddings and Sentence Embeddings**
- [ ] `P1_06_word_embeddings_sentence_embeddings.md` ← Power Doc
- [ ] `P1_06_visual_cheat_sheet.md`
- [ ] `P1_06_breaking_point_qbank.md`
- [ ] `P1_06_code_skeleton.py`

**Sub-topic P1_07 — Sentence Transformers: Encode, Pool, Normalise**
- [ ] `P1_07_sentence_transformers_encode_pool_normalise.md` ← Power Doc
- [ ] `P1_07_visual_cheat_sheet.md`
- [ ] `P1_07_breaking_point_qbank.md`
- [ ] `P1_07_code_skeleton.py`

**Sub-topic P1_08 — Cosine Similarity vs Dot Product vs Euclidean**
- [ ] `P1_08_cosine_similarity_dot_product_euclidean.md` ← Power Doc
- [ ] `P1_08_visual_cheat_sheet.md`
- [ ] `P1_08_breaking_point_qbank.md`
- [ ] `P1_08_code_skeleton.py`

**Sub-topic P1_09 — What is a Vector Database and Why it Exists**
- [ ] `P1_09_vector_database_why_it_exists.md` ← Power Doc
- [ ] `P1_09_visual_cheat_sheet.md`
- [ ] `P1_09_breaking_point_qbank.md`
- [ ] `P1_09_code_skeleton.py`

**Sub-topic P1_10 — ChromaDB Architecture**
- [ ] `P1_10_chromadb_architecture.md` ← Power Doc
- [ ] `P1_10_visual_cheat_sheet.md`
- [ ] `P1_10_breaking_point_qbank.md`
- [ ] `P1_10_code_skeleton.py`

**Sub-topic P1_11 — HNSW Approximate Nearest Neighbour Search**
- [ ] `P1_11_hnsw_approximate_nearest_neighbour.md` ← Power Doc
- [ ] `P1_11_visual_cheat_sheet.md`
- [ ] `P1_11_anki_hnsw_approximate_nearest_neighbour.md` ← Anki
- [ ] `P1_11_breaking_point_qbank.md`
- [ ] `P1_11_code_skeleton.py`

**Sub-topic P1_12 — Embedding Model Selection (mpnet vs MiniLM)**
- [ ] `P1_12_embedding_model_selection_mpnet_vs_minilm.md` ← Power Doc
- [ ] `P1_12_visual_cheat_sheet.md`
- [ ] `P1_12_anki_embedding_model_selection_mpnet_vs_minilm.md` ← Anki
- [ ] `P1_12_breaking_point_qbank.md`
- [ ] `P1_12_code_skeleton.py`

**Topic 02 Problem Set**
- [ ] `Phase1_Topic2_Embeddings_VectorSearch_ProblemSet.md`

---

#### Topic 03 — Sparse Search
`Phase_1_Foundations/Topic_03_Sparse_Search/`

**Sub-topic P1_13 — TF-IDF: Term Frequency and Inverse Document Frequency**
- [ ] `P1_13_tfidf_term_frequency_inverse_document_frequency.md` ← Power Doc
- [ ] `P1_13_visual_cheat_sheet.md`
- [ ] `P1_13_breaking_point_qbank.md`
- [ ] `P1_13_code_skeleton.py`

**Sub-topic P1_14 — BM25: How it Improves on TF-IDF**
- [ ] `P1_14_bm25_how_it_improves_on_tfidf.md` ← Power Doc
- [ ] `P1_14_visual_cheat_sheet.md`
- [ ] `P1_14_breaking_point_qbank.md`
- [ ] `P1_14_code_skeleton.py`

**Sub-topic P1_15 — When Keyword Search Beats Semantic Search**
- [ ] `P1_15_keyword_search_vs_semantic_search.md` ← Power Doc
- [ ] `P1_15_visual_cheat_sheet.md`
- [ ] `P1_15_breaking_point_qbank.md`
- [ ] `P1_15_code_skeleton.py`

**Topic 03 Problem Set**
- [ ] `Phase1_Topic3_Sparse_Search_Problem_Set.md`

---

#### Topic 04 — Hybrid Search and Reranking
`Phase_1_Foundations/Topic_04_Hybrid_Search_Reranking/`

**Sub-topic P1_16 — Why Hybrid Search Exists: Dense vs Sparse Tradeoffs**
- [ ] `P1_16_hybrid_search_dense_vs_sparse.md` ← Power Doc
- [ ] `P1_16_visual_cheat_sheet.md`
- [ ] `P1_16_breaking_point_qbank.md`
- [ ] `P1_16_code_skeleton.py`

**Sub-topic P1_17 — Reciprocal Rank Fusion**
- [ ] `P1_17_reciprocal_rank_fusion.md` ← Power Doc
- [ ] `P1_17_visual_cheat_sheet.md`
- [ ] `P1_17_breaking_point_qbank.md`
- [ ] `P1_17_code_skeleton.py`

**Sub-topic P1_18 — Cross-encoders vs Bi-encoders**
- [ ] `P1_18_cross_encoders_vs_bi_encoders.md` ← Power Doc
- [ ] `P1_18_visual_cheat_sheet.md`
- [ ] `P1_18_breaking_point_qbank.md`
- [ ] `P1_18_code_skeleton.py`

**Sub-topic P1_19 — Why Reranking Improves Precision**
- [ ] `P1_19_reranking_improves_precision.md` ← Power Doc
- [ ] `P1_19_visual_cheat_sheet.md`
- [ ] `P1_19_breaking_point_qbank.md`
- [ ] `P1_19_code_skeleton.py`

**Topic 04 Problem Set**
- [ ] `Phase1_Topic4_Hybrid_Search_Reranking_ProblemSet.md`

**Phase 1 Wrap-up**
- [ ] `P1_connection_map.md` ← connect all Phase 1 concepts
- [ ] `anki_cards_topics_01_10.md` ← full Phase 1 Anki recall pass

---

### PHASE 2 — RAG

Phase files: `Phase_2_RAG/P2_connection_map.md` · `Phase_2_RAG/anki_topics_11_20.md`

---

#### Topic 05 — RAG Fundamentals
`Phase_2_RAG/Topic_05_RAG_Fundamentals/`

**Sub-topic P2_01 — What RAG is and Why it Exists**
- [ ] `P2_01_what_is_rag_and_why_it_exists.md` ← Power Doc
- [ ] `P2_01_visual_cheat_sheet.md`
- [ ] `P2_01_breaking_point_qbank.md`
- [ ] `P2_01_code_skeleton.py`

**Sub-topic P2_02 — Chunking Strategies**
- [ ] `P2_02_chunking_strategies.md` ← Power Doc
- [ ] `P2_02_visual_cheat_sheet.md`
- [ ] `P2_02_breaking_point_qbank.md`
- [ ] `P2_02_code_skeleton.py`

**Sub-topic P2_03 — Naive RAG vs Advanced RAG vs Modular RAG**
- [ ] `P2_03_naive_advanced_modular_rag.md` ← Power Doc
- [ ] `P2_03_visual_cheat_sheet.md`
- [ ] `P2_03_breaking_point_qbank.md`
- [ ] `P2_03_code_skeleton.py`

**Sub-topic P2_04 — Context Window Management**
- [ ] `P2_04_context_window_management.md` ← Power Doc
- [ ] `P2_04_visual_cheat_sheet.md`
- [ ] `P2_04_breaking_point_qbank.md`
- [ ] `P2_04_code_skeleton.py`

**Sub-topic P2_05 — The Lost-in-the-Middle Problem**
- [ ] `P2_05_lost_in_the_middle.md` ← Power Doc
- [ ] `P2_05_visual_cheat_sheet.md`
- [ ] `P2_05_breaking_point_qbank.md`
- [ ] `P2_05_code_skeleton.py`

**Sub-topic P2_06 — RAG Evaluation Metrics**
- [ ] `P2_06_rag_evaluation_metrics.md` ← Power Doc
- [ ] `P2_06_visual_cheat_sheet.md`
- [ ] `P2_06_breaking_point_qbank.md`
- [ ] `P2_06_code_skeleton.py`

**Topic 05 Problem Set**
- [ ] `Phase2_Topic5_RAG_Fundamentals_ProblemSet.md`

---

#### Topic 06 — LangGraph and Agent Orchestration
`Phase_2_RAG/Topic_06_LangGraph_Agent_Orchestration/`

**Sub-topic P2_07 — LangGraph vs LangChain**
- [ ] `P2_07_langgraph_vs_langchain.md` ← Power Doc
- [ ] `P2_07_visual_cheat_sheet.md`
- [ ] `P2_07_breaking_point_qbank.md`
- [ ] `P2_07_code_skeleton.py`

**Sub-topic P2_08 — StateGraph: Nodes, Edges, Conditional Edges**
- [ ] `P2_08_stategraph_nodes_edges.md` ← Power Doc
- [ ] `P2_08_visual_cheat_sheet.md`
- [ ] `P2_08_breaking_point_qbank.md`
- [ ] `P2_08_code_skeleton.py`

**Sub-topic P2_09 — Agent State: TypedDict**
- [ ] `P2_09_agent_state_typeddict.md` ← Power Doc
- [ ] `P2_09_visual_cheat_sheet.md`
- [ ] `P2_09_breaking_point_qbank.md`
- [ ] `P2_09_code_skeleton.py`

**Sub-topic P2_10 — Tool Calling**
- [ ] `P2_10_tool_calling.md` ← Power Doc
- [ ] `P2_10_visual_cheat_sheet.md`
- [ ] `P2_10_breaking_point_qbank.md`
- [ ] `P2_10_code_skeleton.py`

**Sub-topic P2_11 — ReAct Pattern**
- [ ] `P2_11_react_pattern.md` ← Power Doc
- [ ] `P2_11_visual_cheat_sheet.md`
- [ ] `P2_11_breaking_point_qbank.md`
- [ ] `P2_11_code_skeleton.py`

**Sub-topic P2_12 — Memory in Agents: Short Term vs Long Term**
- [ ] `P2_12_agent_memory_short_long_term.md` ← Power Doc
- [ ] `P2_12_visual_cheat_sheet.md`
- [ ] `P2_12_breaking_point_qbank.md`
- [ ] `P2_12_code_skeleton.py`

**Sub-topic P2_13 — Human-in-the-Loop Patterns in LangGraph**
- [ ] `P2_13_human_in_the_loop_langgraph.md` ← Power Doc
- [ ] `P2_13_visual_cheat_sheet.md`
- [ ] `P2_13_breaking_point_qbank.md`
- [ ] `P2_13_code_skeleton.py`

**Topic 06 Problem Set**
- [ ] `Phase2_Topic6_LangGraph_AgentOrchestration_ProblemSet.md`

---

#### Topic 07 — LLM Fundamentals
`Phase_2_RAG/Topic_07_LLM_Fundamentals/`

**Sub-topic P2_14 — Transformer Architecture**
- [ ] `P2_14_transformer_architecture.md` ← Power Doc
- [ ] `P2_14_visual_cheat_sheet.md`
- [ ] `P2_14_breaking_point_qbank.md`
- [ ] `P2_14_code_skeleton.py`

**Sub-topic P2_15 — Tokenisation: BPE, Context Windows, Token Counting**
- [ ] `P2_15_tokenisation_bpe_context_windows.md` ← Power Doc
- [ ] `P2_15_visual_cheat_sheet.md`
- [ ] `P2_15_breaking_point_qbank.md`
- [ ] `P2_15_code_skeleton.py`

**Sub-topic P2_16 — Temperature, Top-k, Top-p**
- [ ] `P2_16_temperature_top_k_top_p.md` ← Power Doc
- [ ] `P2_16_visual_cheat_sheet.md`
- [ ] `P2_16_breaking_point_qbank.md`
- [ ] `P2_16_code_skeleton.py`

**Sub-topic P2_17 — System Prompts vs User Prompts vs Assistant Turns**
- [ ] `P2_17_system_user_assistant_prompts.md` ← Power Doc
- [ ] `P2_17_visual_cheat_sheet.md`
- [ ] `P2_17_breaking_point_qbank.md`
- [ ] `P2_17_code_skeleton.py`

**Sub-topic P2_18 — Structured Output and JSON Mode**
- [ ] `P2_18_structured_output_json_mode.md` ← Power Doc
- [ ] `P2_18_visual_cheat_sheet.md`
- [ ] `P2_18_breaking_point_qbank.md`
- [ ] `P2_18_code_skeleton.py`

**Sub-topic P2_19 — Function Calling and Tool Use**
- [ ] `P2_19_function_calling_tool_use.md` ← Power Doc
- [ ] `P2_19_visual_cheat_sheet.md`
- [ ] `P2_19_breaking_point_qbank.md`
- [ ] `P2_19_code_skeleton.py`

**Sub-topic P2_20 — Prompt Engineering**
- [ ] `P2_20_prompt_engineering.md` ← Power Doc
- [ ] `P2_20_visual_cheat_sheet.md`
- [ ] `P2_20_breaking_point_qbank.md`
- [ ] `P2_20_code_skeleton.py`

**Topic 07 Problem Set**
- [ ] `Phase2_Topic7_LLM_Fundamentals_ProblemSet.md`

**Phase 2 Wrap-up**
- [ ] `P2_connection_map.md`
- [ ] `anki_topics_11_20.md`

---

### PHASE 3 — Evaluation and Production

Phase files: `Phase_3_Evaluation_Production/P3_connection_map.md` · `Phase_3_Evaluation_Production/Anki_Cards_Topics_21_30.md`

---

#### Topic 08 — RAGAS Evaluation Framework
`Phase_3_Evaluation_Production/Topic_08_RAGAS_Evaluation/`

**Sub-topic P3_01 — Faithfulness**
- [ ] `P3_01_ragas_faithfulness.md` ← Power Doc
- [ ] `P3_01_visual_cheat_sheet.md`
- [ ] `P3_01_breaking_point_qbank.md`
- [ ] `P3_01_code_skeleton.py`

**Sub-topic P3_02 — Answer Relevancy**
- [ ] `P3_02_ragas_answer_relevancy.md` ← Power Doc
- [ ] `P3_02_visual_cheat_sheet.md`
- [ ] `P3_02_breaking_point_qbank.md`
- [ ] `P3_02_code_skeleton.py`

**Sub-topic P3_03 — Context Precision**
- [ ] `P3_03_ragas_context_precision.md` ← Power Doc
- [ ] `P3_03_visual_cheat_sheet.md`
- [ ] `P3_03_breaking_point_qbank.md`
- [ ] `P3_03_code_skeleton.py`

**Sub-topic P3_04 — Context Recall**
- [ ] `P3_04_ragas_context_recall.md` ← Power Doc
- [ ] `P3_04_visual_cheat_sheet.md`
- [ ] `P3_04_breaking_point_qbank.md`
- [ ] `P3_04_code_skeleton.py`

**Sub-topic P3_05 — How to Build a Golden Test Set**
- [ ] `P3_05_golden_test_set.md` ← Power Doc
- [ ] `P3_05_visual_cheat_sheet.md`
- [ ] `P3_05_breaking_point_qbank.md`
- [ ] `P3_05_code_skeleton.py`

**Sub-topic P3_06 — LLM-as-Judge Pattern**
- [ ] `P3_06_llm_as_judge.md` ← Power Doc
- [ ] `P3_06_visual_cheat_sheet.md`
- [ ] `P3_06_breaking_point_qbank.md`
- [ ] `P3_06_code_skeleton.py`

**Topic 08 Problem Set**
- [ ] `Phase3_Topic8_RAGAS_Evaluation_ProblemSet.md`

---

#### Topic 09 — MLOps and Experiment Tracking
`Phase_3_Evaluation_Production/Topic_09_MLOps_Experiment_Tracking/`

**Sub-topic P3_07 — What Experiment Tracking Solves**
- [ ] `P3_07_experiment_tracking.md` ← Power Doc
- [ ] `P3_07_visual_cheat_sheet.md`
- [ ] `P3_07_breaking_point_qbank.md`
- [ ] `P3_07_code_skeleton.py`

**Sub-topic P3_08 — Weights and Biases**
- [ ] `P3_08_weights_and_biases.md` ← Power Doc
- [ ] `P3_08_visual_cheat_sheet.md`
- [ ] `P3_08_breaking_point_qbank.md`
- [ ] `P3_08_code_skeleton.py`

**Sub-topic P3_09 — Model Versioning and Model Registry**
- [ ] `P3_09_model_versioning_registry.md` ← Power Doc
- [ ] `P3_09_visual_cheat_sheet.md`
- [ ] `P3_09_breaking_point_qbank.md`
- [ ] `P3_09_code_skeleton.py`

**Sub-topic P3_10 — Data Versioning**
- [ ] `P3_10_data_versioning.md` ← Power Doc
- [ ] `P3_10_visual_cheat_sheet.md`
- [ ] `P3_10_breaking_point_qbank.md`
- [ ] `P3_10_code_skeleton.py`

**Sub-topic P3_11 — CI/CD for ML**
- [ ] `P3_11_cicd_for_ml.md` ← Power Doc
- [ ] `P3_11_visual_cheat_sheet.md`
- [ ] `P3_11_breaking_point_qbank.md`
- [ ] `P3_11_code_skeleton.py`

**Sub-topic P3_12 — Monitoring: Data Drift and Concept Drift**
- [ ] `P3_12_monitoring_data_concept_drift.md` ← Power Doc
- [ ] `P3_12_visual_cheat_sheet.md`
- [ ] `P3_12_breaking_point_qbank.md`
- [ ] `P3_12_code_skeleton.py`

**Topic 09 Problem Set**
- [ ] `Phase3_Topic9_MLOps_ExperimentTracking_ProblemSet.md`

---

#### Topic 10 — FastAPI for ML Services
`Phase_3_Evaluation_Production/Topic_10_FastAPI_ML_Services/`

**Sub-topic P3_13 — FastAPI vs Flask vs Express**
- [ ] `P3_13_fastapi_vs_flask_vs_express.md` ← Power Doc
- [ ] `P3_13_visual_cheat_sheet.md`
- [ ] `P3_13_breaking_point_qbank.md`
- [ ] `P3_13_code_skeleton.py`

**Sub-topic P3_14 — Pydantic Models**
- [ ] `P3_14_pydantic_models.md` ← Power Doc
- [ ] `P3_14_visual_cheat_sheet.md`
- [ ] `P3_14_breaking_point_qbank.md`
- [ ] `P3_14_code_skeleton.py`

**Sub-topic P3_15 — Async Endpoints**
- [ ] `P3_15_async_endpoints.md` ← Power Doc
- [ ] `P3_15_visual_cheat_sheet.md`
- [ ] `P3_15_breaking_point_qbank.md`
- [ ] `P3_15_code_skeleton.py`

**Sub-topic P3_16 — Background Tasks in FastAPI**
- [ ] `P3_16_background_tasks.md` ← Power Doc
- [ ] `P3_16_visual_cheat_sheet.md`
- [ ] `P3_16_breaking_point_qbank.md`
- [ ] `P3_16_code_skeleton.py`

**Sub-topic P3_17 — OpenAPI Docs Auto-generation**
- [ ] `P3_17_openapi_docs.md` ← Power Doc
- [ ] `P3_17_visual_cheat_sheet.md`
- [ ] `P3_17_breaking_point_qbank.md`
- [ ] `P3_17_code_skeleton.py`

**Sub-topic P3_18 — Health Check Endpoints**
- [ ] `P3_18_health_check_endpoints.md` ← Power Doc
- [ ] `P3_18_visual_cheat_sheet.md`
- [ ] `P3_18_breaking_point_qbank.md`
- [ ] `P3_18_code_skeleton.py`

**Topic 10 Problem Set**
- [ ] `Phase3_Topic10_FastAPI_MLServices_ProblemSet.md`

**Phase 3 Wrap-up**
- [ ] `P3_connection_map.md`
- [ ] `Anki_Cards_Topics_21_30.md`

---

### PHASE 4 — Deployment

Phase files: `Phase_4_Deployment/P4_connection_map.md` · `Phase_4_Deployment/anki_cards_topics_31_40.md`

---

#### Topic 11 — Docker for ML
`Phase_4_Deployment/Topic_11_Docker_ML/`

**Sub-topic P4_01 — Docker Concepts: Image, Container, Layer, Volume, Network**
- [ ] `P4_01_docker_concepts.md` ← Power Doc
- [ ] `P4_01_visual_cheat_sheet.md`
- [ ] `P4_01_breaking_point_qbank.md`
- [ ] `P4_01_code_skeleton.py`

**Sub-topic P4_02 — Writing a Dockerfile for a Python ML Service**
- [ ] `P4_02_dockerfile_python_ml.md` ← Power Doc
- [ ] `P4_02_visual_cheat_sheet.md`
- [ ] `P4_02_breaking_point_qbank.md`
- [ ] `P4_02_code_skeleton.py`

**Sub-topic P4_03 — docker-compose for Multi-service Setup**
- [ ] `P4_03_docker_compose.md` ← Power Doc
- [ ] `P4_03_visual_cheat_sheet.md`
- [ ] `P4_03_breaking_point_qbank.md`
- [ ] `P4_03_code_skeleton.py`

**Sub-topic P4_04 — Environment Variables and Secrets Management**
- [ ] `P4_04_env_vars_secrets.md` ← Power Doc
- [ ] `P4_04_visual_cheat_sheet.md`
- [ ] `P4_04_breaking_point_qbank.md`
- [ ] `P4_04_code_skeleton.py`

**Sub-topic P4_05 — Why ML Docker Images are Large and How to Reduce Size**
- [ ] `P4_05_ml_docker_image_size.md` ← Power Doc
- [ ] `P4_05_visual_cheat_sheet.md`
- [ ] `P4_05_breaking_point_qbank.md`
- [ ] `P4_05_code_skeleton.py`

**Sub-topic P4_06 — Multi-stage Builds**
- [ ] `P4_06_multi_stage_builds.md` ← Power Doc
- [ ] `P4_06_visual_cheat_sheet.md`
- [ ] `P4_06_breaking_point_qbank.md`
- [ ] `P4_06_code_skeleton.py`

**Topic 11 Problem Set**
- [ ] `Phase4_Topic11_Docker_ML_ProblemSet.md`

---

#### Topic 12 — MCP Protocol
`Phase_4_Deployment/Topic_12_MCP_Protocol/`

**Sub-topic P4_07 — What Model Context Protocol Is and Why Anthropic Created It**
- [ ] `P4_07_what_is_mcp.md` ← Power Doc
- [ ] `P4_07_visual_cheat_sheet.md`
- [ ] `P4_07_breaking_point_qbank.md`
- [ ] `P4_07_code_skeleton.py`

**Sub-topic P4_08 — MCP Server vs MCP Client Architecture**
- [ ] `P4_08_mcp_server_client_architecture.md` ← Power Doc
- [ ] `P4_08_visual_cheat_sheet.md`
- [ ] `P4_08_breaking_point_qbank.md`
- [ ] `P4_08_code_skeleton.py`

**Sub-topic P4_09 — Tools vs Resources vs Prompts in MCP**
- [ ] `P4_09_mcp_tools_resources_prompts.md` ← Power Doc
- [ ] `P4_09_visual_cheat_sheet.md`
- [ ] `P4_09_breaking_point_qbank.md`
- [ ] `P4_09_code_skeleton.py`

**Sub-topic P4_10 — FastMCP Library**
- [ ] `P4_10_fastmcp.md` ← Power Doc
- [ ] `P4_10_visual_cheat_sheet.md`
- [ ] `P4_10_breaking_point_qbank.md`
- [ ] `P4_10_code_skeleton.py`

**Sub-topic P4_11 — How Claude Desktop Discovers and Calls MCP Tools**
- [ ] `P4_11_claude_desktop_mcp.md` ← Power Doc
- [ ] `P4_11_visual_cheat_sheet.md`
- [ ] `P4_11_breaking_point_qbank.md`
- [ ] `P4_11_code_skeleton.py`

**Sub-topic P4_12 — MCP vs Function Calling**
- [ ] `P4_12_mcp_vs_function_calling.md` ← Power Doc
- [ ] `P4_12_visual_cheat_sheet.md`
- [ ] `P4_12_breaking_point_qbank.md`
- [ ] `P4_12_code_skeleton.py`

**Topic 12 Problem Set**
- [ ] `Phase4_Topic12_MCP_Protocol_ProblemSet.md`

**Phase 4 Wrap-up**
- [ ] `P4_connection_map.md`
- [ ] `anki_cards_topics_31_40.md`

---

### PHASE 5 — Fine-tuning

Phase files: `Phase_5_Fine_Tuning/P5_connection_map.md` · `Phase_5_Fine_Tuning/anki_cards_41_50.md` · `Phase_5_Fine_Tuning/anki_topics_51_60.md`

---

#### Topic 13 — Fine-tuning Fundamentals
`Phase_5_Fine_Tuning/Topic_13_Fine_Tuning_Fundamentals/`

**Sub-topic P5_01 — When to Fine-tune vs Prompt Engineer vs RAG**
- [ ] `P5_01_when_to_finetune.md` ← Power Doc
- [ ] `P5_01_visual_cheat_sheet.md`
- [ ] `P5_01_breaking_point_qbank.md`
- [ ] `P5_01_code_skeleton.py`

**Sub-topic P5_02 — Full Fine-tuning vs Parameter Efficient Fine-tuning**
- [ ] `P5_02_full_finetuning_vs_peft.md` ← Power Doc
- [ ] `P5_02_visual_cheat_sheet.md`
- [ ] `P5_02_breaking_point_qbank.md`
- [ ] `P5_02_code_skeleton.py`

**Sub-topic P5_03 — LoRA: Low Rank Adaptation**
- [ ] `P5_03_lora.md` ← Power Doc
- [ ] `P5_03_visual_cheat_sheet.md`
- [ ] `P5_03_breaking_point_qbank.md`
- [ ] `P5_03_code_skeleton.py`

**Sub-topic P5_04 — QLoRA: Quantisation + LoRA**
- [ ] `P5_04_qlora.md` ← Power Doc
- [ ] `P5_04_visual_cheat_sheet.md`
- [ ] `P5_04_breaking_point_qbank.md`
- [ ] `P5_04_code_skeleton.py`

**Sub-topic P5_05 — Supervised Fine-tuning**
- [ ] `P5_05_supervised_fine_tuning.md` ← Power Doc
- [ ] `P5_05_visual_cheat_sheet.md`
- [ ] `P5_05_breaking_point_qbank.md`
- [ ] `P5_05_code_skeleton.py`

**Sub-topic P5_06 — DPO: Direct Preference Optimisation**
- [ ] `P5_06_dpo.md` ← Power Doc
- [ ] `P5_06_visual_cheat_sheet.md`
- [ ] `P5_06_breaking_point_qbank.md`
- [ ] `P5_06_code_skeleton.py`

**Sub-topic P5_07 — Hugging Face TRL Library**
- [ ] `P5_07_huggingface_trl.md` ← Power Doc
- [ ] `P5_07_visual_cheat_sheet.md`
- [ ] `P5_07_breaking_point_qbank.md`
- [ ] `P5_07_code_skeleton.py`

**Sub-topic P5_08 — Unsloth**
- [ ] `P5_08_unsloth.md` ← Power Doc
- [ ] `P5_08_visual_cheat_sheet.md`
- [ ] `P5_08_breaking_point_qbank.md`
- [ ] `P5_08_code_skeleton.py`

**Topic 13 Problem Set**
- [ ] `Phase5_Topic13_FineTuning_Fundamentals_ProblemSet.md`

---

#### Topic 14 — Model Quantisation
`Phase_5_Fine_Tuning/Topic_14_Model_Quantisation/`

**Sub-topic P5_09 — Why Quantisation Exists: Memory vs Accuracy Tradeoff**
- [ ] `P5_09_why_quantisation_exists.md` ← Power Doc
- [ ] `P5_09_visual_cheat_sheet.md`
- [ ] `P5_09_breaking_point_qbank.md`
- [ ] `P5_09_code_skeleton.py`

**Sub-topic P5_10 — INT8, INT4, FP16, BF16**
- [ ] `P5_10_int8_int4_fp16_bf16.md` ← Power Doc
- [ ] `P5_10_visual_cheat_sheet.md`
- [ ] `P5_10_breaking_point_qbank.md`
- [ ] `P5_10_code_skeleton.py`

**Sub-topic P5_11 — GPTQ: Post Training Quantisation**
- [ ] `P5_11_gptq.md` ← Power Doc
- [ ] `P5_11_visual_cheat_sheet.md`
- [ ] `P5_11_breaking_point_qbank.md`
- [ ] `P5_11_code_skeleton.py`

**Sub-topic P5_12 — AWQ: Activation Aware Weight Quantisation**
- [ ] `P5_12_awq.md` ← Power Doc
- [ ] `P5_12_visual_cheat_sheet.md`
- [ ] `P5_12_breaking_point_qbank.md`
- [ ] `P5_12_code_skeleton.py`

**Sub-topic P5_13 — GGUF: Format for CPU Inference via llama.cpp**
- [ ] `P5_13_gguf.md` ← Power Doc
- [ ] `P5_13_visual_cheat_sheet.md`
- [ ] `P5_13_breaking_point_qbank.md`
- [ ] `P5_13_code_skeleton.py`

**Sub-topic P5_14 — bitsandbytes Library**
- [ ] `P5_14_bitsandbytes.md` ← Power Doc
- [ ] `P5_14_visual_cheat_sheet.md`
- [ ] `P5_14_anki_bitsandbytes.md` ← Anki
- [ ] `P5_14_breaking_point_qbank.md`
- [ ] `P5_14_code_skeleton.py`

**Topic 14 Problem Set**
- [ ] `Phase5_Topic14_ModelQuantisation_ProblemSet.md`

**Phase 5 Wrap-up**
- [ ] `P5_connection_map.md`
- [ ] `anki_cards_41_50.md`
- [ ] `anki_topics_51_60.md`

---

### PHASE 6 — Advanced

Phase files: `Phase_6_Advanced/P6_connection_map.md` · `Phase_6_Advanced/anki_cards_topics_61_70.md` · `Phase_6_Advanced/anki_cards_topics_71_80.md`

---

#### Topic 15 — Distributed Training
`Phase_6_Advanced/Topic_15_Distributed_Training/`

**Overview**
- [ ] `P6_00_overview_distributed_training.md` ← read first

**Sub-topic P6_01 — Data Parallelism vs Model Parallelism vs Pipeline Parallelism**
- [ ] `P6_01_data_model_pipeline_parallelism.md` ← Power Doc
- [ ] `P6_01_visual_cheat_sheet.md`
- [ ] `P6_01_anki_data_model_pipeline_parallelism.md` ← Anki
- [ ] `P6_01_breaking_point_qbank.md`
- [ ] `P6_01_code_skeleton.py`

**Sub-topic P6_02 — PyTorch DDP: Distributed Data Parallel**
- [ ] `P6_02_pytorch_ddp.md` ← Power Doc
- [ ] `P6_02_visual_cheat_sheet.md`
- [ ] `P6_02_anki_pytorch_ddp.md` ← Anki
- [ ] `P6_02_breaking_point_qbank.md`
- [ ] `P6_02_code_skeleton.py`

**Sub-topic P6_03 — PyTorch FSDP: Fully Sharded Data Parallel**
- [ ] `P6_03_pytorch_fsdp.md` ← Power Doc
- [ ] `P6_03_visual_cheat_sheet.md`
- [ ] `P6_03_anki_pytorch_fsdp.md` ← Anki
- [ ] `P6_03_breaking_point_qbank.md`
- [ ] `P6_03_code_skeleton.py`

**Sub-topic P6_04 — DeepSpeed ZeRO Stages 1, 2, 3**
- [ ] `P6_04_deepspeed_zero.md` ← Power Doc
- [ ] `P6_04_visual_cheat_sheet.md`
- [ ] `P6_04_anki_deepspeed_zero.md` ← Anki
- [ ] `P6_04_breaking_point_qbank.md`
- [ ] `P6_04_code_skeleton.py`

**Sub-topic P6_05 — Gradient Accumulation and Gradient Checkpointing**
- [ ] `P6_05_gradient_accumulation_checkpointing.md` ← Power Doc
- [ ] `P6_05_visual_cheat_sheet.md`
- [ ] `P6_05_anki_gradient_accumulation_checkpointing.md` ← Anki
- [ ] `P6_05_breaking_point_qbank.md`
- [ ] `P6_05_code_skeleton.py`

**Sub-topic P6_06 — Mixed Precision Training**
- [ ] `P6_06_mixed_precision_training.md` ← Power Doc
- [ ] `P6_06_visual_cheat_sheet.md`
- [ ] `P6_06_anki_mixed_precision_training.md` ← Anki
- [ ] `P6_06_breaking_point_qbank.md`
- [ ] `P6_06_code_skeleton.py`

**Topic 15 Problem Set**
- [ ] `Phase6_Topic15_DistributedTraining_ProblemSet.md`

---

#### Topic 16 — Reinforcement Learning for LLMs
`Phase_6_Advanced/Topic_16_RL_for_LLMs/`

**Overview**
- [ ] `P6_00_overview_rl_for_llms.md` ← read first

**Sub-topic P6_07 — What RLHF Is: Reward Model, PPO Loop**
- [ ] `P6_07_rlhf.md` ← Power Doc
- [ ] `P6_07_visual_cheat_sheet.md`
- [ ] `P6_07_anki_rlhf.md` ← Anki
- [ ] `P6_07_breaking_point_qbank.md`
- [ ] `P6_07_code_skeleton.py`

**Sub-topic P6_08 — PPO: Proximal Policy Optimisation**
- [ ] `P6_08_ppo.md` ← Power Doc
- [ ] `P6_08_visual_cheat_sheet.md`
- [ ] `P6_08_anki_ppo.md` ← Anki
- [ ] `P6_08_breaking_point_qbank.md`
- [ ] `P6_08_code_skeleton.py`

**Sub-topic P6_09 — DPO: How it Eliminates the Reward Model**
- [ ] `P6_09_dpo_rl_context.md` ← Power Doc
- [ ] `P6_09_visual_cheat_sheet.md`
- [ ] `P6_09_anki_dpo_rl_context.md` ← Anki
- [ ] `P6_09_breaking_point_qbank.md`
- [ ] `P6_09_code_skeleton.py`

**Sub-topic P6_10 — GRPO: Group Relative Policy Optimisation**
- [ ] `P6_10_grpo.md` ← Power Doc
- [ ] `P6_10_visual_cheat_sheet.md`
- [ ] `P6_10_anki_grpo.md` ← Anki
- [ ] `P6_10_breaking_point_qbank.md`
- [ ] `P6_10_code_skeleton.py`

**Sub-topic P6_11 — Constitutional AI**
- [ ] `P6_11_constitutional_ai.md` ← Power Doc
- [ ] `P6_11_visual_cheat_sheet.md`
- [ ] `P6_11_anki_constitutional_ai.md` ← Anki
- [ ] `P6_11_breaking_point_qbank.md`
- [ ] `P6_11_code_skeleton.py`

**Sub-topic P6_12 — Reward Hacking: Why RLHF Fails and Mitigations**
- [ ] `P6_12_reward_hacking.md` ← Power Doc
- [ ] `P6_12_visual_cheat_sheet.md`
- [ ] `P6_12_anki_reward_hacking.md` ← Anki
- [ ] `P6_12_breaking_point_qbank.md`
- [ ] `P6_12_code_skeleton.py`

**Topic 16 Problem Set**
- [ ] `Phase6_Topic16_RLforLLMs_ProblemSet.md`

---

#### Topic 17 — Mechanistic Interpretability
`Phase_6_Advanced/Topic_17_Mechanistic_Interpretability/`

**Sub-topic P6_13 — What Superposition Is in Neural Networks**
- [ ] `P6_13_superposition_in_neural_networks.md` ← Power Doc
- [ ] `P6_13_visual_cheat_sheet.md`
- [ ] `P6_13_anki_superposition_in_neural_networks.md` ← Anki
- [ ] `P6_13_breaking_point_qbank.md`
- [ ] `P6_13_code_skeleton.py`

**Sub-topic P6_14 — Sparse Autoencoders**
- [ ] `P6_14_sparse_autoencoders.md` ← Power Doc
- [ ] `P6_14_visual_cheat_sheet.md`
- [ ] `P6_14_anki_sparse_autoencoders.md` ← Anki
- [ ] `P6_14_breaking_point_qbank.md`
- [ ] `P6_14_code_skeleton.py`

**Sub-topic P6_15 — Circuits: Attention Heads as Computational Units**
- [ ] `P6_15_circuits_attention_heads.md` ← Power Doc
- [ ] `P6_15_visual_cheat_sheet.md`
- [ ] `P6_15_anki_circuits_attention_heads.md` ← Anki
- [ ] `P6_15_breaking_point_qbank.md`
- [ ] `P6_15_code_skeleton.py`

**Sub-topic P6_16 — Linear Probes: Finding Concepts in Activation Space**
- [ ] `P6_16_linear_probes.md` ← Power Doc
- [ ] `P6_16_visual_cheat_sheet.md`
- [ ] `P6_16_anki_linear_probes.md` ← Anki
- [ ] `P6_16_breaking_point_qbank.md`
- [ ] `P6_16_code_skeleton.py`

**Sub-topic P6_17 — Ablation Studies**
- [ ] `P6_17_ablation_studies.md` ← Power Doc
- [ ] `P6_17_visual_cheat_sheet.md`
- [ ] `P6_17_anki_ablation_studies.md` ← Anki
- [ ] `P6_17_breaking_point_qbank.md`
- [ ] `P6_17_code_skeleton.py`

**Topic 17 Problem Set**
- [ ] `Phase6_Topic17_MechanisticInterpretability_ProblemSet.md`

---

#### Topic 18 — Scaling Laws
`Phase_6_Advanced/Topic_18_Scaling_Laws/`

**Sub-topic P6_18 — Kaplan et al 2020: The Original OpenAI Scaling Paper**
- [ ] `P6_18_kaplan_scaling_laws_2020.md` ← Power Doc
- [ ] `P6_18_visual_cheat_sheet.md`
- [ ] `P6_18_anki_kaplan_scaling_laws_2020.md` ← Anki
- [ ] `P6_18_anki.md` ← Anki (batch)
- [ ] `P6_18_breaking_point_qbank.md`
- [ ] `P6_18_code_skeleton.py`

**Sub-topic P6_19 — Chinchilla: Compute Optimal Training**
- [ ] `P6_19_chinchilla.md` ← Power Doc
- [ ] `P6_19_visual_cheat_sheet.md`
- [ ] `P6_19_anki_chinchilla.md` ← Anki
- [ ] `P6_19_anki.md` ← Anki (batch)
- [ ] `P6_19_breaking_point_qbank.md`
- [ ] `P6_19_code_skeleton.py`

**Sub-topic P6_20 — What Overtraining Means and Why Labs Do it**
- [ ] `P6_20_overtraining_why_labs_do_it.md` ← Power Doc
- [ ] `P6_20_visual_cheat_sheet.md`
- [ ] `P6_20_anki_overtraining_why_labs_do_it.md` ← Anki
- [ ] `P6_20_anki.md` ← Anki (batch)
- [ ] `P6_20_breaking_point_qbank.md`
- [ ] `P6_20_code_skeleton.py`

**Sub-topic P6_21 — Emergent Capabilities: Phase Transitions in Model Behaviour**
- [ ] `P6_21_emergent_capabilities.md` ← Power Doc
- [ ] `P6_21_visual_cheat_sheet.md`
- [ ] `P6_21_anki_emergent_capabilities.md` ← Anki
- [ ] `P6_21_anki.md` ← Anki (batch)
- [ ] `P6_21_breaking_point_qbank.md`
- [ ] `P6_21_code_skeleton.py`

**Topic 18 Problem Set**
- [ ] `Phase6_Topic18_ScalingLaws_ProblemSet.md`

**Phase 6 Wrap-up**
- [ ] `P6_connection_map.md`
- [ ] `anki_cards_topics_61_70.md`
- [ ] `anki_cards_topics_71_80.md`

---

### CAPSTONE (Topics 19–22)
`Capstone/`

These are integration problem sets. Do these after completing all 6 phases.

- [ ] `Capstone_Topic19_EndToEnd_RAGSystem_ProblemSet.md`
- [ ] `Capstone_Topic20_LLM_Security_Safety_ProblemSet.md`
- [ ] `Capstone_Topic21_Production_ML_Monitoring_ProblemSet.md`
- [ ] `Capstone_Topic22_FinSight_Integration_ProblemSet.md`

---

### EXTENDED TOPICS (Topics 23–42)
`Extended_Topics/`

Additional problem sets beyond the core curriculum. Work through these after Capstone.

- [ ] `Topic23_AdvancedPromptEngineering_ProblemSet.md`
- [ ] `Topic24_MultiAgentSystems_ProblemSet.md`
- [ ] `Topic25_TimeSeriesML_ProblemSet.md`
- [ ] `Topic26_ModelEvaluation_RedTeaming_ProblemSet.md`
- [ ] `Topic27_KnowledgeGraphs_StructuredReasoning_ProblemSet.md`
- [ ] `Topic28_AttentionMechanisms_TransformersDeepDive_ProblemSet.md`
- [ ] `Topic29_ProductionVectorSearch_ANN_ProblemSet.md`
- [ ] `Topic30_LLMInferenceOptimization_ProblemSet.md`
- [ ] `Topic31_MultimodalAI_DocumentUnderstanding_ProblemSet.md`
- [ ] `Topic32_AdvancedAgenticPatterns_ToolUse_ProblemSet.md`
- [ ] `Topic33_StructuredOutput_SchemaConstrainedGeneration_ProblemSet.md`
- [ ] `Topic34_LongContext_MemoryAugmentedLLMs_ProblemSet.md`
- [ ] `Topic35_SyntheticData_DataAugmentation_ProblemSet.md`
- [ ] `Topic36_FinancialNLP_DomainSpecificEmbeddings_ProblemSet.md`
- [ ] `Topic37_ProductionMLSystem_CostOptimization_ProblemSet.md`
- [ ] `Topic38_AI_Safety_Alignment_Production_ProblemSet.md`
- [ ] `Topic39_Graph_Neural_Networks_Relational_Learning_ProblemSet.md`
- [ ] `Topic40_Continual_Learning_Catastrophic_Forgetting_ProblemSet.md`
- [ ] `Topic41_Neural_Architecture_Search_AutoML_ProblemSet.md`
- [ ] `Topic42_Federated_Learning_Privacy_Preserving_ML_ProblemSet.md`

---

## 📈 Overall Progress

| Phase | Sub-topics | Files per sub-topic | Topic Problem Sets | Status |
|-------|-----------|---------------------|--------------------|--------|
| Phase 1 — Foundations | 19 | 4–5 each | 4 | ⬜ Not started |
| Phase 2 — RAG | 20 | 4 each | 3 | ⬜ Not started |
| Phase 3 — Eval & Production | 18 | 4 each | 3 | ⬜ Not started |
| Phase 4 — Deployment | 12 | 4 each | 2 | ⬜ Not started |
| Phase 5 — Fine-tuning | 14 | 4–5 each | 2 | ⬜ Not started |
| Phase 6 — Advanced | 21 + 2 overviews | 5–6 each | 4 | ⬜ Not started |
| Capstone | — | — | 4 | ⬜ Not started |
| Extended | — | — | 20 | ⬜ Not started |

**Total files tracked: ~430**
