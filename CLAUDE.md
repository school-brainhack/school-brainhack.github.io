# CLAUDE.md — Brainhack School Website

## Project Overview

**Brainhack School** is a 4-week distributed neuroscience and open-science training event running simultaneously at multiple global sites. Participants complete structured training modules (Week 1) then work on collaborative data-science projects (Weeks 2–4).

- **Live site:** https://school-brainhack.github.io
- **Dev docs:** https://school-brainhack.readthedocs.io
- **Stack:** Hugo static site + GitHub Pages deployment
- **Theme:** `hugo-universal-theme` (Git submodule at `themes/hugo-universal-theme`)
- **Hugo version:** 0.128.0 extended

---

## Local Development

```bash
# 1. Initialize submodules (required after first clone)
git submodule update --init --recursive --remote

# 2. Serve locally with drafts
hugo serve -D

# 3. Production build (run by CI)
hugo --minify
```

Site is served at `http://localhost:1313` by default.

---

## Repository Structure

```
config.yaml              # Main Hugo configuration
content/en/              # All site content (markdown)
  modules/               # Training module pages (~26 modules)
  project/               # Student project gallery (60+ projects)
  sites/                 # Distributed site hubs (toronto, polytechnique, criugm, singapore, taiwan)
  weeks/                 # Schedule/week pages
  schedule/              # Calendar output page
  coc/                   # Code of Conduct
  guide.md               # Getting Started guide
  project_guide.md       # Project submission guide
  register.md            # Registration page
data/en/                 # YAML-driven dynamic content
  instructors.yaml       # Global instructor/team list
  carousel/              # Homepage carousel slides (7 YAML files)
  testimonials/          # Quote testimonials (3 YAML files)
  clients/               # Sponsor/partner logos (2 YAML files)
  features/              # Features section (disabled; 6 YAML files)
layouts/                 # Custom Hugo templates (override theme)
  partials/              # Reusable components (nav, footer, carousel, instructors…)
  shortcodes/            # Custom shortcodes: gform, tabs, tab, class, content
  project/               # Project list + single page layouts
  modules/               # Module list + single page layouts
  sites/                 # Site hub layouts
static/img/              # All images
  logo_brainhack_2025.png
  carousel/              # Carousel slide images
  instructors/           # Instructor headshots
  testimonials/          # Testimonial avatars
  locations/             # Site hub images
  clients/               # Sponsor logos
i18n/en.yaml             # English UI strings
i18n/fr.yaml             # French UI strings
.github/workflows/hugo.yml  # CI/CD pipeline
```

---

## config.yaml Key Settings

| Setting | Value | Notes |
|---|---|---|
| `baseURL` | `https://school-brainhack.github.io` | |
| `theme` | `hugo-universal-theme` | Git submodule |
| `params.style` | `green` | Theme color |
| `params.logo` | `img/logo_brainhack_2025.png` | Update for new year |
| `params.logo_small` | `img/logo-small_2025.png` | |
| `params.carousel.enable` | `true` | |
| `params.instructors.enable` | `true` | |
| `params.testimonials.enable` | `true` | |
| `params.features.enable` | `false` | Currently disabled |
| `params.recent_posts.enable` | `false` | Currently disabled |
| Markdown unsafe HTML | `true` | HTML allowed in markdown |

**Main menu** (by weight): Home → Projects → Schedule → Sites → Register → Modules
**Dropdowns:** `documents` (Getting Started, Project Guide, CoC, Dev Docs) · `past` (2024–2018 archives)
**Topbar:** GitHub, Mastodon, email contact

**Custom taxonomies:**
- `tags` → filter projects and modules
- `names` → author/organizer names (used for filtering)

---

## Content Frontmatter Reference

### Project page — `content/en/project/<slug>/index.md`

```yaml
type: "project"
date: "YYYY-MM-DD"
title: "Project Title"
names: [Author1, Author2]           # must match instructor list if applicable
github_repo: "https://github.com/..."
website: ""                          # optional project website
tags: [tag1, tag2]                   # LOWERCASE only
summary: "~75 word description"
image: "cover.png"                   # optional; file must exist in same directory
```

### Module page — `content/en/modules/<slug>/index.md`

```yaml
type: "modules"          # DO NOT change this field
title: "Module Title"
tags: [tag1, tag2]       # lowercase
summary: "~75 word description"
image: "cover.png"       # optional
```

