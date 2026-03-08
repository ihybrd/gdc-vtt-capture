
# gdc-vtt-capture

GDC-vtt-capture is a Python script that helps you download captions from a GDC talk video. It will fetch and merge segmented GDC caption `.vtt` chunks into a single text file. You can use other AI tools to summarize the talk by using this captions file.

## How To Use

1. Login to your GDC Vault account and open the target session page.
2. Play the video, then open browser DevTools -> Network.
3. Find any `.vtt` request and copy its URL.
4. Run this script with that URL as the input parameter.

```bash
python3 capture_gdc_vtt.py "<vtt_segment_url>"
```

An example can be found in the repo, check `run_vtt_capture_example.sh` file.


## How It Works

- Any single `.vtt` URL is used as a sample to get the common caption path template.
- The script brute-forces chunk ids in a while-loop (`..._%d.vtt`) to fetch the full stream.
- If some chunk fails (e.g., timeout or missing file), it logs and skips that chunk.
- After more than `--max-404` 404 responses, it assumes there are no more caption chunks and writes the merged output file.

## Environment Setup

The tools is lightweighted, what you need are

- Python 3
- requests 

## License

MIT. See [LICENSE](./LICENSE).