## Writing Tests for Views

### Setup
- Create test users and objects in `setUp` so they are available to all tests in the class
- Make sure credentials in `setUp` and `client.login()` match exactly
- Use `force_login()` when you want to skip the login process itself

```python
def setUp(self):
    self.user = User.objects.create_user(username='user', password='test')
    self.source = Source.objects.create(user=self.user, ...)

self.client.force_login(user2)  # faster than login() for testing other behaviours
```

### What to test on every view
- Unauthenticated user is redirected (verifies @login_required)
- Authenticated user gets 200 with correct template and context (the happy path)
- User cannot access another user's data

### Detail views — also test
- Nonexistent pk returns 404
- Another user's pk returns 404 (or 403 if your acceptance criteria requires it)

### Assertions
- `assertEqual(response.status_code, 200)` — page loaded
- `assertRedirects(response, '/accounts/login/?next={url}')` — redirect with destination, more precise than checking 302 alone
- `assertTemplateUsed(response, 'app/template.html')` — correct template rendered
- `assertEqual(response.context['key'], expected_object)` — correct data in context
- `assertNotIn(object, response.context['key'])` — object absent from context

### General
- One behaviour per test — if it fails you know exactly what broke
- Name tests after the behaviour, not the implementation: `test_unauthenticated_user_is_redirected` not `test_login_required`
- Regression value: tests like `test_unauthenticated_user_is_redirected` will catch accidental deletion of @login_required in the future
- Document tests with an ID table so you can track coverage against acceptance criteria