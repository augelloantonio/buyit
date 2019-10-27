from django.test import TestCase
from .forms import ReviewForm


class Test_Add_Valid_Review(TestCase):
    '''Test add review form'''

    def test_to_add_valid_review(self):
        form = ReviewForm({
            'review_summary': 'test review',
            'rating': '4',
            'comment': 'test comment'
        })
        # check the add form form is valid
        self.assertTrue(form.is_valid())
