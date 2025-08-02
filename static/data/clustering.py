import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.cluster import KMeans
from pathlib import Path

# إعداد المسارات
BASE_DIR = Path(__file__).resolve().parent
INVESTOR_CSV = BASE_DIR / "InvestorSideMatches.csv"
OWNER_CSV = BASE_DIR / "OwnerSideMatches.csv"
INVESTOR_DIR = BASE_DIR / "investor"
OWNER_DIR = BASE_DIR / "owner"

INVESTOR_DIR.mkdir(parents=True, exist_ok=True)
OWNER_DIR.mkdir(parents=True, exist_ok=True)

# ------------------ المستثمرين ------------------
df_investor = pd.read_csv(INVESTOR_CSV)

cols_investor = ['investor_city', 'interest_type', 'experience', 'risk', 'duration', 'goal']
encoders_investor = {col: LabelEncoder().fit(df_investor[col]) for col in cols_investor}
for col in cols_investor:
    df_investor[col] = encoders_investor[col].transform(df_investor[col])

scaler_investor = MinMaxScaler()
X_investor = scaler_investor.fit_transform(df_investor[cols_investor + ['budget']])

kmeans_investor = KMeans(n_clusters=3, random_state=42)
df_investor['cluster'] = kmeans_investor.fit_predict(X_investor)

# حفظ النماذج
pickle.dump(kmeans_investor, open(INVESTOR_DIR / "model_investor.pkl", "wb"))
pickle.dump(scaler_investor, open(INVESTOR_DIR / "scaler_investor.pkl", "wb"))
pickle.dump(encoders_investor, open(INVESTOR_DIR / "encoders_investor.pkl", "wb"))

print("Done!")


# ------------------ الملاك ------------------
df_owner = pd.read_csv(OWNER_CSV)

cols_owner = ['location', 'type']
encoders_owner = {col: LabelEncoder().fit(df_owner[col]) for col in cols_owner}
for col in cols_owner:
    df_owner[col] = encoders_owner[col].transform(df_owner[col])

scaler_owner = MinMaxScaler()
X_owner = scaler_owner.fit_transform(df_owner[cols_owner + ['price']])

kmeans_owner = KMeans(n_clusters=3, random_state=42)
df_owner['cluster'] = kmeans_owner.fit_predict(X_owner)

# حفظ النماذج
pickle.dump(kmeans_owner, open(OWNER_DIR / "model_owner.pkl", "wb"))
pickle.dump(scaler_owner, open(OWNER_DIR / "scaler_owner.pkl", "wb"))
pickle.dump(encoders_owner, open(OWNER_DIR / "encoders_owner.pkl", "wb"))

print("Done!")

# After your clustering model training code, add:

def predict_investor_cluster(input_data):
    """
    Given input_data (e.g., a dictionary of investor features),
    this function preprocesses the data, loads the scaler, encoders, and kmeans model,
    and returns the predicted cluster for an investor.
    """
    # Example implementation:
    import pickle
    import numpy as np
    from pathlib import Path
    
    # Adjust BASE_DIR if needed
    BASE_DIR = Path(__file__).resolve().parent
    INVESTOR_DIR = BASE_DIR / "investor"
    
    # Load your saved models (use appropriate paths)
    kmeans_investor = pickle.load(open(INVESTOR_DIR / "model_investor.pkl", "rb"))
    scaler_investor = pickle.load(open(INVESTOR_DIR / "scaler_investor.pkl", "rb"))
    encoders_investor = pickle.load(open(INVESTOR_DIR / "encoders_investor.pkl", "rb"))
    
    # Preprocess the input_data similarly as you did for training
    # This is an example assuming input_data is a dict with matching keys.
    cols_investor = ['investor_city', 'interest_type', 'experience', 'risk', 'duration', 'goal']
    processed = []
    for col in cols_investor:
        value = input_data[col]
        # Transform using the pre-fitted encoder
        encoded_value = encoders_investor[col].transform([value])[0]
        processed.append(encoded_value)
    
    # Append numeric column 'budget'
    processed.append(input_data['budget'])
    
    # Scale the data (reshape to 2D array as expected)
    X = scaler_investor.transform(np.array(processed).reshape(1, -1))
    
    # Predict cluster using the trained KMeans model
    cluster = kmeans_investor.predict(X)[0]
    return cluster


def predict_owner_cluster(input_data):
    """
    Given input_data (e.g., a dictionary of owner features),
    this function preprocesses the data, loads the scaler, encoders, and kmeans model,
    and returns the predicted cluster for an owner.
    """
    import pickle
    import numpy as np
    from pathlib import Path
    
    # Adjust BASE_DIR if needed
    BASE_DIR = Path(__file__).resolve().parent
    OWNER_DIR = BASE_DIR / "owner"
    
    # Load your saved models (use appropriate paths)
    kmeans_owner = pickle.load(open(OWNER_DIR / "model_owner.pkl", "rb"))
    scaler_owner = pickle.load(open(OWNER_DIR / "scaler_owner.pkl", "rb"))
    encoders_owner = pickle.load(open(OWNER_DIR / "encoders_owner.pkl", "rb"))
    
    cols_owner = ['location', 'type']  # update these names if needed!
    processed = []
    for col in cols_owner:
        value = input_data[col]
        encoded_value = encoders_owner[col].transform([value])[0]
        processed.append(encoded_value)
    
    # Append numeric column 'price'
    processed.append(input_data['price'])
    
    # Scale the data (reshape to 2D array as expected)
    X = scaler_owner.transform(np.array(processed).reshape(1, -1))
    
    # Predict cluster using the trained KMeans model
    cluster = kmeans_owner.predict(X)[0]
    return cluster
