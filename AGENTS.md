# Agent instructions for the LUNR Lab website

These instructions apply to the repository and all its subdirectories. Read this
file before editing. Follow the user's latest instructions when they explicitly
change a convention described here.

## Approval required before publishing

**Do not publish or deploy anything to the website without the user's explicit
approval.**

- Keep requested edits local and reviewable until approval is given.
- Do not push commits, trigger deployment workflows, merge changes into a branch
  that deploys the site, or use hosting tools to publish without explicit approval.
- A request to edit, fix, preview, or verify a page does not authorize publication.
- Making this file available to other agents does not authorize a push.
- Complete authorized local work and relevant checks before presenting the result.
  Do not repeatedly ask permission for ordinary local edits.
- Distinguish local changes from live deployment in completion messages. Do not
  imply the public website changed when only local files were edited.
- Only commit changes when requested. Approval to commit does not automatically
  authorize pushing or deployment.
- Keep this file eligible for version control. The user explicitly requested that
  `AGENTS.md` be available to other people and their agents; do not ignore it.

## Project overview

This is the Language Understanding and Reasoning (LUNR) Lab website at Stony Brook
University. It is a static HTML/CSS site with a browser-rendered bibliography.

- Repository: `https://github.com/lunrlab/lunrlab.github.io.git`
- Domain configured in `CNAME`: `lunr.cs.stonybrook.edu`
- There is no application build step or Node package manifest in this checkout.
  Do not introduce a framework or package manager for routine edits.
- Pages use Bootstrap 5.3.0 from a CDN and share `index.css`.
- The bibliography also uses jQuery and Moment loaded from CDNs.

| File or directory | Purpose |
| --- | --- |
| `index.html` | Home page, projects, and Latest News |
| `people.html` | Principal investigator, current students, and alumni |
| `publications.html` | Bibliography template, layout, and Scholar cutoff link |
| `index.css` | Shared styling and responsive layout |
| `site.js` | Publication search, result status, and year navigation |
| `images/` | Logo, student portraits, and project illustrations |
| `nb_scholar.bib` | Bibliography loaded by the publications page |
| `bibtex_js.js` | Existing BibTeX parser and browser renderer |
| `process_bib_file.py` | Filters and sorts a supplied bibliography |
| `parse_bib_file.py` | BibTeX parsing helpers using `pybtex` |
| `raw_nb_scholar_06242025.bib` | Historical export, not the current complete bibliography |
| `requirements.txt` | Python dependency for bibliography tools |
| `README.md` | Setup and bibliography maintenance instructions |
| `CNAME` | Custom domain; preserve unless a change is requested |

## Working in the checkout

- Start with `git status --short` and inspect relevant files. Preserve changes
  belonging to the user or earlier tasks.
- Use `rg` and `rg --files` for searches. Check for more specific instructions
  before editing in a subdirectory.
- Keep changes focused. Avoid unrelated formatting, refactors, dependency updates,
  and corrections to other people's entries.
- Do not reset or discard unrelated work. Do not delete untracked images merely
  because they have not been committed.
- Match image filenames and letter case exactly; hosting may be case sensitive.
- Preserve link destinations unless a correction is requested or verified.
- Do not invent biographies, qualifications, workplaces, portraits, or links.
- Do not contact students or alumni unless explicitly authorized.

## Shared visual design

- The local redesign uses warm ivory backgrounds, deep navy text, a restrained red
  accent, serif headings, and system sans-serif body text. Shared colors and fonts
  are defined in `index.css`; keep all three pages visually consistent.
- Keep the shared header, active navigation state, and contact footer consistent
  across pages. Navigation remains visible on narrow screens without a menu toggle.
- Preserve the original LUNR logo and use image-specific sizing. The user requested
  a larger logo: currently 160 pixels wide on desktop and 140 on narrow screens.
- Keep the layout compact and body text at least 16 pixels. Avoid restoring large
  page introductions, decorative section numbers, promotional closing sections,
  or repeated page links. Cross-page navigation belongs in the shared main menu.
- The home network illustration, director blurb, and duplicate research introduction
  were removed. Keep them absent unless the user requests otherwise. The lab's
  mission statement appears once in the compact home introduction.
- Maintain readable body text, visible keyboard focus, the skip link, reduced-motion
  preferences, and layouts that fit narrow mobile viewports.
- Publication search and year links are generated by `site.js` after the existing
  BibTeX renderer finishes. Preserve author text in rendered entries so author
  search works. Test matching, no-result, and clear-search states after changes.
- In BibTeX templates, classes on `.if` elements are interpreted as field conditions.
  Put presentation classes on a separate wrapper to avoid hiding valid metadata.

## People page

The current section order is:

1. Principal Investigator
2. Current PhD Students
3. Current Masters Students
4. Past PhD Students
5. Past Masters Students
6. Past Bachelors Students

The user removed the Current Bachelors Students placeholder. Do not recreate it
unless requested. Keep heading terminology consistent with the page.

- Current students use `.member-card` profiles within a Bootstrap grid, with
  `.member-photo`, `.member-portrait`, and `.research-interests` for profile details.
  Use a provided image when available, descriptive `alt` text, and the existing
  150-pixel circular portrait treatment. Do not fabricate missing portraits.
