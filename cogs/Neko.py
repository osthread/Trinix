#Required Imports
from random import choice
from discord.ext import commands, tasks

import random
import discord

#Links... I will be using a API in the future.
feedGIF = "https://c.tenor.com/Aflxvrwa0woAAAAC/kawaii-wholesome.gif","https://c.tenor.com/Aflxvrwa0woAAAAC/kawaii-wholesome.gif","https://c.tenor.com/euV-iahrkMoAAAAC/radit-succ-anime-eat.gif","https://c.tenor.com/_Wn5KdSnphEAAAAd/anime-feed-anime.gif","https://c.tenor.com/xS09IqCS1e0AAAAd/anime-anime-boy.gif","https://c.tenor.com/JHqOKnXVNDQAAAAM/azunom-feed.gif","https://c.tenor.com/CHTk5L8ls8cAAAAd/eat-food.gif","https://c.tenor.com/gIbE9pZ7raYAAAAM/wataten-watashi-ni-tenshi-ga-maiorita.gif","https://c.tenor.com/255Z_vjnkF8AAAAM/anime-girl.gif","https://c.tenor.com/7iDuLLtmeogAAAAC/kin-iro-mosaic-kinmosa.gif","https://c.tenor.com/njHpJO9PoKYAAAAM/somali-somali-and-the-forest-spirit.gif","https://c.tenor.com/0NfPiObsw8QAAAAM/feed-ryuko.gif","https://c.tenor.com/pTKnWhT6FmMAAAAd/anime-feed.gif"  
slapGIF = "https://c.tenor.com/PeJyQRCSHHkAAAAC/saki-saki-mukai-naoya.gif","https://c.tenor.com/Ws6Dm1ZW_vMAAAAC/girl-slap.gif","https://c.tenor.com/E3OW-MYYum0AAAAC/no-angry.gif","https://c.tenor.com/wOCOTBGZJyEAAAAC/chikku-neesan-girl-hit-wall.gif","https://c.tenor.com/noSQI-GitQMAAAAC/mm-emu-emu.gif","https://c.tenor.com/dojL-xM5KuIAAAAC/slapping-slap-back.gif","https://c.tenor.com/VlSXTbFcvDQAAAAC/naruto-anime.gif","https://c.tenor.com/dyp57YWeUY0AAAAC/oreimo-dumb.gif","https://c.tenor.com/ra17G61QRQQAAAAC/tapa-slap.gif","https://c.tenor.com/OuYAPinRFYgAAAAC/anime-slap.gif","https://c.tenor.com/jgImPggI1ZMAAAAC/bakugo-anime-slap.gif","https://c.tenor.com/AlM5Pxv06fUAAAAC/anime-slap.gif"  
kickkGIF = "https://c.tenor.com/EcdG5oq7MHYAAAAC/shut-up-hit.gif","https://c.tenor.com/Lyqfq7_vJnsAAAAC/kick-funny.gif","https://c.tenor.com/Qs9NYCf1b4YAAAAM/shida-midori-midori.gif","https://c.tenor.com/2U9tTXuO_gUAAAAd/kick-anime.gif","https://c.tenor.com/2l13s2uQ6GkAAAAC/kick.gif","https://c.tenor.com/kvxt9X-gXqQAAAAC/anime-clannad.gif","https://c.tenor.com/4F6aGlGwyrwAAAAd/sdf-avatar.gif","https://c.tenor.com/lxd8SO_uRIYAAAAC/anime-kick.gif","https://c.tenor.com/NYZq5QT9o-UAAAAC/chuunibyou-nibutani.gif","https://c.tenor.com/mEgexCY-65QAAAAC/toradora-taiga.gif","https://c.tenor.com/bpgPEPfFlnIAAAAd/yeet-anime.gif"  
kissGIF = "https://c.tenor.com/I8kWjuAtX-QAAAAC/anime-ano.gif","https://c.tenor.com/SqpFZQfcyEgAAAAC/anime-kiss.gif","https://c.tenor.com/V0nBQduEYb8AAAAM/anime-kiss-making-out.gif","https://c.tenor.com/03wlqWILqpEAAAAC/highschool-dxd-asia.gif","https://c.tenor.com/F02Ep3b2jJgAAAAC/cute-kawai.gif","https://c.tenor.com/I8kWjuAtX-QAAAAC/anime-ano.gif","https://c.tenor.com/wDYWzpOTKgQAAAAC/anime-kiss.gif","https://c.tenor.com/4ofp_xCUBxcAAAAC/eden-of-the-east-akira-takizawa.gif","https://c.tenor.com/v4Ur0OCvaXcAAAAd/koi-to-uso-kiss.gif","https://c.tenor.com/dJU8aKmPKAgAAAAd/anime-kiss.gif","https://c.tenor.com/TnjL6WcdkkwAAAAd/anime-kiss.gif","https://c.tenor.com/Ze6FyEgy4WAAAAAC/kiss-anime.gif","https://c.tenor.com/HgV0doOr_YoAAAAC/golden-time-anime.gif",  
hugGIF = "https://c.tenor.com/S3KQ1sDod7gAAAAC/anime-hug-love.gif","https://c.tenor.com/F1VUry86n7kAAAAC/hug-anime.gif","https://c.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif","https://c.tenor.com/xgVPw2QK5n8AAAAC/sakura-quest-anime.gif","https://c.tenor.com/G9yuomdknAsAAAAd/anime-couple.gif","https://c.tenor.com/xgVPw2QK5n8AAAAC/sakura-quest-anime.gif","https://c.tenor.com/xIuXbMtA38sAAAAd/toilet-bound-hanakokun.gif","https://c.tenor.com/EKS8EWkhZJUAAAAC/anime-anime-hug.gif","https://c.tenor.com/EnfEuWDXthkAAAAC/hug-couple.gif","https://c.tenor.com/c8M8yU1q6c4AAAAC/hug-anime.gif","https://c.tenor.com/VqazOH8fQ8gAAAAC/anime-hug.gif","https://c.tenor.com/83QLplerW8sAAAAC/anime-hug.gif","https://c.tenor.com/dIvoDyyk5LIAAAAC/anime-hug-sweet.gif","https://c.tenor.com/Qw4m3inaSZYAAAAC/crying-anime-kyoukai-no-kanata-hug.gif","https://c.tenor.com/pcULC09CfkgAAAAC/hug-anime.gif","https://c.tenor.com/35RotStN1BkAAAAC/anime-hug-anime.gif","https://c.tenor.com/sBFE3GeNpJ4AAAAC/tackle-hug-couple.gif","https://c.tenor.com/pMh2InORon0AAAAC/anime-hug.gif","https://c.tenor.com/ljXMDMzMaxcAAAAC/cute-anime.gif","https://c.tenor.com/ncblDAj_2FwAAAAC/abrazo-hug.gif","https://c.tenor.com/0vl21YIsGvgAAAAC/hug-anime.gif","https://c.tenor.com/Pd2sMiVr09YAAAAC/hug-anime-hug.gif","https://c.tenor.com/nmzZIEFv8nkAAAAC/hug-anime.gif"  
cuddleGIF = "https://c.tenor.com/08vDStcjoGAAAAAd/cuddle-anime-hug-anime.gif","https://c.tenor.com/BmbTYhCZ5UsAAAAC/yuri-sleeping-yuri-sleep.gif","https://c.tenor.com/wwd7R-pi7DIAAAAC/anime-cuddle.gif","https://c.tenor.com/okeP090NK1cAAAAC/anime-couples.gif","https://c.tenor.com/GuHHnDT6quYAAAAd/anime-couples.gif","https://c.tenor.com/0PIj7XctFr4AAAAM/a-whisker-away-hug.gif","https://c.tenor.com/zvlN9ZJEaj4AAAAC/anime-hug.gif","https://c.tenor.com/GuHHnDT6quYAAAAd/anime-couples.gif","https://c.tenor.com/ch1kq7TOxlkAAAAC/anime-cuddle.gif","https://c.tenor.com/ItpTQW2UKPYAAAAC/cuddle-hug.gif","https://c.tenor.com/5UwhB5xQSTEAAAAC/anime-hug.gif","https://c.tenor.com/xMD2hPYkXasAAAAC/anime-snuggle.gif","https://c.tenor.com/8TwoveHk9n8AAAAC/anime-cuddle.gif","https://c.tenor.com/ZhwUZCqJCNMAAAAM/love-you.gif","https://c.tenor.com/ABT86RpJUMUAAAAC/love-asuna.gif"  
patGIF = "https://c.tenor.com/E6fMkQRZBdIAAAAC/kanna-kamui-pat.gif","https://c.tenor.com/wLqFGYigJuIAAAAC/mai-sakurajima.gif","https://c.tenor.com/TDqVQaQWcFMAAAAC/anime-pat.gif","https://c.tenor.com/AnxesEqY2RwAAAAC/pat-anime.gif","https://c.tenor.com/JWx5wmF6bqAAAAAC/charlotte-pat.gif","https://c.tenor.com/N41zKEDABuUAAAAC/anime-head-pat-anime-pat.gif","https://c.tenor.com/8DaE6qzF0DwAAAAC/neet-anime.gif","https://c.tenor.com/muVzMQS6mW0AAAAM/pat-anime.gif","https://c.tenor.com/tYS5DBIos-UAAAAM/kyo-ani-musaigen.gif","https://c.tenor.com/YDuiSAaax_cAAAAC/anime-pat-head-pats.gif","https://c.tenor.com/G14pV-tr0NAAAAAC/anime-head.gif","https://c.tenor.com/QAIyvivjoB4AAAAC/anime-anime-head-rub.gif","https://c.tenor.com/g75K3KA3VeAAAAAd/anime-sleep.gif","https://c.tenor.com/kM1mVaXE8Y8AAAAC/kaede-azusagawa-kaede.gif","https://c.tenor.com/Q9W-bzJo-4sAAAAM/anime-head-pat.gif","https://c.tenor.com/smeOhSMHr9QAAAAC/behave-anime.gif","https://c.tenor.com/RDfGm9ftwx0AAAAC/anime-pat.gif","https://c.tenor.com/_0WADxsz5QYAAAAC/kawaii-pat-anime-kawaii.gif","https://c.tenor.com/w5cGw7u1NsAAAAAC/anime-pat.gif","https://c.tenor.com/zBPha3hhm7QAAAAC/anime-girl.gif","https://c.tenor.com/U2vAab9-3IkAAAAC/anime-pat.gif","https://c.tenor.com/v_2iFqgV904AAAAC/anime-pat.gif","https://c.tenor.com/E7Ll04_an30AAAAC/anime-pat.gif","https://c.tenor.com/JDeFidfZVfcAAAAC/raphtalia-shield-hero.gif"
punchGIF = "https://c.tenor.com/SwMgGqBirvcAAAAC/saki-saki-kanojo-mo-kanojo.gif","https://c.tenor.com/vv1mgp7IQn8AAAAM/tgggg-anime.gif","https://c.tenor.com/HCde75pCLAcAAAAC/tokyo-revengers-smiley.gif","https://c.tenor.com/wYyB8BBA8fIAAAAd/some-guy-getting-punch-anime-punching-some-guy-anime.gif","https://c.tenor.com/--80HfIQWT4AAAAd/punchy-one-punch-man.gif","https://c.tenor.com/SwMgGqBirvcAAAAC/saki-saki-kanojo-mo-kanojo.gif","https://c.tenor.com/jMVkUG5ouL8AAAAC/punch-anime.gif","https://c.tenor.com/3TvlgppifSMAAAAC/anime-girls.gif","https://c.tenor.com/_kn9cwnIQgkAAAAd/anime-blush.gif","https://c.tenor.com/0vILKVxQcqwAAAAd/anime-punch.gif","https://c.tenor.com/JfTmqjERkSkAAAAC/anime-punch.gif","https://c.tenor.com/jy3svkjYYeIAAAAC/anime-punch.gif","https://c.tenor.com/s3L7pwiBrIcAAAAM/haku-naruto.gif","https://c.tenor.com/BQn6XR66iAUAAAAC/gohan-dyspo.gif","https://c.tenor.com/BESYHOr_4uIAAAAd/v9-fight.gif","https://c.tenor.com/WoMVDZsYYxkAAAAC/punch-anime.gif","https://c.tenor.com/-MuCeCW_TEMAAAAC/anime-my-hero-academia.gif","https://c.tenor.com/SPsqUzhCu8QAAAAC/hajimenoippo-ippo.gif","https://c.tenor.com/UTZsIw3HCTUAAAAC/pain-anime.gif","https://c.tenor.com/pUWz5RrxBJEAAAAd/punch-anime.gif","https://c.tenor.com/jHMMYIoutWMAAAAC/mob100-anime.gif","https://c.tenor.com/5F0IyxzxMbEAAAAC/manjiro-sano-sano-manjiro.gif","https://c.tenor.com/DswSb-BM0s8AAAAC/rokuro-twin-star-exorcists.gif","https://c.tenor.com/v4vdMDSRWSEAAAAM/fighting-anime.gif" 
stompGIF = "https://c.tenor.com/zvIh79DchJ8AAAAM/hologra-hololive.gif","https://c.tenor.com/D67kRWw_cEEAAAAC/voz-dap-chym-dap-chym.gif","https://c.tenor.com/aAvEGbU2WK0AAAAd/maria-osawa-canaan.gif","https://c.tenor.com/LxoWv1cv5UgAAAAd/kintaro-oe.gif","https://c.tenor.com/kU3pH60xJZcAAAAC/anime-stomp.gif","https://c.tenor.com/uccJbpLOxE0AAAAC/neo-rwby-anime.gif","https://c.tenor.com/W_WqQw4_zp8AAAAC/anime-stomp.gif"
madGIF = "https://c.tenor.com/yCR6JOoxS6wAAAAd/anime-angry.gif","https://c.tenor.com/rzDkOlEDun0AAAAC/hayase-nagatoro-nagatoro-angry.gif","https://c.tenor.com/G_YeALOH-iAAAAAC/mao-amatsuka-mad.gif","https://c.tenor.com/lBlcEFqoDnEAAAAM/annoyed-anime.gif","https://c.tenor.com/X3x3Y2mp2W8AAAAC/anime-angry.gif","https://c.tenor.com/2uSb2XPxYNUAAAAC/mad-angry.gif","https://c.tenor.com/yqJW9_9P4tQAAAAC/obito-naruto.gif","https://c.tenor.com/8yMqNs21uTQAAAAd/anime-waiting-for-text.gif","https://c.tenor.com/b76QnX1XVAcAAAAC/raiva-anime.gif","https://c.tenor.com/ikKAd57zDEwAAAAd/anime-mad.gif","https://c.tenor.com/DJk8RI8ZLvQAAAAC/angry-mad.gif","https://c.tenor.com/MvKZZ7JCkUMAAAAC/anime-angry.gif","https://c.tenor.com/4a4d9b6kbKEAAAAC/angry-anime-angry.gif","https://c.tenor.com/0FeJicQD9mMAAAAC/anime-girl.gif","https://c.tenor.com/MifS9QJUGA4AAAAC/anime-angry.gif"
byeGIF = "https://c.tenor.com/_Exw4V_izbkAAAAC/cute-anime.gif","https://c.tenor.com/sPgkxwu-MRsAAAAC/anime-tokyo-revengers.gif","https://c.tenor.com/sRKHQSK5hhEAAAAM/izaya-orihara.gif","https://c.tenor.com/9QbNdvPAjY4AAAAC/wave-bye.gif","https://c.tenor.com/rza_O7Gdk9UAAAAC/anime-bye.gif","https://c.tenor.com/EJ1C6RDW3YoAAAAC/kakashi-bye-bye-anime.gif","https://c.tenor.com/q80PMcmrxDwAAAAd/anime-girl.gif","https://c.tenor.com/17IgpB1KexsAAAAC/trash-disappointed.gif","https://c.tenor.com/1OKqJuV6Bn0AAAAC/anime-bye.gif","https://c.tenor.com/u_tgy22DxOsAAAAM/killua-kil.gif","https://c.tenor.com/s-J6vqs61fkAAAAC/bye-pikachu.gif","https://c.tenor.com/JrdqxQTzNL0AAAAM/arigato-fail.gif","https://c.tenor.com/3n4HIgnnvpYAAAAM/anime-anime-boy.gif","https://c.tenor.com/LnBP33iICOkAAAAC/finral-black-clover.gif"
laughGIF = "https://c.tenor.com/XQxOkKXFG7oAAAAC/satania-laugh.g","https://c.tenor.com/fbWCY-1exTsAAAAC/bokura-wa-minna-kawaisou-gifs-to-reaction.g","https://c.tenor.com/adZJSzcIDfEAAAAC/shinya-laugh.g","https://c.tenor.com/uiiTHEWlNQ8AAAAC/anime-laugh.g","https://c.tenor.com/GpVrlLpkBEsAAAAC/haha-anime.g","https://c.tenor.com/An-9HfjvNkwAAAAC/kuroo-tetsurou-haikyuu.g","https://c.tenor.com/-bB2JahXkMoAAAAC/light-yagami.g","https://c.tenor.com/ibc6FwAYamEAAAAM/black-clover-anime.g","https://c.tenor.com/9f3oQifMmrAAAAAC/jujuju-anime.g","https://c.tenor.com/CAJWKDzTbFEAAAAC/hayase-nagatoro-nagatoro-hehe.g","https://c.tenor.com/5INXYo8F0bEAAAAd/takagi-laugh.g","https://c.tenor.com/GwJ2vJ1gnfcAAAAC/anime-anime-laughing.g","https://c.tenor.com/3SMAyDkjv6MAAAAd/akane-shinj%C5%8D-shinjou-akane.gif"
pokeGIF = "https://c.tenor.com/3dOqO4vVlr8AAAAC/poke-anime.gif","https://c.tenor.com/Ur9uVvSUd1oAAAAM/boop-rascal-does-not-dream-of-bunny-girl-senpai.gif","https://c.tenor.com/gMqsQ1wwbhgAAAAC/anime-poke.gif","https://c.tenor.com/7huC9ySUwnoAAAAC/suzumiya-haruhi-kyon.gif","https://c.tenor.com/t6ABAaRJEA0AAAAC/oreimo-ore-no-im%C5%8Dto-ga-konna-ni-kawaii-wake-ga-nai.gif","https://c.tenor.com/1YMrMsCtxLQAAAAC/anime-poke.gif","https://c.tenor.com/NjIdfk7i3bsAAAAC/poke-poke-poke.gif","https://c.tenor.com/G5u3bfszOPMAAAAC/anime-picking-nose.gif","https://c.tenor.com/QgeL3MJhrpEAAAAC/bite-anime.gif","https://c.tenor.com/YrF6Rm4Lw0MAAAAC/cowboy-bebop-edward.gif","https://c.tenor.com/-yoTM4LZpqEAAAAC/naruto-sasuke.gif","https://c.tenor.com/jNx0V84WbqkAAAAC/anime-anime-poke.gif"
blushGIF = "https://c.tenor.com/cjFjOFwZODIAAAAC/anime-girl.gif","https://c.tenor.com/JhO1fYhvP14AAAAC/face-blush.gif","https://c.tenor.com/T51BLj_Cj8cAAAAC/blush.gif","https://c.tenor.com/VrfSZUjiWn4AAAAC/shy-anime.gif","https://c.tenor.com/drXL2anR7pwAAAAC/karma-anime.gif","https://c.tenor.com/DtgfUZeeuk8AAAAC/vtuber-anime.gif","https://c.tenor.com/cjFjOFwZODIAAAAC/anime-girl.gif","https://c.tenor.com/d3AEjdxSfawAAAAC/anime-blush.gif","https://c.tenor.com/T51BLj_Cj8cAAAAC/blush.gif","https://c.tenor.com/dH4YL72had0AAAAC/blush-anime.gif",  
danceGIF = "https://c.tenor.com/mKTS5nbF1zcAAAAd/cute-anime-dancing.gif","https://c.tenor.com/DbRUHnh1JfsAAAAM/chika-chika-dance.gif","https://c.tenor.com/PXrldoXexykAAAAC/anime-dance.gif","https://c.tenor.com/TVFrC38WTRQAAAAC/celebrate-shinkoukei.gif","https://c.tenor.com/KxQGAWA0BBAAAAAd/hinata-hinata-hyuga.gif","https://c.tenor.com/qXWBVDCCcWoAAAAd/anime-dance.gif","https://c.tenor.com/tNulr7DcsZAAAAAC/yuru-yuri-kyoko.gif",
sneezeGIF = "https://c.tenor.com/cn9tJE3QvBIAAAAM/anime-sneeze.gif","https://c.tenor.com/FZ_dO1DeKHcAAAAC/itona-assassination.gif","https://c.tenor.com/p9oeR9nOtnQAAAAC/eru-chitanda-sneeze.gif","https://c.tenor.com/7y6eR_Oa5wgAAAAC/arifureta-sneeze.gif","https://c.tenor.com/rN07jeUW1eEAAAAM/anime-sneeze.gif","https://c.tenor.com/ZnyCVcHsHK4AAAAd/allergies-sneeze.gif","https://c.tenor.com/qfYsHuCh7BQAAAAC/sneeze-anime.gif"
killGIF = "https://c.tenor.com/Mn4W4D899WEAAAAM/ira-gamagoori-attack.gif","https://c.tenor.com/py184W4488kAAAAC/anime.gif","https://c.tenor.com/Ze50E1rW44UAAAAM/akudama-drive.gif","https://c.tenor.com/Wq-Un4pZq50AAAAC/giant-scissor.gif","https://c.tenor.com/z5HVuzCiMWUAAAAd/angels-of-death-anime.gif","https://c.tenor.com/KxFfj9DgILoAAAAC/toradora-taiga.gif",  
whatGIF = "https://c.tenor.com/aUeurMFvFN8AAAAC/chizuru-hishiro-confused.gif","https://c.tenor.com/96mR_W6LE1EAAAAC/anime-confusion-what.gif","https://c.tenor.com/XNxXLT5i2j8AAAAC/aoba-huh.gif","https://c.tenor.com/kofcVMIWCUoAAAAd/huh-anime-what.gif","https://c.tenor.com/USMq7AuR7LkAAAAd/nani.gif","https://c.tenor.com/y0lat7iYGOUAAAAC/what-day-is-it-huh.gif","https://c.tenor.com/96mR_W6LE1EAAAAC/anime-confusion-what.gif","https://c.tenor.com/zaA5Pjj5uLEAAAAC/what-anime.gif","https://c.tenor.com/STTCuGNqXr0AAAAC/anime-meme-anime.gif",  
thinkingGIF = "https://c.tenor.com/t80Qwz2QouMAAAAC/yuru-yuri-ayano-sugiura.gif","https://c.tenor.com/Rha6TlXId_oAAAAM/gon-freecss-wondering.gif","https://c.tenor.com/mG4E8oJCI2gAAAAC/loading-thinking.gif","https://c.tenor.com/fk67OlKF0GIAAAAC/anime-kawaii.gif","https://c.tenor.com/LnvBjRH4rYwAAAAd/anime-boy.gif","https://c.tenor.com/t80Qwz2QouMAAAAC/yuru-yuri-ayano-sugiura.gif","https://c.tenor.com/nqA9OzT3JzMAAAAC/anime-doubt.gif","https://c.tenor.com/psP-zXQWEyIAAAAC/anime-girl.gif","https://c.tenor.com/JEFQ_QZs8SEAAAAC/well-think.gif","https://c.tenor.com/zmqgvCaJ1yEAAAAC/aqua-konosuba.gif"  
handholdingGIF = "https://c.tenor.com/WUZAwo5KFdMAAAAd/love-holding-hands.gif","https://c.tenor.com/6HrHMauHVbYAAAAC/hand-handholding.gif","https://c.tenor.com/QO3T5tZ4Ia4AAAAd/mai-sakurajima-rascal-does-not-dream-of-bunny-girl-senpai.gif","https://c.tenor.com/6734QJU2yOwAAAAC/yato-anime.gif","https://c.tenor.com/FOepfGFozJEAAAAd/holding-hands-couple.gif","https://c.tenor.com/pqve83ZQ8d8AAAAC/anime-shida-kuroha.gif","https://c.tenor.com/WLnNDNpc8-UAAAAd/konosuba-kono-subarashii.gif","https://c.tenor.com/5HKo-J3sklwAAAAC/walk-anime.gif","https://c.tenor.com/spo9s3TuhvsAAAAC/naruto-anime.gif","https://c.tenor.com/WrSGVKCUHHEAAAAC/hanako-blushing.gif","https://c.tenor.com/wC3hJXbQtYMAAAAd/touch-hands.gif"  
smileGIF = "https://c.tenor.com/nBWlYPbKxzwAAAAC/anime-happy.gif","https://c.tenor.com/3fAZZncIHDQAAAAM/smile-anime.gif","https://c.tenor.com/B5mG_MXzno0AAAAC/anime-taiga-aisaka.gif","https://c.tenor.com/Q--iyrFnBw8AAAAC/anime-smile.gif","https://c.tenor.com/DbRVEHMsm-YAAAAC/yoruka-smile-yoruka.gif","https://c.tenor.com/PfMkNZdluAkAAAAC/haru-yoshida-tonari-no-kaibutsu-kun.gif","https://c.tenor.com/3EcCzBCBXbYAAAAC/yato-anime.gif","https://c.tenor.com/PuX9_sU4VToAAAAC/daddy-little.gif","https://c.tenor.com/kU3-dUX2y8cAAAAC/shy-worried.gif"  
squeezeGIF = "https://c.tenor.com/iEXZT4FlC0EAAAAM/koisuru-asteroid-asteroid-in-love.gif","https://c.tenor.com/ixaDEFhZJSsAAAAC/anime-choke.gif","https://c.tenor.com/tX3V1uUJ4igAAAAC/chino-tighten.gif","https://c.tenor.com/OoNOnGP3xq4AAAAC/anime-thighs-anime-thighs-curshing.gif","https://c.tenor.com/0lbLTHLAqIMAAAAC/cute-fun.gif","https://c.tenor.com/EDJXYEkQu6MAAAAC/noragami-yato.gif","https://c.tenor.com/3eZH8PlHEDQAAAAC/tanakakun-squishy-face.gif","https://c.tenor.com/cg9Yp4fu7VQAAAAC/squishy-cheeky.gif"  
biteGIF = "https://c.tenor.com/IKDf1NMrzsIAAAAM/anime-acchi-kocchi.gif","https://c.tenor.com/nkNsOraAx4AAAAAM/anime-bite.gif","https://c.tenor.com/w4T323o46uYAAAAM/anime-bite.gif","https://c.tenor.com/hwCVSWyji0QAAAAC/anime-bite.gif","https://tenor.com/4sAB.gif","https://c.tenor.com/mXc2f5NeOpgAAAAC/no-blood-neck-bite.gif","https://tenor.com/view/%E0%B8%87%E0%B9%88%E0%B8%B3%E0%B9%86-eat-bite-turtle-gif-15516240","https://c.tenor.com/view/bite-gif-19326440","https://c.tenor.com/view/bite-gif-22830209","https://c.tenor.com/1egHkU3e_8cAAAAC/girl-bite.gif"
footer = "https://cdn.discordapp.com/attachments/888282878973194271/891935435859820574/default.png"

