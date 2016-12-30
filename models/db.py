# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# app configuration made easy. Look inside private/appconfig.ini
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = ['*'] if request.is_local else []
# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get('forms.separator') or ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

from gluon.tools import Auth, Service, PluginManager

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=myconf.get('host.names'))
auth.settings.extra_fields['auth_user']= [
    Field('emp_id',length=10,requires=IS_NOT_EMPTY(),label="رقم السجل المدني") ,
    Field('name',length=10,requires=IS_NOT_EMPTY(),label="الاسم كاملا") ,
    Field('mobil',length=10,requires=IS_NOT_EMPTY(),label="رقم الجوال")
    ]
service = Service()
plugins = PluginManager()

# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.get('smtp.server')
mail.settings.sender = myconf.get('smtp.sender')
mail.settings.login = myconf.get('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
auth.settings.create_user_groups = False
auth.settings.showid = False
# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)
T.force('ar')

#----------------------------------------------------
#  جدول اسماء الايام
db.define_table('key_days',
    Field('name',length=150, label='الوصف'),
    format='%(id)s - %(name)s')
db.key_days.id.label='م'

if db(db.key_days.id>0).isempty() == True:
    db.key_days.insert(name='السبت')
    db.key_days.insert(name='الاحد')
    db.key_days.insert(name='الأثنين')
    db.key_days.insert(name='الثلاثاء')
    db.key_days.insert(name='الاربعاء')
    db.key_days.insert(name='الخميس')
    db.key_days.insert(name='الجمعة')
#----------------------------------------------------
#----------------------------------------------------
#  موعيد الكلمات
db.define_table('key_speech',
    Field('name',length=150, label='الوصف'),
    format='%(id)s - %(name)s')
db.key_speech.id.label='م'

if db(db.key_speech.id>0).isempty() == True:
    db.key_speech.insert(name='بعد الفجر')
    db.key_speech.insert(name='بعد الظهر')
    db.key_speech.insert(name='بعد العصر')
    db.key_speech.insert(name='بعد المغرب')
    db.key_speech.insert(name='بعد العشاء')
#----------------------------------------------------

# الايام و الاسابيع الدراسية
db.define_table('days',
    Field('week_no','integer', requires= IS_NOT_EMPTY() , label='رقم الاسبوع'),
    Field('day_d','integer',requires=[IS_INT_IN_RANGE(1, 31) ,IS_NOT_EMPTY(error_message='يجب ان يكون داخل النطاق الصحيح')],label="اليوم"),
    Field('day_m' ,'integer' , label='الشهر',requires=[IS_INT_IN_RANGE(1, 13) ,IS_NOT_EMPTY(error_message='يجب ان يكون داخل النطاق الصحيح')]),
    Field('day_y' ,'integer' , label='السنة',requires=[IS_INT_IN_RANGE(1435, 1450) , IS_NOT_EMPTY(error_message='يجب ان يكون داخل النطاق الصحيح')] ),
    Field('key_days','reference key_days', label="اليوم" ),
    Field('is_open','boolean',default=False,label="متاح"),
     format='%(day_d)s - %(day_m)s - %(day_y)s' )
db.days.id.label='م'

#----------------------------------------------------
#انواع المواقع
db.define_table('key_location_type',
    Field('name',length=150, label='الوصف'),
    format='%(id)s - %(name)s')
db.key_location_type.id.label='م'

if db(db.key_location_type.id>0).isempty() == True:
    db.key_location_type.insert(name='جامع')
    db.key_location_type.insert(name='مسجد')
    db.key_location_type.insert(name='مسجد طريق')
    db.key_location_type.insert(name='مدرسة')
    db.key_location_type.insert(name='سجن')
#----------------------------------------------------
#  القطاعات
db.define_table('key_location_place',
    Field('name',length=150, label='الوصف'),
    format='%(id)s - %(name)s')
db.key_location_place.id.label='م'

if db(db.key_location_place.id>0).isempty() == True:
    db.key_location_place.insert(name='الشمال')
    db.key_location_place.insert(name='الجنوب')
    db.key_location_place.insert(name='الشرق')
    db.key_location_place.insert(name='الغرب')
    db.key_location_place.insert(name='الوسط')
#----------------------------------------------------
#  الفئات للمواقع
db.define_table('key_location_category',
    Field('name',length=150, label='الوصف'),
    format='%(id)s - %(name)s')
db.key_location_category.id.label='م'

if db(db.key_location_category.id>0).isempty() == True:
    db.key_location_category.insert(name='أ')
    db.key_location_category.insert(name='ب')
    db.key_location_category.insert(name='ج')
    db.key_location_category.insert(name='د')
    db.key_location_category.insert(name='هـ')
#----------------------------------------------------
#----------------------------------------------------
#  الفئات للمواقع
db.define_table('key_degree',
    Field('name',length=150, label='الوصف'),
    format='%(id)s - %(name)s')
db.key_degree.id.label='م'

if db(db.key_degree.id>0).isempty() == True:
    db.key_degree.insert(name='طالب علم')
    db.key_degree.insert(name='جامعي')
    db.key_degree.insert(name='ماجستير')
    db.key_degree.insert(name='دكتوراه')
    db.key_degree.insert(name='استاذ')
#----------------------------------------------------

#-----------------------------------------------------
# المواقع
db.define_table('locations',
    Field('name',length=20,requires=IS_NOT_EMPTY(),label="اسم الموقع"),
    Field('key_location_type','reference key_location_type',label='نوع الموقع' ),
    Field('key_location_place','reference key_location_place',label=' القطاع' ),
    Field('key_location_category','reference key_location_category',label=' الفئة' ),
    Field('admin_name','string',length=100, label=" اسم الامام") ,
    Field('mobil',length=10,label="رقم الجوال"),
    Field('tel',length=20,label="الهاتف الثابت"),
    Field('address','string',length=350, label="العنوان") ,
    Field('c_count','integer' , label='عدد الكلمات في الاسبوع',requires=[IS_INT_IN_RANGE(1, 10) , IS_NOT_EMPTY(error_message='يجب ان يكون داخل النطاق الصحيح')] ) ,
    Field('emam_memo','text',label="ملاحظات الامام للملقين")  ,
    Field('is_open','boolean',default=False,label="متاح") ,
    Field('gps','string',length=100, label="الموقع الجغرافي") ,
    format='%(id)s - %(name)s')
db.locations.id.label='م'
#-----------------------------------------------------
# مواعيد كلمات المواقع
db.define_table('locations_times',
    Field('locations','reference locations',label='الموقع' , default=request.args(0) , writable=False),
    Field('key_days','reference key_days', label="اليوم" ) ,
    Field('key_speech','reference key_speech', label="الموعد" )
    )
db.locations_times.id.label='م'
#-----------------------------------------------------
# بيانات الملقين و الائمة
db.define_table('msajed_users',
    Field('name',length=200,requires=IS_NOT_EMPTY(),label="الاسم"),
    Field('user_id',length=10,requires=IS_NOT_EMPTY(),label="رقم السجل المدني"),
    Field('mobil',length=10,label="رقم الجوال"),
    Field('usr_password',length=10,label="كلمة السر"),
    Field('key_degree','reference key_degree',label='الدرجة العلمية' ),
    Field('user_degree','integer' , label='درجة الملقي' ) ,
    Field('is_speaker','boolean',default=False,label="ملقي") ,
    Field('is_emam','boolean',default=False,label="امام") ,
    Field('emam_location','integer' , label='رقم مسجد الامام' ) ,
    Field('is_open','boolean',default=False,label="متاح") ,
    format='%(id)s - %(name)s')
db.msajed_users.id.label='م'
#=================================================================
# معايير اختيار الملقين للمساجد
db.define_table('standards',
    Field('start_degree','integer' , label='من' ) ,
    Field('end_degree','integer',label="الى") )
db.standards.id.label='م'

# معايير المساجد للملقين
db.define_table('standards_locations',
    Field('standards','reference standards',label='المعيار' , default=request.args(0) , writable=False ),
    Field('key_location_type','reference key_location_type',label='نوع الموقع' ),
    Field('key_location_category','reference key_location_category',label=' الفئة' ) )
db.standards_locations.id.label='م'

#=====================================================================
# كلمات المساجد
db.define_table('locations_speaker',
    Field('days','reference days', label="اليوم"  ) ,
    Field('locations','reference locations',label='الموقع'  ),
    Field('locations_dis',length=120,label="تفاصيل الوقت"),
    Field('msajed_users','reference msajed_users',label='الملقي' ),
    Field('speaker_dis',length=300,label=" عنوان الكلمة"),
    Field('emam_degree','integer' , label='درجة الإمام للملقي' )  ,
    Field('is_chick','boolean',default=False,label="هل حضر الملقي")
    )
db.locations_speaker.id.label='م'
