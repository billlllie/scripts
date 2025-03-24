const headers = {
    ...$request.headers
};
const ua = headers["User-Agent"];
headers["X-Emby-Authorization"] = headers["X-Emby-Authorization"].replace("VidHub_iOS", "Emby_for_iOS");
headers["User-Agent"] = "Emby/3.2.32-17.41 (Linux;Android 14) ExoPlayerLib/2.13.2";
$done({headers});
