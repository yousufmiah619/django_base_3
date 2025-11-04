from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Course
from .form import CourseForm
from django.contrib import messages
from django.contrib import auth
# Create your views here.
def add_course(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CourseForm(request.POST , request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"course added successfully")
                return redirect("add_course")
            else:
                messages.error(request,"error adding-course")
                return redirect("add_course")
    else:
        return redirect("signin")   
        
    form=CourseForm()
    context={
        "form": form
    }
    return render (request,"add_course.html",context)
    #     name=request.POST.get ("name")
    #     age=request.POST.get("age")
    #     course=request.POST.get("course")
    #     print(name,age,course)
        
    #     data=Course(name=name,age=age,course=course)
    #     data.save()
        
    #     print("data saved successfully")
    #     return redirect("course_list") 
    # return render (request,"add_course.html")       
        
def course_list(request):
    if request.user.is_authenticated:
        info=Course.objects.all()
        if info:
            context={
                "data": info
            }
            return render (request,"course_list.html",context)
        else:
            return HttpResponse("no data found")
    else:
        return redirect ('signin')
  #  return render (request,"add_course.html")

def update_course(request,id):
    if request.user.is_authenticated:
        try:
            info=Course.objects.get(id=id)
        except Exception as e :
            print(e)                                                                                                                            
            return HttpResponse("no data found")
        if request.method=="POST":
            form=CourseForm(request.POST,instance=info)
            if form.is_valid():
                form.save()
                messages.success(request,"course update successfully")
                return redirect("update_course",id=info.id)
            else:
                messages.error(request,"error updating-course")
                return redirect("update_course")
    else:
        return redirect("signin")
    form=CourseForm(instance=info)
    context={
        "id":info.id,
        "form":form
    }
    return render (request,"course_update.html",context)
    #     name=request.POST.get("name")
    #     age=request.POST.get("age")
    #     course=request.POST.get("course")
        
    #     info.name=name
    #     info.age=age
    #     info.course=course
    #     info.save()
    #     return redirect("course_list")
    # context={
    #     "id":info.id,
    #     "name":info.name,
    #     "age":info.age,
    #     "course":info.course
    # }
    #return render (request,"course_update.html",context)

def delete_course(request,id):
    if request.user.is_authenticated:
        try:
            info=Course.objects.get(id=id)
        except Exception as e :
            print(e)                                                                                                                            
            return HttpResponse(f"{id} {e}")
        info.delete()
        messages.success(request,"course delete successfully")
        return redirect (request,"course-list")
    else:
        return redirect("signin")
    
 
def calculator(request):
    if request.user.is_authenticated:
        try:
            result=0
            if request.method=="POST":
                num1=eval(request.POST.get("num1"))
                num2=eval(request.POST.get("num2"))
                operation=request.POST.get("operation")
                if operation=="+":
                    result=num1+num2
                elif operation=="-":
                    result=num1-num2
                elif operation=="*":
                    result=num1*num2
                elif operation=="/":
                    result=num1/num2    
                print(result)

        except Exception as e :
            print(e)                                                                                                                            
            return HttpResponse(f"{e}")
        return render (request,"calculator.html",{"result":result})
    else:
        return redirect ('signin')

def home(request):
    if request.user.is_authenticated:
        return render (request,"home.html")
    else:
        return redirect("signin")
    