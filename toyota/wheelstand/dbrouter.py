class CMSRouter(object):

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        db_list = ('default', 'replica')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None


class FormRouter(object):
    def db_for_write(self, model, **hints):
        return None    

    def db_for_read(self, model, **hints):
        if model == TestDrive:
            return 'formdataremote'
        return None