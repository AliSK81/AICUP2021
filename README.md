# AICUP2021
AiCup of Isfahan University of Technology

 مستندات بازی

داستان و هدف بازی
در این بازی شما کنترل یک فضانورد را به دست می‌گیرید. شما مقابل فضانورد تیم حریف در یک نقشه M*N (اندازه نقشه متغیر است) بازی می‌کنید. هدف نهایی وارد کردن بیشترین خسارت و کاهش سلامتی فضانورد تیم مقابل است.

خانه های نقشه
هر خانۀ این نقشه ممکن است خالی یا شامل اشیائی باشد. اگر خانه ای خالی باشد فضانورد به راحتی میتواند در آن خانه حرکت کند. اشیاء عبارتند از:

    دیوار:‌ فضانوردان نمی‌توانند وارد این خانه‌ها شوند. همچنین انفجار از آن‌ها عبور نمی‌کند.
    جعبه: فضانوردان نمی‌توانند وارد این خانه‌ها شوند. در صورتی که شعاع انفجار یک بمب به یک جعبه برسد جعبه نابود می‌شود و هر جعبه میتواند خالی و یا شامل یک ارتقاء باشد.
    ارتقا‌ها:
        تکنولوژی بمب: باعث افزایش شعاع انفجار (تعداد خانه‌های آسیب زننده پس از انفجار بمب) می‌شود.
        معجون زندگی: باعث افزایش سطح سلامتی فضانورد می‌شود.
        تله: یک تله به تله‌های فضانورد اضافه می‌شود.
    تله: تله‌ها برای فضانوردان قابل مشاهده نیستند (حتی تله‌هایی که خودشان کار گذاشته‌اند) و در صورت حرکت روی خانه ای که تله در آن قرار دارد، فضانورد آسیب می‌بیند.
    بمب: بمب‌ها توسط فضانوردان کاشته می‌شوند و پس از مدتی منفجر می‌شوند. هر فضانوردی که در شعاع انفجار بمب قرار داشته باشد (حتی فضانوردی که خودش بمب را کار گذاشته است) آسیب می‌بیند.

اعمال فضانوردان
در هر مرحله نوبت یک فضانورد است که عملی را انجام دهد. اعمال قابل انتخاب شامل:

    حرکت به چهار جهت
    ایستادن در جای قبلی (بدون حرکت)
    کاشتن بمب
    گذاشتن تله
    می‌باشد.

ترتیب رخدادها
در هر مرحله ابتدا تاثیر عمل انتخاب شده فضانورد اعمال می‌شود، سپس اگر فضانورد به خانه‌ای که شامل ارتقاء است وارد شود، آن ارتقاء به صورت خودکار برای او برداشته می‌شود. سپس بمب‌هایی که موعد انفجارشان رسیده است منفجر می‌شوند. پس از آن اگر فضانورد وارد خانه‌ای شده باشد که در آن تله گذاشته شده باشد (چه از طرف خودش چه از طرف فضانورد تیم مقابل) آن تله فعال می‌شود. پس از آن تغییرات منطقه مرگ اتفاق می‌افتد و چنانچه فضانوردی در آن باشد، آسیب می‌بیند. دقت کنید که در هر نوبت حداکثر یک بار آسیب می‌بیند. مثلا اگر فضانوردی در شعاع انفجار دو بمب باشد و همزمان در منطقه مرگ باشد فقط یک مرتبه (یک جان) سطح سلامتی‌اش کاهش می‌یابد.

انفجار بمب‌ها
هر بمب شعاع انفجار مشخصی دارد. این شعاع انفجار بستگی به سطح تکنولوژی بمب فضانورد هنگام کاشتن آن بمب دارد. اگر بمب دیگری در شعاع انفجار بمب منفجر شده قرار گرفته باشد، در همان نوبت منفجر می‌شود. تعداد بمب های منفجر شده در هر نوبت محدودیتی ندارد. بمب‌ها باعث فعالسازی تله‌ای نخواهند شد.

دید فضانورد (ویژن)
هر فضانورد نسبت به نقشه‌ای که در آن قرار دارد، دید محدودی خواهد داشت. به این صورت که در هر نوبت، فضانورد فقط خانه‌هایی که در فاصلۀ منهتنی مشخصی (از محل کنونی او) قرار دارند را می‌تواند ببیند. یک نمونه دید فضانورد با فاصله های 2 الی 4:

