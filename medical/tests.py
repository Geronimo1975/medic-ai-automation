from django.test import TestCase


class PatientModelTest(TestCase):
    def test_patient_creation(self):
        patient = Patient.objects.create(nume="Ion", prenume="Popescu", varsta=30, diagnostic="Gripa")
        self.assertEqual(patient.nume, "Ion")
        self.assertEqual(patient.diagnostic, "Gripa")
