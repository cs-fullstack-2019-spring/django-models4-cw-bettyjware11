
from django.shortcuts import render
from django.http import HttpResponse

from .models import Mom
from .models import Child


# print out all moms with their children
# objects returns something in a collection
def list_moms(request):
    moms = Mom.objects.all()
    for mom in moms: # Go through moms one at a time
        print(f'{mom.mom_first_name} {mom.mom_last_name}')
        # Use the foreign key relation with children to get the children where the mom_name of current mom from loop
        # matches Child records linked
        children = child.objects.filter(child_mom__mom_last_name=mom.mom_last_name)
        for child in children:
            print(f'{child.child_first_name} {child.child_last_name})
            print(f'{mom.mom_first_name} {mom.mom_last_name})
    return HttpResponse()

def deletemom(request):
    return HttpResponse('delete')


def listChildrenAndMom():
    return None


def listAllChildren():
    return None


def addAChild():
    return None