# from hc.test import BaseTestCase
# from hc.front.models import Blog_post, Category
# from django.shortcuts import reverse


# class BlogTest(BaseTestCase):
#     def setUp(self):
#         self.client.login(username="alice@example.org", password="password")

#         self.test_category = Category.objects.create(
#             name='Tech Category'
#         )
#         self.test_post = Blog_post.objects.create(
#             title='Python Blog',
#             content='This is a blog on python.',
#             category=self.test_category
#         )

#     def test_landing_page_returns_all_posts(self):
#         response = self.client.get(reverse('hc-blog'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'front/blog_posts.html')
    
#     def test_view_one_blog(self):
#         response = self.client.get(reverse('hc-read_blog'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'front/read_blog.html')
        
#     def test_create_blog(self):
#         response = self.client.get(reverse('hc-create_blog'))        
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'front/create_blog.html')
#         form = {
#             'title':'Html Blog',
#             'content':'This is a blog on html.',
#             'category':self.test_category
#         }
#         response_one = self.client.post(reverse('hc-create_blog'), form)
#         self.assertEqual(response_one.status_code, 200)