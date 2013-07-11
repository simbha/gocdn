#encoding: utf-8
import re
import random
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

TR_DICT = {u'ç':'c', u'Ç':'C',
           u'ğ':'g', u'Ğ':'G',
           u'ı':'i', u'İ':'I',
           u'ö':'o', u'Ö':'O',
           u'ş':'s', u'Ş':'S',
           u'ü':'u', u'Ü':'U'}

SLUG_REMOVE_PAT = re.compile(r'[^\w\s]', re.MULTILINE)
class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self




def create_activation_code(length):

    alphabet = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'
    ustring = ''
    for x in random.sample(alphabet, random.randint(length-2, length-2)):
        ustring += x
    return "G%sM"%ustring

def email_embed_image(email, img_content_id, img_data):
    """
    email is a django.core.mail.EmailMessage object
    """
    img = MIMEImage(img_data, 'jpg')
    img.add_header('Content-ID', '<%s>' % img_content_id)
    img.add_header('Content-Disposition', 'inline')
    email.attach(img)
    return email


def create_cdn_code(length):

    alphabet = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'
    ustring = ''
    for x in random.sample(alphabet, random.randint(length-2, length-2)):
        ustring += x
    return "CDN%s"%ustring


# -*- coding: utf-8 -*-

import re



TR_DICT = {u'ç':'c', u'Ç':'C',
           u'ğ':'g', u'Ğ':'G',
           u'ı':'i', u'İ':'I',
           u'ö':'o', u'Ö':'O',
           u'ş':'s', u'Ş':'S',
           u'ü':'u', u'Ü':'U'}


SLUG_REMOVE_PAT = re.compile(r'[^\w\s]', re.MULTILINE)


def slugify(s, replace_dict = TR_DICT, length = 200):
    if not isinstance(s, unicode):
        s = unicode(s, 'utf-8')

    if len(s):
        s = s.strip()
        if replace_dict:
            for char in replace_dict:
                try:
                    s = s.replace(char, replace_dict[char])
                except:
                    s = s.replace(char, replace_dict[char].encode('utf-8'))
        s = s.lower()
        s = s.replace(' ', '-')
        s = s.replace('\n', '-')
        s = s.replace('\r', '-')
        s = SLUG_REMOVE_PAT.sub('-', s)

        while '--' in s:
            s = s.replace('--', '-')

        if s and s[0] == '-':
            s = s[1:]
        if s and s[len(s)-1] == '-':
            s = s[:-1]

        if length:
            s = s[:length]

        if len(s) == 0:
            s = '-'

    return s.encode('utf-8')


def money_format(amount):
    from django.utils.numberformat import format
    amount = "%.2f" % amount
    return format(amount, ",", 2, 3, ".")