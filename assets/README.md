# AMAYA — client media

Drop files in at exactly these paths and filenames. Nothing else needs to change:
the page picks them up automatically, and any slot without a file stays empty
rather than showing a broken image.

## Copper Ore Mine — mines.html#copper
    assets/images/mines/copper/copper-mine-1.jpg   ← also used as the large hero image
    assets/images/mines/copper/copper-mine-2.jpg
    assets/images/mines/copper/copper-mine-3.jpg
    assets/videos/mines/copper/copper-mine-video.mp4
    assets/videos/mines/copper/copper-mine-video.webm   (optional, smaller)
    assets/videos/mines/copper/copper-mine-poster.jpg   (still frame, optional)

## Iron Ore Mine — mines.html#iron
    assets/images/mines/iron/iron-mine-1.jpg       ← also used as the large hero image
    assets/images/mines/iron/iron-mine-2.jpg
    assets/images/mines/iron/iron-mine-3.jpg
    assets/videos/mines/iron/iron-mine-video.mp4
    assets/videos/mines/iron/iron-mine-video.webm       (optional)
    assets/videos/mines/iron/iron-mine-poster.jpg       (optional)

## Leadership portraits — leadership.html
    assets/images/leadership/satish-naidu.jpg
    assets/images/leadership/jitendra-khatwani.jpg
    assets/images/leadership/gopal-agrawal.jpg
    assets/images/leadership/marcelo-astengo-montenegro.jpg

## Specifications
| Asset | Size | Ratio | Format | Target weight |
|---|---|---|---|---|
| Mine hero / gallery | 2400 px wide or more | landscape, 3:2 works best | JPG | under 300 KB each |
| Mine video | 1920×1080 | 16:9 | MP4 (H.264) + WebM | under 10 MB |
| Leadership portrait | 1200×1500 or larger | 4:5 portrait | JPG | under 250 KB |

Externally hosted media: the `src` attributes are plain relative paths, so they
can be swapped for absolute URLs (a CDN, S3, Vimeo/YouTube file URL) without any
other change to the markup.
