from .models import DNNAgreeDisagree


def update_selection(request, pk, sel):

    agree_disagree_obj = DNNAgreeDisagree.objects.get(id=pk)
    if(sel == "1"):
        agree_disagree_obj.selected = True
    else:
        agree_disagree_obj.selected = False
    agree_disagree_obj.save()