- Preserve user-supplied research descriptions unless asked to edit them.
- Alumni use `alumni-grid`, `alumni-card`, `alumni-info`, `alumni-name`, and
  `current-position`, with `alumni-degree` for degree details. Follow neighboring
  entries for markup and spacing.
- Link names to supplied or verified profiles. Preserve meaningful punctuation
  in LinkedIn URLs.
- Keep degree details separately from workplace information. Only label a degree
  as a thesis when supported.
- Check for existing entries before adding someone. Moving a student between
  sections should not leave a duplicate visible entry.
- Follow the user's classification of current or past lab membership. A past lab
  member can still be enrolled at the university.
- If a master's category is ambiguous and context cannot resolve it, clarify
  Current versus Past Masters Students while completing independent work.

## Workplace research

- Verify current employment with public sources. Prefer supplied LinkedIn
  profiles; official employer or university pages and personal professional sites
  can corroborate details when LinkedIn is unavailable.
- Match identities using supplied URLs, education, research, and other professional
  details. A matching name alone is insufficient.
- Headlines and snippets may be incomplete or stale. Check dates and distinguish
  current employment, previous employment, and internships.
- Liked posts and reposts describe other people and do not establish employment
  for the profile owner.
- Do not describe an internship or expired summer position as current permanent
  employment. Label historical internships with dates when including them.
- If only the employer is supported, omit an unverified title. If no current
  workplace is supported, add the name and degree without a workplace claim.
- Preserve the existing display name unless a change is requested. Confirm identity
  before linking a profile that uses a different name.
- Record useful verification dates or sources in concise HTML comments as needed.
  Mention material verification limits in the completion note.

## Home page

- Keep Latest News in reverse chronological order with dates such as `Jul '26`.
  Use the user-supplied year; clarify an ambiguous year instead of guessing.
- Preserve the requested event and names. A defense does not itself establish a
  graduation date or authorize changing a student's category.
- Project diagrams must display completely without cropping or stretching. Use
  `.project-image-container` and `.project-image`, with `width: 100%`, `height: auto`,
  and centered placement.
- Do not restore `h-100` or `object-fit-cover` utilities on project diagrams.
- Prefer specific image classes. Broad `.img-fluid` or `.card .img-fluid` changes
  can unintentionally alter other pages and portraits.

## Publications

- Source profile:
  `https://scholar.google.com/citations?hl=en&user=X3JCGVIAAAAJ&view_op=list_works&sortby=pubdate`
- Include publications from the newest year through **2020 inclusive**. Preserve
  the bottom ellipsis and full Scholar profile link for earlier work.
- Edit `nb_scholar.bib` to update displayed records. Changing only an old raw export
  does not update the page.
- Preserve descending year groups and descending `sortdate` ordering within years.
  `sortdate` is numeric `YYYYMMDD`, with `00` for unknown months or days.
- Keep unique citation keys, valid BibTeX, full authors where available, and working
  citation URLs. Preserve corrected titles such as DIAMONDs.
- Consolidate genuine duplicate records carefully. Similar titles alone do not
  establish that publications or versions are identical.
- Scholar list views can truncate titles, authors, and venues. Use citation details
  or another primary source for complete metadata.
- Keep URL fields compatible with the browser renderer. Rendered URLs must not
  contain literal backslashes before query-string ampersands.
- Keep the cutoff and full-profile link outside `#bibtex_display`; the renderer
  replaces the contents of that container.
- Avoid modifying `bibtex_js.js` for routine publication additions.

The optional bibliography processing workflow is:

```bash
python3 -m venv /tmp/lunr-bib-venv
/tmp/lunr-bib-venv/bin/python -m pip install -r requirements.txt
/tmp/lunr-bib-venv/bin/python process_bib_file.py \
  --bibfile /path/to/fresh-export.bib \
  --output_file /tmp/lunr-processed.bib
```

Review temporary output before replacing `nb_scholar.bib`. The processor filters
out entries before 2020, but does not fetch new data, deduplicate records, or create
missing `sortdate` fields. Regenerating from the historical 2025 export would remove
newer entries and manual corrections; do not do that unintentionally.

## Local preview

Run from the repository root:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Open these local pages:

- `http://127.0.0.1:8765/index.html`
- `http://127.0.0.1:8765/people.html`
- `http://127.0.0.1:8765/publications.html`

Local preview does not publish the website. Reuse an existing preview server when
appropriate; do not terminate unrelated processes.

Opening the publications page with `file://` can block the AJAX request for
`nb_scholar.bib`. Use HTTP for bibliography checks. If changes appear stale, use a
hard refresh (`Cmd+Shift+R` on macOS). CDN dependencies require network access.

## Verification and handoff

- Run `git diff --check` and review the relevant diff.
- For content edits, check placement, names, spelling, dates, links, and duplicates.
  Confirm referenced local images exist.
- For layout or image changes, inspect desktop and narrow browser previews when
  tooling is available. Check full images, natural proportions, readable text,
  and horizontal overflow.
- For bibliography changes, check actual rendered entries, year and date ordering,
  valid links, and the visible cutoff. Static HTML alone does not verify the
  JavaScript-generated list.
- Use existing tools. Do not add a test framework for routine content edits or
  claim browser verification that was not performed.
- Keep temporary scripts, downloads, screenshots, and browser profiles outside the
  repository, such as under `/tmp`, unless an artifact is requested.
- Finish with the change, relevant verification, and any unresolved source limits.
  State that edits remain local when publishing has not been approved.
