from django.shortcuts import render
from .forms import PredictionForm
from .predictor_utils import predict_story_point

def predict_view(request):
    prediction = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            prediction = predict_story_point(cd['story_type'], cd['complexity'], cd['team_experience'], cd['dependencies'], cd['priority'])
    else:
        form = PredictionForm()

    return render(request, 'predictor/form.html', {'form': form, 'prediction': prediction})