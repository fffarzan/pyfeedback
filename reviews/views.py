from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, View
from django.views.generic.base import TemplateView

from reviews.forms import ReviewForm
from reviews.models import Review

class NewReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/new_review.html'
    success_url = '/thank-you'

class ThankyYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'

        return context

class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        return super().get_queryset().filter(rating__gt=4)

class ReviewDetail(DetailView):
    template_name = 'reviews/review_detail.html'
    model = Review
    context_object_name = 'review_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        favorite_id = self.request.session.get('favorite_review')
        context['is_favorite'] = favorite_id == str(loaded_review.id)

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['favorite_review'] = review_id

        return HttpResponseRedirect('/reviews' + review_id)