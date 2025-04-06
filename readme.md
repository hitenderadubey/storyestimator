- Django Web App to estimate Story Points
- ML Model using RandomForest
- OneHotEncoding for Story_Type
- API & Form based Prediction
- Postman ready

post/predict

Body:
json
{
  "Story_Type": "Bug",
  "Complexity": 3,
  "Team_Experience": 5,
  "Dependencies": 2,
  "Priority": 2
}

set up:
git clone <repo-url>
cd userstory-predictor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
