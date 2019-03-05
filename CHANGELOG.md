# Changelog

## 0.2.1 - 2019-03-05

* Added `show_filters` option to pagination

## 0.2.0 - 2019-03-05

* Refactored to simplify new filters
* Added new filters
    * `__between`
    * `__not_between`
    * `__in`
    * `__not_in`
* Added order_by column `ordering=field` or `ordering=-field`

## 0.1.1 - 2019-03-05

* Improved backward compatibility
* Version up and renamed methods to avoid masonite-api colisions

## 0.0.8 - 2019-03-05

* Allow filtering

## 0.0.7 - 2019-03-05

* Basic pagination
* Allow custom queries with the `self.paginate(query)`
* Count total rows
* Allow set `_per_page` rows