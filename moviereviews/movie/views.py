from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from movie.forms import ReviewForm
from movie.models import Movie, Review


def home_page(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    context = {'searchTerm': searchTerm, 'movies': movies}
    return render(request, 'movie/home.html', context=context)


def about(request):
    pass


def signup(request):
    email = request.GET.get('email')
    return render(request, 'movie/signup.html', {'email': email})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    context = {'movie': movie, 'reviews': reviews}
    return render(request, 'movie/detail.html', context=context)


@login_required
def createreview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return render(request, 'movie/createreview.html', {
            'form': ReviewForm(),
            'movie': movie})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('detail', newReview.movie.id)
        except ValueError:
            return render(request, 'movie/createreview.html', {
                'form': ReviewForm(),
                'error': 'bad data passed in'})


@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'movie/updatereview.html', {'review': review, 'form': form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.movie.id)
        except ValueError:
            return render(request, 'movie/updatereview.html', {'review': review, 'error': 'Bad data in form'})


@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)