### Site hub page — `content/en/sites/<slug>/index.md`

```yaml
type: "sites"
date: "YYYY-MM-DD"
title: "Institution Name, City, Country"
names: [Organizer1, Organizer2]
website: ""              # optional
summary: "~75 word description"
image: "location.png"
```

---

## Data Files — How to Update

### Add or update an instructor (`data/en/instructors.yaml`)

```yaml
- name: Full Name
  gh: github_username          # GitHub handle (no @)
  email: email@example.com
  website: https://...
  affiliation: Institution Name
  urlaff: https://institution-url.com
```

Place headshot at `static/img/instructors/<github_username>.png` (or `.jpg`).

### Update homepage carousel (`data/en/carousel/*.yaml`)

```yaml
weight: 0                    # display order (lower = first)
title: "Slide Title"
description: >
  <ul class="list-style-none">
    <li>Location</li>
    <li>Year</li>
  </ul>
image: "img/carousel/filename.png"
```

### Update testimonials (`data/en/testimonials/1.yaml`)

```yaml
text: "Quote text here"
name: "Quoted Person Name"
link: "https://..."
avatar: "img/testimonials/avatar.jpg"
```

### Update sponsors/clients (`data/en/clients/1.yaml`, `2.yaml`)

```yaml
title: Sponsor Name
url: https://sponsor-site.com
logo: img/clients/logo.png
```

---

## Custom Shortcodes

| Shortcode | Usage | Purpose |
|---|---|---|
| `gform` | `{{< gform "FORM_ID" >}}` | Embed a Google Form |
| `tabs` / `tab` | `{{< tabs >}}{{< tab name="Tab 1" >}}...{{< /tab >}}{{< /tabs >}}` | Tabbed content sections |
| `class` | `{{< class "css-class-name" >}}...{{< /class >}}` | Wrap content in a CSS class |

---

## Adding New Content

### New student project

1. Create directory: `content/en/project/<slug>/` (use hyphens, no spaces)
2. Create `index.md` with frontmatter above
3. Add cover image to same directory (reference it as `image: "filename.png"`)
4. Write project content in markdown — HTML is allowed
5. Open a PR referencing the tracking issue: `closes #<issue-number>`

### New training module

1. Create `content/en/modules/<slug>/index.md`
2. Set `type: "modules"` (required — do not change)
3. Follow existing modules (e.g., `content/en/modules/git_github/`) as examples
4. Module list layout is at `layouts/modules/list.html`

### New site hub

1. Create `content/en/sites/<slug>/index.md`
2. Add site image to `static/img/locations/` and reference in frontmatter
3. Follow `content/en/sites/toronto/` as an example

### Update schedule/weeks

Edit pages in `content/en/weeks/`. The schedule page at `/weeks/` also outputs an iCal calendar feed.

---

## Deployment

CI/CD is fully automated via `.github/workflows/hugo.yml`:

- **Trigger:** push to `main` branch, or manual workflow dispatch
- **Build:** Hugo 0.128.0 extended + Dart Sass, with `--minify` flag
- **Deploy:** artifacts published to GitHub Pages automatically

No manual deployment steps needed — merge to `main` and the site updates within ~2 minutes.

---

## Key Conventions

- **Tags must be lowercase** — `[machine-learning, fmri]` not `[Machine-Learning, fMRI]`
- **Summaries ~75 words** — used in listing cards; too long breaks layout
- **Directory names use hyphens** — `my-project/` not `my_project/` or `my project/`
- **Do not change `type:` fields** in existing frontmatter — it controls which layout is used
- **HTML is allowed** in markdown (Goldmark unsafe mode enabled)
- **PR descriptions must reference the linked issue** — use `closes #<number>`
- **Submodule must be initialized** before `hugo serve` works locally
- **Instructor photos** named `<github_username>.png` in `static/img/instructors/`

---

## Past Editions

| Year | URL |
|---|---|
| 2025 | https://2025-school-brainhack.github.io/ |
| 2024 | https://2024-school-brainhack.github.io/ |
| 2022 | https://2022-school-brainhack.github.io/ |
| 2021 | https://psy6983.brainhackmtl.org/ |
| 2020 | https://school2020.brainhackmtl.org/ |
| 2019 | https://brainhackmtl.github.io/school2019/ |
| 2018 | https://brainhackmtl.github.io/school2018/ |