منطقۀ مرگ
پس از گذشت مدتی از شروع بازی، نقشه بازی شروع به کوچک شدن می‌کند. به این صورت که به مرور حاشیۀ نقشه تبدیل به منطقۀ مرگ (deadzone) می‌شود. این فرایند، محیط قابل حرکت برای فضانوردان را کوچک و کوچک‌تر خواهد کرد. ماندن در این منطقه در هر نوبت به فضانورد آسیب می‌زند. به این توجه کنید که هر نوبت مختص به یک فضانورد است پس اگر در نوبت خود از منطقۀ مرگ خارج نشوید، فضانورد شما دو مرتبه آسیب می‌بیند.

محدودیت فرصت انتخاب عمل
اعلام عمل انتخاب شده به موتور بازی محدودیت زمانی دارد. در صورت عدم رعایت این محدودیت زمانی، فضانورد تیم خاطی از بازی حذف شده و فضانورد دیگر برندۀ بازی اعلام خواهد شد. محدودیت زمانی 400 میلی ثانیه است. ممکن است در آینده این زمان بیشتر شود.

خاتمه بازی و مشخص شدن برنده
بازی با مرگ یکی از فضانوردان خاتمه می‌یابد و برنده فضانورد زنده اعلام می‌شود. در صورتی که هر دو فضانورد باهم بمیرند یا در تعداد مشخصی دور هیچکدام از فضانوردان نمیرند، یکی از فضانوردان با استفاده از معیارهای زیر که به ترتیب اولویت مرتب شده‌اند به عنوان برنده انتخاب می‌شود.

    بازیکنی که سطح سلامتی بیشتری دارد
    بازیکنی که معجون زندگی کمتری مصرف کرده است
    بازیکنی که بمب بیشتری کاشته است
    بازیکنی که تله بیشتری گذاشته است
    یک بازیکن رندوم

درصورتیکه یکی از ایجنت‌ها دیرتر از زمان مشخص شده حرکت بعدیِ خود را به موتور بازی اعلام کند، در لحظه بازندۀ بازی اعلام خواهد شد و بازی خاتمه می‌یابد.
مستندات فنی

اجرای بازی

پس از دانلود فایل‌های بازی برای شروع یک بازی باید فایل main.py را اجرا کنید. این اسکریپت دو آرگومان به نام‌های p1 و p2 برای مشخص کردن فایل ایجنت‌ها دریافت می‌کند. فایل‌های ورودی می‌توانند از نوع py یا jar یا یک فایل اجرایی باشند. تشخیص نوع فایل به کمک پسوند آن انجام می‌شود.

یک نمونه دستور اجرای بازی:
py main.py -p1 player1.py -p2 player2.jar

ارتباط با موتور بازی
انتقال اطلاعات بین ایجنت ها و موتور بازی با استفاده از ورودی و خروجی استاندارد (Standard I/O) انجام می‌شود.

مختصات
سیستم مختصاتی بازی به صورت ماتریسی است. یعنی مؤلفۀ اول (x) سطر و مؤلفۀ دوم (y) ستون را مشخص می‌کند. مثلاً بعد از حرکت به کاشیِ پایین، مؤلفۀ اول یک واحد افزایش می یابد.

شروع بازی
موتور بازی به هر دو ایجنت یک پیام init ارسال می کند که فرمت آن به صورت نشان داده شده است: (کل پیام در یک خط است و اطلاعات با استفاده از یک فاصله از هم جدا شده اند)
init {map.height} {map.width} {player.x} {player.y} {player.health} {player.bombRange} {player.trapCount} {vision} {bombDelay} {maxBombRange} {deadzoneStartingStep} {deadzoneExpansionDelay} {maxStep}

    map.height: Number of map rows
    map.width: Number of map columns
    player.x: Index of the row which the player is in
    player.y: Index of the column which the player is in
    player.health: Initial health of the player
    player.bombRange: Initial range/power of the player’s bombs
    player.trapCount: Initial number of traps the player has
    vision: Manhattan distance of the farthest tile the player can see
    bombDelay: Number of steps it takes for a bomb to explode
    maxBombRange: Maximum upgradable bomb range
    deadzoneStartingStep: Step number in which deadzone starts to appear on the map
    deadzoneExpansionDelay: Number of steps before deadzone expands towards the center of the map
    maxStep: Maximum number of steps that the game continues

