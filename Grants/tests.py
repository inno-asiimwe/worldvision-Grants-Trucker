from django.test import TestCase
from .models import *
import datetime
from django.utils import timezone

# Create your tests here.
class ProjectMethodsTest(TestCase):
    """A class to test all methods partaining to the project model"""

    def test_get_status_with_ongoing_project(self):
        """testing get_status() returns Open for an ongoing project"""
        start = timezone.now() - datetime.timedelta(days = 365)
        end = timezone.now() + datetime.timedelta(days = 365)
        project = Project(start_date = start, end_date = end)
        self.assertIs(project.get_status(), 'Open')

    def test_get_status_with_past_project(self):
        """testing get_status returns Closed for past projects"""
        start = timezone.now() - datetime.timedelta(days = 3)
        end = timezone.now() - datetime.timedelta(days = 1)
        project = Project(start_date = start, end_date = end)
        self.assertEqual(project.get_status(), 'Closed')

    def test_get_status_with_future_project(self):
        """testing returns upcoming for future project"""
        start = timezone.now() + datetime.timedelta(days = 30)
        end = timezone.now() + datetime.timedelta(days = 365)
        project = Project(start_date = start, end_date = end)
        self.assertEqual(project.get_status(), 'Upcoming')

    def test_get_donor_and_donor_name_success(self):
        """get_donor should return the correct Donor object for a Project object"""
        support_office = SupportOffice(name = 'Head Office', location = "Kampala")
        support_office.save()
        start = timezone.now() - datetime.timedelta(days = 365)
        end = timezone.now() + datetime.timedelta(days = 365)
        project = Project(project_name = 'project1', start_date = start, end_date = end, grant_amount = 8000, support_office = support_office )
        project.save()
        donor = Donor(name = 'donor1', project = project)
        donor.save()
        self.assertQuerysetEqual(project.get_donor(), ['<Donor: donor1>',] )
        self.assertEqual(project.donor_name, ['donor1'])
