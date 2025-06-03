from django.test import TestCase
from django.template.defaultfilters import slugify

from posts.models import BlogPost


class BlogPostSlugTest(TestCase):
    def test_slug_generated_on_save(self):
        """Saving a BlogPost without slug should populate slug from title."""
        title = "Un titre de test"
        post = BlogPost(title=title)
        post.save()
        self.assertEqual(post.slug, slugify(title))
# Définir ici les tests de l'application posts.
