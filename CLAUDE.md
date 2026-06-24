# Project: Loopstack Page

## Deployment Rules

- NEVER suggest drag and drop to deploy to Netlify

- Always use `netlify deploy` for previews

- Always use `netlify deploy --prod` for production

- Netlify site: jazzy-brioche-dd1bf4

## Integrations
- Contact form uses Netlify Forms for client inquiries

## 3D / Animations
- Using Three.js for 3D effects
- Keep 3D performant — must work on mobile
- Fallback gracefully if WebGL not supported

## Stack

- Frontend: HTML/CSS/JS (static site)

- Hosting: Netlify (CLI linked)

- Supabase project (cxsudbjemmkgasmuiega) — available if needed, but not currently used

- Region: West EU Ireland

## Coding Preferences

- I am not an expert programmer, explain what you are doing briefly

- Make changes incrementally, not all at once

- Confirm before making large changes

- Keep code clean and well commented

## Known Issues / Notes

- Contact form uses **Netlify Forms** — just add `netlify` attribute to `<form>` tag and a hidden `form-name` field. No backend code needed. Submissions appear in Netlify dashboard > Forms.
- The old custom function at `netlify/functions/contact.js` has been removed (replaced by Netlify Forms)
- Custom 404 page at 404.html
- llms.txt for AI crawler/AEO optimization
- About page at about.html (linked in nav/footer)
