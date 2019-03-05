import json
import math

from api.resources import Resource

from masonite_api_pagination.resources.FiltersHelper import FiltersHelper


class PaginatedResource(Resource):

    def index(self):
        return self.paginate(query=None)

    def package_filter(self, query=None):
        if query is None:
            model = self.model
        else:
            model = query

        ordering = self.request.input('ordering')

        for key in self.request.request_variables:
            if key != 'page' and key != 'ordering' and key != 'show_filters':
                model = FiltersHelper().mount(key, self.request.request_variables[key], model, ordering)

        return model

    def paginate(self, query=None):

        if query is None:
            query = self.model

        query = self.package_filter(query)

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

        response_format = {
            "count": total_rows_count,
            "previous": previous,
            "next": next,
            "results": json.loads(results.to_json())
        }

        filters = self.request.input('show_filters')
        if filters is not False:
            response_format['filters'] = FiltersHelper().get_allowed_filters()

        return response_format