سپس ایجنت باید پیام init confirm را به کرنل بدهد.

یک نمونه از پیام شروع بازی (از انجین به ایجنت) می‌تواند به این صورت باشد:
init 11 15 1 1 3 2 1 5 5 5 150 5 400

و جواب ایجنت به کرنل:
init confirm

حین بازی

در هرنوبت، موتور بازی به بازیکنی که نوبت اوست، یک پیام که حاوی استیت بازی است را به فرمت زیر ارسال می‌کند: (کل پیام در یک خط است و اطلاعات با استفاده از یک فاصله از هم جدا شده اند)

    در صورتی که بازیکن حریف در دید فضانورد باشد اطلاعات به صورت زیر ارسال می‌شود:
    {stepCount} {lastActionTakenByThePlayer} {player.x} {player.y} {player.health} {player.healthUpgradeCount} {player.bombRange} {player.trapCount} 1 {otherPlayer.x} {otherPlayer.y} {otherPlayer.health} {numberOfTilesInVision} {tileInfoTuples} EOM

    در صورتی که بازیکن حریف در دید فضانورد نباشد اطلاعات به صورت زیر ارسال می‌شود:
    {stepCount} {lastActionTakenByThePlayer} {player.x} {player.y} {player.health} {player.healthUpgradeCount} {player.bombRange} {player.trapCount} 0 {numberOfTilesInVision} {tileInfoTuples} EOM
        stepCount:‌ Current step (0-based)

        lastActionTakenByThePlayer: A feedback of the last submitted action.

        Game actions are as follows:
            0: Go left
            1: Go right
            2: Go up
            3: Go down
            4: Stay
            5: Place bomb
            6: place trap left
            7: Place trap right
            8: Place trap up
            9: Place trap down
            10: Init
            11: No action

        دقت کنید که اعداد بالا فقط پاسخ سرور به فضانورد هستند. اعمال مجاز برای انجام در بخش‌های بعدی ذکر شده‌اند.
        player.x: Index of the row which the player is in
        player.y: Index of the column which the player is in
        player.health: Current health of the player
        player.healthUpgradeCount: Number of health upgrades picked up by the player
        player.bombRange: Current range/power of the player’s bombs
        player.trapCount: Current number of traps the player has
        otherPlayer.x: Index of the row which the other player is in
        otherPlayer.y: Index of the column which the other player is in
        otherPlayer.health: Current health of the other player
        numberOfTilesInVision: Number of info tuples coming up next

        tileInfoTuples: a 3-part info chunk in the format shown below
        {tile.x} {tile.y} {tile.state}
            tile.x: Index of the tile row
            tile.y: Index of the tile column
            tile.state: A number representing the entities in the tile. The i-th bit shows if the tile has the i-th entity or not.
                0: Tile is in dead zone
                1: Fire (explosion side effect)
                2: Box
                3: Wall
                4: Bomb
                5: Bomb range upgrade
                6: Health upgrade
                7: Trap upgrade
                8: A player

    سپس بازیکن اکشنی که می‌خواهد انجام دهد را به صورت زیر برای کرنل ارسال می‌کند:
    {action}

        Action: The action taken by the agent.

        If an illegal action is taken by the player, ‘no_action’ is automatically selected as the player's action. Legal actions are as follows:
            0: Go left
            1: Go right
            2: Go up
            3: Go down
            4: Stay
            5: Place bomb
            6: Place trap left
            7: Place trap right
            8: Place trap up
            9: Place trap down

    یک نمونه از پیام حین بازی (از انجین به ایجنت) می‌تواند به این صورت باشد:
    0 7 5 6 3 0 2 1 1 5 8 3 25 2 6 0 3 5 0 3 6 0 3 7 0 4 4 0 4 5 0 4 6 0 4 7 0 4 8 0 5 3 0 5 4 0 5 5 0 5 6 0 5 7 0 5 8 0 5 9 0 6 4 0 6 5 0 6 6 0 6 7 0 6 8 0 7 5 0 7 6 0 7 7 0 8 6 0 EOM

    و جواب ایجنت به انجین:
    3

خاتمۀ بازی

در انتهای مسابقه، اگر هیچ بازیکنی از قوانین تخطی نکرده باشد، پیام زیر برای هر بازیکن ارسال میشود:
term {lastStepCount} {result}

    lastStepCount: Last step (in which the game ended).
    result: Winner of the game. (1-based)

