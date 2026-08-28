# Fake-News-Detector--machine-learning


```markdown
# 📰 Fake News Detector

An end-to-end Machine Learning web application designed to classify news articles and headlines as authentic (**TRUE**) or fabricated (**FALSE**). Built with Python, Scikit-Learn, Flask, and vanilla HTML/CSS/JavaScript.

---

## 🚀 Live Demo

- **Web App**: `https://your-app-name.onrender.com` *(Update with your Render URL)*

---

## 🛠️ Tech Stack

- **Machine Learning**: Scikit-Learn (`TfidfVectorizer`, `PassiveAggressiveClassifier`), Pandas
- **Backend**: Python, Flask, Gunicorn
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)
- **Deployment**: Render / GitHub

---

## 📁 Project Structure

```text
fake-news-detector/
│
├── static/
│   ├── style.css          # UI styles & responsive design
│   └── script.js          # Asynchronous API handler (Fetch)
├── templates/
│   └── index.html         # Main dashboard interface
├── app.py                 # Flask server & inference endpoint
├── train_model.py         # Model training script
├── requirements.txt       # Dependencies
├── .gitignore             # Ignored files & binaries
└── README.md              # Project documentation

```

---

## ⚙️ How It Works

1. **Text Preprocessing & Feature Extraction**: Incoming text is converted into n-gram features using **TF-IDF (Term Frequency-Inverse Document Frequency)** to evaluate word importance.
2. **Classification**: A **Passive-Aggressive Classifier** analyzes lexical patterns and assigns a binary classification label.
3. **API & Interface**: The Flask backend exposes a `/predict` endpoint that serves predictions dynamically to the frontend without reloading the page.

---

## 💻 Local Setup & Installation

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/fake-news-detector.git](https://github.com/your-username/fake-news-detector.git)
cd fake-news-detector

```

### 2. Create and activate a virtual environment

```bash
# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Train the ML Model (Optional)

The application automatically trains a baseline model if no serialized weights exist, or you can train it manually:

```bash
python train_model.py

```

### 5. Run the application

```bash
python app.py

```

Open your browser and navigate to `http://127.0.0.1:5000`.

---

## 🧪 Testing with Sample Prompts

| Expected Result | Sample Text Input |
| --- | --- |
| **TRUE (Real)** | *"Scientists discover new Earth-like planet with water atmosphere."* |
| **TRUE (Real)** | *"Central bank announces a 0.25 percent cut in baseline interest rates."* |
| **FALSE (Fake)** | *"Secret government chip found inside all common grocery store bananas."* |
| **FALSE (Fake)** | *"Drinking boiled lemon water cures every known disease instantly without medicine."* |

---

## 🌐 Deployment Settings (Render)

If deploying to Render as a **Web Service**, configure the following:

* **Environment**: `Python 3`
* **Build Command**: `pip install -r requirements.txt`
* **Start Command**: `gunicorn app:app`


---
Live 
--
link->Here is a clean, production-ready `README.md` tailored for your GitHub repository and Render deployment:

```markdown
# 📰 Fake News Detector

An end-to-end Machine Learning web application designed to classify news articles and headlines as authentic (**TRUE**) or fabricated (**FALSE**). Built with Python, Scikit-Learn, Flask, and vanilla HTML/CSS/JavaScript.

---

## 🚀 Live Demo

- **Web App**: `https://your-app-name.onrender.com` *(Update with your Render URL)*

---

## 🛠️ Tech Stack

- **Machine Learning**: Scikit-Learn (`TfidfVectorizer`, `PassiveAggressiveClassifier`), Pandas
- **Backend**: Python, Flask, Gunicorn
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)
- **Deployment**: Render / GitHub

---

## 📁 Project Structure

```text
fake-news-detector/
│
├── static/
│   ├── style.css          # UI styles & responsive design
│   └── script.js          # Asynchronous API handler (Fetch)
├── templates/
│   └── index.html         # Main dashboard interface
├── app.py                 # Flask server & inference endpoint
├── train_model.py         # Model training script
├── requirements.txt       # Dependencies
├── .gitignore             # Ignored files & binaries
└── README.md              # Project documentation

```

---

## ⚙️ How It Works

1. **Text Preprocessing & Feature Extraction**: Incoming text is converted into n-gram features using **TF-IDF (Term Frequency-Inverse Document Frequency)** to evaluate word importance.
2. **Classification**: A **Passive-Aggressive Classifier** analyzes lexical patterns and assigns a binary classification label.
3. **API & Interface**: The Flask backend exposes a `/predict` endpoint that serves predictions dynamically to the frontend without reloading the page.

---

## 💻 Local Setup & Installation

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/fake-news-detector.git](https://github.com/your-username/fake-news-detector.git)
cd fake-news-detector

```

### 2. Create and activate a virtual environment

```bash
# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Train the ML Model (Optional)

The application automatically trains a baseline model if no serialized weights exist, or you can train it manually:

```bash
python train_model.py

```

### 5. Run the application

```bash
python app.py

```

Open your browser and navigate to `http://127.0.0.1:5000`.

---

## 🧪 Testing with Sample Prompts

| Expected Result | Sample Text Input |
| --- | --- |
| **TRUE (Real)** | *"Scientists discover new Earth-like planet with water atmosphere."* |
| **TRUE (Real)** | *"Central bank announces a 0.25 percent cut in baseline interest rates."* |
| **FALSE (Fake)** | *"Secret government chip found inside all common grocery store bananas."* |
| **FALSE (Fake)** | *"Drinking boiled lemon water cures every known disease instantly without medicine."* |

---

## 🌐 Deployment Settings (Render)

If deploying to Render as a **Web Service**, configure the following:

* **Environment**: `Python 3`
* **Build Command**: `pip install -r requirements.txt`
* **Start Command**: `gunicorn app:app`

---
🌐💻Live
---
 **link**->https://fake-news-detector-machine-learning.onrender.com



## ✍️ Author
Kashish Vishwakarma 

```


