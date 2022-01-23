
from email import message
from unicodedata import category
from django.contrib import messages
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from polls.forms import SignUpForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

from polls.models import Category, QuesModel, UserProfile


def index(request):
    category = Category.objects.all()
    context={'category':category, }
    return render(request, 'index.html', context) 

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user =request.user
            request.session['userimage'] = current_user.email
            ''' Multi Langugae
            request.session[translation.LANGUAGE_SESSION_KEY] = userprofile.language.code
            request.session['currency'] = userprofile.currency.code
            translation.activate(userprofile.language.code) '''

            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect('/user_login')
    # Return an 'invalid login' error message.
    
    category = Category.objects.all()
    context = {'category': category
     }
    return render(request, 'login.html', context)
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.filter(email=email).exists()
            if user:
                messages.warning(request, 'Emain address already taken')
                return HttpResponseRedirect('/signup')
            else:
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                current_user = request.user
                data=UserProfile()
                data.user_id=current_user.id
                data.save()
                messages.success(request, 'your account has been created')
                return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')
    form = SignUpForm()

    category = Category.objects.all()
    context = {'category': category,
                'form' : form,
     }
    return render(request, 'register.html', context)

def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')

def quiz(request):
    category = Category.objects.all()
    quesmodel = QuesModel.objects.all()
    context = {'category': category,
               'quesmodel': quesmodel
     }
    return render(request, 'quiz.html', context)

@login_required(login_url='/login')
def userprofile(request):
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    category = Category.objects.all()
    context = {'category': category,
               'profile': profile

    }
    return render(request, 'userprofile.html', context)

def quiz(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quiz.html',context)