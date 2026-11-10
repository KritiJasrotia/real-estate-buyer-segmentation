
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Real Estate Buyer Intelligence",
    page_icon="🏡",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("buyer_segmentation_results.csv")

df = load_data()

# Dashboard title
st.title("🏡 Real Estate Buyer Segmentation")
st.caption("Machine Learning Based Buyer & Investment Intelligence")

# Sidebar filters
st.sidebar.title("Dashboard Filters")

def filter_options(column):
    return sorted(df[column].dropna().unique().tolist())

country = st.sidebar.multiselect(
    "Select Country", filter_options("country")
)

region = st.sidebar.multiselect(
    "Select Region", filter_options("region")
)

purpose = st.sidebar.multiselect(
    "Acquisition Purpose", filter_options("acquisition_purpose")
)

buyer_type = st.sidebar.multiselect(
    "Buyer Type", filter_options("client_type")
)

cluster = st.sidebar.multiselect(
    "Buyer Segment", filter_options("KMeans_Cluster")
)

# Apply filters
filtered = df.copy()

if country:
    filtered = filtered[filtered["country"].isin(country)]

if region:
    filtered = filtered[filtered["region"].isin(region)]

if purpose:
    filtered = filtered[
        filtered["acquisition_purpose"].isin(purpose)
    ]

if buyer_type:
    filtered = filtered[
        filtered["client_type"].isin(buyer_type)
    ]

if cluster:
    filtered = filtered[
        filtered["KMeans_Cluster"].astype(str).isin(cluster)
    ]

st.sidebar.caption(f"Showing {len(filtered):,} buyers")

if filtered.empty:
    st.warning("No buyers match the selected filters.")
    st.stop()

# KPI cards
st.subheader("Buyer Segmentation Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Buyers", f"{len(filtered):,}")

c2.metric(
    "Investment Buyers",
    f"{(filtered['acquisition_purpose'] == 'Investment').sum():,}"
)

c3.metric(
    "Average Age",
    f"{filtered['age'].mean():.1f}"
)

c4.metric(
    "Buyer Segments",
    filtered["KMeans_Cluster"].nunique()
)

st.divider()

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "💰 Investor Behaviour",
    "🌍 Geographic Analysis",
    "👥 Segment Insights"
])

# TAB 1: OVERVIEW
with tab1:
    left, right = st.columns(2)

    with left:
        cluster_counts = (
            filtered["KMeans_Cluster"]
            .astype(str)
            .value_counts()
            .rename_axis("Cluster")
            .reset_index(name="Buyers")
        )

        fig = px.pie(
            cluster_counts,
            names="Cluster",
            values="Buyers",
            hole=0.45,
            title="Buyer Distribution by Cluster"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:
        purpose_counts = (
            filtered["acquisition_purpose"]
            .value_counts()
            .rename_axis("Purpose")
            .reset_index(name="Buyers")
        )

        fig = px.bar(
            purpose_counts,
            x="Purpose",
            y="Buyers",
            color="Purpose",
            title="Home vs Investment Buyers",
            text="Buyers"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Buyer Age Distribution")

    fig = px.histogram(
        filtered,
        x="age",
        color="client_type",
        nbins=20,
        title="Age Distribution by Buyer Type"
    )

    st.plotly_chart(fig, use_container_width=True)


# TAB 2: INVESTOR BEHAVIOUR
with tab2:
    investment = filtered[
        filtered["acquisition_purpose"] == "Investment"
    ]

    st.metric("Total Investment Buyers", len(investment))

    if not investment.empty:
        fig = px.histogram(
            investment,
            x="KMeans_Cluster",
            color="client_type",
            title="Investment Buyers Across Clusters",
            barmode="group"
        )

        st.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(
            investment,
            x="property_count",
            y="average_sale_price",
            color="KMeans_Cluster",
            hover_data=[
                "client_type",
                "country",
                "region"
            ],
            title="Property Activity vs Average Sale Price",
            labels={
                "property_count": "Number of Linked Properties",
                "average_sale_price": "Average Sale Price"
            }
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No investment buyers match these filters.")


# TAB 3: GEOGRAPHIC ANALYSIS
with tab3:
    left, right = st.columns(2)

    with left:
        country_counts = (
            filtered["country"]
            .value_counts()
            .head(10)
            .rename_axis("Country")
            .reset_index(name="Buyers")
        )

        fig = px.bar(
            country_counts,
            x="Country",
            y="Buyers",
            title="Top 10 Countries by Buyers",
            color="Buyers"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:
        region_counts = (
            filtered["region"]
            .value_counts()
            .head(10)
            .rename_axis("Region")
            .reset_index(name="Buyers")
        )

        fig = px.bar(
            region_counts,
            x="Buyers",
            y="Region",
            orientation="h",
            title="Top 10 Regions by Buyers",
            color="Buyers"
        )

        st.plotly_chart(fig, use_container_width=True)


# TAB 4: SEGMENT INSIGHTS
with tab4:
    st.subheader("Cluster-wise Buyer Profile")

    profile = filtered.groupby("KMeans_Cluster").agg(
        Total_Buyers=("client_id", "count"),
        Average_Age=("age", "mean"),
        Average_Satisfaction=("satisfaction_score", "mean"),
        Average_Properties=("property_count", "mean"),
        Average_Sale_Price=("average_sale_price", "mean")
    ).round(2).reset_index()

    st.dataframe(profile, use_container_width=True)

    fig = px.bar(
        profile,
        x="KMeans_Cluster",
        y="Total_Buyers",
        color="KMeans_Cluster",
        title="Number of Buyers in Each Cluster",
        text="Total_Buyers"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Buyer Records")

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )

# Download filtered data
st.divider()

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Buyer Data",
    data=csv,
    file_name="filtered_buyer_data.csv",
    mime="text/csv"
)

st.success("Interactive dashboard loaded successfully!")
