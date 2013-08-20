import string
import random
from hashlib import md5

import requests


class TempMail(object):
    """
    API Wrapper for service which provides temporary email address.

    :param login: (optional) login for email address.
    :param domain: (optional) domain (from current available)
    for email address.
    :param api_domain: (optional) domain for temp-mail api.
    Default value is ``api.temp-mail.ru``.
    """

    def __init__(self, login=None, domain=None, api_domain='api.temp-mail.ru'):
        self.login = login
        self.domain = domain
        self.api_domain = api_domain

    def __repr__(self):
        return u'<TempMail [{0}]>'.format(self.get_email_address())

    @property
    def available_domains(self):
        """
        Return list of available domains for use in email address.
        """
        if not hasattr(self, '_available_domains'):
            url = 'http://{0}/request/domains/format/json/'.format(
                self.api_domain)
            req = requests.get(url)
            domains = req.json()
            setattr(self, '_available_domains', domains)
        return self._available_domains

    def generate_login(self, min_length=6, max_length=10, digits=True):
        """
        Generate string for email address login with defined length and
        alphabet.

        :param min_length: (optional) min login length.
        Default value is ``6``.
        :param max_length: (optional) max login length.
        Default value is ``10``.
        :param digits: (optional) use digits in login generation.
        Default value is ``True``.
        """
        chars = string.ascii_lowercase
        if digits:
            chars += string.digits
        length = random.randint(min_length, max_length)
        return ''.join(random.choice(chars) for x in range(length))

    def get_email_address(self):
        """
        Return full email address from login and domain from params in class
        initialization or generate new.
        """
        if self.login is None:
            self.login = self.generate_login()

        available_domains = self.available_domains
        if self.domain is None:
            self.domain = random.choice(available_domains)
        elif self.domain not in available_domains:
            raise ValueError('Domain not found in available domains!')
        return u'{0}{1}'.format(self.login, self.domain)

    def get_hash(self, email):
        """
        Return md5 hash for given email address.

        :param email: email address for generate md5 hash.
        """
        return md5(email).hexdigest()

    def get_mailbox(self, email=None, email_hash=None):
        """
        Return list of emails in given email address
        or dict with `error` key if mail box is empty.

        :param email: (optional) email address.
        :param email_hash: (optional) md5 hash from email address.
        """
        if email is None:
            email = self.get_email_address()
        if email_hash is None:
            email_hash = self.get_hash(email)

        url = 'http://{0}/request/mail/id/{1}/format/json/'.format(
            self.api_domain, email_hash)
        req = requests.get(url)
        return req.json()
