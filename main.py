from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "images"
MUSIC_DIR = BASE_DIR / "music"

IMAGES_DIR.mkdir(exist_ok=True)
MUSIC_DIR.mkdir(exist_ok=True)

app = FastAPI(title="Anime Recommender API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images", StaticFiles(directory=IMAGES_DIR), name="images")
app.mount("/music", StaticFiles(directory=MUSIC_DIR), name="music")

ANIME_LIST = [
    {
        "id": 1,
        "title": "Re：从零开始的异世界生活",
        "title_en": "Re:Life in a different world from zero",
        "tagline": "死亡回归不是外挂，而是把绝望一遍遍重放。",
        "description": "菜月昴突然被召唤到异世界，唯一能依靠的是死亡后回到过去的能力。它真正厉害的地方不是设定本身，而是一次次失败、崩溃与重新站起来的过程拍得特别痛。",
        "year": "2016",
        "studio": "WHITE FOX",
        "status": "TV 动画第 4 季已确认 2026 年播出",
        "genres": ["异世界", "悬疑", "成长", "轮回"],
        "theme": "如果你喜欢角色在极限情绪里反复破碎又重建，这部会很有后劲。",
        "why_watch": "前期像残酷试错，越往后越像情绪与意志的拉锯战。它能把角色的无力感拍得非常具体，所以每一次翻盘都会更有重量。",
        "source_note": "资料按 Re:ZERO 官方动画站整理：故事页围绕菜月昴在异世界从零书写命运展开；官网新闻已公布第 4 季 2026 年播出，Staff&Cast 页面显示动画制作继续由 WHITE FOX 担任。",
        "official_url": "https://re-zero-anime.jp/tv/",
        "official_label": "官方动画站",
        "accent": "#7c6cff",
        "image_file": "1.jpg",
    },
    {
        "id": 2,
        "title": "进击的巨人",
        "title_en": "Attack on Titan",
        "tagline": "从墙内求生，到把自由、历史和战争问到底。",
        "description": "它一开始像人类对巨人的生存战，越往后越像一部关于自由、国家、真相与仇恨循环的史诗。最强的地方在于，它几乎每一段都会把你对世界的理解整块翻过来。",
        "year": "2013",
        "studio": "WIT STUDIO / MAPPA",
        "status": "TV 系列已完结，2024 年推出剧场版重构《THE LAST ATTACK》",
        "genres": ["黑暗奇幻", "战争", "群像", "悬疑"],
        "theme": "如果你喜欢世界观层层翻面、角色立场持续碰撞，这部几乎绕不开。",
        "why_watch": "它不是只靠热血和打斗推进，而是不断让角色、阵营与真相相互反噬。你会发现真正让人记住的，不只是立体机动，而是每个人在时代里的选择。",
        "source_note": "资料按《进击的巨人》官方站和 AOT Portal 整理：Season 1 故事页设定是人类依靠高墙抵御巨人；官方新闻说明 TV 动画自 2013 年开播并于 2023 年完结，完结篇制作信息页显示 MAPPA 负责最终阶段动画制作。",
        "official_url": "https://aot-portal.com/",
        "official_label": "官方动画站",
        "accent": "#ff8a3d",
        "image_file": "2.jpg",
    },
    {
        "id": 3,
        "title": "夏日重现",
        "title_en": "Summer Time Rendering",
        "tagline": "回到海岛的那个夏天后，死亡像存档点一样不断重来。",
        "description": "慎平因为青梅竹马小舟潮的葬礼回到日都岛，却发现她的死并不单纯。随着“影”的传说浮出水面，这部作品把海岛夏日、循环推理和强压迫感揉得非常顺。",
        "year": "2022",
        "studio": "OLM",
        "status": "TV 动画全 25 话，单季完结",
        "genres": ["悬疑", "科幻", "轮回", "海岛"],
        "theme": "如果你想找一部节奏很紧、设定闭环漂亮、气氛又带点潮湿夏意的作品，它很合适。",
        "why_watch": "它少见地把“夏天的明亮感”和“真相逼近的窒息感”叠在一起。前中后期节奏都比较稳，很多伏笔回收也干净，不会只靠反转硬撑。",
        "source_note": "资料按《夏日重现》官网与 Disney+ 页面整理：故事从慎平因葬礼返乡开始，海岛上逐渐出现“影”的异常；官方 Staff 页面显示动画制作公司为 OLM，Disney+ 页面收录为 2022 年上线的 1 季作品。",
        "official_url": "https://summertime-anime.com/",
        "official_label": "官方动画站",
        "accent": "#35c2ff",
        "image_file": "3.jpg",
    },
    {
        "id": 4,
        "title": "Charlotte",
        "title_en": "Charlotte",
        "tagline": "青春期短暂的超能力，最后会把人推向哪里。",
        "description": "以为只是校园系超能力故事，结果越往后越有一种“明知道会失去，还得继续往前”的苦味。它体量不长，但情绪推进很快，很适合一口气补完。",
        "year": "2015",
        "studio": "P.A.WORKS",
        "status": "TV 动画 13 话，另有特别篇",
        "genres": ["校园", "超能力", "青春", "催泪"],
        "theme": "如果你喜欢少年少女式的超能力设定，但又希望后面能突然收紧成情绪系作品，这部值得看。",
        "why_watch": "前面有校园与角色互动的轻盈感，后面会逐步切到失去、责任和选择。它的转调很明显，所以特别适合喜欢“前甜后痛”观感的人。",
        "source_note": "资料按《Charlotte》官网、P.A.WORKS 页面与 Netflix 页面整理：官方故事页核心设定是思春期少年少女会短暂拥有特殊能力；P.A.WORKS 将其列为原创电视动画，Netflix 页面收录年份为 2015。",
        "official_url": "https://charlotte-anime.jp/",
        "official_label": "官方动画站",
        "accent": "#ff6f91",
        "image_file": "4.jpg",
    },
]


@app.get("/")
async def read_index():
    return FileResponse(BASE_DIR / "index.html")


@app.get("/anime")
async def read_anime_page():
    return FileResponse(BASE_DIR / "anime.html")


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/anime")
def get_anime(request: Request):
    result = []
    for anime in ANIME_LIST:
        item = anime.copy()
        item["image_url"] = f"{str(request.base_url).rstrip('/')}/images/{anime['image_file']}"
        result.append(item)
    return result
from fastapi.responses import FileResponse

# 当用户访问主网址时，返回主页
@app.get("/")
async def get_index():
    return FileResponse("index.html")

# 当用户访问 /anime 时，返回动漫推荐页
@app.get("/anime")
async def get_anime():
    return FileResponse("anime.html")