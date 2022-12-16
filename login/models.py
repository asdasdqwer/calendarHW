from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class School(models.Model):
    schoolName = models.CharField(max_length=50)

    def __str__(self):
        return str(self.schoolName)

class Grade(models.Model):
    grade = models.SmallIntegerField()

    def __str__(self):
        return str(self.grade)

    def __int__(self):
        return int(self.grade)

class SubjectClass(models.Model):
    subjectClassName = models.CharField(max_length=50)

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="subjectClass_school",
    )

    grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE,
        related_name="subjectClass_grade"
    )

    def __str__(self):
        return str(self.subjectClassName)

class Subject(models.Model):
    subjectName = models.CharField(max_length=50)

    subjectClass = models.ForeignKey(
        SubjectClass,
        on_delete = models.CASCADE,
        related_name="subject_subjectClass",
    )

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="subject_school",
    )

    gradeList = models.CharField(max_length=100, blank=True, null=True)

    grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE,
        related_name="subject_grade"
    )

    def __str__(self):
        return str(self.subjectName)

class Course(models.Model):
    courseName = models.CharField(max_length=10)
    teacher = models.CharField(max_length=40, blank=True, null=True)


    subjectName = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    user = models.ManyToManyField(
        User,
        blank=True,
        related_name="courses"
    )

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="course_school",
    )

    grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE,
        related_name="course_grade",
    )

    def __str__(self):
        return "".join((self.courseName, " (", self.teacher, ")"))

    def __unicode__(self):
        return "".join((self.courseName, " (", self.teacher, ")"))


class Task(models.Model):
    TASK_TITLE_CHOICES = [
        ('HA', 'Hausaufgabe'),
        ('TS', 'Test'),
        ('KL', 'Klausur (ohne Test)'),
        ('KT', 'Klausur (mit Test)')
    ]
    taskTitle = models.CharField(max_length=100)
    finishDate = models.DateField()
    taskDescription = models.TextField()
    taskType = models.CharField(
        max_length=50,
        choices=TASK_TITLE_CHOICES
    )
        
    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name="user"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="courses"
    )


    def __str__(self):
        return self.taskTitle

class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_user",
        blank=True, null=True
    )

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="student_school",
    )

    grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE,
        related_name="student_grade",
    )

    darkModeEnabled = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.user.username


class CheckBox(models.Model):
    checked = models.BooleanField()
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="checkbox_user"
    )
    
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="checkbox_task"
    )
    
    def __int__(self):
        return int(self.checked)
    
    def __str__(self):
        return str(int(self.checked))