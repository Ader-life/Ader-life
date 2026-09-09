from pathlib import Path
p=Path('/mnt/data/prazz_project/index.html')
s=p.read_text()
start=s.index('<section class="hero" id="me">')
end=s.index('<div class="closing"', start)
new=r'''<section class="hero" id="me">
  <p class="hero-eye">welcome to my universe</p>
  <h1 class="hero-title">Ader<em>quiet. shy. still becoming.</em></h1>
  <div class="hero-vline"></div>
  <p class="hero-sub">I’m Ader. I’m 19 years old — an introverted, shy, insecure, and underconfident guy who wasn’t always this way.<span>Welcome to my little universe.</span></p>
  <div class="scroll-h" aria-hidden="true">scroll</div>
</section>

<div class="band rb reveal"><p>When I was a kid, I had so many friends. We played together, fought over the stupidest things, laughed until our stomachs hurt, and turned ordinary days into unforgettable memories. Growing up changed everything. People moved away, life changed, and slowly the days became quieter. But somewhere along the way, I found people who made that silence feel less lonely.</p></div>

<div class="origin">
  <p class="origin-sub">who I am</p>
  <span class="ts reveal">19 years old · introverted by nature · feeling everything deeply</span>
  <h2 class="origin-title reveal">not the same<br>boy I used to be.</h2>
  <div class="badge reveal">Ader — still becoming</div>
  <div class="reveal"><p>I’m an introverted, shy, insecure, and underconfident guy. But I wasn’t always this way. As a kid, I was surrounded by friends. We played in our society, fought over absolutely nothing, laughed over the smallest things, and somehow made the simplest days feel magical.</p></div>
  <div class="reveal"><p>Sometimes I look back at those days and get emotional. I miss those moments more than I can explain. Those really were the days.</p></div>
  <div class="reveal"><p>Then growing up happened. One by one, my friends moved away — different cities, different states, different lives. I do have friends offline, but it never felt exactly the same. So most places became places I went alone.</p></div>
  <div class="reveal"><p>My family sometimes asks why I don’t go outside and hang out. I wish I could explain that sometimes you just want someone you can sit with, talk about life with, share your feelings with, or laugh about completely random things.</p></div>
  <div class="reveal"><p class="hl" style="font-size:clamp(1.3rem,3vw,2rem);font-style:italic">“Main akela zaroor tha,<br>par meri kahaani kabhi khaali nahi thi.”</p></div>
  <div class="stat reveal"><span class="stat-n" id="statCount">0</span><span class="stat-l">things I keep choosing:<br>memories<br>friendship<br>music<br>gaming<br>laughter<br>my people</span></div>
</div>

<div class="origin" style="padding-top:2rem;padding-bottom:3rem;border-top:1px solid rgba(196,168,130,.06)">
  <p class="origin-sub" style="margin-bottom:2.5rem">the little things that feel like me</p>
  <div class="reveal"><p>I love playing cricket, gaming, listening to songs, going on bike rides, going on long drives with my friends, eating until I’m completely full, messing around and doing stupid things with my people, reading books, and going to the gym.</p></div>
  <div class="reveal"><p>I also love waking up late in the morning, eating late at night, and somehow having breakfast before going to the bathroom. 😭</p></div>
  <div class="reveal"><p>Basically, I love the little things that make life feel fun — good music, good food, bikes, games, books, and most importantly, spending time with my people.</p></div>
  <div class="reveal"><p style="color:var(--dim);font-style:italic">“Zindagi badi cheezon se nahi,<br>chhoti chhoti khushiyon se khoobsurat banti hai.”</p></div>
</div>

<section class="space-s" id="space">
  <p class="slabel" style="justify-content:center">the game that changed something</p>
  <h2 class="space-title reveal">I found <em>people.</em></h2>
  <p class="space-copy reveal">Then I started playing Free Fire. It was just a game at first, but somehow it gave me something I was missing — a place where I could meet people, talk, laugh, and make memories.</p>
  <p class="space-copy reveal" style="color:var(--dust)">I made some really good friends there. Even when some friendships faded because of small misunderstandings, those memories stayed.</p>
</section>

<section class="alone" id="alone">
  <p class="slabel">the chapter I still remember</p>
  <div class="alone-card reveal">
    <p>Then came November 6, 2025.</p>
    <p>That was the day I met a girl whose name I won’t mention. She was Muslim, I was Hindu. We started as friends — playing games, sharing Instagram accounts, talking for hours, and spending almost every online moment together.</p>
    <p>Eventually, I started liking her. And she knew it.</p>
    <p>One small fight changed everything. We fought on November 19. I didn’t talk to her that day or the next. Then, on November 21 at 5:13 PM, she messaged me saying she was leaving the game and said goodbye.</p>
    <p>And I replied rudely.</p>
    <p>That became one of my biggest regrets.</p>
  </div>
</section>

<div class="love-wrap" id="interests">
  <p class="slabel">the memory I couldn’t erase</p>
  <p class="love-intro reveal">Sometimes you don’t lose someone because you stopped caring.<br>You lose them because life becomes bigger than what two people want.</p>
  <ul class="love-list" id="loveList">
    <li>November 6, 2025</li><li>November 19</li><li>November 21 · 5:13 PM</li><li>10:03 PM</li><li>Free Fire nights</li><li>hours of talking</li><li>Instagram accounts</li><li>small fights</li><li>big feelings</li><li>things left unsaid</li><li>regret</li><li>forgiveness I wish I had given</li><li>memories that stayed</li><li>people who came later</li><li>friendships that became family</li><li class="big">Ader.</li>
  </ul>
</div>

<div class="dv"><span>∗</span></div>
<div class="band rb reveal"><p>“Kuch yaadein waqt ke saath purani nahi hoti,<br>bas unhe yaad karne ki aadat ho jaati hai.”</p></div>

<section class="poetry">
  <p class="slabel">fragments of my story</p>
  <div class="poem large reveal"><div class="pnum">I</div><p>I wish I had forgiven her.</p><p>I wish I had handled everything differently.</p><span class="gap"></span><p>But sometimes,</p><p>no matter how much you want someone to stay,</p><p>life has a different plan.</p></div>
  <div class="poem reveal"><div class="pnum">II</div><p>Later that night,</p><p>at 10:03 PM,</p><p>we both knew</p><p>it would be difficult.</p><span class="gap"></span><p>Maybe she was right.</p><p>But I still loved her.</p></div>
  <div class="poem ita reveal"><div class="pnum">III</div><p>Some endings</p><p>don’t happen because</p><p>feelings disappear.</p><span class="gap"></span><p>Sometimes people leave</p><p>because staying hurts more.</p></div>
  <div class="poem reveal"><div class="pnum">IV</div><p>“Jo mere naseeb mein nahi tha,</p><p>uski yaad mere dil mein kyun hai?”</p></div>
</section>

<div class="hindi-s">
  <p class="slabel">in the language that feels closest</p>
  <div class="reveal"><p class="hl big">Kuch log milte hain,<br>zindagi bhar ke liye nahi,<br>zindagi badalne ke liye.</p></div>
  <div class="reveal"><p class="hl">Woh chali gayi,<br>par kuch yaadein chhod gayi<br>jo aaj bhi mere saath chalti hain.</p></div>
  <div class="reveal"><p class="hl">Dil maanta raha,<br>haalat nahi maane.</p></div>
  <div class="reveal"><p class="hl" style="color:var(--rose);font-style:italic">Kabhi kabhi kisi ko chhodna padta hai,<br>chahe dil abhi bhi uska intezaar karta ho.</p></div>
</div>

<div class="band db reveal"><p>And somehow, after losing people, I found people again.</p></div>

<div class="origin" style="padding-top:5rem;padding-bottom:3rem">
  <p class="origin-sub">the people who stayed</p>
  <span class="ts reveal">online friends · real memories · pieces of my heart</span>
  <h2 class="origin-title big reveal">just online?<br>not to me.</h2>
  <div class="reveal"><p>Then Mango and Rahewa entered my life, and slowly, I started laughing again. We joked around, messed with each other, fought over stupid things, and made memories I’ll always remember.</p></div>
  <div class="reveal"><p>Mango is still here with me today. Always caring, always looking out for me. He may be an online friend, but to me, he’s worth more than a diamond. No matter how many fights we’ve had, you’ll always be my jaan.</p></div>
  <div class="reveal"><p>Aarav — my jaan, my bro, a piece of my heart. We may fight over the smallest things, but you’re still my brother. How could I ever forget you? Love youuu.</p></div>
  <div class="reveal"><p>Rhaewa — my legendary haggu friend who somehow manages to fart at every possible moment. 😭 Countless fights, countless moments of madness, and somehow we always ended up laughing and fixing everything.</p></div>
  <div class="reveal"><p style="color:var(--rose);font-style:italic;font-family:'Cormorant Garamond',serif;font-size:clamp(1.2rem,2.8vw,1.8rem);line-height:2.1">“Jo log meri khamoshi mein bhi mujhe samajhne ki koshish karein,<br>shayad wahi mere asli log hain.”</p></div>
</div>

<section class="poetry" style="padding-top:2rem">
  <p class="slabel">my people</p>
  <div class="poem reveal"><div class="pnum">01</div><p>Zeegly.</p><p>Jace.</p><p>Sasuke.</p><p>Prazz.</p><p>Jamiee.</p><p>Ashford.</p><p>Krish.</p><p>Lakshya.</p><p>Abhinav.</p><p>Yel.</p><p>Coward.</p></div>
  <div class="poem reveal"><div class="pnum">02</div><p>Maybe they are just online friends to the world.</p><span class="gap"></span><p>But to me,</p><p>they are the people who made me laugh when I was lonely,</p><p>stayed when others left,</p><p>and gave me memories when I had nothing to look forward to.</p></div>
  <div class="poem reveal"><div class="pnum">03</div><p>I’ve lost people.</p><p>I’ve missed people.</p><p>I’ve made mistakes.</p><span class="gap"></span><p>But I also found people</p><p>who became pieces of my heart.</p></div>
</section>

<section class="thoughts" id="thoughts">
  <p class="slabel">things I want my people to know</p>
  <div class="thought reveal"><small>01 · Mango</small>“My guy, my brother, my piece of heart. No matter how many fights we’ve had, nothing will separate us. We’ll always find our way back.” ❤️</div>
  <div class="thought reveal"><small>02 · Aarav</small>“My jaan, my bakchod friend. Fulchand, the nonsense we’ve done together is unforgettable. Love you so much.” ❤️</div>
  <div class="thought reveal"><small>03 · Rhaewa</small>“You’ve always supported me. Our bakchodi has always been greater than our fights. You’ll always be one of my closest friends.” ❤️</div>
  <div class="thought reveal"><small>04 · Jace</small>“My chhadi chor yaar. No risk, no Porsche. One day we’ll get that Porsche, bro.” 😭❤️</div>
  <div class="thought reveal"><small>05 · Prazz</small>“My guy, my jaan, my brother. We have dreams to chase. One day, partner, we’ll be in Amsterdam.” ❤️</div>
  <div class="thought reveal"><small>06 · Jamiee</small>“My jaan, my bakchod friend. Come back to the game, bro. I’ll genuinely miss you.” ❤️</div>
  <div class="thought reveal"><small>07 · Ashford</small>“Oye sale, you get upset over the smallest things and then somehow make up two minutes later. You’re impossible, bro.” 😭❤️</div>
  <div class="thought reveal"><small>08 · Pranav</small>“My guy, my jaan. Those BR matches with our mics on are memories I’ll never forget. I really miss those days.”</div>
  <div class="thought reveal"><small>09 · Colour</small>“You left the game and never came back. 😭 I’m genuinely sorry, yaar. Because of one mistake from my side, the whole group got messed up. Please forgive me someday.” ❤️</div>
  <div class="thought reveal"><small>10 · Xylia</small>“Social chalna hai oye! 😭 Come back soon. We’ll have fun like before. I really miss you.”</div>
  <div class="thought reveal"><small>11 · Adeline</small>“Where did you disappear? 😭 You used to ragebait me every time, pagal. I was just joking around. Whatever happened before, I’m genuinely sorry.” ❤️</div>
  <div class="thought reveal"><small>12 · Abhinav</small>“Sale, my bakchod friend. You used to disturb me during movie time with that sound. 😭 Come on, let’s play customs. No horror movie today.” ❤️</div>
  <div class="thought reveal"><small>13 · Zeegly</small>“Oh hi Zeegly! 😭 Come into the game after doing your potty, crazy friend. Let’s yap together. Hurry up!” 😂❤️</div>
  <div class="thought reveal"><small>14 · Luma</small>“My friend, please get me a plate of idli-sambar, I’m hungry! 😭 Oye, social tonight? Come early. I’ll be waiting.”</div>
  <div class="thought reveal"><small>15 · Ike</small>“You’re genuinely precious to me. Whenever I remember your voice, I forget everything. Whether you remember me or not, I’ll always remember you.” ❤️</div>
  <div class="thought reveal"><small>16 · Sasuke</small>“Meri jaan Sasuke, let’s ragebait someone again. Remember that Instagram GC? Make a new one and come quickly. And when are you treating me to biryani?” 😂❤️</div>
  <div class="thought reveal"><small>17 · Krish & Yel</small>“My favourite couple. Always stay together and no evil eye. ❤️ Krish, let’s go to social and ragebait Mox!”</div>
  <div class="thought reveal"><small>18 · Lakshya</small>“My jaan, come on, let’s 1v1. And if I lose, don’t tell anyone, okay? 😭 We’ve got a movie to watch too.” 😂❤️</div>
</section>

<div class="band db reveal"><p>“Maybe growing up isn’t about keeping everyone forever.<br>Maybe it’s about being grateful for the people who chose to stay while they were here.”</p></div>

<section class="poetry" id="future">
  <p class="slabel">the people I found through a screen</p>
  <div class="poem large reveal"><div class="pnum">∞</div><p>We met through a game.</p><p>We started as strangers.</p><p>Somehow, we became family.</p><span class="gap"></span><p>We laughed.</p><p>We fought.</p><p>We annoyed each other.</p><p>We made memories.</p></div>
  <div class="poem reveal"><div class="pnum">and maybe</div><p>One day, life will get busy.</p><p>Games will change.</p><p>Group chats might become silent.</p><p>Everyone might go their own way.</p><span class="gap"></span><p>But I hope when you look back,</p><p>you remember this crazy little family we created.</p></div>
  <div class="poem reveal"><div class="pnum">Sonic</div><p>Meri jaan, how are you, bro?</p><p>I still remember all the crazy things we used to do together.</p><p>When my Instagram got suspended and you helped me recover it, I never forgot that.</p><p>You’ve always stood by me whenever I needed you.</p><span class="gap"></span><p>Those days of absolute bakchodi will always have a special place in my memories.</p></div>
</section>

<div class="dv"><span>∗</span></div>
<div class="band rb reveal"><p>These are my people.<br>My friends. My memories. My jigar ke tukde.</p></div>

<section class="poetry">
  <p class="slabel">the quote</p>
  <div class="poem large reveal"><div class="pnum">∞</div><p>“Jo mere saath thode waqt ke liye chale,</p><p>unka zikr meri poori zindagi mein rahega.”</p></div>
  <div class="poem reveal"><div class="pnum">∞</div><p>“I may have met them through a screen,</p><p>but the memories they gave me</p><p>were never virtual.”</p></div>
</section>

'''
s=s[:start]+new+s[end:]
s=s.replace('20 years old.<br>Still learning. Still losing. Still growing.<br>Still becoming.','19 years old.<br>Still learning. Still losing. Still growing.<br>Still becoming.')
s=s.replace('cars · F1 · music · space · games · trading · travelling · solitude','cricket · gaming · music · bikes · books · gym · long drives · my people')
s=s.replace('“I may not know exactly where I’m going yet.<br>But I know I’m not staying where I am.”','“I don’t know what the future holds.<br>But I know I’ll cherish the people who made the journey worth remembering.”')
p.write_text(s)
