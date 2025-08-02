# تَهْلَل | Tahlal: National Investment Matching Platform 🇸🇦

**Tahlal** is a smart matching platform designed for the **عسير هاكثون** that connects property owners with potential investors using machine learning clustering.

The app supports two types of users:
- **👤 مستثمر (Investor)** — fills out a survey to be matched with suitable investment properties.
- **🏡 مالك (Owner)** — registers their property to find matching investors interested in similar opportunities.

---

## 🚀 Features

- ✨ Personalized investor/property recommendations based on KMeans clustering.
- 🧠 ML-trained models to suggest matches based on preferences and profiles.
- 📊 Visual dashboards for investors and owners.
- 🖼️ Beautiful Arabic UI with branded backgrounds and theme colors.
- 📂 Works fully offline — preprocessed sample data is bundled.

---

## 🏗️ Project Structure

```

tahlal\_final\_clustering\_mcq\_data/
├── app.py                         # Flask app entry point
├── clustering.py                 # ML prediction logic
├── models\_training.py            # Optional: re-train models using CSVs
├── requirements.txt              # Python dependencies
│
├── ML/                           # Saved models for clustering
│   ├── investor/
│   │   ├── model\_investor.pkl
│   │   ├── encoders\_investor.pkl
│   │   └── scaler\_investor.pkl
│   └── owner/
│       ├── model\_owner.pkl
│       ├── encoders\_owner.pkl
│       └── scaler\_owner.pkl
│
├── static/
│   ├── data/
│   │   ├── investors.json        # Simulated investor profiles with clusters
│   │   └── properties.json       # Simulated property listings with clusters
│   └── images/
│       ├── logo2.png             # Project logo
│       └── Hackathon Asseer.png  # Landing page background
│
├── templates/
│   ├── base.html                 # Base layout
│   ├── index.html                # Welcome page
│   ├── investor\_form.html        # Investor survey
│   ├── investor\_dashboard.html   # Property matches
│   ├── owner\_form.html           # Owner submission
│   └── owner\_dashboard.html      # Investor matches

````

---

##⚙️ Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone <your-repo-url>
   cd tahlal_final_clustering_mcq_data
````

2. **Create virtual environment**
   *(Optional but recommended)*

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   python app.py
   ```

5. **Visit in browser**
   [http://localhost:5000](http://localhost:5000)

---

##🧠 How It Works

### For Investors:

* Users fill out preferences like city, budget, risk level, duration, and experience.
* The app uses the trained **KMeans model** to assign a cluster.
* Matches are filtered from `properties.json` by cluster.
* Recommendations are displayed on `investor_dashboard.html`.

### For Owners:

* Owners submit property type, price, city, return rate, and a free description.
* The app predicts their cluster using another trained model.
* Matches are filtered from `investors.json` based on shared cluster.
* Suggestions are shown on `owner_dashboard.html`.

---

##🎯 Customization

* **Data**:

  * To use your own data, retrain via `models_training.py`.
  * Save new JSON outputs to `static/data/`.

* **Theme**:

  * Colors are defined in `base.html` and individual templates.
  * Background image: `/static/images/Hackathon Asseer.png`

* **Language**:

  * UI and form fields are fully in Arabic.

---

##📋 Dependencies

Listed in `requirements.txt`, key ones include:

* `Flask`
* `scikit-learn`
* `pandas`
* `numpy`
* `jinja2`

To regenerate:

```bash
pip freeze > requirements.txt
```

---

##💡 Example Users

* Sample `investors.json` and `properties.json` include 10 items each with:

  * 📍 City
  * 📐 Budget or Price
  * 💼 Type
  * 🎓 Experience
  * 🎯 Goals
  * ⚖️ Risk Appetite
  * 🕒 Duration
  * 🧠 Cluster

---

## 🧽 Cleanup

You may safely delete:

* `investor_centroids.npy`
* Any old `.csv` files (if not retraining)
* `__pycache__/` folders

---

##🏁 Future Improvements

* Add image uploads to listings
* Filter matches with weights instead of cluster-only logic
* Support search/sort in dashboards
* Add persistent DB storage (e.g., SQLite or Firebase)

---

##🏅 Built For


> **هاكثون عسير 2025**


