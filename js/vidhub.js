const headers = {
    ...$request.headers
};
const ua = headers["User-Agent"];
if (/MediaCenter.*/.test(ua) || /VidHub/.test(ua)) {
    console.log("Start to patch");
    headers["X-Emby-Authorization"] = headers["X-Emby-Authorization"].replace("VidHub_iOS", "Emby_for_iOS");
    headers["User-Agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2_1 like Mac OS X)";
}
$done({headers});
