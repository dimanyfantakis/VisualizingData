# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Countries(models.Model):
    c_id = models.SmallIntegerField(db_column='C_ID', primary_key=True)  # Field name made lowercase.
    c_name = models.CharField(db_column='C_Name', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'countries'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Years(models.Model):
    y_id = models.IntegerField(db_column='Y_ID', primary_key=True)  # Field name made lowercase.
    year = models.TextField(db_column='Year', unique=True)  # Field name made lowercase. This field type is a guess.
    lustrum = models.IntegerField(db_column='Lustrum')  # Field name made lowercase.
    decade = models.IntegerField(db_column='Decade')  # Field name made lowercase.
    vicennial = models.IntegerField(db_column='Vicennial')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'years'


class Measurements(models.Model):
    countries_c = models.ForeignKey(Countries, models.DO_NOTHING, db_column='Countries_C_ID')
    years_y = models.ForeignKey(Years, models.DO_NOTHING, db_column='Years_Y_ID')
    civil_liberties = models.DecimalField(db_column='Civil_Liberties', max_digits=6, decimal_places=3)
    democracy = models.DecimalField(db_column='Democracy', max_digits=6, decimal_places=3)
    direct_democracy = models.DecimalField(db_column='Direct_Democracy', max_digits=6, decimal_places=3)
    electoral_participation = models.DecimalField(db_column='Electoral_Participation', max_digits=6, decimal_places=3)
    freedom_of_expression = models.DecimalField(db_column='Freedom_Of_Expression', max_digits=6, decimal_places=3)
    freedom_of_movement = models.DecimalField(db_column='Freedom_Of_Movement', max_digits=6, decimal_places=3)
    freedom_of_religion = models.DecimalField(db_column='Freedom_Of_Religion', max_digits=6, decimal_places=3)
    free_political_parties = models.DecimalField(db_column='Free_Political_Parties', max_digits=6, decimal_places=3)
    fundamental_rights = models.DecimalField(db_column='Fundamental_Rights', max_digits=6, decimal_places=3)
    gender_equality = models.DecimalField(db_column='Gender_Equality', max_digits=6, decimal_places=3)
    gini_index = models.DecimalField(db_column='Gini_Index', max_digits=5, decimal_places=2)
    hapiscore = models.DecimalField(db_column='Hapiscore', max_digits=6, decimal_places=3)
    human_development = models.DecimalField(db_column='Human_Development', max_digits=6, decimal_places=3)
    local_democracy = models.DecimalField(db_column='Local_Democracy', max_digits=6, decimal_places=3)
    social_group = models.DecimalField(db_column='Social_Group', max_digits=6, decimal_places=3)
    social_rights_and_equality = models.DecimalField(db_column='Social_Rights_And_Equality', max_digits=6, decimal_places=3)
    urban_population = models.IntegerField(db_column='Urban_Population')
    measurementscol = models.CharField(db_column='Measurementscol', max_length=45)

    class Meta:
        managed = False
        db_table = 'measurements'

