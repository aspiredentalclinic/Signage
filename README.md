# Aspire Dental Signage

Digital signage display for Aspire Dental Clinic, served via GitHub Pages and displayed through AbleSign.

## How It Works

The player loads `videos.json` and displays each video fullscreen, looping back to the start indefinitely.

## Adding / Removing Videos

Edit `videos.json` only — no changes to `index.html` needed.

```json
[
  "https://aspiredentalclinic.github.io/Signage/gumsGuide.mp4"
]
```

1. Upload the image file to the repository
2. Add its GitHub Pages URL to `images.json`
3. Commit and push — the display updates automatically

## Files

| File | Purpose |
|------|---------|
| `index.html` | Signage player — do not edit for playlist changes |
| `images.json` | Playlist — add/remove image URLs here |
| `home.html` | Fullscreen iframe wrapper pointing to GitHub Pages |
| `assets/img/` | Image files served via GitHub Pages |
| `update_images.py` | Script to auto-regenerate `images.json` from `assets/img/` |
