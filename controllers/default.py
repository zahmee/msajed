# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():

    return dict(form=auth())

def index_1():
    return dict()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    if request.args(0)=='profile':
        db.auth_user.key_spe.writable=False
        db.auth_user.tch_count.writable=False
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


def start():
    return dict()

def speaker():
    if (session.login == 0) :
        form = FORM()
        session.login = 1
        return dict(mess="الدخول غير صحيح")
    else:
        form = FORM()
        return dict(mess="")

def getusr():
    #try :
        sss= ""
        if ( request.vars.sp_id  ) and  ( request.vars.sp_ps   )  :
            q = db(db.msajed_users.user_id == str(request.vars.sp_id) ).select().first()
            if q :
                usr = q.user_id
                pwd =''
                sss='0'
                if (q.usr_password) :
                    sss="1"
                    pwd = str(q.usr_password)
                else :
                    sss="2"
                    pwd = str(q.mobil)
                if (pwd==request.vars.sp_ps) :
                    sss="3"
                    session.login = 9
                    session.usr = q.id
                    if db.msajed_users[session.usr].is_speaker :
                        redirect(URL('getusr2'))
                    elif  db.msajed_users[session.usr].is_emam :
                        redirect(URL('emam'))
                    else:
                        redirect(URL('speaker'))
                else:
                    sss="4"
                    session.login = 0
                    redirect(URL('speaker'))
            else:
                session.login = 0
                redirect(URL('speaker'))
        else:
            redirect(URL('speaker'))
    #except Exception as e:
    #    return ( str(e) +"<br/>"+request.vars.sp_id +'<br/>'+ request.vars.sp_ps+"<br/>" + sss)


def usrout():
    session.login = 1
    redirect(URL('speaker'))


def add():
    if ((session.login != 9) ) :
        redirect(URL('speaker'))
    return dict()


def add_spk():
    #try:
        if ( request.vars.sel1 ) and ( request.vars.inp1 ) and ( request.vars.inp2 ) and ( request.vars.inp3 ):
            nr = db.locations_speaker.insert( days = request.vars.inp2  , locations = request.vars.sel1 , msajed_users =session.usr ,
             locations_dis = str(request.vars.inp3) , speaker_dis =  str(request.vars.inp1) )
            if (nr>0):
                redirect(URL('getusr2'))
            else :
                redirect(URL('error'))
        else :
            redirect(URL('getusr2'))
    #except :
    #    return ( str(request.vars.inp2)  +'-'+ str(request.vars.sel1) +'-'+ str(session.usr) +'-'+ str(request.vars.inp1) +'-'+ str(request.vars.inp3))
        #redirect(URL('error'))

def error():
    return dict()

def getusr2():
    if ((session.login != 9) ) :
        redirect(URL('speaker'))
    return dict()


def delk():
    try:
        ids = request.args(0)
        tb_z = db.locations_speaker[ids]
        if (tb_z.msajed_users == session.usr ):
            db(db.locations_speaker.id==ids).delete()
            db.commit()
            return "1"
        else:
            return "0"
    except Exception, e:
        db.rollback()
        return "2"

def emam():
    return dict()

def spk_chk():
    try: 
        ids = request.args(0)
        tb_z = db.locations_speaker[ids]
        if tb_z.is_chick == True :
            tb_z.is_chick = False
        else:
            tb_z.is_chick = True
        tb_z.update_record()
        db.commit()
        redirect(URL('emam'))
    except Exception, e:
        db.rollback()
        redirect(URL('emam'))

def chg_pass():
    q = db.msajed_users[session.usr]
    db.msajed_users.id.writable=False
    db.msajed_users.user_degree.writable=False
    db.msajed_users.is_speaker.writable=False
    db.msajed_users.is_emam.writable=False
    db.msajed_users.emam_location.writable=False
    db.msajed_users.is_open.writable=False

    db.msajed_users.id.readable=False
    db.msajed_users.user_degree.readable=False
    db.msajed_users.is_speaker.readable=False
    db.msajed_users.is_emam.readable=False
    db.msajed_users.emam_location.readable=False
    db.msajed_users.is_open.readable=False
    form = SQLFORM(db.msajed_users, q ).process()
    return dict(form=form)
