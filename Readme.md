## youtube_search

An async API and a cli tool to search youtube (without using the data API.)

[![asciicast](https://asciinema.org/a/GfXr5ymgna1pCeoLVyvZp20oz.svg)](https://asciinema.org/a/GfXr5ymgna1pCeoLVyvZp20oz)

## install

```bash
pip install utube-search
```

## usage:

The package has a simple cli, which has one subcommand `search`:

```bash
Usage: utube COMMAND <query>
Commands:
  info    information about the tool.
  search  search for videos with query on youtube.
```

## example

### command

```bash
utube search blackholes
```

### output:

```bash
searching for videos using query: blackholes...
                                                  Search Results
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃                           Title ┃ Video URL                           ┃ Duration ┃ View count ┃ Published Time ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│    Black Holes Explained – From │ www.youtube.com/watch?v=e-P5IFTqB98 │ 5:56     │ 17131808   │ 5 years ago    │
│         The Most Powerful Black │ www.youtube.com/watch?v=vLM-v7LeiEg │ 48:01    │ 406185     │ 2 months ago   │
│               Black Holes 101 | │ www.youtube.com/watch?v=kOEDG3j1bjs │ 3:12     │ 3066240    │ 2 years ago    │
│            Monster BLACK HOLE | │ www.youtube.com/watch?v=VzWTyufdkug │ 50:01    │ 6119031    │ 3 years ago    │
│       Black Holes Explained for │ www.youtube.com/watch?v=y8ymU_UBD3I │ 16:20    │ 1449019    │ 2 years ago    │
│        What's Actually Inside A │ www.youtube.com/watch?v=poE8CuucCEg │ 9:28     │ 433273     │ 4 months ago   │
│           Why Black Holes Could │ www.youtube.com/watch?v=yWO-cvGETRQ │ 10:13    │ 21951885   │ 3 years ago    │
│       Black Holes: Crash Course │ www.youtube.com/watch?v=qZWPBKULkdQ │ 12:26    │ 2236560    │ 5 years ago    │
│    Physicist Brian Cox Explains │ www.youtube.com/watch?v=0sr1Xeocuuc │ 5:39     │ 8400688    │ 2 years ago    │
│            The Univese The Most │ www.youtube.com/watch?v=LdtB2xLDcho │ 51:46    │ 17826      │ 4 months ago   │
│         Biggest Black Holes and │ www.youtube.com/watch?v=TMiGQDeSPA0 │ 1:23:28  │ 139783     │ 5 years ago    │
│ Black Holes National Geographic │ www.youtube.com/watch?v=dCxcIzpDgow │ 50:33    │ 99211      │ 3 years ago    │
│                 What Is a White │ www.youtube.com/watch?v=7QFuHb_DYUE │ 10:01    │ 509539     │ 3 months ago   │
│      The Incredible Theory That │ www.youtube.com/watch?v=lff72Sl7GIo │ 11:18    │ 6844       │ 4 months ago   │
│                BLACK HOLE | The │ www.youtube.com/watch?v=X4fcI4PMvwg │ 3:24     │ 5558958    │ 4 years ago    │
│              An Epic Journey to │ www.youtube.com/watch?v=RV170sqhm4Q │ 8:26     │ 1317314    │ 2 months ago   │
│        Soundgarden - Black Hole │ www.youtube.com/watch?v=3mbBbFH9fAg │ 5:21     │ 178116567  │ 10 years ago   │
│                     Black Holes │ www.youtube.com/watch?v=SBl1tQlCkBo │ 50:33    │ 1908747    │ 4 years ago    │
│           How to Understand the │ www.youtube.com/watch?v=zUyH3XhpLTo │ 9:19     │ 7386724    │ 1 year ago     │
└─────────────────────────────────┴─────────────────────────────────────┴──────────┴────────────┴────────────────┘
```

### API

The cli is powered by an async API, which again has only one function:

```bash
async def search(query: str, cache: bool = False, kind="json")
```

Where,
	- `query` is the query string
	- `cache` if set, the results will be saved to disk into `~/.utube_search` directory
	- `kind` is the type of query data returned, it has three valid types: json, dict, str.

### TODO:
- integrate with yl-downloader
- enable sorted output based on user requirement
