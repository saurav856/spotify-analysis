import pandas as pd
import plotly.express as px
import streamlit as st
import os

st.set_page_config(page_title="Spotify Analysis Dashboard", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, 'data', 'cleaned', 'spotify_cleaned.csv'))

st.title("🎵 Spotify Music Analysis Dashboard")
st.markdown("Exploring what makes songs popular on Spotify")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tracks", f"{len(df):,}")
col2.metric("Total Artists", f"{df['artists'].nunique():,}")
col3.metric("Total Genres", f"{df['track_genre'].nunique():,}")
col4.metric("Avg Popularity", f"{df['popularity'].mean():.1f}")

st.subheader("Top 10 Genres by Popularity")

top_genres = df.groupby('track_genre')['popularity'].mean().sort_values(ascending=True).tail(10).reset_index()

fig1 = px.bar(top_genres, x='popularity', y='track_genre', orientation='h', title='Top 10 Genres by Average Popularity')
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Top 10 Artists by Popularity")

top_artists = df.groupby('artists')['popularity'].mean().sort_values(ascending=True).tail(10).reset_index()

fig2 = px.bar(top_artists, x='popularity', y='artists', orientation='h', title='Top 10 Artists by Average Popularity')
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Song Duration vs Popularity")

sample_df = df.sample(5000, random_state=42)

fig3 = px.scatter(sample_df, x='duration_sec', y='popularity', 
                  color='track_genre',
                  opacity=0.4,
                  title='Duration vs Popularity',
                  labels={'duration_sec': 'Duration (seconds)', 'popularity': 'Popularity'})
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Explore Audio Features by Genre")

selected_genre = st.selectbox("Select a Genre", sorted(df['track_genre'].unique()))

genre_df = df[df['track_genre'] == selected_genre]

features = ['danceability', 'energy', 'acousticness', 'valence', 'speechiness']
avg_features = genre_df[features].mean().reset_index()
avg_features.columns = ['feature', 'value']

fig4 = px.bar(avg_features, x='feature', y='value', title=f'Audio Features for {selected_genre}')
st.plotly_chart(fig4, use_container_width=True)