import pickle

def exportConfig():
    with open("config.pkl", "rb") as file:
        config = pickle.load(file)
        return config

def editConfig(name, value):
    with open("config.pkl", "rb") as file:
        config = pickle.load(file)
    config[name] = value
    with open("config.pkl", "wb") as file:
        pickle.dump(config, file)