
import pickle

# de-serialize mlp_nn.pkl file into an object called mlp_nn using pickle

with open('model.pkl', 'rb') as handle:
    mdl = pickle.load(handle)

with open('scalar.pkl', 'rb') as handle:
    scl = pickle.load(handle)

def scale(sample):
    return scl.transform(sample)

def predict(sample):
    sample_scaled = scale(sample)
    return mdl.predict(sample_scaled)

# no we can call various methods over mlp_nn as as:
# Let X_test be the feature (UNIX timestamp) for which we want to predict the output
# sample = np.array([[8,  # department code
#            2,  # masters degree
#            0,  # male
#            1,  # 1 training
#            57,  # 30 years old
#            1,  # previous year rating
#            29,  # length of service
#            0,  # KPIs met >80%
#            0,  # awards won
#            81,  # avg training score
#            1,  # sum of metric
#            81  # total score
#            ]])

