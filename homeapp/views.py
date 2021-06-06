from django.views.generic import TemplateView


# Create your views here.
class HomeTemplateView(TemplateView):

    template_name = "homeapp/home-page.html"
    # model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["currpage"] = "homeapp"

        # Add in a QuerySet of all the books
        # context['book_list'] = Book.objects.all()
        return context
