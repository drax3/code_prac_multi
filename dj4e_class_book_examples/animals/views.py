from django.shortcuts import render, redirect
from django.views import View
from animals.models import Cat
from datetime import datetime


# Create your views here.
class CatListView(View):
    
    def get(self, request):
        cats = Cat.objects.all()
        current_year = datetime.now().year
        cat_display = []
        for cat_objects in cats:

            age = current_year - cat_objects.birth_year
            cat_display.append({
                'cat': cat_objects.cat,
                'age': age,
                'pk':cat_objects.pk,
            })
        # for year in cats:
        #     age = 2023 - year.birth_year

        cntx = {'cat_list': cat_display}
        return render(request, 'animals/cats_list.html', cntx)
    
class CatDetailView(View):
    def get(self, request, pk):
        cat = Cat.objects.get(pk=pk)
        current_year = datetime.now().year
        age = current_year - cat.birth_year


        cntx = {'cat_detail': cat, 'age': age}
        return render(request, 'animals/cat_detail.html',cntx)

class CatNewView(View):
    def post(self, request, *arg, **kwargs):
        cat = request.POST.get('cat')
        birth_year = request.POST.get('birth_year')

        img = request.POST.get('img')

        cat_objects = Cat(
            cat = cat,
            birth_year = birth_year,
        )
        if img:
            cat_objects.img = img

        cat_objects.save()

        return redirect('cat_list')
        