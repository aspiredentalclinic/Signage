# Aspire Dental Signage

Digital signage display for Aspire Dental Clinic, served via GitHub Pages and displayed through AbleSign.

## How It Works

The player loads `images.json` and displays each image fullscreen for 60 seconds, looping back to the start indefinitely.

## Adding / Removing Images

Edit `images.json` only — no changes to `index.html` needed.

```json
[
  "https://aspiredentalclinic.github.io/Signage/assets/img/ORTHO.png",
  "https://aspiredentalclinic.github.io/Signage/assets/img/2.png",
  "https://aspiredentalclinic.github.io/Signage/assets/img/3.png",
  "https://aspiredentalclinic.github.io/Signage/assets/img/Aspire Ad signage (297 x 210 mm).png"
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
