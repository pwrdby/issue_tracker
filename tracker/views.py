from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db.models import Avg, Max, Min

from tracker.models import Category, Issue
from tracker.forms import CategoryForm


def user_login(request):
    """
    Login user.
    """
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('tracker:index', args=['all']))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "tracker/auth/login.html", context)
    else:
        return render(request, "tracker/auth/login.html", context)

def user_logout(request):
    """
    Logout user.
    """
    logout(request)
    return HttpResponseRedirect(reverse('tracker:index',  args=['all']))


def change_category(request):
    """
    Call IssueView with choosen category.
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            url_path = form.data['current_category']
            return HttpResponseRedirect(reverse('tracker:index',  args=[url_path]))


class IssueView(generic.ListView):
    """
    View for all issues.
    """
    template_name = 'tracker/issue_list.html'
    context_object_name = 'issues'

    def get_queryset(self):
        """
        Return all issues.
        """
        return Issue.objects.all()
        
    def get(self, *args, **kwargs):
        """
        Overriden get method for listView.
        """
        cat_name = self.request.path.split('/')[-1]
        if cat_name != 'all':
            cat = Category.objects.get(name=cat_name)
            self.object_list = Issue.objects.filter(category=cat)
        else:
            self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)


    def get_context_data(self, **kwargs):
        """
        Add own context data for template.
        """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        objs = Issue.objects.all().aggregate
        attr = 'worked_time'
        context['avg'] = objs(Avg(attr)).get(f"{attr}__avg")
        context['max'] = objs(Max(attr)).get(f"{attr}__max")
        context['min'] = objs(Min(attr)).get(f"{attr}__min")
        context['user'] = username=self.request.user
        context['form'] = CategoryForm()

        return context


class DetailView(generic.DetailView):
    """
    View for detail issue.
    """
    model = Issue
    template_name = "tracker/detail.html"



def update(request, category_id):
    """
    Update category
    """
    category = get_object_or_404(Category, id=category_id)
    try:
        new_description = request.POST['description']
        print(new_description)
    except KeyError:
        render(request, 'tracker/detail.html', {
            'category': category,
            'error_message': "You didn't fill a new description"
            })
    else:
        category.description = new_description
        category.save()

        return HttpResponseRedirect(reverse('tracker:index'))
