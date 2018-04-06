from django.db import models

from jobs.models import Job
from candidates.models import SavedCandidate


class Group(models.Model):
    name = models.CharField(max_length=150)
    parent_group = models.ForeignKey('Group', null=True, blank=True, on_delete=models.CASCADE)
    jobs = models.ManyToManyField(Job, related_name='job_groups')
    saved_candidates = models.ManyToManyField(SavedCandidate, related_name='candidate_groups')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
