Titles By Location
===

This plugin lets you offer up a complete list of all titles by location,
including a list of titles with an "Unknown" location if some of your metadata
has been broken.

The output is pure text and should suffice as an alternative to the map plugin
for people who prefer (or need) something text-based.

Compatibility
---

The "main" branch should not be considered stable.  Unlike the core Open ONI
repository, plugins don't warrant the extra overhead of having separate
development branches, release branches, etc.  Instead, it is best to find a tag
that works and stick with that tag.

- Titles By Location v0.1.1 and prior only work with Python 2 and Django 1.11
  and prior
  - Therefore these versions of the Titles By Location plugin are only
    compatible up to (and including) ONI v0.11
- Titles By Location releases v0.2.0 and later require Python 3 and Django 2.2,
  and should be used with ONI 0.12 and later.

Setup
---

Grab the plugin from github:

```bash
git clone git@github.com:open-oni/plugin_title_locations.git onisite/plugins/title_locations
```

Add it to your `INSTALLED_APPS` in `onisite/settings_local.py`:

```python
INSTALLED_APPS = (
    'django.contrib.humanize',
    'django.contrib.staticfiles',

    'onisite.plugins.title_locations',
    'themes.oregon',
    'core',
)
```

Put in a new URL path into `onisite/urls.py` (or your theme's `urls.py`) above
the `core.urls` line:

```python
from django.conf.urls import url, include
from onisite.plugins.title_locations import views as tl_views

urlpatterns = [
  url(r'^titles_by_location$', tl_views.titles_by_location, name="oregon_titles_by_location"),

  # make sure you include your titles_by_location link above the core urls
  url('', include("core.urls")),
```

API
---

You can also pull the list of location data directly if you'd prefer to render
the list in another template, or alter the data before sending it to your
template:

```python
# In your theme's views.py:
from title_locations import views as tl_views

def home(request):
    locs, locations = tl_views.get_titles_by_location()

    # Get rid of all the titles in Broken City!  It's broken!
    locs.remove("Broken City")

    # Render our homepage where we embed the list for some reason
    return render(request, 'home.html', locals())
```
