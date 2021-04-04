import pickle

var = "Narendra Modi is prime minister of india"


def detecting_fake_news(var):
    load_model = pickle.load(open('finalized_model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    return (print("The given statement is ", prediction[0]),
            print("The truth probability score is ", prob[0][1]))

detecting_fake_news(var)
