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
    }

    def mount(self, input, param):
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

        return field, filter, param

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
