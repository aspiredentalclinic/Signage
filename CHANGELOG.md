# Changelog

## [2.0.0] - 2025-07-14
### Changed
- Replaced video player with fullscreen image slideshow
- `index.html` now loads from `images.json` instead of `videos.json`
- Each image displays for 60 seconds before advancing

### Added
- `images.json` — playlist file for managing slideshow images
- `home.html` — fullscreen iframe wrapper pointing to GitHub Pages

### Removed
- Video playback functionality
- `videos.json` (superseded by `images.json`)

## [1.1.0] - 2025-07-14
### Added
- `videos.json` playlist file — manage videos without editing `index.html`
- Dynamic video player that fetches playlist and cycles through all videos in order

### Changed
- `index.html` now loads video sources from `videos.json` instead of a hardcoded URL
- Removed `loop` attribute from video element in favour of playlist cycling

### Notes
- Deployed via AbleSign; audio plays automatically without user interaction required

## [1.0.0] - Initial Release
### Added
- Fullscreen looping video player (`index.html`)
- Single hardcoded video source (`clinic_final.mp4`) served via GitHub Pages
