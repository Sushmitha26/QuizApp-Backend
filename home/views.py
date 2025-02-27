from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Choice, Admin
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
 
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def quiz(request):
    try:
        if request.method == 'GET':
            questions_list = Question.objects.all()
            context = {
                'questions_list': questions_list
            }

        if request.method == 'POST':
            print('submitted ans:', request.POST.items())
            correct_answers = 0

            for key, val in request.POST.items():
                print('kv:',key, val)
                if key.startswith('choice'):
                    selected_choice = Choice.objects.get(id=val)
                    if selected_choice.is_correct == True:
                        correct_answers += 1

            return render(request, 'home/results.html', {'correct_answers': correct_answers})


    except:
        messages.info(request,'Something went wrong!!')
        return redirect('/home')

    return render(request, 'home/quiz.html', context)


def adminpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user = Admin.objects.get(username = username)
            if password == user.password:
                return render(request, 'home/actions.html')
            else:
                messages.info(request,'password does not match')
        except Admin.DoesNotExist:
            messages.info(request,'Invalid username')
            return redirect('adminpage')

    return render(request, 'home/adminLogin.html')

#temporarily disable csrf for testing
@csrf_exempt
def create_quiz(request):
    if request.method == 'POST':
        try: 
            q_text = request.POST.get('question')
            choices = request.POST.getlist('choices')
            correct_choice_index = request.POST.get('correct_choice')

            question = Question.objects.create(question=q_text)
            
            for index, c_text in enumerate(choices):
                is_correct = False
                if str(index) == correct_choice_index:
                    is_correct = True
                Choice.objects.create(choice_text=c_text, question=question, is_correct=is_correct)
            
            return Response({'msg': 'success!'}, status=status.HTTP_200_OK)

        except:
            return Response({'msg': 'failure!'}, status=status.HTTP_400_BAD_REQUEST)


#temporarily disable csrf for testing
@csrf_exempt
def list_questions(request):
    if request.method == 'GET':
        try:
            questions_list = Question.objects.all()
            return Response({'msg': 'success!'}, status=status.HTTP_200_OK)
        except:
            return Response({'msg': 'failure!'}, status=status.HTTP_400_BAD_REQUEST)


#temporarily disable csrf for testing
@csrf_exempt
def update_quiz(request, question_id):
    if request.method == 'PUT':
        try:
            question_to_update = Question.objects.get(id=question_id)
            choices = Choice.objects.filter(question=question_to_update)

            new_q_text = request.PUT.get('question')
            data = Question(question=new_q_text)
            data.save()

            new_choices = request.PUT.getlist('choices')
            for choice in new_choices:
                choice_text = choice.get('text')
                is_correct = choice.get('is_correct', False)

                Choice.objects.update_or_create(question=data.question, choice_text=choice_text, defaults={'is_correct': is_correct})

            return Response({'msg': 'success!'}, status=status.HTTP_200_OK)

        except:
            return Response({'msg': 'failure!'}, status=status.HTTP_400_BAD_REQUEST)
        

#temporarily disable csrf for testing
@csrf_exempt
def delete_quiz(request, question_id):
    if request.method == 'DELETE':
        try: 
            question = Question.objects.get(id=question_id)
            question.delete()
            return Response({'msg': 'success!'}, status=status.HTTP_200_OK)

        except:
            return Response({'msg': 'failure!'}, status=status.HTTP_400_BAD_REQUEST)

