# Spotify Music Analysis Dashboard

## Questions This Project Answers
1. What makes a song popular on Spotify — is it danceability, energy, or something else?
2. What do the most popular songs have in common?
3. How do audio features differ across genres?

## Live Dashboard
[View Interactive Dashboard](https://spotify-analysis14.streamlit.app/)

## Key Insights
1. Popularity has NO strong correlation with any single audio feature — marketing and artist fame matter more than sound
2. Pop-film and K-pop are most popular genres — mood-based genres beat traditional pop
3. Latin artists dominate top 10 — Bad Bunny, Bizarrap, Manuel Turizo reflect global latin music wave
4. Popular songs are short — sweet spot is 2-5 minutes, nothing above 8 minutes goes viral
5. Explicit songs are slightly more popular (36 vs 33 avg popularity)
6. Grunge = high energy, low danceability. Chill = low energy, high acousticness. Each genre has a distinct audio fingerprint
7. 18000+ songs have zero popularity — most Spotify content is never discovered

## Tech Stack
- Python, Pandas — data cleaning and EDA
- PostgreSQL — SQL analysis
- Plotly, Seaborn — visualizations
- Streamlit — interactive dashboard

## Project Structure

spotify-analysis/
├── data/
│   ├── raw/
│   └── cleaned/
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── queries.sql
├── dashboard/
│   └── app.py
└── README.md

## Dataset
Spotify Tracks Dataset via Kaggle — 114,000 tracks across 114 genres.
