#!/usr/bin/env python3
"""
Netflix Exploratory Data Analysis (EDA)
=======================================

This script performs comprehensive analysis of Netflix content data including:
- Data cleaning and preprocessing
- Content type analysis (Movies vs TV Shows)
- Release trends over time
- Genre popularity analysis
- Country contribution analysis
- Duration analysis for movies and TV shows
- Content rating distribution
- Comprehensive visualizations

Author: Netflix EDA Project
Date: 2024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class NetflixEDA:
    """Main class for Netflix Exploratory Data Analysis"""
    
    def __init__(self, data_path):
        """
        Initialize the Netflix EDA class
        
        Args:
            data_path (str): Path to the Netflix dataset CSV file
        """
        self.data_path = data_path
        self.df = None
        self.cleaned_df = None
        
    def load_data(self):
        """Load the Netflix dataset"""
        try:
            print("Loading Netflix dataset...")
            self.df = pd.read_csv(self.data_path)
            print(f"Dataset loaded successfully! Shape: {self.df.shape}")
            return True
        except FileNotFoundError:
            print(f"Error: Could not find file at {self.data_path}")
            print("Please ensure the Netflix dataset CSV file exists at the specified path.")
            return False
        except Exception as e:
            print(f"Error loading dataset: {e}")
            return False
    
    def explore_data(self):
        """Display basic information about the dataset"""
        if self.df is None:
            print("No data loaded. Please load data first.")
            return
            
        print("\n" + "="*50)
        print("DATASET OVERVIEW")
        print("="*50)
        print(f"Dataset shape: {self.df.shape}")
        print(f"Columns: {list(self.df.columns)}")
        
        print("\nFirst 5 rows:")
        print(self.df.head())
        
        print("\nDataset Info:")
        print(self.df.info())
        
        print("\nMissing values:")
        missing_values = self.df.isnull().sum()
        print(missing_values[missing_values > 0])
        
        print("\nBasic statistics:")
        print(self.df.describe())
    
    def clean_data(self):
        """Clean and preprocess the dataset"""
        if self.df is None:
            print("No data loaded. Please load data first.")
            return
            
        print("\n" + "="*50)
        print("DATA CLEANING")
        print("="*50)
        
        # Create a copy for cleaning
        self.cleaned_df = self.df.copy()
        
        # Handle missing values
        print("Handling missing values...")
        
        # Fill missing dates with forward fill
        if 'date_added' in self.cleaned_df.columns:
            self.cleaned_df['date_added'] = pd.to_datetime(self.cleaned_df['date_added'], errors='coerce')
            self.cleaned_df['date_added'] = self.cleaned_df['date_added'].fillna(method='ffill')
        
        # Fill missing countries with 'Unknown'
        if 'country' in self.cleaned_df.columns:
            self.cleaned_df['country'] = self.cleaned_df['country'].fillna('Unknown')
        
        # Fill missing ratings with 'Unknown'
        if 'rating' in self.cleaned_df.columns:
            self.cleaned_df['rating'] = self.cleaned_df['rating'].fillna('Unknown')
        
        # Fill missing durations with median/mode
        if 'duration' in self.cleaned_df.columns:
            self.cleaned_df['duration'] = self.cleaned_df['duration'].fillna('Unknown')
        
        # Remove duplicates based on show_id
        initial_count = len(self.cleaned_df)
        self.cleaned_df = self.cleaned_df.drop_duplicates(subset=['show_id'], keep='first')
        final_count = len(self.cleaned_df)
        print(f"Removed {initial_count - final_count} duplicate entries")
        
        # Extract year from date_added for analysis
        if 'date_added' in self.cleaned_df.columns:
            self.cleaned_df['year_added'] = self.cleaned_df['date_added'].dt.year
        
        print(f"Data cleaning completed! Final shape: {self.cleaned_df.shape}")
        
        # Display missing values after cleaning
        print("\nMissing values after cleaning:")
        missing_after = self.cleaned_df.isnull().sum()
        print(missing_after[missing_after > 0])
    
    def analyze_content_types(self):
        """Analyze distribution of Movies vs TV Shows"""
        if self.cleaned_df is None:
            print("No cleaned data available. Please clean data first.")
            return
            
        print("\n" + "="*50)
        print("CONTENT TYPE ANALYSIS")
        print("="*50)
        
        content_counts = self.cleaned_df['type'].value_counts()
        content_percentages = self.cleaned_df['type'].value_counts(normalize=True) * 100
        
        print("Content Type Distribution:")
        for content_type, count in content_counts.items():
            percentage = content_percentages[content_type]
            print(f"{content_type}: {count:,} ({percentage:.1f}%)")
        
        return content_counts
    
    def analyze_release_trends(self):
        """Analyze release trends over years"""
        if self.cleaned_df is None:
            print("No cleaned data available. Please clean data first.")
            return
            
        print("\n" + "="*50)
        print("RELEASE TREND ANALYSIS")
        print("="*50)
        
        # Analyze by release year
        release_trends = self.cleaned_df['release_year'].value_counts().sort_index()
        
        print("Top 10 years by number of releases:")
        top_years = release_trends.tail(10)
        for year, count in top_years.items():
            print(f"{year}: {count:,} releases")
        
        print(f"\nRelease year range: {self.cleaned_df['release_year'].min()} - {self.cleaned_df['release_year'].max()}")
        
        return release_trends
    
    def analyze_genres(self):
        """Analyze most popular genres"""
        if self.cleaned_df is None:
            print("No cleaned data available. Please clean data first.")
            return
            
        print("\n" + "="*50)
        print("GENRE ANALYSIS")
        print("="*50)
        
        # Split genres and count them
        all_genres = []
        for genres in self.cleaned_df['listed_in'].dropna():
            genre_list = [genre.strip() for genre in str(genres).split(',')]
            all_genres.extend(genre_list)
        
        genre_counts = Counter(all_genres)
        top_genres = genre_counts.most_common(10)
        
        print("Top 10 Most Popular Genres:")
        for i, (genre, count) in enumerate(top_genres, 1):
            print(f"{i:2d}. {genre}: {count:,}")
        
        return dict(top_genres)
    
    def analyze_countries(self):
        """Analyze countries contributing most content"""
        if self.cleaned_df is None:
            print("No cleaned data available. Please clean data first.")
            return
            
        print("\n" + "="*50)
        print("COUNTRY ANALYSIS")
        print("="*50)
        
        # Split countries and count them
        all_countries = []
        for countries in self.cleaned_df['country'].dropna():
            country_list = [country.strip() for country in str(countries).split(',')]
            all_countries.extend(country_list)
        
        country_counts = Counter(all_countries)
        top_countries = country_counts.most_common(15)
        
        print("Top 15 Countries by Content Contribution:")
        for i, (country, count) in enumerate(top_countries, 1):
            print(f"{i:2d}. {country}: {count:,}")
        
        return dict(top_countries)
    
    def analyze_duration(self):
        """Analyze duration patterns for movies and TV shows"""
        if self.cleaned_df is None:
            print("No cleaned data available. Please clean data first.")
            return
            
        print("\n" + "="*50)
        print("DURATION ANALYSIS")
        print("="*50)
        
        # Separate movies and TV shows
        movies = self.cleaned_df[self.cleaned_df['type'] == 'Movie']
        tv_shows = self.cleaned_df[self.cleaned_df['type'] == 'TV Show']
        
        print("MOVIE DURATION ANALYSIS:")
        movie_durations = []
        for duration in movies['duration'].dropna():
            if 'min' in str(duration):
                try:
                    duration_min = int(str(duration).split()[0])
                    movie_durations.append(duration_min)
                except:
                    continue
        
        if movie_durations:
            movie_durations = np.array(movie_durations)
            print(f"Average movie duration: {np.mean(movie_durations):.1f} minutes")
            print(f"Median movie duration: {np.median(movie_durations):.1f} minutes")
            print(f"Duration range: {np.min(movie_durations)} - {np.max(movie_durations)} minutes")
        
        print("\nTV SHOW DURATION ANALYSIS:")
        tv_durations = []
        for duration in tv_shows['duration'].dropna():
            if 'Season' in str(duration):
                try:
                    seasons = int(str(duration).split()[0])
                    tv_durations.append(seasons)
                except:
                    continue
        
        if tv_durations:
            tv_durations = np.array(tv_durations)
            print(f"Average TV show seasons: {np.mean(tv_durations):.1f}")
            print(f"Median TV show seasons: {np.median(tv_durations):.1f}")
            print(f"Seasons range: {np.min(tv_durations)} - {np.max(tv_durations)}")
        
        return movie_durations, tv_durations
    
    def analyze_ratings(self):
        """Analyze content rating distribution"""
        if self.cleaned_df is None:
            print("No cleaned data available. Please clean data first.")
            return
            
        print("\n" + "="*50)
        print("RATING ANALYSIS")
        print("="*50)
        
        rating_counts = self.cleaned_df['rating'].value_counts()
        rating_percentages = self.cleaned_df['rating'].value_counts(normalize=True) * 100
        
        print("Content Rating Distribution:")
        for rating, count in rating_counts.items():
            percentage = rating_percentages[rating]
            print(f"{rating}: {count:,} ({percentage:.1f}%)")
        
        return rating_counts
    
    def create_visualizations(self):
        """Create comprehensive visualizations"""
        if self.cleaned_df is None:
            print("No cleaned data available. Please clean data first.")
            return
            
        print("\n" + "="*50)
        print("CREATING VISUALIZATIONS")
        print("="*50)
        
        # Set up the plotting style
        plt.rcParams['figure.figsize'] = (12, 8)
        plt.rcParams['font.size'] = 10
        
        # 1. Content Type Distribution
        plt.figure(figsize=(10, 6))
        content_counts = self.cleaned_df['type'].value_counts()
        plt.subplot(2, 2, 1)
        content_counts.plot(kind='bar', color=['#e74c3c', '#3498db'])
        plt.title('Movies vs TV Shows Distribution', fontsize=14, fontweight='bold')
        plt.xlabel('Content Type')
        plt.ylabel('Count')
        plt.xticks(rotation=0)
        
        # Add value labels on bars
        for i, v in enumerate(content_counts.values):
            plt.text(i, v + 1000, f'{v:,}', ha='center', va='bottom', fontweight='bold')
        
        # 2. Release Trends Over Years
        plt.subplot(2, 2, 2)
        release_trends = self.cleaned_df['release_year'].value_counts().sort_index()
        recent_years = release_trends.tail(20)  # Last 20 years
        plt.plot(recent_years.index, recent_years.values, marker='o', linewidth=2, markersize=6)
        plt.title('Content Releases Over Years (Last 20 Years)', fontsize=14, fontweight='bold')
        plt.xlabel('Year')
        plt.ylabel('Number of Releases')
        plt.grid(True, alpha=0.3)
        
        # 3. Top Genres
        plt.subplot(2, 2, 3)
        all_genres = []
        for genres in self.cleaned_df['listed_in'].dropna():
            genre_list = [genre.strip() for genre in str(genres).split(',')]
            all_genres.extend(genre_list)
        
        genre_counts = Counter(all_genres)
        top_genres = dict(genre_counts.most_common(10))
        
        genres = list(top_genres.keys())
        counts = list(top_genres.values())
        
        plt.barh(range(len(genres)), counts, color='lightcoral')
        plt.yticks(range(len(genres)), genres)
        plt.title('Top 10 Genres', fontsize=14, fontweight='bold')
        plt.xlabel('Count')
        
        # 4. Top Countries
        plt.subplot(2, 2, 4)
        all_countries = []
        for countries in self.cleaned_df['country'].dropna():
            country_list = [country.strip() for country in str(countries).split(',')]
            all_countries.extend(country_list)
        
        country_counts = Counter(all_countries)
        top_countries = dict(country_counts.most_common(10))
        
        countries = list(top_countries.keys())
        counts = list(top_countries.values())
        
        plt.barh(range(len(countries)), counts, color='lightblue')
        plt.yticks(range(len(countries)), countries)
        plt.title('Top 10 Countries', fontsize=14, fontweight='bold')
        plt.xlabel('Count')
        
        plt.tight_layout()
        plt.savefig('netflix_analysis_overview.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # 5. Duration Analysis
        plt.figure(figsize=(15, 5))
        
        # Movie Duration Distribution
        plt.subplot(1, 3, 1)
        movies = self.cleaned_df[self.cleaned_df['type'] == 'Movie']
        movie_durations = []
        for duration in movies['duration'].dropna():
            if 'min' in str(duration):
                try:
                    duration_min = int(str(duration).split()[0])
                    movie_durations.append(duration_min)
                except:
                    continue
        
        if movie_durations:
            plt.hist(movie_durations, bins=30, color='skyblue', alpha=0.7, edgecolor='black')
            plt.title('Movie Duration Distribution', fontsize=14, fontweight='bold')
            plt.xlabel('Duration (minutes)')
            plt.ylabel('Frequency')
            plt.axvline(np.mean(movie_durations), color='red', linestyle='--', 
                       label=f'Mean: {np.mean(movie_durations):.1f} min')
            plt.legend()
        
        # TV Show Seasons Distribution
        plt.subplot(1, 3, 2)
        tv_shows = self.cleaned_df[self.cleaned_df['type'] == 'TV Show']
        tv_durations = []
        for duration in tv_shows['duration'].dropna():
            if 'Season' in str(duration):
                try:
                    seasons = int(str(duration).split()[0])
                    tv_durations.append(seasons)
                except:
                    continue
        
        if tv_durations:
            plt.hist(tv_durations, bins=20, color='lightgreen', alpha=0.7, edgecolor='black')
            plt.title('TV Show Seasons Distribution', fontsize=14, fontweight='bold')
            plt.xlabel('Number of Seasons')
            plt.ylabel('Frequency')
            plt.axvline(np.mean(tv_durations), color='red', linestyle='--', 
                       label=f'Mean: {np.mean(tv_durations):.1f} seasons')
            plt.legend()
        
        # Rating Distribution
        plt.subplot(1, 3, 3)
        rating_counts = self.cleaned_df['rating'].value_counts()
        plt.pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
        plt.title('Content Rating Distribution', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('netflix_duration_ratings.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # 6. Heatmap: Releases by Year and Month
        plt.figure(figsize=(12, 8))
        
        # Extract month from date_added
        if 'date_added' in self.cleaned_df.columns:
            self.cleaned_df['month_added'] = self.cleaned_df['date_added'].dt.month
            self.cleaned_df['year_added'] = self.cleaned_df['date_added'].dt.year
            
            # Create pivot table for heatmap
            heatmap_data = self.cleaned_df.groupby(['year_added', 'month_added']).size().unstack(fill_value=0)
            
            # Only show recent years for better visualization
            recent_years = heatmap_data.tail(10)
            
            plt.subplot(2, 1, 1)
            sns.heatmap(recent_years, annot=True, fmt='d', cmap='YlOrRd', cbar_kws={'label': 'Number of Releases'})
            plt.title('Netflix Releases Heatmap (Year vs Month)', fontsize=14, fontweight='bold')
            plt.xlabel('Month')
            plt.ylabel('Year')
        
        plt.tight_layout()
        plt.savefig('netflix_heatmap.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("All visualizations saved as PNG files!")
    
    def run_complete_analysis(self):
        """Run the complete Netflix EDA analysis"""
        print("NETFLIX EXPLORATORY DATA ANALYSIS")
        print("="*50)
        
        # Load and explore data
        if not self.load_data():
            return
        
        self.explore_data()
        self.clean_data()
        
        # Perform all analyses
        self.analyze_content_types()
        self.analyze_release_trends()
        self.analyze_genres()
        self.analyze_countries()
        self.analyze_duration()
        self.analyze_ratings()
        
        # Create visualizations
        self.create_visualizations()
        
        print("\n" + "="*50)
        print("ANALYSIS COMPLETED SUCCESSFULLY!")
        print("="*50)
        print("Generated files:")
        print("- netflix_analysis_overview.png")
        print("- netflix_duration_ratings.png")
        print("- netflix_heatmap.png")


def main():
    """Main function to run the Netflix EDA"""
    # You can change this path to your Netflix dataset location
    data_path = "netflix_titles.csv"
    
    # Create Netflix EDA instance
    netflix_eda = NetflixEDA(data_path)
    
    # Run complete analysis
    netflix_eda.run_complete_analysis()


if __name__ == "__main__":
    main()
