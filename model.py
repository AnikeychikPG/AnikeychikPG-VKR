from tensorflow import keras

model = keras.models.load_model("/Users/pavelanikejcik/Downloads/Аникейчик ПГ ВКР/model_mlp")



def predict(inputs):
    prediction = model.predict(inputs)
    return prediction

def get_model():
    return "Hello MODEL"
