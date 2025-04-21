# Mega-Hatsu Solar Property Scraper

A Scrapy spider for collecting detailed information about solar power plants listed for sale on [mega-hatsu.com](https://mega-hatsu.com).

## Features

- Crawls paginated listing pages and extracts individual property URLs
- Collects comprehensive property details including:
  - Pricing and financial metrics
  - Technical specifications
  - Location information
  - Warranty and guarantee details
  - Additional features and costs
- Stores data in PostgreSQL with status tracking (new/still available/deleted)
- Handles data cleaning and normalization

## Project Structure
```bash
├── mega_hatsu/
│ ├── init.py
│ ├── items.py # Defines data structure for scraped items
│ ├── pipelines.py # PostgreSQL storage pipeline
│ ├── settings.py # Project settings
│ └── spiders/
│ ├── init.py
│ └── infos.py # Main spider implementation
├── scrapy.cfg
├── requirements.txt
└── README.md
```


## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mega-hatsu-scraper.git
cd mega-hatsu-scraper
```

2.Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Add you database credentials into settings (this solution is only for local use) : 
```bash
POSTGRES_USER=your_username
POSTGRES_PASS=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=mega_hatsu
```
2. Configure settings in mega_hatsu/settings.py as needed: 
- Adjust download delays
- Enable/disable pipelines
- Set user agent

