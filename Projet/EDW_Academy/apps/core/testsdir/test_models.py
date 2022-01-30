from django.test import TestCase
from apps.userprofile.models import Userss
from datetime import date


class TestUser(TestCase):
    def setUp(self):
        self.user = Userss.objects.create(first_name='usertestusertestusertestusertestusertest')
        self.user = Userss.objects.create(first_name='a')
        self.user = Userss.objects.create(first_name='Lucas')
        self.user = Userss.objects.create(first_name='blablaFalse', is_coach=False)
        self.user = Userss.objects.create(first_name='blablaTrue', is_coach=True)
        self.user = Userss.objects.create(first_name='schtroumpfFalse', jour=5, mois=6, annee=2010)
        self.user = Userss.objects.create(first_name='schtroumpfTrue', jour=5, mois=6, annee=1999)
        self.user = Userss.objects.create(first_name='schtroumpfRefactor', is_coach=False, jour=17, mois=3, annee=1999)

    def test_first_name_max_length_35(self):
        user = Userss.objects.get(first_name='Lucas')
        # a = user.first_name.__len__()
        longueur_first_name = len(user.first_name)
        self.assertLessEqual(longueur_first_name, 35)

    def test_if_user_is_coach(self):
        user = Userss.objects.get(first_name='blablaTrue')
        # a = user.is_coach
        self.assertEqual(user.is_coach, True)

    def test_if_user_is_major(self):
        user = Userss.objects.get(first_name='schtroumpfRefactor')
        # a = user.jour
        # b = user.mois
        # c = user.annee
        # d = calculateAge(a, b, c)
        birthday = user.jour
        birthmonth = user.mois
        birthyear = user.annee
        age = calculateAge(birthday, birthmonth, birthyear)
        self.assertGreaterEqual(age, 18)

    def test_if_user_username_exists(self):
        b = Userss._meta.get_field('username').null
        self.assertEquals(b, False)


def calculateAge(jour, mois, annee):
    today = date.today()
    age = today.year - annee
    if today.month < mois:
        age -= 1
    elif today.month == mois:
        if today.day < jour:
            age -= 1

    return age
