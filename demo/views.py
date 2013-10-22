from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from demo.models import Car, Part

class DemoCarView(DetailView):
    # 1st query implicitly here, basically Car.objects.get(pk=<pk>), desired
    model = Car

class DemoCarViewPreload(TemplateView):
    template_name = 'demo/car_detail_preload.html'
    def get_context_data(self, **kwargs):
        context = super(DemoCarViewPreload, self).get_context_data(**kwargs)
        # 1st query here
        car = Car.objects.get(pk=kwargs.get('pk'))
        context['car'] = car
        # 2nd and final query here. Optimum
        context['parts'] = Part.objects.select_related('manufacturer').filter(car=car)
        return context