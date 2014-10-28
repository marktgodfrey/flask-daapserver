__all__ = ["dmapDataTypes", "dmapNames", "dmapReverseDataTypes", "dmapCodeTypes"]

dmapCodeTypes = {
    #"f\x8dch": ("dmap.haschildcontainers", "b", 1),
    "abal": ("daap.browsealbumlisting", "c", 12),
    "abar": ("daap.browseartistlisting", "c", 12),
    "abcp": ("daap.browsecomposerlisting", "c", 12),
    "abgn": ("daap.browsegenrelisting", "c", 12),
    "abpl": ("daap.baseplaylist", "b", 1),
    "abro": ("daap.databasebrowse", "c", 12),
    "adbs": ("daap.databasesongs", "c", 12),
    "aeAI": ("com.apple.itunes.itms-artistid", "i", 5),
    "aeCI": ("com.apple.itunes.itms-composerid", "i", 5),
    "aeEN": ("com.apple.itunes.episode-num-str", "s", 9),
    "aeES": ("com.apple.itunes.episode-sort", "i", 5),
    "aeFP": ("com.apple.itunes.req-fplay", "b", 1),
    "aeGD": ("com.apple.itunes.gapless-enc-dr", "i", 5),
    "aeGE": ("com.apple.itunes.gapless-enc-del", "i", 5),
    "aeGH": ("com.apple.itunes.gapless-heur", "i", 5),
    "aeGI": ("com.apple.itunes.itms-genreid", "i", 5),
    "aeGR": ("com.apple.itunes.gapless-resy", "l", 7),
    "aeGU": ("com.apple.itunes.gapless-dur", "l", 7),
    "aeHV": ("com.apple.itunes.has-video", "b", 1),
    "aeMK": ("com.apple.itunes.mediakind", "b", 1),
    "aeNN": ("com.apple.itunes.network-name", "s", 9),
    "aeNV": ("com.apple.itunes.norm-volume", "i", 5),
    "aePC": ("com.apple.itunes.is-podcast", "b", 1),
    "aePI": ("com.apple.itunes.itms-playlistid", "i", 5),
    "aePP": ("com.apple.itunes.is-podcast-playlist", "b", 1),
    "aePS": ("com.apple.itunes.special-playlist", "b", 1),
    "aeSF": ("com.apple.itunes.itms-storefrontid", "i", 5),
    "aeSI": ("com.apple.itunes.itms-songid", "i", 5),
    "aeSN": ("com.apple.itunes.series-name", "s", 9),
    "aeSP": ("com.apple.itunes.smart-playlist", "b", 1),
    "aeSU": ("com.apple.itunes.season-num", "i", 5),
    "aeSV": ("com.apple.itunes.music-sharing-version", "i", 5),
    "agrp": ("daap.songgrouping", "s", 9),
    "aply": ("daap.databaseplaylists", "c", 12),
    "aprm": ("daap.playlistrepeatmode", "b", 1),
    "apro": ("daap.protocolversion", "v", 11),
    "apsm": ("daap.playlistshufflemode", "b", 1),
    "apso": ("daap.playlistsongs", "c", 12),
    "arif": ("daap.resolveinfo", "c", 12),
    "arsv": ("daap.resolve", "c", 12),
    "asaa": ("daap.songalbumartist", "s", 9),
    "asac": ("daap.songartworkcount", "h", 3),
    "asal": ("daap.songalbum", "s", 9),
    "asar": ("daap.songartist", "s", 9),
    "asbk": ("daap.bookmarkable", "b", 1),
    "asbo": ("daap.songbookmark", "i", 5),
    "asbr": ("daap.songbitrate", "h", 3),
    "asbt": ("daap.songbeatsperminute", "h", 3),
    "ascd": ("daap.songcodectype", "i", 5),
    "ascm": ("daap.songcomment", "s", 9),
    "ascn": ("daap.songcontentdescription", "s", 9),
    "asco": ("daap.songcompilation", "b", 1),
    "ascp": ("daap.songcomposer", "s", 9),
    "ascr": ("daap.songcontentrating", "b", 1),
    "ascs": ("daap.songcodecsubtype", "i", 5),
    "asct": ("daap.songcategory", "s", 9),
    "asda": ("daap.songdateadded", "t", 10),
    "asdb": ("daap.songdisabled", "b", 1),
    "asdc": ("daap.songdisccount", "h", 3),
    "asdk": ("daap.songdatakind", "b", 1),
    "asdm": ("daap.songdatemodified", "t", 10),
    "asdn": ("daap.songdiscnumber", "h", 3),
    "asdp": ("daap.songdatepurchased", "t", 10),
    "asdr": ("daap.songdatereleased", "t", 10),
    "asdt": ("daap.songdescription", "s", 9),
    "ased": ("daap.songextradata", "h", 3),
    "aseq": ("daap.songeqpreset", "s", 9),
    "asfm": ("daap.songformat", "s", 9),
    "asgn": ("daap.songgenre", "s", 9),
    "asgp": ("daap.songgapless", "b", 1),
    "ashp": ("daap.songhasbeenplayed", "b", 1),
    "asky": ("daap.songkeywords", "s", 9),
    "aslc": ("daap.songlongcontentdescription", "s", 9),
    "asrv": ("daap.songrelativevolume", "ub", 2),
    "assa": ("daap.sortartist", "s", 9),
    "assc": ("daap.sortcomposer", "s", 9),
    "assl": ("daap.sortalbumartist", "s", 9),
    "assn": ("daap.sortname", "s", 9),
    "assp": ("daap.songstoptime", "i", 5),
    "assr": ("daap.songsamplerate", "i", 5),
    "asss": ("daap.sortseriesname", "s", 9),
    "asst": ("daap.songstarttime", "i", 5),
    "assu": ("daap.sortalbum", "s", 9),
    "assz": ("daap.songsize", "i", 5),
    "astc": ("daap.songtrackcount", "h", 3),
    "astm": ("daap.songtime", "i", 5),
    "astn": ("daap.songtracknumber", "h", 3),
    "asul": ("daap.songdataurl", "s", 9),
    "asur": ("daap.songuserrating", "b", 1),
    "asyr": ("daap.songyear", "h", 3),
    "ated": ("daap.supportsextradata", "h", 3),
    "avdb": ("daap.serverdatabases", "c", 12),
    "mbcl": ("dmap.bag", "c", 12),
    "mccr": ("dmap.contentcodesresponse", "c", 12),
    "mcna": ("dmap.contentcodesname", "s", 9),
    "mcnm": ("dmap.contentcodesnumber", "i", 5),
    "mcon": ("dmap.container", "c", 12),
    "mctc": ("dmap.containercount", "i", 5),
    "mcti": ("dmap.containeritemid", "i", 5),
    "mcty": ("dmap.contentcodestype", "h", 3),
    "mdcl": ("dmap.dictionary", "c", 12),
    "miid": ("dmap.itemid", "i", 5),
    "mikd": ("dmap.itemkind", "b", 1),
    "mimc": ("dmap.itemcount", "i", 5),
    "minm": ("dmap.itemname", "s", 9),
    "mlcl": ("dmap.listing", "c", 12),
    "mlid": ("dmap.sessionid", "i", 5),
    "mlit": ("dmap.listingitem", "c", 12),
    "mlog": ("dmap.loginresponse", "c", 12),
    "mpco": ("dmap.parentcontainerid", "i", 5),
    "mper": ("dmap.persistentid", "l", 7),
    "mpro": ("dmap.protocolversion", "v", 11),
    "mrco": ("dmap.returnedcount", "i", 5),
    "msal": ("dmap.supportsautologout", "b", 1),
    "msas": ("dmap.authenticationschemes", "i", 5),
    "msau": ("dmap.authenticationmethod", "b", 1),
    "msbr": ("dmap.supportsbrowse", "b", 1),
    "msdc": ("dmap.databasescount", "i", 5),
    "msex": ("dmap.supportsextensions", "b", 1),
    "msix": ("dmap.supportsindex", "b", 1),
    "mslr": ("dmap.loginrequired", "b", 1),
    "mspi": ("dmap.supportspersistentids", "b", 1),
    "msqy": ("dmap.supportsquery", "b", 1),
    "msrs": ("dmap.supportsresolve", "b", 1),
    "msrv": ("dmap.serverinforesponse", "c", 12),
    "mstc": ("dmap.utctime", "t", 10),
    "mstm": ("dmap.timeoutinterval", "i", 5),
    "msto": ("dmap.utcoffset", "ui", 6),
    "msts": ("dmap.statusstring", "s", 9),
    "mstt": ("dmap.status", "i", 5),
    "msup": ("dmap.supportsupdate", "b", 1),
    "mtco": ("dmap.specifiedtotalcount", "i", 5),
    "mudl": ("dmap.deletedidlisting", "c", 12),
    "mupd": ("dmap.updateresponse", "c", 12),
    "musr": ("dmap.serverrevision", "i", 5),
    "muty": ("dmap.updatetype", "b", 1),
    "ppro": ("dpap.protocolversion", "i", 5),
    "pret": ("dpap.unknown", "c", 12),
}

dmapDataTypes = {
    1: "b",  # byte
    2: "ub", # unsigned byte
    3: "h",  # short
    4: "uh", # unsigned short
    5: "i",  # integer
    6: "ui", # unsigned integer
    7: "l",  # long
    8: "ul", # unsigned long
    9: "s",  # string
    10: "t", # timestamp
    11: "v", # version
    12: "c", # container
}

dmapNames = { dmapCodeTypes[k][0]: k for k in dmapCodeTypes }
dmapReverseDataTypes = { dmapDataTypes[k]: k for k in dmapDataTypes }