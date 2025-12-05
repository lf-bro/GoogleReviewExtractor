# Google Maps Review Scraper

_Automation script for extracting Google Maps reviews of any place using Selenium and Python._

## 📌 Overview

This project automates the process of scraping reviews from Google Maps. It scrolls through the reviews section, extracts relevant information, and stores it in a structured format (JSON).

You can use this for:

- Research and analytics
- Website testimonial
- Sentiment analysis
- Business insights
- Data collection projects

---

## ✨ Features

- Automatically loads and scrolls through all reviews
- Extracts reviewer name, profile image, rating and full review text
- Saves data in JSON format
- Easy-to-run Python script
- Modular and extendable code

---

## 🛠️ Installation

Follow these steps to set up the script on your machine.

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/google-maps-review-scraper.git
cd google-maps-review-scraper
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install selenium bs4 flask
```

### 4. Install WebDriver

- Download ChromeDriver matching your Chrome version
- Place it in your project folder or system PATH

---

## 🚀 Usage

### ▶️ Run the Scraper

To run the script that collects reviews:

```bash
python scrap.py
```

This will:

1. Launch Chrome via Selenium
2. Open Google Maps
3. Scroll through reviews
4. Extract all data
5. Save it to `data.json`

### ▶️ Run the Flask Server

If you want to serve the extracted data using a simple web interface:

```bash
python app.py
```

Then open the displayed URL in your browser (usually `http://127.0.0.1:5000`).

---

## 📂 Project Structure

```
├── scrap.py            # Main script for scraping Google Maps reviews
├── app.py              # Flask server to serve/display data
├── data.json           # Scraped output data
├── requirements.txt
├── README.md
├── templates
|  └── index.html
└── images/             # (Optional) folder for screenshots
```

---

## 🖼️ Screenshots / Preview

> _Place your screenshots here_

```
[Screenshots](Screenshots/preview.png)
![Preview](images/preview.png)

```

---

## 🤝 Contributing

Feel free to open issues or make PRs to improve the scraper.

---

## 📄 License

MIT License

---

## ⭐ Support

If you like this project, consider giving the repo a ⭐

```

```
