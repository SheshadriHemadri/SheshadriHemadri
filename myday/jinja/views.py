from django.shortcuts import render

# Create your views here.
def displaygreen(request):
    stu=[{'name':'sheshu','marks':35},{'name':'Hemu','marks':85},
         {'name':'Dahlia','marks':80},{'name':'Radha','marks':99}]

    return render(request,'green.html',{'data': stu})

##def displaygreen(request):
##    stu=['shiva','navmohan','shravani','salma']
##    return render(request,'green.html',{'data': stu})
