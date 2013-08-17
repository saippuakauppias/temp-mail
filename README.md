temp-mail
=========

Wrapper for online service which provides temporary email address: https://temp-mail.ru/

Requirements
------------

Required: [requests] =>1.2 and <1.3.

Installation
------------

Installing is simple with pip:

    $ pip install temp-mail

Usage
-----

Get all emails from given email login and domain:

    from tempmail import TempMail

    tm = TempMail(email='denis', domain='@gnail.pw')
    print tm.get_mailbox()  # list of emails in denis@gnail.pw

Generate email address and get emails from it:

    from tempmail import TempMail

    tm = TempMail()
    email = tm.get_email_address()  # v5gwnrnk7f@gnail.pw
    print tm.get_mailbox(email)  # list of emails

[requests]: https://crate.io/packages/requests/
