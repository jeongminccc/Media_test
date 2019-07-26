from django.shortcuts import render
from .models import Portfolio
from .forms import PortfolioForm

# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolios' : portfolios})


def create(request):
    form = PortfolioForm()
    ctx = {
        'form' : form,
    }
    return render(request, 'portnew.html', ctx)