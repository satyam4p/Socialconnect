from django.views.generic import TemplateView

class homepage(TemplateView):
    template_name = 'index.html'



class testpage(TemplateView):
    template_name = 'test.html'

class thenkspage(TemplateView):
    template_name = 'thanks.html'



