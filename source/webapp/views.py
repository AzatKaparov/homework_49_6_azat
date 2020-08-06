from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, Type, Status
from django.http import HttpResponseNotFound, HttpResponseNotAllowed
from django.views.generic import View, TemplateView
from .forms import TaskForm


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        return render(request, 'index.html', context)


class TaskView(TemplateView):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        context = {'task': task}
        return render(request, 'view.html', context)


class CreateView(TemplateView):
    def get(self, request, *args, **kwargs):
            form = TaskForm()
            return render(request, 'create.html', context={
                'form': form
            })

    def post(self, request):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                type=form.cleaned_data['type'],
                status=form.cleaned_data['status'],
            )
        else:
            return render(request, 'create.html', context={
                'form': form
            })

        return redirect('view', pk=task.pk)


class DeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'delete.html', context={'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('index')


class UpdateView(TemplateView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(initial={
            'summary': task.summary,
            'description': task.description,
            'type': task.type,
            'status': task.status,
            'created_at': task.created_at,
        })
        return render(request, 'update.html', context={
            'form': form,
            'task': task
        })

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.type = form.cleaned_data['type']
            task.status = form.cleaned_data['status']
            task.save()
            return redirect('view', pk=task.pk)
        else:
            return render(request, 'update.html', context={
                'task': task,
                'form': form,
                'errors': form.errors
            })
