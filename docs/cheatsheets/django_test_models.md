# TDD Model Testing in Django


## The cycle:
1. Write the test — red;
2. Write the code to make it pass — green;
3. Move to the next test


## Testing model existence:
<pre>
def test_your_model_exists(self):
    self.assertTrue(Model
    )
</pre>


## Testing field existence:
<pre>
def test_model_has_field(self):
    self.assertTrue(hasattr(Model, 'field'))

</pre>

- hasattr is a built-in Python function that takes 2 parameters: the model name and field name as a string


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