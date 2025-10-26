# Netflix Exploratory Data Analysis (EDA)

A comprehensive Python project for analyzing Netflix content data using pandas, matplotlib, and seaborn.

## Project Overview

This project performs exploratory data analysis on Netflix content data, including:

- **Data Cleaning**: Handle missing values, convert data types, remove duplicates
- **Content Analysis**: Movies vs TV Shows distribution
- **Trend Analysis**: Release patterns over years and months
- **Genre Analysis**: Most popular content genres
- **Geographic Analysis**: Countries contributing most content
- **Duration Analysis**: Movie lengths and TV show seasons
- **Rating Analysis**: Content rating distribution
- **Visualizations**: Comprehensive charts and graphs

## Features

- Modular, object-oriented design with `NetflixEDA` class
- Flexible data loading (works with any Netflix dataset format)
- Comprehensive data cleaning and preprocessing
- Statistical analysis and insights
- Beautiful visualizations using matplotlib and seaborn
- Export charts as high-quality PNG files

## Installation

### Option 1: Using pip

1. Clone or download this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Option 2: Using conda

1. Clone or download this repository
2. Create conda environment:
```bash
conda env create -f environment.yml
conda activate netflix-eda
```

## Usage

### Basic Usage

1. Place your Netflix dataset CSV file in the project directory (rename it to `netflix_titles.csv`)
2. Run the analysis:
```bash
python netflix_eda.py
```

### Custom Dataset Path

To use a different dataset path, modify the `data_path` variable in the `main()` function:

```python
def main():
    data_path = "path/to/your/netflix_dataset.csv"  # Change this path
    netflix_eda = NetflixEDA(data_path)
    netflix_eda.run_complete_analysis()
```

### Programmatic Usage

```python
from netflix_eda import NetflixEDA

# Create instance
eda = NetflixEDA("netflix_titles.csv")

# Run complete analysis
eda.run_complete_analysis()

# Or run individual components
eda.load_data()
eda.clean_data()
eda.analyze_content_types()
eda.create_visualizations()
```

## Expected Dataset Format

The script expects a CSV file with the following columns:
- `show_id`: Unique identifier
- `type`: Content type (Movie/TV Show)
- `title`: Content title
- `director`: Director name(s)
- `cast`: Cast members
- `country`: Country of origin
- `date_added`: Date added to Netflix
- `release_year`: Year of release
- `rating`: Content rating
- `duration`: Duration (minutes for movies, seasons for TV shows)
- `listed_in`: Genres/categories

## Output Files

The analysis generates the following visualization files:

1. **`netflix_analysis_overview.png`**: Overview dashboard with content types, release trends, top genres, and top countries
2. **`netflix_duration_ratings.png`**: Duration distributions and rating analysis
3. **`netflix_heatmap.png`**: Heatmap showing releases by year and month

## Sample Output

The script provides detailed console output including:

- Dataset overview and statistics
- Missing value analysis
- Content type distribution
- Release trend analysis
- Top genres and countries
- Duration statistics
- Rating distribution
- Visualization generation status

## Requirements

- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- jupyter (optional, for interactive use)

## Dataset Sources

You can obtain Netflix datasets from:
- [Kaggle Netflix Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data)

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.

## License

This project is open source and available under the MIT License.
