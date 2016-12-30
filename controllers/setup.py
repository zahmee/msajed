

@auth.requires_membership("admin")
def index():
    return dict()



# التخصصات
#@auth.requires_membership('super_admin')
@auth.requires_membership("admin")
def msajed_users():
    links = [
        lambda row: A(SPAN("الاساليب الاشرافية",_class="btn btn-info btn-xs" ),_href=URL("setup","asleeb_dep",args=[row.id]))
    ]
    grid = SQLFORM.grid(db.msajed_users, user_signature=True, editable=True, deletable=True, create=True, csv=True,
                        searchable=True, showbuttontext=True,maxtextlengths={'msajed_users.name':150})
    return dict(grid=grid)


@auth.requires_membership("admin")
def key_degree():
    grid = SQLFORM.grid(db.key_degree, user_signature=True, editable=True, deletable=True, create=True, csv=False,
                        searchable=False, showbuttontext=True,maxtextlengths={'key_degree.name':150})
    return dict(grid=grid)

@auth.requires_membership("admin")
def days():
    grid = SQLFORM.grid(db.days, user_signature=False, editable=True, deletable=True, create=True, csv=False,
                        searchable=True, showbuttontext=True )
    return dict(grid=grid)

@auth.requires_membership("admin")
def standards():
    links = [
            lambda row: A(SPAN("معايير المواقع",_class="btn btn-info btn-xs" ),_href=URL("setup","standards_locations",args=[row.id]))
        ]
    grid = SQLFORM.grid(db.standards, user_signature=True, editable=True,links=links , deletable=True, create=True, csv=False,
                        searchable=False, showbuttontext=True )
    return dict(grid=grid)

@auth.requires_membership('admin')
def standards_locations():
    response.title = " معايير المواقع"
    if request.args(0) ==None :
        URL("setup","standards")
    q = (db.standards_locations.standards == request.args(0))
    grid = SQLFORM.grid(q ,user_signature=False,editable=True,deletable=True,create=True,csv=False,showbuttontext=True,searchable=False,args=request.args[:1])
    return  dict(grid=grid )

@auth.requires_membership('admin')
def locations_times():
    response.title = "مواعيد كلمات الموقع"
    if request.args(0) ==None :
        URL("setup","locations")
    q = (db.locations_times.locations == request.args(0))
    grid = SQLFORM.grid(q ,user_signature=False,editable=True,deletable=True,create=True,csv=False,showbuttontext=True,searchable=False,args=request.args[:1])
    return  dict(grid=grid )

@auth.requires_membership("admin")
def key_location_type():
    grid = SQLFORM.grid(db.key_location_type, user_signature=True, editable=True, deletable=True, create=True, csv=False,
                        searchable=False, showbuttontext=True,maxtextlengths={'key_location_type.name':150})
    return dict(grid=grid)

@auth.requires_membership("admin")
def key_location_place():
    grid = SQLFORM.grid(db.key_location_place, user_signature=True, editable=True, deletable=True, create=True, csv=False,
                        searchable=False, showbuttontext=True,maxtextlengths={'key_location_place.name':150})
    return dict(grid=grid)

@auth.requires_membership("admin")
def key_location_category():
    grid = SQLFORM.grid(db.key_location_category, user_signature=True, editable=True, deletable=True, create=True, csv=False,
                        searchable=False, showbuttontext=True,maxtextlengths={'key_location_category.name':150})
    return dict(grid=grid)

@auth.requires_membership("admin")
def locations():
    headers={'locations.name':'اسم الموقع','locations.key_location_type':'نوع الموقع' , 'locations.key_location_place':'القطاع'}
    fields=[ db.locations.name,db.locations.key_location_type , db.locations.key_location_place ]
    links = [
    lambda row: A(SPAN("مواعيد الكلمات" , _class="btn btn-info btn" ,_title="مواعيد الكلمات", ),_href=URL("setup","locations_times",args=[row.id])) ,

    ]
    grid = SQLFORM.grid(db.locations,headers=headers,fields=fields ,links=links ,  user_signature=False, editable=True, deletable=True, create=True, csv=False,
                        searchable=True, showbuttontext=True,maxtextlengths={'locations.name':150 ,'locations.key_location_place':150 })
    return dict(grid=grid)

#===================================================================================================
@auth.requires_membership("admin")
def membership():
    grid=SQLFORM.grid(db.auth_membership,user_signature=True,editable=True,deletable=True,create=True,csv=False,searchable=False,showbuttontext=True)
    return dict(grid=grid)


@auth.requires_membership("admin")
def users():
    db.auth_user.id.label='م'
    grid=SQLFORM.grid(db.auth_user,user_signature=True,editable=True,deletable=True,create=True,csv=False,searchable=False,showbuttontext=True)
    return dict(grid=grid)

@auth.requires_membership("admin")
def groups():
    grid=SQLFORM.grid(db.auth_group,user_signature=True,editable=True,deletable=True,create=True,csv=False,searchable=False,showbuttontext=True)
    return dict(grid=grid)

def t1():
    return dict()
