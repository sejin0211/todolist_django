from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# request(요청)이 들어왔을 때, todo/todo_list.html과 todos 템플릿을 띄워 보내 주라는 함수
def todo_list(request):
    todos = Todo.objects.filter(complete=False) #완료되지 않은 Todo만 전달해야 하므로 complete=False 옵션으로 필터링
    return render(request, 'todo/todo_list.html', {'todos': todos})

# 선택된 Todo의 pk인 id를 기반으로 Todo 객체를 찾아 todo_detail.html로 전달할 수 있도록 작성
def todo_detail(request, pk): # model에서 정의된 todo 객체 중에서 pk(선택된 객체)만 request하라는 뜻 
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list') 
    else:
        form = TodoForm()
        return render(request, 'todo/todo_post.html', {'form': form})

def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
        return render(request, 'todo/todo_post.html', {'form': form})

def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, 'todo/done_list.html', {'dones': dones})

def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo_list')