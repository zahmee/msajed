def admin_index():
    grid = SQLFORM.grid(db.locations_speaker, user_signature=True, editable=True, deletable=True, create=True, csv=True,
                        searchable=True, showbuttontext=True )
    return dict(grid=grid)
