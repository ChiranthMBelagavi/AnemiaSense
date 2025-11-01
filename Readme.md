# Anemia Sense: Anemia Prediction Web App

## 📝 Project Overview

Anemia Sense is a web application that predicts the likelihood of a person having anemic disease based on blood test parameters. The project uses a machine learning model, trained on a comprehensive dataset, and deploys it using the Flask web framework.

This tool aims to provide a simple and accessible way for users to check their health indicators, empowering them with early detection for better management and healthier living.

---

## ⚙️ Project Flow & Technical Architecture

The project follows a standard MLOps (Machine Learning Operations) workflow:

1.  **User Interaction (UI):** The user interacts with the web interface to enter input parameters.
2.  **Input Analysis & Model Integration:** The entered input is analyzed by the integrated machine learning model.
3.  **Prediction Showcase:** Once the model analyzes the input, the prediction result (e.g., "You have anemic disease" or "You don't have any Anemic Disease") is showcased on the UI.

To accomplish this, the project involves the following activities:

* **Data Collection & Preparation:**
    * Collect the dataset (`anemia.csv`).
    * Perform data cleaning and preparation (e.g., balancing the dataset).
* **Exploratory Data Analysis (EDA):**
    * Conduct descriptive statistical analysis.
    * Perform visual analysis to understand data patterns.
* **Model Building:**
    * Train the model using multiple machine learning algorithms.
    * Select the best-performing model.
* **Performance Testing & Hyperparameter Tuning:**
    * Test the model with multiple evaluation metrics.
    * Compare model accuracy before and after applying hyperparameter tuning (though specific tuning code is not provided in the current scripts, this is an identified step).
* **Model Deployment:**
    * Save the best-trained model (`model.pkl`).
    * Integrate the model with a Flask web framework for a user-facing application.

[Image of the project's technical architecture]

## 📋 How to Run the Project

These are the steps to set up and run the project on local machine.

### Prerequisites

To complete this project, you will need the following software, concepts, and Python packages:

* **Software:**
    * Anaconda Navigator and Visual Studio Code.
        * Refer to this link to download Anaconda Navigator: [https://youtu.be/1ra4zH2G4o0](https://youtu.be/1ra4zH2G4o0)
* **Python Packages:**
    * Open Anaconda Prompt as administrator and run the following commands:
        ```bash
        pip install numpy
        pip install pandas
        pip install scikit-learn
        pip install matplotlib
        pip install scipy
        pip install pickle-mixin # Note: 'pickle' is built-in; 'pickle-mixin' might be a specific library you intend to use.
        pip install seaborn
        pip install Flask
        ```

### Step 1: Project Structure

Ensure your project folder has the following structure:

AnemiaSense/
├── data/
│   └── anemia.csv
├── static/
│   └── images/
│       └── anemia.jpg
├── templates/
│   ├── index.html
│   └── predict.html
├── venv/
├── app.py
├── model.pkl
├── Readme.md
├── requirements.txt
└── train_model.py


### Step 2: Install Dependencies (using `requirements.txt`)

For a quick setup, open your terminal, navigate to the project directory, and install all required libraries using the `requirements.txt` file. This is the most efficient way to install all project dependencies at once.

```bash
pip install -r requirements.txt

Step 3: Train the Model
Run the train_model.py script to train the machine learning model and save it as model.pkl.

Bash

python train_model.py

Step 4: Run the Application
Start the Flask web server to launch the web application.

Bash

python app.py

Step 5: Access the Web App
Open your web browser and navigate to the following URL:

[http://127.0.0.1:5000](http://127.0.0.1:5000)
You can now use the application to get anemia predictions.
The Demo of Anemia Sense app : https://drive.google.com/file/d/17MnawXvPOrwTu2sInEfq8sADnfHEJjau/view?usp=sharing
