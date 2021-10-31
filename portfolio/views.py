from django.shortcuts import render
import logging
from django.http import HttpResponse
from projects.models import Category, Project

# Create your views here.
def index(request):
  projects_id_categories = Project.objects.filter(public=True).values_list('categories',flat=True).distinct()
  projects_id = Project.objects.filter(public=True).values_list('id',flat=True)
  categories_used = Category.objects.filter(id__in=projects_id_categories).values()
  projects = []
  for id in projects_id:
    id_categories_project = Project.objects.filter(id=id).values_list('categories', flat=True)
    p = Project.objects.filter(id=id).values()
    cat = list(Category.objects.filter(id__in=id_categories_project).values_list('id', 'title'))
    txcat = ""
    classcat = ""
    for c in cat:
      classcat += " cat"+str(c[0])
      txcat += " | " + c[1]
    item = {
      'id': p[0]['id'],
      'title': p[0]['title'],
      'classcat': classcat,
      'txcat': txcat
    }
    projects.append(item)
  

      
  data = {
      'categories_used': categories_used,
      'projects': projects
  }
  #return HttpResponse(projects)
  return render(request,'index.html', data)


def project_details(request):

  return render(request, 'project-details.html')
