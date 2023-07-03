from django.urls import path
from . import views

app_name = 'instructions'

urlpatterns = [
    path('', views.all_instructions, name='allIns'),
    path('<int:instruction_id>/', views.instruction_detail, name='singleIns'),
]
