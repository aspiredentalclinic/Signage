# Aspire Dental Signage

Digital signage display for Aspire Dental Clinic, served via GitHub Pages and displayed through AbleSign.

## How It Works

The player loads `images.json` and displays each image fullscreen for 60 seconds, looping back to the start indefinitely.

## Adding / Removing Images

Edit `images.json` only — no changes to `index.html` needed.

```json
[
  "https://aspiredentalclinic.github.io/Signage/image1.jpg",
  "https://aspiredentalclinic.github.io/Signage/image2.jpg"
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
