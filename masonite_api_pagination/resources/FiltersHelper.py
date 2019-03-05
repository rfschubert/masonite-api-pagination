class FiltersHelper:
    filters = {
        "gt": ">",
        "gte": ">=",
        "lt": "<",
        "lte": "<=",
        "not": "!=",
        "contains": "like",
        "not_contains": "not like",
        "starts_with": "like",
        "not_starts_with": "not like",
        "ends_with": "like",
        "not_ends_with": "not like",
        "between": "between",
        "not_between": "not_between",
        "in": "in",
        "not_in": "not_in",
    }

    def mount(self, input, param, model, ordering=False):

        field = input.split('__')[0]
        try:
            ini_filter = input.split('__')[1]
        except:
            ini_filter = None

        if ini_filter is not None:
            filter = self.filters[ini_filter]
        else:
            filter = None

        if filter is not None and "like" in filter:
            param = self.mount_like(ini_filter, param)
        else:
            param = "{}".format(param) if isinstance(param, str) else param

        if filter == 'between':
            model = model.where_between(field, self.param_to_array(param))
        elif filter == 'not_between':
            model = model.where_not_between(field, self.param_to_array(param))
        elif filter == 'in':
            model = model.where_in(field, self.param_to_array(param))
        elif filter == 'not_in':
            model = model.where_not_in(field, self.param_to_array(param))
        elif filter is not None:
            model = model.where(field, filter, param)
        else:
            model = model.where(field, param)

        if ordering is not False:
            if ordering[:1] == '-':
                order_by_field = ordering[1:]
                direction = "DESC"
            else:
                order_by_field = ordering
                direction = "ASC"

            model = model.order_by(order_by_field, direction)

        return model

    def param_to_array(self, param):
        return param.split(',')

    def mount_like(self, filter, param):
        like_filters = {
            "contains": "%{}%".format(param),
            "not_contains": "%{}%".format(param),
            "starts_with": "{}%".format(param),
            "not_starts_with": "{}%".format(param),
            "ends_with": "%{}".format(param),
            "not_ends_with": "%{}".format(param),
        }

        return like_filters[filter]

    def get_allowed_filters(self):
        allowed_filters = []
        for key in self.filters:
            allowed_filters.append(key)

        return allowed_filters
