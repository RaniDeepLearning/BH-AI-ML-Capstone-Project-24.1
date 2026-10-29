"""Pipeline operator risk explorer.

Shows the logistic regression risk scores for the 2021-2024 test years.
The model was trained on 2010-2020, so these are out-of-sample results.
Run with:  streamlit run app.py
"""
import numpy as np
import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Pipeline Operator Risk", layout="wide")

print("path:", Path(__file__).parent)

DATA_FILE = Path(__file__).parent / "operator_risk_scores.csv"


@st.cache_data
def load_scores():
    return pd.read_csv(DATA_FILE, dtype={"OPERATOR_ID": str})


df = load_scores()

# ---------- Sidebar: choices ----------
st.sidebar.header("Choose what to look at")

years = sorted(df["REPORT_YEAR"].unique().tolist())
year_choice = st.sidebar.selectbox("Report year", ["All (2021-2024)"] + [str(y) for y in years])

if year_choice == "All (2021-2024)":
    view = df.copy()
else:
    view = df[df["REPORT_YEAR"] == int(year_choice)].copy()

mode = st.sidebar.radio("How to flag operator-years",
                        ["Top N highest risk", "Risk score at or above a cutoff"])

if mode == "Top N highest risk":
    max_n = len(view)
    n_flag = st.sidebar.slider("Number of operator-years to flag", 10, max_n, min(546, max_n), step=1)
    ranked = view.sort_values("RISK_SCORE", ascending=False)
    flagged = ranked.head(n_flag)
else:
    cutoff = st.sidebar.slider("Risk score cutoff", 0.0, 1.0, 0.485, step=0.001,
                               help="0.485 is the cutoff chosen in the notebook on the training years.")
    flagged = view[view["RISK_SCORE"] >= cutoff].sort_values("RISK_SCORE", ascending=False)

name_search = st.sidebar.text_input("Search operator name")

# ---------- Header ----------
st.title("Pipeline operator risk explorer")
st.caption("Predicts whether an operator will have a significant hazardous liquid pipeline incident "
           "in the following year. Scores are out-of-sample predictions for 2021-2024, from a model "
           "trained on 2010-2020. This is for learning and discussion, not for regulatory decisions.")

# ---------- Key numbers ----------
total_positive = int(view["ACTUAL_SIGNIFICANT_NEXT_YEAR"].sum())
caught = int(flagged["ACTUAL_SIGNIFICANT_NEXT_YEAR"].sum())
n_flagged = len(flagged)
precision = caught / n_flagged if n_flagged else 0.0
recall = caught / total_positive if total_positive else 0.0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Operator-years flagged", f"{n_flagged:,}", f"{n_flagged / len(view):.0%} of rows")
c2.metric("Significant incidents caught", f"{caught:,}", f"of {total_positive:,} that happened")
c3.metric("Recall", f"{recall:.1%}", help="Share of the real significant incidents that were flagged")
c4.metric("Precision", f"{precision:.1%}", help="Share of the flagged operator-years that had one")

# ---------- Trade-off curve ----------
st.subheader("Trade-off: how many operators to inspect")
st.write("Each point shows what happens if the top N operator-years are flagged. More flags catch more "
         "incidents, but each flag is less likely to be a real one.")

ordered = view.sort_values("RISK_SCORE", ascending=False).reset_index(drop=True)
k = np.arange(1, len(ordered) + 1)
cumulative_caught = ordered["ACTUAL_SIGNIFICANT_NEXT_YEAR"].cumsum().to_numpy()
curve = pd.DataFrame({"Recall": cumulative_caught / max(total_positive, 1),
                      "Precision": cumulative_caught / k}, index=k)
curve.index.name = "Operator-years flagged"
st.line_chart(curve.iloc[:: max(1, len(curve) // 300)])

# ---------- Flagged list ----------
st.subheader("Flagged operator-years")

shown = flagged[["OPERATOR_NAME", "REPORT_YEAR", "RISK_SCORE", "TOTAL_MILES",
                 "SIG_INCIDENTS_PRIOR_YEARS", "SIG_LAST3", "ACTUAL_SIGNIFICANT_NEXT_YEAR"]].rename(columns={
    "OPERATOR_NAME": "Operator",
    "REPORT_YEAR": "Year",
    "RISK_SCORE": "Risk score",
    "TOTAL_MILES": "Pipeline miles",
    "SIG_INCIDENTS_PRIOR_YEARS": "Significant incidents, earlier years",
    "SIG_LAST3": "Significant incidents, last 3 years",
    "ACTUAL_SIGNIFICANT_NEXT_YEAR": "Significant incident next year (actual)",
})

if name_search:
    shown = shown[shown["Operator"].str.contains(name_search, case=False, na=False)]

st.write(f"Showing {len(shown):,} operator-years.")
st.dataframe(shown, width="stretch", hide_index=True)
