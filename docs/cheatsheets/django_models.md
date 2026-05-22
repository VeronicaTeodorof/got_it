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
- Use blank=True for optional form fields, null=True for optional DB columns — on string fields prefer blank=True without null=True so you store empty string rather than NULL
- Add __str__ to every model so it's readable in the admin and shell


### Common Field Types: 
- CharField(max_length=255) — for short text, always needs max_length
- TextField() — for long text, no max_length needed
- BooleanField(default=False) — true/false
- DateTimeField(auto_now_add=True) — auto-sets on creation
- DateTimeField(auto_now=True) — auto-updates on every save
- ForeignKey(Model, on_delete=models.CASCADE) — relationship
