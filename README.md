# Johnson Oliyide — Personal Website

A static academic website for GitHub Pages. The design uses a fixed white background and burgundy accents, with About, Research, CV, Macro Lab, and Contact pages.

## Research content

All nine entries from the existing research page are retained: four policy articles and five academic journal publications. Each abstract opens with an accessible button. Available PDFs are hosted in `papers/` so the download links work directly. An unavailable PDF is explicitly marked as forthcoming; a publisher page is never presented as a direct PDF download.

Edit `content/research.json`, then regenerate the HTML:

```bash
python3 scripts/build.py
```

To add a PDF, save the author's file in `papers/`, set that entry's `pdf` field to `papers/filename.pdf`, and rebuild. To add work in progress, replace the empty section in `scripts/build.py` with the confirmed project information and rebuild.

## Publish on GitHub Pages

1. Use the repository `JohnsonOliyide.github.io`.
2. Commit the website files to `main`.
3. In **Settings → Pages**, choose **Deploy from a branch**, **main**, and **/(root)**.
4. Verify the site at `https://johnsonoliyide.github.io`.
5. After review, add `johnsonoliyide.com` under Pages custom domain and update the domain's DNS records. Keep the current domain pointed to the current website until the new site is ready.

No build service, package installation, database, or API key is required for the live site. The `.openai` directory is only for local preview and is ignored by Git.

## Content verification

The resource-rents article's citation was corrected against its DOI: **2022, Energy Policy 164, 112888**, with O. B. Adekoya, G. E. Ajayi, and M. Suhrab as coauthors. The old website duplicated another article's year, volume, and coauthors.

The CV page uses education and employment already published on the current résumé page. It can be printed or saved as a PDF. Work-in-progress titles are awaiting the author's confirmed list.
