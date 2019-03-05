import json
import math

from api.resources import Resource

from masonite_api_pagination.resources.FiltersHelper import FiltersHelper


class PaginatedResource(Resource):

    def index(self):
        return self.filter(query=None)

    def filter(self, query=None):
        if query is None
            model = self.model
        else:
            model = query

        for key in self.request.request_variables:
            if key != 'page':
                res = FiltersHelper().mount(key, self.request.request_variables[key])
                if res[1] is not None:
                    model = model.where(res[0], res[1], res[2])
                else:
                    model = model.where(res[0], res[2])

        return self.paginate(model)

    def paginate(self, query=None):
        if query is None:
            query = self.model

        max_rows = self.model._per_page
        current_page = None if self.request.input('page') is False else self.request.input('page')
        results = query.paginate(max_rows, 1 if current_page is None else current_page)
        total_rows_count = results.total
        max_pages = math.ceil(total_rows_count / max_rows)
        previous = None
        next = None

        if current_page is not None:
            if current_page > 1:
                if (current_page - 1) > max_pages:
                    current_page = max_pages

                previous = "{}?page={}".format(self.route_url, current_page - 1)
        else:
            current_page = 1

        if math.ceil(total_rows_count / max_rows) > current_page:
            next = "{}?page={}".format(self.route_url, current_page + 1)

        return {
            "count": total_rows_count,
            "previous": previous,
            "next": next,
            "results": json.loads(results.to_json())
        }
