import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set visual style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def run_analysis():
    # Load dataset
    data_path = 'data/netflix_titles.csv'
    if not os.path.exists(data_path):
        print(f"Error: Dataset not found at {data_path}")
        return

    df = pd.read_csv(data_path)
    print("Dataset loaded successfully.")

    # 1. Type Distribution (Movies vs TV Shows)
    plt.figure()
    sns.countplot(data=df, x='type', palette='viridis')
    plt.title('Distribution of Content Types on Netflix')
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.savefig('images/type_distribution.png')
    plt.close()

    # 2. Content Growth Over Years
    plt.figure()
    df_growth = df[df['release_year'] > 2000]
    sns.histplot(data=df_growth, x='release_year', hue='type', multiple='stack', bins=20)
    plt.title('Content Growth Over the Years (Post-2000)')
    plt.xlabel('Release Year')
    plt.ylabel('Count')
    plt.savefig('images/content_growth.png')
    plt.close()

    # 3. Top 10 Genres
    plt.figure()
    genres = df['listed_in'].str.split(', ').explode()
    top_genres = genres.value_counts().head(10)
    sns.barplot(x=top_genres.values, y=top_genres.index, palette='magma')
    plt.title('Top 10 Genres on Netflix')
    plt.xlabel('Count')
    plt.ylabel('Genre')
    plt.tight_layout()
    plt.savefig('images/top_genres.png')
    plt.close()

    # 4. Top 10 Countries
    plt.figure()
    countries = df['country'].dropna().str.split(', ').explode()
    top_countries = countries.value_counts().head(10)
    sns.barplot(x=top_countries.values, y=top_countries.index, palette='rocket')
    plt.title('Top 10 Content Producing Countries')
    plt.xlabel('Count')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.savefig('images/top_countries.png')
    plt.close()

    # 5. Rating Distribution
    plt.figure()
    sns.countplot(data=df, y='rating', order=df['rating'].value_counts().index, palette='cubehelix')
    plt.title('Distribution of Content Ratings')
    plt.xlabel('Count')
    plt.ylabel('Rating')
    plt.tight_layout()
    plt.savefig('images/rating_distribution.png')
    plt.close()

    print("Analysis complete. Visualizations saved in 'images/'.")

if __name__ == "__main__":
    # Ensure images directory exists
    if not os.path.exists('images'):
        os.makedirs('images')
    run_analysis()
