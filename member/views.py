from django.shortcuts import render


def member_list(request):
    return render(request, "memberList.html", locals())

def member_detail(request):
    return render(request, "memberDetail.html", locals())