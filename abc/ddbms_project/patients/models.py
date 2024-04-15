from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_visit = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()

class LabResult(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    test_date = models.DateField()
    test_result = models.TextField()

class UserRole(models.Model):
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name

class AccessControl(models.Model):
    user_name = models.CharField(max_length=100)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
