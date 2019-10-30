from django.test import TestCase
from .models import Review
from django.contrib.auth.models import User
from products.models import Product


class Test_Review_model(TestCase):
    '''Test Review Model'''

    def test_review_model(self):
        # Create review
        user = User.objects.create(username='tester')
        product = Product.objects.create(name='test product', price='2')
        review = Review(
            rating=4,
            review_summary='testing summary',
            pub_date='2019-10-21 19:47:27.674081',
            comment='test comment'
        )

        # check the add form form is valid
        review.product_id = product.id
        review.user_id = user.id
        # Save review
        review.save()
        # check to see that the review summary equal the saved review value
        self.assertEqual(review.review_summary, "testing summary")
        self.assertEqual(review.rating, 4)
        self.assertEqual(review.pub_date, "2019-10-21 19:47:27.674081")
        self.assertEqual(review.comment, "test comment")
        self.assertEqual(review.user_id, 1)
        self.assertEqual(review.product_id, 1)

        ''' Test review as string'''
        self.assertEqual('testing summary', str(review))