یک نمونه از پیام پایان بازی (از انجین به ایجنت) می‌تواند به این صورت باشد (بازیکن اول در نوبت 18 برنده شده است):
term 18 1

اینجا ایجنت پیامی به انجین نمیدهد.

یک نمونه ایجنت رندوم می‌تواند به صورت زیر باشد:
import random
init_msg = input()
# Do stuff
print('init confirm')
while True:
    state_msg = input()
    if 'term' in state_msg:
        break
    # Do stuff
    print(int(random.random() * 10))

نکات و تذکرات سیستم تبادل پیام

    هر پیام بین موتور بازی و ایجنت‌ها فقط شامل یک خط با پایانِ newline خواهد بود. فراموش نکنید که برای ثبت پاسخ حتماً در انتهای پیام خود یک newline چاپ کنید و اگر دستور مورد استفادۀ شما autoflush نمی‌کند، stdout را یکبار flush کنید. مثلاً در زبان سی‌پلاس‌پلاس می‌توان از دستور
    fflush(stdout); // if you use scanf/printf
    برای فلاش کردن استفاده کرد.

    در هر پیام اطلاعات با استفاده از یک فاصله (whitespace) از هم جدا شده‌اند.

    زمان چاپ شدن پاسخ خود برای موتور بازی را نیز در محاسبات خود لحاظ کنید.

نمایش گرافیکی بازی

پس از خاتمه بازی شما می‌توانید لاگ تولید شده بازی که در پوشه gameLog ذخیره شده را به ویژوالایزر بازی بدهید و بازی انجام شده را مشاهده کنید.

کلیدهای میانبر ویزوالایزر به شرح زیر است:
Q : Toggle music
E : Toggle sound
R : Restart
F : Show full player names
W / UP : Increase game speed
S / DOWN : Decrease game speed
ENTER / SPACE : Play/Pause
A / LEFT : Step back (x5 while holding ctrl)
D / RIGHT : Step forward (x5 while holding ctrl)
0 - 9 : Jump to the n-th decile (e.g. press 5 to jump to the middle of the game)
F2 : Take a screenshot
ESC : Back to menu

لاگ برای ایجنت ها

درصورتی که می‌خواهید برای دیباگ، ایجنت‌های شما لاگ تولید کنند، می‌توانید آن را در stderr چاپ کنید. دقت کنید که چون موتور بازی از stdout برای تبادل پیام استفاده میکند، لذا نمی‌توانید از آن برای این کار استفاده کنید. این قابلیت وجود دارد که لاگ ایجنت ها در کنسول نمایش داده شود یا در یک فایل مشخص ذخیره شود (روش فایل بهتر است). این تنظیمات در فایل تنظیمات قابل تغییر است.

یک نمونه لاگ به زبان پایتون:
import sys
print(f'Currently in step {step}.', file=sys.stderr)

نکتۀ مهم: کار با IO زمان زیادی از ایجنت شما می‌گیرد، لذا توصیه می‌شود در کدی که برای مسابقۀ اصلی ارسال می‌کنید قسمت‌های مربوط به لاگ را حذف کنید.

تنظیمات بازی

تنظیمات کلی موتور بازی را می‌توانید در فایل settings.py تغییر دهید. این تنظیمات شامل محل ذخیره سازی لاگ بازی، محل ذخیره سازی لاگ ایجنت‌ها، آدرس نقشۀ بازی، تغییر محدودیت زمانی و دیگر تنظیمات کلی است.

تنظیمات نقشۀ بازی

تنظیمات نقشۀ بازی در فایل نقشه قابل تغییر است. این تنظیمات شامل ابعاد نقشه، محل شروع فضانوردان، محدودیت دید فضانوردان، سطح سلامتی اولیّۀ فضانوردان، شعاع انفجار اولیّۀ بمب‌ها، زمان شروع گسترش منطقۀ مرگ، تاخیر گسترش منطقۀ مرگ، حداکثر تعداد دور بازی و نقشۀ بازی است.

دامنۀ متغیرهای بازی

    Map width/height: [5, 25]
    Initial player health: [3, 6]
    Initial bomb range: [1, 3]
    Initial trap count: [1, 3]
    Vision: [5, 7]
    Bomb delay: [8, 16]
    Maximum bomb range: [4, 6]
    Maximum number of steps: [200, 400]
    Deadzone starting step: TBA
    Deadzone expansion delay: TBA
