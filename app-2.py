import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Smart Analytics Tool",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Smart Analytics Tool")

st.write("Upload any CSV file and get instant analysis.")

# --------------------------------
# FILE UPLOAD
# --------------------------------

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Uploaded Successfully ✅")

    # ----------------------------
    # DATASET PREVIEW
    # ----------------------------

    st.header("📋 Dataset Preview")

    st.dataframe(df.head())

    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    # ----------------------------
    # MISSING VALUES
    # ----------------------------

    st.header("🧹 Missing Value Analysis")

    missing = df.isnull().sum()

    st.dataframe(missing)

    # ----------------------------
    # STATISTICAL SUMMARY
    # ----------------------------

    st.header("📈 Statistical Summary")

    st.dataframe(df.describe())

    # ----------------------------
    # NUMERIC COLUMNS
    # ----------------------------

    numeric_cols = df.select_dtypes(
        include=["number"]
    ).columns

    if len(numeric_cols) > 0:

        st.header("📊 Dynamic Visualization 1")

        col = st.selectbox(
            "Select Column",
            numeric_cols
        )

        fig1 = px.histogram(
            df,
            x=col,
            title=f"Distribution of {col}"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

        # ------------------------

        st.header("📊 Dynamic Visualization 2")

        col2 = st.selectbox(
            "Select Column for Box Plot",
            numeric_cols,
            key="box"
        )

        fig2 = px.box(
            df,
            y=col2,
            title=f"Box Plot of {col2}"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        # ------------------------

        st.header("📊 Dynamic Visualization 3")

        x_col = st.selectbox(
            "X Axis",
            numeric_cols,
            key="x"
        )

        y_col = st.selectbox(
            "Y Axis",
            numeric_cols,
            key="y"
        )

        fig3 = px.scatter(
            df,
            x=x_col,
            y=y_col,
            title=f"{x_col} vs {y_col}"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    else:
        st.warning(
            "No numeric columns found in dataset."
        )

else:
    st.info("Please upload a CSV file.")