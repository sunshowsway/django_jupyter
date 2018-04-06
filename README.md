# django_jupyter
Example setup for creating notebooks for Django projects.

# Getting Started
Install requirements (recommended to create a virtual environment)

```
> cd djanjupy
> pip install -r reqirements.txt
```

Run migrations

```
> python manage.py migrate
```

Start up th jupyter notebook, we are doing this from one level up so we can keep the notebooks seperated away from django
and also still be able to access our django modules etc.. from within a jupyter notebook

```
> cd ..
> python djanjupy/manage.py shell_plus --notebook
```

That command will open jupyter in your browser. Click into the notebooks directory and select Django Models.ipynb to see a 
notebook in action. Optionally from the notebooks directory you can select New Django-Shell Plus to create a new notebook.

Make sure you save your changes when your done and also once you open a notebook use Kernel -> Restart & Run All to run all
the commands over again.
