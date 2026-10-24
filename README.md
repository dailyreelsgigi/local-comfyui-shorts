# Local ComfyUI — Cantonese AI short (EP1)

A 46.7-second Cantonese short made entirely on a local ComfyUI install: no cloud rendering, no paid API.

**Watch:** open `index.html` (or the GitHub Pages URL) — the video is embedded there.

## Output

| | |
|---|---|
| Title | 《今晚去邊》EP1 |
| Length | 46.7 s |
| Resolution | 1088 × 608, 24 fps |
| Shots | 5 clips (3–6 shots each) |
| Dialogue | Native Cantonese generated with the picture (MiniMax H3 Ref2VA) |
| Music | ACE-Step 1.5 XL Turbo, 72 BPM instrumental, ducked under dialogue |
| Subtitles | Cantonese, burned in |

## Stack (all local)

- **ComfyUI** with **MiniMax H3 Ref2VA** (open weights) — 5 clips × 360 frames, ~13 min per clip
- Character identity locked with turnaround reference sheets + a clean empty-scene plate per location
- **ACE-Step 1.5 XL Turbo** for the score
- **ffmpeg** for silence trimming, subtitle burn, sidechain ducking, fade-to-black transitions

## Notes that actually mattered

1. The speaker must be visible in frame — otherwise the model puts the line in the listener's mouth.
2. Dialogue above roughly 4.5 Cantonese characters per second loses its word endings.
3. Scene continuity needs the identical scene-description string in every shot of that scene.
4. 15.08 s is the practical ceiling per generated clip; split the scene, not the shot.
5. A first-frame anchor locks the cut points (2 cuts max); without an anchor you get up to 5.

Full workflow: [`workflow.html`](workflow.html)
