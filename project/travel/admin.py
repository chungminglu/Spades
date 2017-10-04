from django.contrib import admin
from travel.models import site , gthoteltime , gtsitactivity
from travel.models import gtsiteapparel,gtsiteother,gtsiterestaurant, gtsiteshop
from travel.models import kthoteltime,ktsiteactivity,ktsiteapparel,ktsiteother,ktsiterestaurant,ktsiteshop
# Register your models here.
###site
class siteAdmin(admin.ModelAdmin):
    list_display=('ID','Name','Address','Lat','Lng','URL') 

admin.site.register(site,siteAdmin)
#####金閣寺
#####飯店時間
class gthoteltimeAdmin(admin.ModelAdmin):
    list_display=('Id','ChiName','Lat','Lng','CheckIn','CheckOut','Score')

admin.site.register(gthoteltime,gthoteltimeAdmin)

#活動分數
class gtsitactivityAdmin(admin.ModelAdmin):
    list_display=('Id','Name','Lat','Lng','Score')

admin.site.register(gtsitactivity,gtsitactivityAdmin)

##染店分數
class gtsiteapparelAdmin(admin.ModelAdmin):
    list_display=('Id','Name','Lat','Lng','Score')

admin.site.register(gtsiteapparel,gtsiteapparelAdmin)

##其他景點
class gtsiteotherAdmin(admin.ModelAdmin):
    list_display=('Id','Name','Lat','Lng','Score')

admin.site.register(gtsiteother,gtsiteotherAdmin)

##餐廳分數
class gtsiterestaurantAdmin(admin.ModelAdmin):
    list_display=('Id','Name','Lat','Lng','Score')

admin.site.register(gtsiterestaurant,gtsiterestaurantAdmin)

#購物分數
class gtsiteshopAdmin(admin.ModelAdmin):
    list_display=('Id','Name','Lat','Lng','Score')

admin.site.register(gtsiteshop,gtsiteshopAdmin)

#######清水寺

#####飯店時間
class kthoteltimeAdmin(admin.ModelAdmin):
    list_display=('Id','ChiName','Lat','Lng','CheckIn','CheckOut','Score')

admin.site.register(kthoteltime,kthoteltimeAdmin)

#活動分數
class ktsiteactivityAdmin(admin.ModelAdmin):
    list_display=('Id','Name','Lat','Lng','Score')

admin.site.register(ktsiteactivity,ktsiteactivityAdmin)

##染店分數
class ktsiteapparelAdmin(admin.ModelAdmin):
    list_display=('Id','Name','Lat','Lng','Score')

admin.site.register(ktsiteapparel,ktsiteapparelAdmin)

##其他景點
class ktsiteotherAdmin(admin.ModelAdmin):
    list_display=('Id','Name','Lat','Lng','Score')

admin.site.register(ktsiteother,ktsiteotherAdmin)

##餐廳分數
class ktsiterestaurantAdmin(admin.ModelAdmin):
    list_display=('Id','Name','Lat','Lng','Score')

admin.site.register(ktsiterestaurant,ktsiterestaurantAdmin)

#購物分數
class ktsiteshopAdmin(admin.ModelAdmin):
    list_display=('Id','Name','Lat','Lng','Score')

admin.site.register(ktsiteshop,ktsiteshopAdmin)