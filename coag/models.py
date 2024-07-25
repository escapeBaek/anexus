from django.db import models

# Create your models here.
class Coag(models.Model):
    drugName = models.CharField(max_length=100, default='default')
    
    nx_hold_b_p = models.TextField(default='default')
    nx_restart_a_p = models.TextField(default='default')
    nx_hold_b_c = models.TextField(default='default')
    nx_restart_a_c = models.TextField(default='default')
    
    db_hold_b_p = models.TextField(default='default')
    db_restart_a_p = models.TextField(default='default')
    db_hold_b_c = models.TextField(default='default')
    db_restart_a_c = models.TextField(default='default')
    
    sp_hold_b_p = models.TextField(default='default')
    sp_restart_a_p = models.TextField(default='default')
    sp_hold_b_c = models.TextField(default='default')
    sp_restart_a_c = models.TextField(default='default')
    
    ap_hold_b_p = models.TextField(default='default')
    ap_restart_a_p = models.TextField(default='default')
    ap_hold_b_c = models.TextField(default='default')
    ap_restart_a_c = models.TextField(default='default')
    
    