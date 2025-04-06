import joblib
import numpy as np
import pandas as pd

model = joblib.load('model/story_model.pkl')
encoder = joblib.load('model/encoder.pkl')

def predict_story_point(story_type, complexity, team_experience, dependencies, priority):
    df = pd.DataFrame([[story_type, complexity, team_experience, dependencies, priority]],
                      columns=['Story_Type', 'Complexity', 'Team_Experience', 'Dependencies', 'Priority'])
    
    encoded = encoder.transform(df[['Story_Type']]) #.toarray()
    rest = df.drop('Story_Type', axis=1).values
    final_input = np.hstack([encoded, rest])
    
    prediction = model.predict(final_input)
    return prediction[0]