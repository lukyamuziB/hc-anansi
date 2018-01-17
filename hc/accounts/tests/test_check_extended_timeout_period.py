from hc.api.models import Check
from hc.test import BaseTestCase


class UpdateTimeoutTestCase(BaseTestCase):
    """ tests grace and check periods can be set to more than a month"""
    def setUp(self):
        super(UpdateTimeoutTestCase, self).setUp()
        self.check = Check(user=self.alice)
        self.check.save()

    def test_it_works(self):
        """ test that the new extended timeouts actually resgister"""

        url = "/checks/%s/timeout/" % self.check.code
        payload = {"timeout": 5184000, "grace": 5184000}

        self.client.login(username="alice@example.org", password="password")
        r = self.client.post(url, data=payload)
        self.assertRedirects(r, "/checks/")

        check = Check.objects.get(code=self.check.code)
        assert check.timeout.total_seconds() == 5184000
        assert check.grace.total_seconds() == 5184000
