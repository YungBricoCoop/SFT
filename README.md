# Spotify For Terminal

SFT is a simple python app that makes request to spotify to display the current playing song, you can also press f1 to play next song, g2 to play previous and f3 to pause

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install -r requirements.txt
```
You need to get a  [TOKEN](https://developer.spotify.com/console/get-users-currently-playing-track/)  to use this app. Just choose thse two scopes 
<b> user-read-currently-playing</b> , <b>user-modify-playback-state</b>
Just change the token value in the code

```python
ACCESS_TOKEN = YOUR_TOKEN
```
## Usage

```bash
python SFT.py
```

## Example

```bash
python mlg.py "OnlyfansBabes1" 10 2 "new" 1 True True "mlg.txt"
```

## Result

![IMG](https://elwan.ch/MLG/github3.png)
