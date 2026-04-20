-- Query 1: Audio features of popular songs (popularity >= 80)
SELECT 
    ROUND(AVG(danceability)::numeric, 3) as avg_danceability,
    ROUND(AVG(energy)::numeric, 3) as avg_energy,
    ROUND(AVG(loudness)::numeric, 3) as avg_loudness,
    ROUND(AVG(acousticness)::numeric, 3) as avg_acousticness,
    ROUND(AVG(tempo)::numeric, 3) as avg_tempo
FROM spotify
WHERE popularity >= 80;

-- Query 2: Audio features of unpopular songs (popularity <= 20)
SELECT 
    ROUND(AVG(danceability)::numeric, 3) as avg_danceability,
    ROUND(AVG(energy)::numeric, 3) as avg_energy,
    ROUND(AVG(loudness)::numeric, 3) as avg_loudness,
    ROUND(AVG(acousticness)::numeric, 3) as avg_acousticness,
    ROUND(AVG(tempo)::numeric, 3) as avg_tempo
FROM spotify
WHERE popularity <= 20;

-- Query 3: Top 10 most popular songs with audio features
SELECT 
    track_name,
    artists,
    popularity,
    ROUND(danceability::numeric, 3) as danceability,
    ROUND(energy::numeric, 3) as energy,
    track_genre
FROM spotify
ORDER BY popularity DESC
LIMIT 10;

-- Query 4: Average audio features by genre ordered by popularity
SELECT 
    track_genre,
    ROUND(AVG(danceability)::numeric, 3) as avg_danceability,
    ROUND(AVG(energy)::numeric, 3) as avg_energy,
    ROUND(AVG(acousticness)::numeric, 3) as avg_acousticness,
    ROUND(AVG(tempo)::numeric, 3) as avg_tempo,
    ROUND(AVG(popularity)::numeric, 1) as avg_popularity
FROM spotify
GROUP BY track_genre
ORDER BY avg_popularity DESC
LIMIT 10;

-- Query 5: Explicit vs non-explicit song popularity
SELECT 
    explicit,
    COUNT(*) as total_songs,
    ROUND(AVG(popularity)::numeric, 2) as avg_popularity,
    ROUND(AVG(danceability)::numeric, 3) as avg_danceability
FROM spotify
GROUP BY explicit
ORDER BY avg_popularity DESC;