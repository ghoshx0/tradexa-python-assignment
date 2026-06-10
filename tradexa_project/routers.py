class ProductRouter:

    route_app_labels = {'products'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'products_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'products_db'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == 'products':
            return db == 'products_db'

        return db == 'default'