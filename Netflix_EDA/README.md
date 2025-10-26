# Netflix Exploratory Data Analysis (EDA) Project

## 📊 Project Overview

This is a comprehensive Python project for analyzing Netflix content data using pandas, matplotlib, and seaborn. The project performs thorough exploratory data analysis on Netflix's content library, providing insights into content distribution, trends, and patterns.

## 🎯 Project Goals

The Netflix EDA project aims to:
- **Clean and preprocess** Netflix content data
- **Analyze content distribution** between Movies and TV Shows
- **Identify release trends** over time
- **Discover popular genres** and content categories
- **Examine geographic distribution** of content
- **Analyze duration patterns** for different content types
- **Visualize rating distributions** across content
- **Generate comprehensive reports** and visualizations

## 🔧 Technical Features

### **Modular Design**
- Object-oriented `NetflixEDA` class for clean, maintainable code
- Separate modules for data loading, cleaning, analysis, and visualization
- Flexible data path handling for different dataset locations

### **Comprehensive Data Processing**
- **Data Loading**: Flexible CSV loading with error handling
- **Data Cleaning**: Missing value handling, duplicate removal, data type conversions
- **Data Validation**: Comprehensive data quality checks and reporting

### **Advanced Analytics**
- **Content Type Analysis**: Movies vs TV Shows distribution with percentages
- **Release Trend Analysis**: Year-over-year content release patterns
- **Genre Analysis**: Top 10 most popular content genres
- **Geographic Analysis**: Top 15 countries by content contribution
- **Duration Analysis**: Separate analysis for movies (minutes) and TV shows (seasons)
- **Rating Analysis**: Content rating distribution across all categories

### **Rich Visualizations**
- **Bar Charts**: Content types, top genres, top countries
- **Line Plots**: Release trends over time
- **Histograms**: Duration distributions for movies and TV shows
- **Pie Charts**: Rating distribution
- **Heatmaps**: Releases by year and month
- **High-Quality Output**: 300 DPI PNG files for presentations

## 📁 Project Structure

```
netflix-eda-project/
├── netflix_eda.py          # Main analysis script (500+ lines)
├── requirements.txt         # pip dependencies
├── environment.yml         # conda environment specification
├── README.md              # Project documentation
├── netflix_titles.csv     # Sample dataset (1,000 records)
└── Generated Visualizations:
    ├── netflix_analysis_overview.png
    ├── netflix_duration_ratings.png
    └── netflix_heatmap.png
```

## 🚀 Key Capabilities

### **Data Analysis Modules**
1. **Data Loading & Cleaning Module**
   - Flexible CSV loading with comprehensive error handling
   - Missing value analysis and intelligent handling
   - Duplicate detection and removal
   - Data type conversions and validation

2. **Exploratory Data Analysis Module**
   - Content type distribution analysis
   - Release trend analysis over years
   - Genre popularity analysis
   - Country contribution analysis
   - Duration pattern analysis
   - Rating distribution analysis

3. **Visualization Module**
   - Professional-quality charts and graphs
   - Multiple visualization types (bar, line, histogram, pie, heatmap)
   - Customizable styling and color schemes
   - High-resolution output for presentations

### **Output Features**
- **Console Reports**: Detailed statistical analysis and insights
- **Visualization Files**: 3 high-quality PNG files
- **Data Summary**: Comprehensive dataset overview and statistics
- **Missing Value Reports**: Before and after cleaning analysis

## 📊 Sample Analysis Results

Based on the sample dataset (1,000 records):

- **Content Distribution**: 52.5% Movies, 47.5% TV Shows
- **Top Genres**: Sci-Fi & Fantasy, Comedies, Action & Adventure
- **Top Countries**: South Korea, France, Japan, India
- **Movie Duration**: Average 117.3 minutes (range: 60-180 min)
- **TV Shows**: Average 4.5 seasons (range: 1-8 seasons)
- **Release Years**: 1990-2023 with peak activity in 2014-2015

## 🛠️ Technical Requirements

- **Python 3.7+**
- **Core Libraries**: pandas, numpy, matplotlib, seaborn
- **Optional**: jupyter for interactive analysis
- **Dependencies Management**: Both pip and conda support

## 📈 Use Cases

This project is perfect for:
- **Data Scientists** learning EDA techniques
- **Business Analysts** analyzing content trends
- **Students** studying data analysis with Python
- **Researchers** examining streaming content patterns
- **Content Creators** understanding market trends

## 🎓 Learning Outcomes

Users will gain experience with:
- **Data Cleaning** and preprocessing techniques
- **Statistical Analysis** and data exploration
- **Data Visualization** with matplotlib and seaborn
- **Object-Oriented Programming** in Python
- **Project Structure** and documentation
- **Dependency Management** with pip and conda

## 🔄 Extensibility

The modular design allows for easy extension:
- Add new analysis modules
- Customize visualizations
- Integrate with other datasets
- Add machine learning components
- Export to different formats

This project provides a solid foundation for Netflix data analysis and serves as an excellent template for similar EDA projects in the entertainment industry.