from django.http import HttpResponseRedirect
from django.shortcuts import render

def review(request):
    if request.method == 'POST':
        username = request.POST['username']

        if username == '':
            return render(request, 'reviews/review.html', {
                'has_error': True,
            })

        print(username)
        return HttpResponseRedirect('/thank-you')

    return render(request, 'reviews/review.html', {
        'has_error': False,
    })

def thank_you(request):
    return render(request, 'reviews/thank_you.html')