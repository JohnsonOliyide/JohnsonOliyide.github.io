# Johnson Oliyide — Personal Website

A static academic website for GitHub Pages. The design uses a fixed white background and burgundy accents, with About, Pre-PhD Research, CV, Macro Lab, and Contact pages.

## Research content

All nine entries from the existing research page are retained, followed by three confirmed work-in-progress entries. The sections appear in this order: academic journal publications, policy research, and work in progress. Each abstract opens with an accessible button. Available PDFs are hosted in `papers/` so the download links work directly. Published entries without a PDF omit that action. Work-in-progress Abstract and PDF File buttons display “Coming soon” until their content is supplied.

Edit `content/research.json`, then regenerate the HTML:

```bash
python3 scripts/build.py
```

To add a PDF, save the author's file in `papers/`, set that entry's `pdf` field to `papers/filename.pdf`, and rebuild. Update a work-in-progress entry's `abstract` field when its abstract is available; use category `wip` for additional ongoing projects.

## Macro Lab content

Edit `content/macro-lab.json` and rebuild. JointShocks appears first, followed by the Labor Market Tightness Dashboard, Employment Dynamics Dashboard, and Monetary Policy Gap Tracker. Dashboard descriptions were checked against their project pages and repository documentation. JointShocks uses the author's confirmed description of joint and generalized spillover analysis; its public documentation and download URL are pending.

## Publish on GitHub Pages

1. Use the repository `JohnsonOliyide.github.io`.
2. Commit the website files to `main`.
3. In **Settings → Pages**, choose **Deploy from a branch**, **main**, and **/(root)**.
4. Verify the site at `https://johnsonoliyide.github.io`.
5. After review, add `johnsonoliyide.com` under Pages custom domain and update the domain's DNS records. Keep the current domain pointed to the current website until the new site is ready.

No build service, package installation, database, or API key is required for the live site. The `.openai` directory is only for local preview and is ignored by Git.

## Content verification

The resource-rents article's citation was corrected against its DOI: **2022, Energy Policy 164, 112888**, with O. B. Adekoya, G. E. Ajayi, and M. Suhrab as coauthors. The old website duplicated another article's year, volume, and coauthors.

The CV page uses education and employment already published on the current résumé page. It can be printed or saved as a PDF. The three work-in-progress titles, years, and coauthors were transcribed from the author's supplied résumé photo.
