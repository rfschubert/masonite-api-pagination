from unittest import TestCase

from masonite_api_pagination.resources.FiltersHelper import FiltersHelper


class FiltersTestCase(TestCase):

    def setUp(self):
        self.helper = FiltersHelper()

    def test_field__gt(self):
        self.assertEqual(
            ('field', '>', 10),
            self.helper.mount("field__gt", 10)
        )

    def test_field__gte(self):
        self.assertEqual(
            ('field', '>=', 10),
            self.helper.mount("field__gte", 10)
        )

    def test_field__lt(self):
        self.assertEqual(
            ('field', '<', 10),
            self.helper.mount("field__lt", 10)
        )

    def test_field__lte(self):
        self.assertEqual(
            ('field', '<=', 10),
            self.helper.mount("field__lte", 10)
        )

    def test_field__contains(self):
        self.assertEqual(
            ('field', 'like', '%abc%'),
            self.helper.mount("field__contains", "abc")
        )

    def test_field__not_contains(self):
        self.assertEqual(
            ('field', 'not like', '%abc%'),
            self.helper.mount("field__not_contains", "abc")
        )

    def test_field(self):
        self.assertEqual(
            ('field', None, 'abc'),
            self.helper.mount("field", "abc")
        )

    def test_field__not(self):
        self.assertEqual(
            ('field', '!=', 'abc'),
            self.helper.mount("field__not", "abc")
        )

    def test_field__starts_with(self):
        self.assertEqual(
            ('field', 'like', 'abc%'),
            self.helper.mount("field__starts_with", "abc")
        )

    def test_field__ends_with(self):
        self.assertEqual(
            ('field', 'like', '%abc'),
            self.helper.mount("field__ends_with", "abc")
        )

    def test_field__not_starts_with(self):
        self.assertEqual(
            ('field', 'not like', 'abc%'),
            self.helper.mount("field__not_starts_with", "abc")
        )

    def test_field__not_ends_with(self):
        self.assertEqual(
            ('field', 'not like', '%abc'),
            self.helper.mount("field__not_ends_with", "abc")
        )
