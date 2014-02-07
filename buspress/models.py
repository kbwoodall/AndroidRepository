from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField, USStateField
import datetime

class AccountingFirm(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_cpa = models.IntegerField()
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    headquarters_state = USStateField(blank=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    specialties = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Accounting & Tax Preparation Firm'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(AccountingFirm, self).save(force_insert, force_update)

class AdvertisingAgency(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    percent_print = models.IntegerField(blank=True, null=True)
    percent_broadcast = models.IntegerField(blank=True, null=True)
    percent_new_media = models.IntegerField(blank=True, null=True)
    percent_direct_mail = models.IntegerField(blank=True, null=True)
    specialty_area = models.TextField(blank=True)
    selected_accounts = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Advertising Agency'
        verbose_name_plural = 'Advertising Agencies'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(AdvertisingAgency, self).save(force_insert, force_update)

class AlternativeEnergy(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_subscribers = models.IntegerField()
    headquarters_state = USStateField(blank=True)
    cities = models.TextField(blank=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Alternative Energy Provider'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(AlternativeEnergy, self).save(force_insert, force_update)

class AutomotiveDealer(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_employees = models.IntegerField()
    sales_gross = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    new_units_sold = models.IntegerField(blank=True, null=True)
    used_units_sold = models.IntegerField(blank=True, null=True)
    nbr_locations = models.IntegerField(blank=True, null=True)
    nbr_sales_people = models.IntegerField(blank=True, null=True)
    specialties = models.TextField(blank=True)
    most_popular_car = models.TextField(blank=True)
#general_manager fields
    general_manager_first_name = models.CharField(max_length=255, blank=True)
    general_manager_last_name = models.CharField(max_length=255, blank=True)
    general_manager_title = models.CharField(max_length=255, blank=True)
#sales_manager fields
    sales_manager_first_name = models.CharField(max_length=255, blank=True)
    sales_manager_last_name = models.CharField(max_length=255, blank=True)
    sales_manager_title = models.CharField(max_length=255, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Automotive Dealer'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(AutomotiveDealer, self).save(force_insert, force_update)

class BankruptcyAttorney(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_attorneys = models.IntegerField()
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    practice_areas = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Bankruptcy Attorney'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(BankruptcyAttorney, self).save(force_insert, force_update)

class BusinessBank(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    portfolio = models.DecimalField(max_digits=14, decimal_places=2)
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    nbr_local_locations = models.IntegerField(blank=True, null=True)
    headquarters_state = USStateField(blank=True)
    CHARTER_CHOICES = (
        ('ST', 'State'),
        ('FED', 'Federal'),
    )
    charter = models.CharField(max_length=3, choices=CHARTER_CHOICES, blank=True)
    nv_assets = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    percent_return_nv_assets = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Business Bank'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(BusinessBank, self).save(force_insert, force_update)

class Casino(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    total_square_footage = models.IntegerField()
    nbr_guest_rooms = models.IntegerField(null=True, blank=True)
    year_est = models.CharField(max_length=4, blank=True)
    keno = models.BooleanField()
    bingo = models.BooleanField()
    table_games = models.BooleanField()
    sports_book = models.BooleanField()
    other_gaming_categories = models.CharField(max_length=255, blank=True)
    nbr_slot_machines = models.IntegerField(blank=True, null=True)
    special_events = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)
    property_owner = models.CharField(max_length=255)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Casino/Resort'
        verbose_name_plural = 'Casinos & Resorts'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(Casino, self).save(force_insert, force_update)

class ChamberOfCommerce(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    chamber_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_members = models.IntegerField()
    nbr_employees = models.IntegerField(blank=True, null=True)
    initial_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    annual_dues = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    services = models.TextField(blank=True)
    publications = models.TextField(blank=True)
#president fields
    president_first_name = models.CharField(max_length=255, blank=True)
    president_last_name = models.CharField(max_length=255, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Chamber of Commerce'
        verbose_name_plural = 'Chambers of Commerce'

    def __unicode__(self):
        return self.chamber_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ChamberOfCommerce, self).save(force_insert, force_update)

class CharitableOrganization(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    organization_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_full_time_employees = models.IntegerField()
    nbr_part_time_employees = models.IntegerField()
    budget = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    mission = models.TextField(blank=True)
    events = models.TextField(blank=True)
#chairperson fields
    chairperson_first_name = models.CharField(max_length=255, blank=True)
    chairperson_last_name = models.CharField(max_length=255, blank=True)
    chairperson_title = models.CharField(max_length=255, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Charitable Organization'

    def __unicode__(self):
        return self.organization_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CharitableOrganization, self).save(force_insert, force_update)

class College(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    school_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_students = models.IntegerField()
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    annual_tuition = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    student_teacher_ratio = models.CharField(max_length=255, blank=True)
    nbr_local_campuses = models.IntegerField(blank=True, null=True)
    programs_offered = models.TextField(blank=True)
    degrees_offered = models.TextField(blank=True)
#admissions fields
    admissions_first_name = models.CharField(max_length=255, blank=True)
    admissions_last_name = models.CharField(max_length=255, blank=True)
    admissions_title = models.CharField(max_length=255, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'College/University'
        verbose_name_plural = 'Colleges & Universities'

    def __unicode__(self):
        return self.school_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(College, self).save(force_insert, force_update)

class CommercialMortgage(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    volume_local_mortgage_loans = models.DecimalField(max_digits=14, decimal_places=2)
    LENDER_CHOICES = (
        ('BROKER', 'Mortgage broker'),
        ('BANKER', 'Mortgage banker'),
        ('LENDER', 'Mortgage lender'),
    )
    lender_type = models.CharField(max_length=6, choices=LENDER_CHOICES, blank=True)
    turnaround_time = models.CharField(max_length=255, blank=True)
    nbr_loans = models.IntegerField(blank=True, null=True)
    nbr_loan_officers = models.IntegerField(blank=True, null=True)
    size_range_loans = models.CharField(max_length=255, blank=True)
    portfolio = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Commercial Mortgage Broker'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CommercialMortgage, self).save(force_insert, force_update)

class CommercialDeveloper(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_employees = models.IntegerField(blank=True, null=True)
    current_projects = models.TextField(blank=True)
    recent_projects = models.TextField(blank=True)
    notable_projects = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Commercial Property Developer'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CommercialDeveloper, self).save(force_insert, force_update)

class CommercialInsurance(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_members = models.IntegerField()
    plan_types = models.TextField(blank=True)
    nbr_providers = models.IntegerField(blank=True, null=True)
    parent_company = models.CharField(max_length=255, blank=True)
    covered_hospitals = models.TextField(blank=True)
    riders = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Commercial Insurance Provider'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CommercialInsurance, self).save(force_insert, force_update)

class CommercialPrinting(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    total_sales = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    services = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Commercial Printing/Graphic Design Company'
        verbose_name_plural = 'Commercial Printing & Graphic Design Companies'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CommercialPrinting, self).save(force_insert, force_update)

class CommercialPropertyManager(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_properties = models.IntegerField()
    total_square_footage = models.IntegerField(blank=True, null=True)
    percent_office = models.IntegerField(blank=True, null=True)
    percent_retail = models.IntegerField(blank=True, null=True)
    percent_industrial = models.IntegerField(blank=True, null=True)
    nbr_leasing_agents = models.IntegerField(blank=True, null=True)
    nbr_brokers = models.IntegerField(blank=True, null=True)
    nbr_property_managers = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Commercial Property Manager'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CommercialPropertyManager, self).save(force_insert, force_update)

class CommercialRealEstate(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    property_total_value = models.DecimalField(max_digits=14, decimal_places=2)
    total_leased = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total_sold = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    brokers = models.IntegerField(blank=True, null=True)
    agents = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Commercial Real Estate Broker'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CommercialRealEstate, self).save(force_insert, force_update)

class CommunityBank(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_branches = models.IntegerField()
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    headquarters_state = USStateField(blank=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Community Bank'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CommunityBank, self).save(force_insert, force_update)

class ComputerService(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    services = models.TextField(blank=True)
    brands = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Computer Service/Repair Company'
        verbose_name_plural = 'Computer Service/Repair Companies'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ComputerService, self).save(force_insert, force_update)

class Concierge(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    services = models.TextField(blank=True)
    rates = models.TextField(blank=True)
    membership_program = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Concierge Service'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(Concierge, self).save(force_insert, force_update)

class ConventionServiceContractor(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    nbr_locations = models.IntegerField(blank=True, null=True)
    headquarters_state = USStateField(blank=True)
    nbr_conventions_serviced = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
#sales fields
    sales_first_name = models.CharField(max_length=255, blank=True)
    sales_last_name = models.CharField(max_length=255, blank=True)
    sales_title = models.CharField(max_length=255, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Convention Service Contractor'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ConventionServiceContractor, self).save(force_insert, force_update)

class ConventionSpace(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    total_space_square_footage = models.IntegerField()
    basic_rates = models.CharField(max_length=255, blank=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Convention & Meeting Space'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ConventionSpace, self).save(force_insert, force_update)

class CreditUnion(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_members = models.IntegerField()
    nbr_potential_members = models.IntegerField(blank=True, null=True)
    membership_eligibility = models.TextField(blank=True)
    nbr_employees = models.IntegerField(blank=True, null=True)
    nbr_branches = models.IntegerField(blank=True, null=True)
    CHARTER_CHOICES = (
        ('ST', 'State'),
        ('FED', 'Federal'),
    )
    charter = models.CharField(max_length=3, choices=CHARTER_CHOICES, blank=True)
    year_chartered = models.CharField(max_length=4, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Credit Union'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CreditUnion, self).save(force_insert, force_update)

class CriminalAttorney(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_attorneys = models.IntegerField()
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    practice_areas = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Criminal Attorney'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CriminalAttorney, self).save(force_insert, force_update)

class DentalCareProvider(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    insurance_types = models.TextField(blank=True)
    services = models.TextField(blank=True)
    parent_company = models.CharField(max_length=255, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Dental Care Provider'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(DentalCareProvider, self).save(force_insert, force_update)

class EnergyCompany(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_subscribers = models.IntegerField()
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Energy/Utility Company'
        verbose_name_plural = 'Energy & Utility Companies'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(EnergyCompany, self).save(force_insert, force_update)

class EngineeringFirm(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_engineers = models.IntegerField()
    nbr_surveyors = models.IntegerField()
    nbr_technicians = models.IntegerField()
    percent_public = models.IntegerField(blank=True, null=True)
    percent_private = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
    current_projects = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Engineering Firm'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(EngineeringFirm, self).save(force_insert, force_update)

class EnvironmentalServices(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_professional_staff = models.IntegerField()
    nbr_employees = models.IntegerField(blank=True, null=True)
    percent_government = models.IntegerField(blank=True, null=True)
    percent_private = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
    current_projects = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Environmental Services Firm'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(EnvironmentalServices, self).save(force_insert, force_update)

class ExecRecruiter(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    industries = models.TextField(blank=True)
    fees = models.TextField(blank=True)
    nbr_local_placements = models.IntegerField(blank=True, null=True)
    job_categories = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Executive Search Firm/Recruiter'
        verbose_name_plural = 'Executive Search Firms & Recruiters'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ExecRecruiter, self).save(force_insert, force_update)

class FemaleBusinessLeader(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=255, blank=True)
    years_with_co = models.IntegerField(blank=True, null=True)
    years_in_industry = models.IntegerField(blank=True, null=True)
    degree = models.TextField(blank=True)
    affiliations = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Female Business Leader'

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(FemaleBusinessLeader, self).save(force_insert, force_update)

class FinancialAdviser(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_advisers = models.IntegerField()
    nbr_planners = models.IntegerField()
    nbr_sales_reps = models.IntegerField(blank=True, null=True)
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_locations = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
    licensed = models.BooleanField()
    fee_only = models.BooleanField()
    broker = models.BooleanField()
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Financial Adviser/Planner'
        verbose_name_plural = 'Financial Advisers & Planners'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(FinancialAdviser, self).save(force_insert, force_update)

class FinancialInstitution(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    local_deposits = models.DecimalField(max_digits=14, decimal_places=2)
    overall_assets = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    earnings = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    roa_roe = models.CharField(max_length=255, blank=True)
    nbr_local_branches = models.IntegerField(blank=True, null=True)
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    nv_assets = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    percent_return_on_nv_assets = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Financial Institution'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(FinancialInstitution, self).save(force_insert, force_update)

class Franchiser(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_units = models.IntegerField()
    business_description = models.TextField(blank=True)
    total_investment = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)
    nbr_local_employees = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Franchiser'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(Franchiser, self).save(force_insert, force_update)

class GraduateProgram(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    school_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_students = models.IntegerField()
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    annual_tuition = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    student_to_teacher_ratio = models.CharField(max_length=255, blank=True)
    nbr_local_schools = models.IntegerField(blank=True, null=True)
    job_placement_percent = models.IntegerField(blank=True, null=True)
    concentrations = models.TextField(blank=True)
    year_est = models.CharField(max_length=4, blank=True)
    headquarters_state = USStateField(blank=True)
#admissions fields
    admissions_first_name = models.CharField(max_length=255, blank=True)
    admissions_last_name = models.CharField(max_length=255, blank=True)
    admissions_title = models.CharField(max_length=255, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'MBA/Graduate Program'
        verbose_name_plural = 'MBA & Graduate Programs'

    def __unicode__(self):
        return self.school_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(GraduateProgram, self).save(force_insert, force_update)

class GreenBuilder(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    percent_private = models.IntegerField(blank=True, null=True)
    percent_county = models.IntegerField(blank=True, null=True)
    percent_state = models.IntegerField(blank=True, null=True)
    percent_federal = models.IntegerField(blank=True, null=True)
    specialties = models.TextField(blank=True)
    leed_projects = models.TextField(blank=True)
    current_projects = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Green Commercial Builder/Architect'
        verbose_name_plural = 'Green Commercial Builders & Architects'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(GreenBuilder, self).save(force_insert, force_update)

class HealthCareProvider(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    caregiver_types = models.TextField(blank=True)
    insurance_types = models.TextField(blank=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Health Care Provider'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(HealthCareProvider, self).save(force_insert, force_update)

class HispanicMedia(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    tv = models.BooleanField()
    radio = models.BooleanField()
    print_media = models.BooleanField()
    online = models.BooleanField()
    other = models.TextField(blank=True)
    products = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Hispanic Media'
        verbose_name_plural = 'Hispanic Media'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(HispanicMedia, self).save(force_insert, force_update)

class ImmigrationAttorney(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_attorneys = models.IntegerField()
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    practice_areas = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Immigration Attorney'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ImmigrationAttorney, self).save(force_insert, force_update)

class IndustrialPark(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    property_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    developer = models.CharField(max_length=255, blank=True)
    year_built = models.CharField(max_length=4, blank=True)
    leasable_area = models.IntegerField()
    percent_leased = models.IntegerField(blank=True, null=True)
    percent_office = models.IntegerField(blank=True, null=True)
    percent_industrial = models.IntegerField(blank=True, null=True)
    major_tenants = models.TextField(blank=True)
#agent fields
    agent_first_name = models.CharField(max_length=255, blank=True)
    agent_last_name = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Industrial Park'

    def __unicode__(self):
        return self.property_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(IndustrialPark, self).save(force_insert, force_update)

class IndustryLeader(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=255, blank=True)
    years_with_co = models.IntegerField(blank=True, null=True)
    years_in_industry = models.IntegerField(blank=True, null=True)
    degree = models.TextField(blank=True)
    affiliations = models.TextField(blank=True)
    hobbies = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Industry Leader'

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(IndustryLeader, self).save(force_insert, force_update)

class InsuranceBroker(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_agents = models.IntegerField()
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    nbr_policies = models.IntegerField(blank=True, null=True)
    insurance_type = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Insurance Broker/Agent'
        verbose_name_plural = 'Insurance Brokers & Agents'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(InsuranceBroker, self).save(force_insert, force_update)

class IntellectualPropertyAttorney(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_attorneys = models.IntegerField()
    nbr_partners = models.IntegerField(blank=True, null=True)
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    practice_areas = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Intellectual Property Attorney'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(IntellectualPropertyAttorney, self).save(force_insert, force_update)

class LargestEmployer(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    nbr_local_locations = models.IntegerField(blank=True, null=True)
    year_est = models.CharField(max_length=4, blank=True)
    specialties = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Largest Employer'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(LargestEmployer, self).save(force_insert, force_update)

class LargestManufacturer(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    headquarters_state = USStateField(blank=True)
    year_est = models.CharField(max_length=4, blank=True)
    specialties = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Largest Manufacturer'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(LargestManufacturer, self).save(force_insert, force_update)

class LargestRetail(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    lessee = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    lessor = models.CharField(max_length=255, blank=True)
    total_square_footage = models.IntegerField()
    lease_length = models.CharField(max_length=255, blank=True)
    year_started = models.CharField(max_length=4, blank=True)
    lease_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    special_terms = models.TextField(blank=True)
#agent fields
    agent_first_name = models.CharField(max_length=255, blank=True)
    agent_last_name = models.CharField(max_length=255, blank=True)
    agency = models.CharField(max_length=255, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone = PhoneNumberField(blank=True)
    author_fax = PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Largest Retail Transaction'

    def __unicode__(self):
        return self.lessee

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(LargestRetail, self).save(force_insert, force_update)

class LawFirm(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_attorneys = models.IntegerField()
    nbr_partners = models.IntegerField(blank=True, null=True)
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    practice_areas = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Law Firm'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(LawFirm, self).save(force_insert, force_update)

class LegalSupportService(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    attorneys_on_staff = models.BooleanField()
    nbr_attorneys = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
    client_types = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Legal Support Service'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(LegalSupportService, self).save(force_insert, force_update)

class LitigationAttorney(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_attorneys = models.IntegerField()
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    practice_areas = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Litigation Attorney'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(LitigationAttorney, self).save(force_insert, force_update)

class MedicalMalpracticeAttorney(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_attorneys = models.IntegerField()
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    practice_areas = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Medical Malpractice Attorney'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(MedicalMalpracticeAttorney, self).save(force_insert, force_update)

class MeetingFacility(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    total_square_footage = models.IntegerField()
    rates = models.TextField(blank=True)
    meeting_types = models.TextField(blank=True)
    services = models.TextField(blank=True)
#contact fields
    contact_first_name = models.CharField(max_length=255, blank=True)
    contact_last_name = models.CharField(max_length=255, blank=True)
    contact_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Meeting & Banquet Facility'
        verbose_name_plural = 'Meeting & Banquet Facilities'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(MeetingFacility, self).save(force_insert, force_update)

class MortgageLender(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    volume_local_mortgage_loans = models.DecimalField(max_digits=14, decimal_places=2)
    LENDER_CHOICES = (
        ('BROKER', 'Mortgage broker'),
        ('BANKER', 'Mortgage banker'),
        ('LENDER', 'Mortgage lender'),
    )
    lender_type = models.CharField(max_length=6, choices=LENDER_CHOICES, blank=True)
    turnaround_time = models.CharField(max_length=255, blank=True)
    nbr_loans = models.IntegerField(blank=True, null=True)
    nbr_loan_officers = models.IntegerField(blank=True, null=True)
    size_range_loans = models.CharField(max_length=255, blank=True)
    portfolio = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Mortgage Lender/Broker'
        verbose_name_plural = 'Mortgage Lenders & Brokers'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(MortgageLender, self).save(force_insert, force_update)

class NetworkingGroup(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    group_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    meeting_location = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_members = models.IntegerField()
    nbr_meetings = models.IntegerField(blank=True, null=True)
    field = models.CharField(max_length=255, blank=True)
    events = models.TextField(blank=True)
    services = models.TextField(blank=True)
#leader fields
    leader_first_name = models.CharField(max_length=255, blank=True)
    leader_last_name = models.CharField(max_length=255, blank=True)
    leader_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Networking Group'

    def __unicode__(self):
        return self.group_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(NetworkingGroup, self).save(force_insert, force_update)

class OfficeFurniture(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    tot_sales = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nbr_locations = models.IntegerField(blank=True, null=True)
    headquarters_location = models.CharField(max_length=255, blank=True)
    specialties = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Office Furniture/Supply Company'
        verbose_name_plural = 'Office Furniture & Supply Companies'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(OfficeFurniture, self).save(force_insert, force_update)

class OfficeMachine(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    nbr_locations = models.IntegerField(blank=True, null=True)
    commercial_discounts = models.BooleanField()
    maintenance_agreements = models.BooleanField()
    delivery = models.BooleanField()
    brands = models.TextField(blank=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Office Machine Company'
        verbose_name_plural = 'Office Machine Companies'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(OfficeMachine, self).save(force_insert, force_update)

class OfficePark(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    property_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    developer = models.CharField(max_length=255, blank=True)
    year_built = models.CharField(max_length=4, blank=True)
    leasable_area = models.IntegerField()
    percent_leased = models.IntegerField(blank=True, null=True)
    space_available = models.IntegerField(blank=True, null=True)
    rent_range = models.CharField(max_length=255, blank=True)
    leases_offered = models.CharField(max_length=255, blank=True)
    major_tenants = models.TextField(blank=True)
#agent fields
    agent_first_name = models.CharField(max_length=255, blank=True)
    agent_last_name = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone = PhoneNumberField(blank=True)
    author_fax = PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Office Park'

    def __unicode__(self):
        return self.property_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(OfficePark, self).save(force_insert, force_update)

class PersonalInjuryAttorney(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_attorneys = models.IntegerField()
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    practice_areas = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)
    nbr_partners = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Personal Injury Attorney'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(PersonalInjuryAttorney, self).save(force_insert, force_update)

class Pharmacy(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_locations = models.IntegerField(blank=True, null=True)
    online_ordering = models.BooleanField()
    headquarters = models.CharField(max_length=255, blank=True)
    services = models.TextField(blank=True)
    insurance_types = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Pharmacy'
        verbose_name_plural = 'Pharmacies'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(Pharmacy, self).save(force_insert, force_update)

class PhysicalTherapy(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    caregiver_types = models.TextField(blank=True)
    insurance_types = models.TextField(blank=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Physical & Occupational Therapy Center'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(PhysicalTherapy, self).save(force_insert, force_update)

class PrivateSchool(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    school_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_students = models.IntegerField()
    grade_range = models.CharField(max_length=255, blank=True)
    waiting_list = models.BooleanField()
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    annual_tuition = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    student_teacher_ratio = models.CharField(max_length=255, blank=True)
    nbr_local_schools = models.IntegerField(blank=True, null=True)
    special_concentration_areas = models.TextField(blank=True)
    headquarters_state = USStateField(blank=True)
#admissions fields
    admissions_first_name = models.CharField(max_length=255, blank=True)
    admissions_last_name = models.CharField(max_length=255, blank=True)
    admissions_title = models.CharField(max_length=255, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Private School'

    def __unicode__(self):
        return self.school_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(PrivateSchool, self).save(force_insert, force_update)

class ProfessionalCertification(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    school_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_students = models.IntegerField()
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    average_cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    renewal_period = models.CharField(max_length=255, blank=True)
    nbr_local_schools = models.IntegerField(blank=True, null=True)
    licenses_offered = models.TextField(blank=True)
    year_est = models.CharField(max_length=4, blank=True)
    headquarters_state = USStateField(blank=True)
#admissions fields
    admissions_first_name = models.CharField(max_length=255, blank=True)
    admissions_last_name = models.CharField(max_length=255, blank=True)
    admissions_title = models.CharField(max_length=255, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Professional License/Certification'
        verbose_name_plural = 'Professional Licenses & Certifications'

    def __unicode__(self):
        return self.school_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ProfessionalCertification, self).save(force_insert, force_update)

class PublicRelations(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    specialties = models.TextField(blank=True)
    notable_accounts = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Public Relations Firm'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(PublicRelations, self).save(force_insert, force_update)

class Restaurant(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    restaurant_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    meeting_space_square_footage = models.IntegerField()
    restaurant_type = models.CharField(max_length=255, blank=True)
    opening_closing_times = models.CharField(max_length=255, blank=True)
    dress_code = models.CharField(max_length=255, blank=True)
    specialties = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Restaurant With Meeting Space'
        verbose_name_plural = 'Restaurants With Meeting Space'

    def __unicode__(self):
        return self.restaurant_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(Restaurant, self).save(force_insert, force_update)

class SBALender(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    sba_loans_total = models.DecimalField(max_digits=15, decimal_places=2)
    nbr_sba_loans = models.IntegerField(blank=True, null=True)
    sba_loans_avg = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    sba_loans_total_minorities = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nbr_sba_loans_minorities = models.IntegerField(blank=True, null=True)
    sba_loans_avg_minorities = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    STATUS_CHOICES = (
        ('CLP', 'CLP'),
        ('PLP', 'PLP'),
        ('GP', 'GP'),
        ('ALP', 'ALP'),
        ('CDC', 'CDC'),
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)
    nbr_local_employees = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'SBA Lender'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(SBALender, self).save(force_insert, force_update)

class ShoppingCenter(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    mall_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    owner = models.CharField(max_length=255, blank=True)
    total_square_footage = models.IntegerField()
    nbr_tenants = models.IntegerField(blank=True, null=True)
    year_opened = models.CharField(max_length=4, blank=True)
    nbr_parking_spaces = models.IntegerField(blank=True, null=True)
    anchor_tenants = models.TextField(blank=True)
    leasing_agent = models.CharField(max_length=255, blank=True)
    leasing_agency = models.CharField(max_length=255, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Shopping Center/Mall'
        verbose_name_plural = 'Shopping Centers & Malls'

    def __unicode__(self):
        return self.mall_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ShoppingCenter, self).save(force_insert, force_update)

class SpecialtyClinic(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    caregiver_types = models.TextField(blank=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Specialty Clinic'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(SpecialtyClinic, self).save(force_insert, force_update)

class StaffingFirm(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    PLACEMENT_CHOICES = (
        ('TEMPORARY', 'Temporary'),
        ('PERMANENT', 'Permanent'),
        ('BOTH', 'Both'),
    )
    placement = models.CharField(max_length=15, choices=PLACEMENT_CHOICES, blank=True)
    fee = models.BooleanField()
    fee_percent = models.IntegerField(blank=True, null=True)
    nbr_local_placements = models.IntegerField(blank=True, null=True)
    specialties = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Staffing Firm'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(StaffingFirm, self).save(force_insert, force_update)

class Stockbroker(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_stockbrokers = models.IntegerField()
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Stockbroker'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(Stockbroker, self).save(force_insert, force_update)

class Technology(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Technology Firm'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(Technology, self).save(force_insert, force_update)

class Telecommunications(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    nbr_local_customers = models.IntegerField(blank=True, null=True)
    brands = models.TextField(blank=True)
    services = models.TextField(blank=True)
#sales manager fields
    sales_manager_first_name = models.CharField(max_length=255, blank=True)
    sales_manager_last_name = models.CharField(max_length=255, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Telecommunications Company'
        verbose_name_plural = 'Telecommunications Companies'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(Telecommunications, self).save(force_insert, force_update)

class TitleCompany(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_insurable_transactions = models.IntegerField()
    market_share_percent = models.IntegerField(blank=True, null=True)
    percent_residential = models.IntegerField(blank=True, null=True)
    percent_commercial = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    nbr_national_offices = models.IntegerField(blank=True, null=True)
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    underwriters_represented = models.TextField(blank=True)
    top_local_principal = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Title Company'
        verbose_name_plural = 'Title Companies'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(TitleCompany, self).save(force_insert, force_update)

class TradeAssociation(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    association_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_members = models.IntegerField()
    industries_enrolled = models.TextField(blank=True)
    affiliated_organizations = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Trade Association'

    def __unicode__(self):
        return self.association_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(TradeAssociation, self).save(force_insert, force_update)

class TransportationService(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_employees = models.IntegerField()
    nbr_in_fleet = models.IntegerField(blank=True, null=True)
    national_headquarters = models.CharField(max_length=255, blank=True)
    services = models.TextField(blank=True)
    rates = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Transportation Service'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(TransportationService, self).save(force_insert, force_update)

class TreatmentCenter(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    caregiver_types = models.TextField(blank=True)
    insurance_types = models.TextField(blank=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Treatment Center'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(TreatmentCenter, self).save(force_insert, force_update)

class TVAnchor(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    station = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    first_year = models.CharField(max_length=4, blank=True)
    programs = models.TextField(blank=True)
    degree = models.TextField(blank=True)
    hobbies = models.TextField(blank=True)
    favorite_places = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Top Rated TV Anchor'

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(TVAnchor, self).save(force_insert, force_update)

class VentureCapitalFirm(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    amount_invested = models.DecimalField(max_digits=15, decimal_places=2)
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    industries = models.TextField(blank=True)
    recent_investments = models.TextField(blank=True)
    size_range_investments = models.CharField(max_length=255, blank=True)
    funding_stage = models.CharField(max_length=255, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Venture Capital/Private Equity Firm'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(VentureCapitalFirm, self).save(force_insert, force_update)
#--------------------------------------------------------------------------------------------------------------------------
class ProfessionalOrg(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_members = models.IntegerField()
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_meetings = models.IntegerField(blank=True, null=True)
    membership_field = models.TextField(blank=True)
    publications = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Professional Organization'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ProfessionalOrg, self).save(force_insert, force_update)

class Hospital(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    caregiver_types = models.TextField(blank=True)
    insurance_types = models.TextField(blank=True)
    services = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Hospital'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(Hospital, self).save(force_insert, force_update)


class ArchitectureFirm(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_licensed_architects = models.IntegerField(blank=True, null=True)
    nbr_local_employees = models.IntegerField(blank=True, null=True)

    percent_private = models.IntegerField(blank=True, null=True)
    percent_county = models.IntegerField(blank=True, null=True)
    percent_state = models.IntegerField(blank=True, null=True)
    percent_federal = models.IntegerField(blank=True, null=True)

    specialties = models.TextField(blank=True)
    current_projects = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Architecture Firm'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ArchitectureFirm, self).save(force_insert, force_update)

class BusCommLitigationAttorney(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_attorneys = models.IntegerField()
    nbr_partners = models.IntegerField(blank=True, null=True)
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    practice_areas = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Business Commerical Litigation Attorney'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(BusCommLitigationAttorney, self).save(force_insert, force_update)


class EventPlanner(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    event_types = models.TextField(blank=True)

    rates = models.TextField(blank=True)
    services = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Event Planner'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(EventPlanner, self).save(force_insert, force_update)

class FamilyOwnedBusiness(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    percent_family_owned = models.IntegerField(blank=True, null=True)
    business_description = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Family Owned Businesse'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(FamilyOwnedBusiness, self).save(force_insert, force_update)

class FitnessRecreationCenter(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_members = models.IntegerField()
    nbr_locations = models.IntegerField(blank=True, null=True)
    membership_eligibility = models.TextField(blank=True)
    services = models.TextField(blank=True)
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    fees = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Fitness Recreation Center'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(FitnessRecreationCenter, self).save(force_insert, force_update)

class GamingSuppliersCasinoOperator(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    headquarters = models.CharField(max_length=255, blank=True)
    properties_owned_serviced = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Gaming Suppliers Casino Operator'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(GamingSuppliersCasinoOperator, self).save(force_insert, force_update)

class ConstructionCompanyContractor(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    billings = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    headquarters = models.CharField(max_length=255, blank=True)
    specialties = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Construction Company Contractor'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ConstructionCompanyContractor, self).save(force_insert, force_update)

class GovernmentAffairsAttorney(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_attorneys = models.IntegerField()
    nbr_partners = models.IntegerField(blank=True, null=True)
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)

    practice_areas = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Government Affairs Attorney'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(GovernmentAffairsAttorney, self).save(force_insert, force_update)

class GreenServiceProvider(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
    percent_services = models.IntegerField(blank=True, null=True)
    awards = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Green Service Provider'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(GreenServiceProvider, self).save(force_insert, force_update)

class HealthInsuranceProvider(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_members = models.IntegerField()
    plan_types = models.TextField(blank=True)
    nbr_providers = models.IntegerField(blank=True, null=True)
    parent_company = models.CharField(max_length=255, blank=True)
    covered_hospitals = models.TextField(blank=True)
    riders = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Health Insurance Provider'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(HealthInsuranceProvider, self).save(force_insert, force_update)

class ITServiceProvider(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
    authorized_reseller = models.BooleanField()
    authorized_company_name = models.CharField(max_length=255)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'IT Service Provider'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ITServiceProvider, self).save(force_insert, force_update)

class LargestOfficeIndustrial(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    lessee_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    total_square_footage = models.IntegerField()
    lessor = models.CharField(max_length=255)
    lease_length = models.CharField(max_length=255, blank=True)
    year_started = models.CharField(max_length=4, blank=True)
    lease_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    special_terms = models.TextField(blank=True)
#agent fields
    agent_first_name = models.CharField(max_length=255, blank=True)
    agent_last_name = models.CharField(max_length=255, blank=True)
    agency = models.CharField(max_length=255, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Largest Office Industrial Transaction'

    def __unicode__(self):
        return self.lessee_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(LargestOfficeIndustrial, self).save(force_insert, force_update)

class LocalLawFirm(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_attorneys = models.IntegerField()
    nbr_partners = models.IntegerField(blank=True, null=True)
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    practice_areas = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Local Law Firm'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(LocalLawFirm, self).save(force_insert, force_update)

class MediaCompany(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    outlet_types = models.TextField(blank=True)
    products = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Media Company'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(MediaCompany, self).save(force_insert, force_update)

class MedicalGroup(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_physicians = models.IntegerField(blank=True, null=True)
    specialties = models.TextField(blank=True)
    parent_company = models.CharField(max_length=255, blank=True)
    headquarters = models.CharField(max_length=255, blank=True)
    insurance_types = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Medical Group'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(MedicalGroup, self).save(force_insert, force_update)

class MinorityOwnedBusiness(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    percent_owned = models.IntegerField(blank=True, null=True)
    background = models.CharField(max_length=255, blank=True)
    sales_gross = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    business_description = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Minority Owned Businesse'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(MinorityOwnedBusiness, self).save(force_insert, force_update)

class MunicipalBusinessService(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    department_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
    online = models.BooleanField()
    services_online = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Municipal Business Service'

    def __unicode__(self):
        return self.department_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(MunicipalBusinessService, self).save(force_insert, force_update)

class NationalBank(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_branches = models.IntegerField()
    nbr_local_branches_nationwide = models.IntegerField()
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    headquarters_state = USStateField(blank=True)
    services = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'National Bank'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(NationalBank, self).save(force_insert, force_update)

class NationalLawFirm(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_attorneys = models.IntegerField()
    nbr_partners = models.IntegerField(blank=True, null=True)
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)

    nbr_attorneys_nationwide = models.IntegerField()
    nbr_offices_nationwide = models.IntegerField(blank=True, null=True)

    practice_areas = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'National Law Firm'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(NationalLawFirm, self).save(force_insert, force_update)

class Optometrist(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    insurance_types = models.TextField(blank=True)
    specialties = models.TextField(blank=True)
    parent_company = models.CharField(max_length=255, blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Optometrist'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(Optometrist, self).save(force_insert, force_update)

class PayrollCompany(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
    size_range_services = models.CharField(max_length=255, blank=True)
    provides_direct_deposit = models.BooleanField()

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Payroll Company'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(PayrollCompany, self).save(force_insert, force_update)

class ResidentialREBroker(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    agents = models.IntegerField(blank=True, null=True)
    nbr_local_branches = models.IntegerField()
    sales_gross = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    home_sales = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    headquarters_state = USStateField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Residential Real Estate Broker'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ResidentialREBroker, self).save(force_insert, force_update)

class CasinoVendor(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    sales_gross = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    headquarters_state = USStateField(blank=True)
    specialties = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Casino Vendor'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CasinoVendor, self).save(force_insert, force_update)

class WasteManagementService(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    materials_recycled = models.TextField(blank=True)
    services = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Waste Management Services Recycler'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(WasteManagementService, self).save(force_insert, force_update)

class TopBankPresident(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    bank = models.CharField(max_length=255, blank=True)
    president = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    years_in_industry = models.IntegerField(blank=True, null=True)
    years_at_company = models.IntegerField(blank=True, null=True)
    years_in_las_vegas = models.IntegerField(blank=True, null=True)
    affiliations = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Top Bank President'

    def __unicode__(self):
        return self.bank

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(TopBankPresident, self).save(force_insert, force_update)

class LaborUnion(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    union_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_members = models.IntegerField()
    field = models.CharField(max_length=255, blank=True)
    events = models.TextField(blank=True)
    services = models.TextField(blank=True)
#leader fields
    leader_first_name = models.CharField(max_length=255, blank=True)
    leader_last_name = models.CharField(max_length=255, blank=True)
    leader_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Labor Union'

    def __unicode__(self):
        return self.union_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(LaborUnion, self).save(force_insert, force_update)

class MinorityBusinessLeader(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=255, blank=True)
    years_with_co = models.IntegerField(blank=True, null=True)
    years_in_industry = models.IntegerField(blank=True, null=True)
    degree = models.TextField(blank=True)
    affiliations = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Minority Business Leader'

    def __unicode__(self):
        return self.full_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(MinorityBusinessLeader, self).save(force_insert, force_update)

class CosmeticPlasticSurgeryPractice(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    specialties = models.TextField(blank=True)
    insurance_accepted = models.TextField(blank=True)
    doctor_types = models.TextField(blank=True)
    parent_company = models.CharField(max_length=255, blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Cosmetic & Plastic Surgery Practice'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CosmeticPlasticSurgeryPractice, self).save(force_insert, force_update)

class UrgentCareCenter(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    nbr_locations = models.IntegerField(blank=True, null=True)
    caregiver_types = models.TextField(blank=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Urgent Care Center'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(UrgentCareCenter, self).save(force_insert, force_update)

class MinorityMediaCompany(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    outlet_types = models.TextField(blank=True)
    products = models.TextField(blank=True)
    primary_demographic = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Minority Media Company'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(MinorityMediaCompany, self).save(force_insert, force_update)

class AngelFundInvestor(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    amount_invested = models.DecimalField(max_digits=15, decimal_places=2)
    industries = models.TextField(blank=True)
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Angel Fund Investor'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(AngelFundInvestor, self).save(force_insert, force_update)


class FilmVideoProductionCompany(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Film Video Production'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(FilmVideoProductionCompany, self).save(force_insert, force_update)

class ResidentialTopSalesAgent(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    agent_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    sales_gross = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    home_sales = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    specialties = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Residential Top Sales Agent'

    def __unicode__(self):
        return self.agent_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ResidentialTopSalesAgent, self).save(force_insert, force_update)

class CommercialMovingCompany(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    sales_gross = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    nbr_moves = models.IntegerField()
    total_square_footage = models.IntegerField()
    specialties = models.TextField(blank=True)
    affiliations = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Commercial Moving Company'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CommercialMovingCompany, self).save(force_insert, force_update)

class GeneralPracticeAttorney(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_attorneys = models.IntegerField()
    nbr_partners = models.IntegerField(blank=True, null=True)
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    practice_areas = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'General Practice Attorney'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(GeneralPracticeAttorney, self).save(force_insert, force_update)

class GamingAttorney(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_attorneys = models.IntegerField()
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    practice_areas = models.TextField(blank=True)
    managing_partner = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Gaming Attorney'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(GamingAttorney, self).save(force_insert, force_update)

class WirelessCableProvider(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    nbr_local_customers = models.IntegerField(blank=True, null=True)
    brands = models.TextField(blank=True)
    services = models.TextField(blank=True)
    sales_manager_first_name = models.CharField(max_length=255, blank=True)
    sales_manager_last_name = models.CharField(max_length=255, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Wireless Cable Provider'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(WirelessCableProvider, self).save(force_insert, force_update)

class ResidentialHomeBuilder(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    years_in_nevada = models.IntegerField()
    local_subdivisions = models.TextField(blank=True)
    national_headquarters = models.CharField(max_length=255, blank=True)
    nbr_local_employees = models.IntegerField(blank=True, null=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Residential Home Builder'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ResidentialHomeBuilder, self).save(force_insert, force_update)

class CommercialResidentialLandscaper(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField(blank=True, null=True)
    commercialoresidential = models.TextField(blank=True)

    services = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Commercial Residential Landscaper'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CommercialResidentialLandscaper, self).save(force_insert, force_update)

class CityCountyBusinessService(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    department_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_department_employees = models.IntegerField()
    services = models.TextField(blank=True)
    online_services_available = models.BooleanField()
    online_services = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'City County Business Service'

    def __unicode__(self):
        return self.department_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(CityCountyBusinessService, self).save(force_insert, force_update)

class PediatricGroupPractice(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    group_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField()
    nbr_staff = models.IntegerField(blank=True, null=True)
    insurance_types = models.TextField(blank=True)
    specialties = models.TextField(blank=True)
    parent_company = models.CharField(max_length=255, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Pediatric Group Practice'

    def __unicode__(self):
        return self.group_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(PediatricGroupPractice,self).save(force_insert, force_update)

class DaySpa(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField()
    nbr_locations = models.IntegerField(blank=True, null=True)
    services = models.TextField(blank=True)
    rates = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Day Spa'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(DaySpa,self).save(force_insert, force_update)

class GraphicDesignCompany(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_local_employees = models.IntegerField()
    sales_gross = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    services = models.TextField(blank=True)
    notable_clients = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Graphic Design Company'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(GraphicDesignCompany,self).save(force_insert, force_update)

class AssistedLivingFacility(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    facility_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)

    nbr_residents = models.IntegerField()
    nbr_staff = models.IntegerField(blank=True, null=True)
    level_of_care_available = models.TextField(blank=True)
    caregiver_types = models.TextField(blank=True)
    services = models.TextField(blank=True)

#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Assisted Living Facility'

    def __unicode__(self):
        return self.facility_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(AssistedLivingFacility,self).save(force_insert, force_update)

class ConstructionAttorney(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    firm_name = models.CharField(max_length=255)
    year_est = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_attorneys = models.IntegerField()
    nbr_staff = models.IntegerField(blank=True, null=True)
    nbr_local_offices = models.IntegerField(blank=True, null=True)
    practice_areas = models.TextField(blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Construction Attorney'

    def __unicode__(self):
        return self.firm_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(ConstructionAttorney, self).save(force_insert, force_update)

class StudentLoanProvider(models.Model):
    submitted_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    nbr_local_employees = models.IntegerField(blank=True, null=True)
    student_loans_total = models.DecimalField(max_digits=15, decimal_places=2)
    nbr_student_loans = models.IntegerField(blank=True, null=True)
    student_loans_avg = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    student_loans_total_minorities = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nbr_student_loans_minorities = models.IntegerField(blank=True, null=True)
    student_loans_avg_minorities = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    STATUS_CHOICES = (
        ('CLP', 'CLP'),
        ('PLP', 'PLP'),
        ('GP', 'GP'),
        ('ALP', 'ALP'),
        ('CDC', 'CDC'),
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, blank=True)
#exec fields
    exec_first_name = models.CharField(max_length=255, blank=True)
    exec_last_name = models.CharField(max_length=255, blank=True)
    exec_title = models.CharField(max_length=255, blank=True)
#author fields
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_phone =  PhoneNumberField(blank=True)
    author_fax =  PhoneNumberField(blank=True)
    author_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Student Loan Provider'

    def __unicode__(self):
        return self.company_name

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.submitted_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(StudentLoanProvider, self).save(force_insert, force_update)

