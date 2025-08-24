# TuneBuddy

A Python-based song recommendation system that suggests songs based on **artist** and **track name** using **TF-IDF vectorization** and **cosine similarity**. 

---

## Features

- Recommend songs based on artist and song name.
- Displays song posters from Spotify.
- Uses TF-IDF vectorization and cosine similarity for recommendations.
- Lightweight and easy to set up.

---

## **DEMO**:

![DEMO ONE](https://raw.githubusercontent.com/MuhammadHamza123c/TuneBuddy/main/d3.png)



## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/tunebuddy.git
cd tunebuddy
```

## **Create a virtual environment (optional but recommended)**:
```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

## **Install dependencies**:

```
pip install -r requirements.txt

```
## **Usage**:
Add your Spotify API credentials in a .env file:
```
client_id=YOUR_SPOTIFY_CLIENT_ID
client_secret=YOUR_SPOTIFY_CLIENT_SECRET
```
## **Run the main program**:

```
streamlit run main.py
```
Enter the song name to get recommendations.

## **Files**

```

main.py → Main script to run the recommendation system.

spotify_poster.py → Fetches song posters from Spotify.

.gitignore → Standard gitignore file.

requirements.txt → Python dependencies.
```
## **License**

This project is licensed under the MIT License.
Made with ❤️ by Hamza
