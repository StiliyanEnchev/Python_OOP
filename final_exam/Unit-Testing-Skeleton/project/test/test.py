from unittest import TestCase, main
from project.social_media import SocialMedia

class TestSocialMedia(TestCase):

    def setUp(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']



    def test_if_platform_raises_value_error(self):
        fb = SocialMedia('Mario',
                              'FB',
                              10,
                              'Posts')

        self.assertEqual(fb, "Platform should be one of 'Instagram', 'YouTube', 'Twitter'")
        self.assertEqual(fb._platform, None)
    def test_correct_init(self):
        self.assertEqual(self.twitter._username, 'Petar')
        self.assertEqual(self.twitter.platform, 'Twitter')
        self.assertEqual(self.twitter.followers, 10)
        self.assertEqual(self.twitter._content_type, 'Photos')

    def test_wrong_platform_raises_value_error_and_returns_correct_message(self):

        with self.assertRaises(ValueError) as ve:
            self.twitter._platform = 'DB'

        self.assertEqual("Platform should be one of 'Instagram', 'YouTube', 'Twitter'",
                         str(ve.exception))

    def test_followers_below_zero(self):
        self.twitter._followers = 0
        self.assertEqual(self.twitter._followers, "Followers cannot be negative.")

    def test_if_new_post_is_created_returned_properly_and_appended(self):

        self.assertEqual(len(self.twitter._posts), 0)

        expected_result = f"New Photos post created by Petar on Twitter"
        self.assertEqual(self.twitter.create_post('Here is my new picture')
, expected_result)

        self.assertEqual(len(self.twitter._posts), 1)

        post = self.twitter._posts[0]
        self.assertEqual(post, {'content': 'Photos', 'likes': 0, 'comments': []})


    def test_if_invalid_index_returns_crrect_message(self):
        result = self.twitter.like_post(5)
        self.assertEqual(result, "Invalid post index.")

    def test_when_valid_index_if_post_gest_a_like_if_on_maximum_likes(self):
        self.twitter.create_post('Here is it')
        self.twitter._posts[0]['likes'] = 10
        result = self.twitter.like_post(0)
        self.assertEqual(result, "Post has reached the maximum number of likes.")

    def test_when_indx_is_valid_and_not_on_max_likes(self):
        self.twitter.create_post('Here is it')
        self.twitter._posts[0]['likes'] = 9
        result = self.twitter.like_post(0)
        self.assertEqual(result, "Post liked by Petar.")

    def test_if_comment_is_less_than_needed_characters_correct_return(self):
        self.twitter.create_post('Here is it')
        result = self.twitter.comment_on_post(0, 'small')

        self.assertEqual(result, "Comment should be more than 10 characters.")

    def test_if_comment_is_correctly_returned_and_added_when_more_than_neeeded_characters(self):
        self.twitter.create_post('Here is it')
        self.assertEqual(self.twitter.comment_on_post(0, 'it is enought'), "Comment added by Petar on the post.")
        self.assertEqual(self.twitter._posts[0]['comments'], 'Here is it')

    def test_followers_validation(self):

        with self.assertRaises(ValueError):
            self.twitter.followers = -100

    def test_Validate_and_set_platform(self):
        with self.assertRaises(ValueError):
            self.twitter._validate_and_set_platform('Facebook')


    def test_like_post_max_likes(self):
        post_content = "Test post"
        self.twitter.create_post(post_content)
        for _ in range(10):
            self.twitter.like_post(0)
        result = self.twitter.like_post(0)
        self.assertEqual(result, "Post has reached the maximum number of likes.")


if __name__ == "__main__":
    main()