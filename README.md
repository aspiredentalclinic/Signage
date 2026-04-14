# Aspire Dental Signage

Digital signage display for Aspire Dental Clinic, served via GitHub Pages and displayed through AbleSign.

## How It Works

The player loads `videos.json` and plays each video in sequence, looping back to the start indefinitely.

## Adding / Removing Videos

Edit `videos.json` only — no changes to `index.html` needed.

```json
[
  "https://aspiredentalclinic.github.io/Signage/clinic_final.mp4",
  "https://aspiredentalclinic.github.io/Signage/video2.mp4"
]
```

1. Upload the `.mp4` file to the repository
2. Add its GitHub Pages URL to `videos.json`
3. Commit and push — the display updates automatically

## Audio

Audio plays automatically. In AbleSign, ensure **Allow Audio** is enabled on the webpage zone/widget. If there is a global **Autoplay Policy** setting, set it to **No user gesture required**.

## Files

| File | Purpose |
|------|---------|
| `index.html` | Signage player — do not edit for playlist changes |
| `videos.json` | Playlist — add/remove video URLs here |
| `clinic_final.mp4` | Source video file |
