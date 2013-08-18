temp-mail
=========

Python API Wrapper for `temp-mail.ru <http://temp-mail.ru/>`_ service. This service provide temporary email address.

Requirements
------------

`requests <https://crate.io/packages/requests/>`_- required.

`simplejson <https://crate.io/packages/simplejson/>`_ - not required, but useful for a serious speed boost in JSON decode.

Installation
------------

Installing is simple with pip::

    $ pip install temp-mail

Usage
-----

Get all emails from given email login and domain::

    from tempmail import TempMail

    tm = TempMail(login='denis', domain='@gnail.pw')
    print tm.get_mailbox()  # list of emails in denis@gnail.pw

Generate email address and get emails from it::

    from tempmail import TempMail

    tm = TempMail()
    email = tm.get_email_address()  # v5gwnrnk7f@gnail.pw
    print tm.get_mailbox(email)  # list of emails
