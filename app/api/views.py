from job.models import Job
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def search(request):
    if is_ajax(request):
        query = request.POST.get('data')
        qs = Job.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))

        res = None
        if len(qs) > 0 and len(query)>0:
            data = []
            for pos in qs:
                item = {
                    'pk': pos.pk,
                    'title': pos.title,
                    'description': pos.description,
                    'created_at': pos.created_at
                }
                data.append(item)
            res = data
        else:
            res = "No job found..."

        context = {
            "data":res
        }
        return JsonResponse(context)
    return JsonResponse({})