class Neko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Commands
    @commands.command(name = 'feed')
    async def feed(self, ctx, member:discord.Member = None):
        if (member == ctx.author or member == None):
            feed1 = [f"{ctx.author.mention} Seems lonly eating by themselfs",f"{ctx.author.mention} Feeds themselves yummyy",f"{ctx.author.mention} Is it sad eating alone?",f"{ctx.author.mention} Is being fed by... themselves",]
            feed = random.choice(feed1)
            embed = discord.Embed(color=discord.Color.blurple())
            embed.set_image(url=random.choice(feedGIF))
            embed.add_field(name="Trinix Bot", value=feed)
            embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
            await ctx.reply(embed=embed, mention_author=False) 
        else:
            feedResponse = [f"{ctx.author.mention} feeds {member.mention}",f"{member.mention} is being feed by {ctx.author.mention}. Open wide!",f"Yum! {ctx.author.mention} feeds {member.mention}. Here comes the airplane!",    ]  
            feed = random.choice(feedResponse)
            embed = discord.Embed(color=discord.Color.blurple())
            embed.set_image(url=random.choice(feedGIF))
            embed.add_field(name="Trinix Bot", value=(feed))
            embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
            await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'slap', aliases=['smack'])
    async def slap(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                slap = f"{ctx.author.mention} slaps themselves..."
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(slapGIF))
                embed.add_field(name="Trinix Bot", value=slap)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 
            else:
                slapResponse = [f"{ctx.author.mention} slaps {member.mention}",f"{member.mention} is being slapped by {ctx.author.mention}. !",f" {ctx.author.mention} slaps {member.mention}. FOR NO REASON!",]  
                slap = random.choice(slapResponse)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(slapGIF))
                embed.add_field(name="Trinix Bot", value=(slap))
                embed.set_footer(text="Trinix Made by : Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'bite')
    async def bite(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                bite = f"{ctx.author.mention} Bites Themselves..."
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(biteGIF))
                embed.add_field(name="Trinix Bot", value=bite)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 
            else:
                biteResponse = [f"{ctx.author.mention} Bites {member.mention}",f"{member.mention} is being bitten by {ctx.author.mention}. !",f" {ctx.author.mention} Bites {member.mention}. FOR NO REASON!",]  
                bite = random.choice(biteResponse)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(biteGIF))
                embed.add_field(name="Trinix Bot", value=(bite))
                embed.set_footer(text="Trinix Made by : Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'kickk')
    async def kickk(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                kickk= f"{ctx.author.mention} kicks themselves..."
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(kickkGIF))
                embed.add_field(name="Trinix Bot", value=kickk)
                embed.set_footer(text="Trinix Made by : Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 
            else:
                kickkResponse = [f"{ctx.author.mention} Kicks {member.mention}",f"{member.mention} is being Kicked by {ctx.author.mention}. !",f" {ctx.author.mention} Kicks {member.mention}. FOR NO REASON!",]  
                kickk = random.choice(kickkResponse)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(kickkGIF))
                embed.add_field(name="Kick", value=(kickk))
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'kiss')
    async def kiss(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                kiss = f"{ctx.author.mention} kisses themselves..."
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(kissGIF))
                embed.add_field(name="Trinix Bot", value=kiss)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 
            else:
                kissResponse = [f"{ctx.author.mention} Kisses {member.mention}",f"{member.mention} is being Kissed by {ctx.author.mention}. !",f" {ctx.author.mention} Kisses {member.mention}. SOO ROMANTIC!",    ]  
                kiss = random.choice(kissResponse)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(kissGIF))
                embed.add_field(name="Trinix Bot", value=(kiss))
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'hug')
    async def hug(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                hug = f"{ctx.author.mention} Hugs themselves..."
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(hugGIF))
                embed.add_field(name="Trinix Bot", value=hug)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 
            else:
                hugResponse = [f"{ctx.author.mention} Hugs {member.mention}",f"{member.mention} is being Hugged by {ctx.author.mention}. !",f" {ctx.author.mention} Hugs {member.mention}. SOO CUTEE!",]  
                hug = random.choice(hugResponse)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(hugGIF))
                embed.add_field(name="Trinix Bot", value=(hug))
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 


    @commands.command(name = 'cuddle')
    async def cuddle(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                cuddle = f"{ctx.author.mention} Cuddles themselves..."
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(cuddleGIF))
                embed.add_field(name="Trinix Bot", value=cuddle)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 
            else:
                cuddleResponse = [f"{ctx.author.mention} Cuddles {member.mention}",f"{member.mention} is being Cuddled by {ctx.author.mention}. !",f" {ctx.author.mention} Cuddles {member.mention}. I SHIP THIS!",    ]  
                cuddle = random.choice(cuddleResponse)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(cuddleGIF))
                embed.add_field(name="Trinix Bot", value=(cuddle))
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'pat')
    async def pat(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                pat = f"{ctx.author.mention} Pats themselves..."
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(patGIF))
                embed.add_field(name="Trinix Bot", value=pat)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 
            else:
                patResponse = [f"{ctx.author.mention} Pats {member.mention}",f"{member.mention} is being Patted by {ctx.author.mention}. !",f" {ctx.author.mention} Pats {member.mention}. I THINK I LIKE THIS...",]  
                pat = random.choice(patResponse)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(patGIF))
                embed.add_field(name="Trinix Bot", value=(pat))
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'punch')
    async def punch(self, ctx, member:discord.Member = None):
           if (member == ctx.author or member == None):
               punch = f"{ctx.author.mention} Punches themselves..."
               embed = discord.Embed(color=discord.Color.blurple())
               embed.set_image(url=random.choice(punchGIF))
               embed.add_field(name="Trinix Bot", value=punch)
               embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
               await ctx.reply(embed=embed, mention_author=False) 
           else:
               punchResponse = [f"{ctx.author.mention} Punches {member.mention}",f"{member.mention} is being Punched by {ctx.author.mention}. !",f" {ctx.author.mention} Punched {member.mention}. WOW looks like I win...",]  
               punch = random.choice(punchResponse)
               embed = discord.Embed(color=discord.Color.blurple())
               embed.set_image(url=random.choice(punchGIF))
               embed.add_field(name="Trinix Bot", value=(punch))
               embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
               await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'stomp')
    async def stomp(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                stomp = f"{ctx.author.mention} Stomps themselves..."
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(stompGIF))
                embed.add_field(name="Trinix Bot", value=stomp)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 
            else:
                stompResponse = [f"{ctx.author.mention} Stomps {member.mention}",f"{member.mention} is being Stopmed out by {ctx.author.mention}. !",f" {ctx.author.mention} Stomped {member.mention}. WOW looks FUNNNNN...",]  
                stomp = random.choice(stompResponse)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(stompGIF))
                embed.add_field(name="Trinix Bot", value=(stomp))
                embed.set_footer(text="Trinix Made by : Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'mad')
    async def mad(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                mad1 = [f"{ctx.author.mention} is MADDDDD!!!!!!!!!",f"{ctx.author.mention} is PISSEEDDDD OFFFFF!!!!!!!!!",f"{ctx.author.mention} LOOKS LIKE SOMEONE IS MAD!!!!!!!!!",f"{ctx.author.mention} CHILLL MANNNN!!!!!!!!!",]
                mad = random.choice(mad1)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(madGIF))
                embed.add_field(name="Trinix Bot", value=mad)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'bye')
    async def bye(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                bye1 = [f"{ctx.author.mention} is now leaving",f"{ctx.author.mention} is saying goodbye </3",f"{ctx.author.mention} sad to see you go.",f"{ctx.author.mention} see yea later!",]
                bye = random.choice(bye1)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(byeGIF))
                embed.add_field(name="Trinix Bot", value=bye)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'laugh')
    async def laugh(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                laugh = f"{ctx.author.mention} is laughing"
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(laughGIF))
                embed.add_field(name="Trinix Bot", value=laugh)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'poke')
    async def poke(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                poke = f"{ctx.author.mention} pokes themselves..."
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(pokeGIF))
                embed.add_field(name="Trinix Bot", value=poke)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 
            else:
                pokeResponse = [f"{ctx.author.mention} Pokes {member.mention}",f"{member.mention} is being Poked by {ctx.author.mention}. !",f" {ctx.author.mention} just poked {member.mention}. my turn...",]  
                poke = random.choice(pokeResponse)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(pokeGIF))
                embed.add_field(name="Trinix Bot", value=(poke))
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'blush')
    async def blush(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                blush = f"{ctx.author.mention} is blushing"
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(blushGIF))
                embed.add_field(name="Trinix Bot", value=blush)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'dance')
    async def dance(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                dance = f"{ctx.author.mention} is danceing"
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(danceGIF))
                embed.add_field(name="Trinix Bot", value=dance)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'sneeze')
    async def sneeze(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                sneeze = f"{ctx.author.mention} is squeezing"
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(sneezeGIF))
                embed.add_field(name="Trinix Bot", value=sneeze)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'squeeze')
    async def squeeze(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                squeeze = f"{ctx.author.mention} squeezes themselves..."
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(squeezeGIF))
                embed.add_field(name="Trinix Bot", value=squeeze)
                embed.set_footer(text="Trinix Made by : Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 
            else:
                squeezeResponse = [f"{ctx.author.mention} Squeezes {member.mention}",f"{member.mention} is being squeezed by {ctx.author.mention}. !",f" {ctx.author.mention} squeezed {member.mention}. SHEEEESHHHH.",]  
                squeeze = random.choice(squeezeResponse)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(squeezeGIF))
                embed.add_field(name="Trinix Bot", value=(squeeze))
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'kill')
    async def kill(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                kill =  f"{ctx.author.mention} kills themselves..."
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(killGIF))
                embed.add_field(name="Trinix Bot", value=kill)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 
            else:
                killResponse = [f"{ctx.author.mention} kills {member.mention}",f"{member.mention} is being killed by {ctx.author.mention}. !",f" {ctx.author.mention} just killed {member.mention}. SHEEEESHHHH.",    ]  
                kill = random.choice(killResponse)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(killGIF))
                embed.add_field(name="Trinix Bot", value=(kill))
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'what')
    async def what(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                what = f"{ctx.author.mention} Is confused..."
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(whatGIF))
                embed.add_field(name="Trinix Bot", value=what)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'thinking')
    async def thinking(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
               thinking = f"{ctx.author.mention} is thinking....."
               embed = discord.Embed(color=discord.Color.blurple())
               embed.set_image(url=random.choice(thinkingGIF))
               embed.add_field(name="Trinix Bot", value=thinking)
               embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
               await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'handholding')
    async def handholding(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                handholding = f"{ctx.author.mention} hand there own hand..?? waitttt"
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(handholdingGIF))
                embed.add_field(name="Trinix Bot", value=handholding)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 
            else:
                handholdingResponse = [f"{ctx.author.mention} Holds {member.mention} hand <3",f"{member.mention} is holding {ctx.author.mention} hand. HOWW CUTE!",f" I SEE YOU {ctx.author.mention} is holding hands with {member.mention}.",]  
                handholding = random.choice(handholdingResponse)
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(handholdingGIF))
                embed.add_field(name="Trinix Bot", value=(handholding))
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

    @commands.command(name = 'smile')
    async def smile(self, ctx, member:discord.Member = None):
            if (member == ctx.author or member == None):
                smile = f"{ctx.author.mention} is smiling HEHE.. <3"
                embed = discord.Embed(color=discord.Color.blurple())
                embed.set_image(url=random.choice(smileGIF))
                embed.add_field(name="Trinix Bot", value=smile)
                embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
                await ctx.reply(embed=embed, mention_author=False) 

def setup(bot): #Must have a setup function
    bot.add_cog(Neko(bot)) # Add the class to the cog.
