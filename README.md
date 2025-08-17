# Steam Releases Scraper 🚀

A **Python-based web scraper** that automatically collects **Popular Releases** and **Hot Releases** data from [SteamDB](https://steamdb.info/) and saves them as CSV files. Built with **Selenium** and **pandas**, this project helps you track Steam game trends effortlessly.

## Why This Project? 🎯

Steam is one of the largest digital game platforms. If you want to:
- Analyze the most played games  
- Track hot releases and their ratings  
- Monitor game pricing trends  

...this scraper provides all the data in a structured, ready-to-use format.

## Features ✨

### Popular Releases Scraper
- Game name  
- 24h peak players  
- Price  

### Hot Releases Scraper
- Game name  
- User rating  
- Price  

### Additional Features
- Saves scraped data into CSV files (`popular.csv` and `hot.csv`)
- Fully automated with **Selenium** + **ChromeDriver Manager**
- Clean, structured data output ready for analysis

## Installation ⚡

### Prerequisites
- Python 3.7 or higher
- Chrome browser installed

### Setup Steps

1. **Clone the repository:**
```bash
git clone https://github.com/Ameer-pasha/steam-releases-scraper.git
cd steam-releases-scraper
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the scraper:**
```bash
python main.py
```

## Requirements 📋

Create a `requirements.txt` file with the following dependencies:
```
selenium>=4.0.0
pandas>=1.3.0
webdriver-manager>=3.8.0
```

## Output 📊

After running the scraper, you will get two CSV files:

### popular.csv
```
Popular_Releases,24h_Peak,Price
Counter-Strike 2,1,234,567,Free
Dota 2,587,432,Free
PUBG: BATTLEGROUNDS,312,891,$29.99
Apex Legends,298,745,Free
```

### hot.csv
```
Hot_Releases,Rating,Price
Baldur's Gate 3,96.2%,$59.99
Cyberpunk 2077,78.4%,$29.99
Elden Ring,92.1%,$59.99
Hades II,94.8%,$29.99
```

## Project Structure 📁

```
steam-releases-scraper/
│
├── main.py              # Main scraper script
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── popular.csv         # Output file for popular releases
├── hot.csv            # Output file for hot releases
└── .gitignore         # Git ignore file
```

## Usage Examples 🔧

### Basic Usage
```python
# Run the complete scraper
python main.py
```

### Import as Module
```python
from main import SteamScraper

scraper = SteamScraper()
popular_data = scraper.scrape_popular_releases()
hot_data = scraper.scrape_hot_releases()
```

## Customization 🛠️

### Modifying Data Collection
- **Update XPaths**: Modify XPath selectors if SteamDB updates its layout
- **Add columns**: Extend scraping logic to include release date, developer, or tags
- **Data filtering**: Add filters for specific price ranges or ratings

### Visualization Integration
```python
import matplotlib.pyplot as plt
import pandas as pd

# Load and visualize data
df = pd.read_csv('popular.csv')
df.plot(x='Popular_Releases', y='24h_Peak', kind='bar')
plt.show()
```

## Troubleshooting 🔧

### Common Issues

**Chrome Driver Issues:**
- Ensure Chrome browser is installed
- ChromeDriver is automatically managed by webdriver-manager

**Scraping Failures:**
- Check if SteamDB website structure has changed
- Verify internet connection
- Update XPath selectors if needed

**Data Format Issues:**
- Ensure proper CSV encoding (UTF-8)
- Check for special characters in game names

## Legal Notice ⚖️

This scraper is for educational and research purposes only. Please respect SteamDB's terms of service and implement appropriate delays between requests to avoid overloading their servers.

## Contributing 🤝

Contributions, issues, and feature requests are welcome! Here's how you can contribute:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Areas for Contribution
- Error handling improvements
- Additional data fields
- Data visualization features
- Performance optimizations
- Unit tests

## Roadmap 🗺️

- [ ] Add support for multiple pages
- [ ] Implement data visualization dashboard
- [ ] Add scheduling capabilities (cron jobs)
- [ ] Create Docker container
- [ ] Add unit tests
- [ ] Implement logging system



## Acknowledgments 🙏

- [SteamDB](https://steamdb.info/) for providing the data
- [Selenium](https://selenium-python.readthedocs.io/) for web automation
- [Pandas](https://pandas.pydata.org/) for data manipulation

## Support 💬

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the troubleshooting section
- Review existing issues for solutions

---

**Happy scraping!** 🎮✨
