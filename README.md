# gdc-vtt-capture

Fetch and merge segmented GDC caption `.vtt` chunks into a single text file.

## How To Use

1. Login to your GDC Vault account and open the target session page.
2. Play the video, then open browser DevTools -> Network.
3. Find any `.vtt` request and copy its URL.
4. Run this script with that URL as the input parameter.

## How It Works

- Any single `.vtt` URL is used as a sample to get the common caption path template.
- The script brute-forces chunk ids in a while-loop (`..._%d.vtt`) to fetch the full stream.
- If some chunk fails (e.g., timeout or missing file), it logs and skips that chunk.
- After more than `--max-404` 404 responses, it assumes there are no more caption chunks and writes the merged output file.

## Environment Setup

Requires Python 3.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python3 capture_gdc_vtt.py "<vtt_segment_url>"
```

Example:

```bash
python3 capture_gdc_vtt.py \
  "https://.../index_4_0_33.vtt" \
  --output captions.txt \
  --max-range 1000 \
  --max-404 3
```

## Optional: Run Batch Script on macOS

```bash
./run_vtt_capture_example.sh
```

## License

MIT. See [LICENSE](./LICENSE).
