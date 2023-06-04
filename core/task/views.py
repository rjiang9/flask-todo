from flask import render_template, redirect, url_for, request
from .models import Category
from ..models import Todo
from . import task
from .forms import TaskForm, CategoryForm
from .. import db
from datetime import datetime


@task.route('/create-task', methods=['GET', 'POST'])
def tasks():
    check= None
    todo= Todo.query.all()
    date= datetime.now()
    now= date.strftime("%Y-%m-%d")

    form= TaskForm()
    form.category.choices =[(category.id, category.name) for category in Category.query.all()]

    print('hello {} '.format(now))
    print(todo)
    print('hello--------')

    if request.method == "POST":
        if request.form.get('taskDelete') is not None:
            deleteTask = request.form.get('checkedbox')
            if deleteTask is not None:
                todo = Todo.query.filter_by(id=int(deleteTask)).one()
                db.session.delete(todo)
                db.session.commit()
                return redirect(url_for('task.tasks'))
            else:
                check = 'Please check-box of task to be deleted'

        elif form.validate_on_submit():
            selected= form.category.data
            category= Category.query.get(selected)
            todo = Todo(title=form.title.data, date=form.date.data, time= form.time.data, category= category.name)
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('task.tasks'))


    return render_template('task/tasks.html', title='Create Tasks', form=form, todo=todo, DateNow=now, check=check)

@task.route('/create-cat', methods=['GET', 'POST'])
def cats():
    form= CategoryForm()
    cats = Category.query.all()

    if request.method == "POST":
        if request.form.get('catDelete') is not None:
            deleteCat = request.form.get('checkedbox')
            if deleteCat is not None:
                cat = Category.query.filter_by(id=int(deleteCat)).one()
                db.session.delete(todo)
                db.session.commit()
                return redirect(url_for('task.cats'))
            else:
                check = 'Please check-box of category to be deleted'

        elif form.validate_on_submit():
            cat = Category(name=form.name.data)
            db.session.add(cat)
            db.session.commit()
            return redirect(url_for('task.cats'))


    return render_template('task/cats.html', title='Create categories', form=form, cats=cats)
