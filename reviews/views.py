from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
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