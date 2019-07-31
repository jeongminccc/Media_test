from django.shortcuts import render, redirect, get_object_or_404
from .models import Portfolio
from .forms import PortfolioForm

# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolios' : portfolios})


def create(request):
    if request.method == "GET":
        form = PortfolioForm()
    elif request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        
        if form.is_valid():
            obj = form.save()
            return redirect( '/portdetail/' + str(obj.id) )

    ctx = {
        'form' : form,
    }
    return render(request, 'portfolio/portnew.html', ctx)

    
def detail(request, portfolio_id):
    portfolio_detail = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'portfolio/portdetail.html', {'portfolio': portfolio_detail})