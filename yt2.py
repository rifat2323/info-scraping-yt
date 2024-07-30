from pytube import Channel,Playlist,YouTube

import regex as re
import json


yt = YouTube('https://www.youtube.com/watch?v=at6aeXHF1gg')


c = Channel(yt.channel_url)
vid = c.playlists_html



l = re.search("webCommandMetadata",vid)
pattern = r'"webCommandMetadata":\s*\{(?:[^{}]++|(?R))*\}'
k = re.findall(pattern,vid)
urls =[]
for ks in k:
     json_string = '{' + ks + '}'
     try:
        # Parse the JSON to access its content
        json_data = json.loads(json_string)
        
        # Extract the URL from the JSON
        url = json_data.get('webCommandMetadata', {}).get('url', None)
        
        
        if url:
            urls.append(url)
     except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        
        
playlist_urls = [f"https://www.youtube.com{url}" for url in urls if re.match(r'^/playlist\?', url)]
print(playlist_urls)
fs = open("html.txt","w",encoding="utf-8",errors="replace")
for url in playlist_urls:
    play_l = Playlist(url).video_urls
    print("new url provided")
    for vid in play_l:
        yt =YouTube(vid)
        fs.writelines(f" url:{vid} \n")
        fs.writelines(f" title:{yt.title} \n")
        fs.writelines(f" description:{yt.description} \n")
        fs.writelines(f" vid_info:{yt.vid_info} \n")
        fs.writelines(f" keywords:{yt.keywords} \n")
        fs.writelines(f" views:{yt.views} \n")
        fs.writelines(f" publish_date:{yt.publish_date} \n")
        fs.writelines(f"\n" + "+" * 40 + "\n")
        print(f"getting vide for {vid}")
          
fs.close()        