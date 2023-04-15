from .models import SubRubric


def bboard1_context_processor(request):
    context = {}
    context['rubrics'] = SubRubric.objects.all()
    return context


