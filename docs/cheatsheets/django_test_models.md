# Model Testing


## Testing behaviour:

To test behaviour you need real instances of the Models being tested in the test database that Django creates. To create these instances you need to define a special setUP(self) method with a self parameter, to  make it accessible to all tests in that class (each class needs a setUP(self) method). This method populates the Django test database with actual rows, so your tests can interact with them like a real application would.

Even if you need setUP after having written tests that didn't require it, always write it first in the class, before any test methods. It's a convention that makes the class readable — anyone looking at the test class sees what's being set up before they read the individual tests.

<pre>
def setUp(self):
    self.instance_name = Model.objects.create(field='value')
</pre>

- objects.create() is Django's ORM method for inserting a row into the test database. For models with no required fields (like a model you've written with just a pass) you can call it with no arguments:

<pre>
self.instance_name = Model.objects.create()
</pre>

- for models with required fields you must pass them:

<pre>
self.instance_name = Model.objects.create_user(field1='value', field2='value')
</pre>


The syntax Model.objects.method() — is used to talk to the table, not a specific row. Used for querying or creating:
<pre>
Model.objects.create()                           # insert a new row
Model.objects.filter()                           # query multiple rows
Model.objects.get()                              # query one row
Source.objects.exists()                          # any rows at all in the table?
Source.objects.filter(user=self.user).exists()   # any rows matching the filter?
</pre>

When you need to talk to a specific row that already exists you use: self.instance_name.method()
<pre>
self.instance_name.delete()         # delete this specific row
self.instance_name.save()           # save changes to this specific row
self.instance_name.field_name       # access a field on this specific row
</pre>

The rule of thumb: if you already have an instance, use dot notation on it. If you need to find or create one, go through objects.

**Note**
Any time you've added or changed a model and haven't migrated yet, setUp will fail because the table doesn't exist. The order is always:

- Add/change model
- makemigrations
- migrate
- Run tests


## Assertions:

- assertEqual(a, b) — passes if a == b
- assertIsNotNone(x) — passes if x is not None; use to confirm an object was saved (check its pk)
- assertRaises(ExceptionType) — passes if the code inside the with block raises that exception; use to test constraints

<pre>
with self.assertRaises(IntegrityError):
    Model.objects.create(...)
</pre>

IntegrityError must be imported: from django.db import IntegrityError


## What is worth testing on a model:

- __str__ output — test each branch separately (e.g. with and without author)
- constraints — UniqueConstraint and CheckConstraint; test that violations raise IntegrityError
- optional fields — confirm None saves correctly
- get_fieldname_display() — confirm human readable label is correct for at least one choice

## What is not worth testing:

- auto_now_add and auto_now timestamps — Django built-in behaviour
- on_delete behaviour on ForeignKey — Django built-in behaviour
