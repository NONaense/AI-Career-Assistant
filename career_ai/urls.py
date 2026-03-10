from django.contrib import admin
from django.urls import path
from assistant import views


urlpatterns = [

path('admin/', admin.site.urls),

path('',views.home),

path('resume/',views.resume_analyzer),

path('interview/',views.interview_generator_view),

path('tracker/',views.job_tracker),

path('login/',views.login_user),

path('register/',views.register_user),

path('logout/',views.logout_user),

path('roadmap/',views.career_roadmap),

path('jobmatch/',views.job_matcher),

]