from django.contrib import admin
from django.urls import path
from home import views



urlpatterns = [
    # path("",views.index,name='home'),
    # path("about",views.about,name='about'),
    # path("services",views.services,name='services'),
    # path("contact",views.contact,name='contact'),


    ##  This is for new site
    path("newapp",views.newapp,name='newapp'),
    path("",views.newapp,name='newapp'),
    path("viewtable",views.viewtable,name='viewtable'),
    path("deletenewapp/<newapp_id>",views.deletenewapp,name='deletenewapp'),
    path("updatenewapp/<newapp_id>",views.updatenewapp,name='updatenewapp'),
    path("updatenewappfunc/<newapp_id>",views.updatenewappfunc,name='updatenewappfunc'),


    path("testsite",views.testsite,name='testsite'),
    path("addexam",views.addexam,name='addexam'),
    path("viewexam",views.viewexam,name='viewexam'),
    path("updateexam/<addexam_id>",views.updateexam,name='updateexam'),
    path("updatefunc/<addexam_id>",views.updatefunc,name='updatefunc'),
    path("deleteexam/<addexam_id>",views.deleteexam,name='deleteexam'),

    path("addinvigilator/<newapp_id>/<addexam_id>",views.addinvigilator,name='addinvigilator'),
    path("deleteinvigilator/<newapp_id>/<addexam_id>",views.deleteinvigilator,name='deleteinvigilator'),

    path("addroom",views.addroom,name='addroom'),
    path("deleteroom/<addroom_id>",views.deleteroom,name='deleteroom'),
    path("updateroom/<addroom_id>",views.updateroom,name='updateroom'),
    path("updateroomfunc/<addroom_id>",views.updateroomfunc,name='updateroomfunc'),


    path("addinvigilatorinroom/<newapp_id>/<addroom_id>",views.addinvigilatorinroom,name='addinvigilatorinroom'),
    path("deleteinvigilatorfromroom/<newapp_id>/<addroom_id>",views.deleteinvigilatorfromroom,name='deleteinvigilatorfromroom'),
    
    path("addbuilding",views.addbuilding,name='addbuilding'),
    path("deletebuilding/<addbuilding_id>",views.deletebuilding,name='deletebuilding'),
    path("updatebuilding/<addbuilding_id>",views.updatebuilding,name='updatebuilding'),
    path("updatebuildingfunc/<addbuilding_id>",views.updatebuildingfunc,name='updatebuildingfunc'),

    path("deleteroomfrombuilding/<addroom_id>/<addbuilding_id>",views.deleteroomfrombuilding,name='deleteroomfrombuilding'),
    path("addroominbuilding/<addroom_id>/<addbuilding_id>",views.addroominbuilding,name='addroominbuilding'),
]
