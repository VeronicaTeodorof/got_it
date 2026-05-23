## Naming Models Conventions:

- singular not plural — Source not Sources
- PascalCase — SourceType not source_type or sourcetype
- Django automatically creates the table name as appname_modelname in snake_case — so Source in a notes app becomes notes_source


## Fields


### Syntax
field_name = models.FieldType(options)

### Conventions:
- snake_case for field names — source_name not sourceName
- Don't add _id suffix to FK fields — Django adds it automatically. So source_type not source_type_id; Django creates the source_type_id column in the DB for you
- Don't include a manual id field — Django creates it automatically


### Best Practices:
- Always set on_delete explicitly on FKs — don't let Django guess
- Use blank=True for optional form fields, null=True for optional DB columns — on string fields prefer blank=True without null=True so you store empty string rather than NULL, unless the field is genuinely absent for some instances (e.g. an optional author), in which case null=True is more honest and allows clean isnull filtering
- Add __str__ to every model so it's readable in the admin and shell
- Add related_name to FKs for readable reverse access — e.g. related_name='sources' allows user.sources.all()


### Choices:
- Use TextChoices for a fixed set of valid string values — cleaner than plain tuples and supports dot access e.g. Source.SourceType.BOOK
- Each entry has three parts: CONSTANT = 'db_value', 'Human Readable Label'
- DB value is lowercase and stable — changing it breaks existing data
- Human readable label can change freely
- Wrap labels with _() from gettext_lazy if i18n is needed
- TextChoices validates at the form level, not the database level — add a CheckConstraint if you want database level protection


### Constraints (Meta class):
- UniqueConstraint — prevents duplicate combinations of fields per user
- CheckConstraint — enforces valid values at the database level, catches mistakes even when form validation is bypassed
- Add constraints before any data is entered — adding them later risks migration failures if duplicates already exist


### Common Field Types:
- CharField(max_length=255) — for short text, always needs max_length
- TextField() — for long text, no max_length needed
- BooleanField(default=False) — true/false
- DateTimeField(auto_now_add=True) — auto-sets on creation
- DateTimeField(auto_now=True) — auto-updates on every save
- ForeignKey(Model, on_delete=models.CASCADE) — relationship
