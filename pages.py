"""
AMAYA Project — page bodies.

Everything between <main id="main"> and the previous/next pager for each page.
Shared chrome (head, nav, footer, JSON-LD) lives in build.py.

These bodies were extracted from the deployed site on 14 September 2026, so the
de-duplication edits that previously existed only in the published HTML are now
captured here and will survive a rebuild.
"""

BODIES = {}

BODIES['index'] = r'''
  <section class="hero">
    <div class="wrap hero-in">
      <div>
        <p class="eyebrow rise">Copper Exploration &middot; Atacama Desert &middot; Chile</p>
        <h1 class="rise">Amaya<br><em>Project</em></h1>
        <p class="hero-sub rise">Copper Exploration Project &middot; Atacama Desert, Chile</p>
        <p class="lead rise">AMAYA comprises <strong>9 copper concessions</strong> covering a total area of <strong>2,353 hectares</strong>, equivalent to approximately <strong>5,814 acres</strong>, at 3,800 metres above sea level, 80 km north of Calama.</p>
        <div class="btns rise">
          <a class="cta solid" href="project.html">Explore the project</a>
          <a class="cta" href="about.html#contact">Investor enquiries</a>
        </div>
      </div>
      <figure class="scanner rise" aria-label="Illustrative subsurface model of the AMAYA porphyry copper target">
        <canvas id="terrain" width="760" height="470" role="img" aria-label="Animated illustration of a wireframe terrain surface with a subsurface copper anomaly and a drill trace"></canvas>
        <div class="hud" aria-hidden="true">
          <span class="c tl"></span><span class="c tr"></span><span class="c bl"></span><span class="c br"></span>
          <div class="hud-top"><span class="dot"></span>Subsurface model &middot; illustrative<b>Atacama &middot; Chile</b></div>
          <div class="hud-bot">
            <div><small>Elevation</small><b>3,800 m</b></div>
            <div><small>Concessions</small><b>9</b></div>
            <div><small>Target</small><b class="hot">Cu porphyry</b></div>
          </div>
        </div>
      </figure>
    </div>
  </section>

  <div class="stats" aria-label="Key project statistics">
    <div class="stat rise"><b data-count="9">0</b><small>Copper concessions</small></div>
    <div class="stat rise"><b data-count="2353">0</b><small>Hectares</small></div>
    <div class="stat rise"><b data-count="5814">0</b><small>Acres</small></div>
    <div class="stat rise"><b data-count="3800" data-suffix=" m">0</b><small>Above sea level</small></div>
    <div class="stat rise"><b data-count="80" data-suffix=" km">0</b><small>North of Calama</small></div>
  </div>

  <section>
    <div class="wrap split">
      <div class="rise">
        <p class="tag">Overview</p>
        <h2>A copper exploration project in the world&rsquo;s premier copper belt.</h2>
        <p class="body">AMAYA is a copper exploration project located in the Atacama Desert, Chile. The project comprises 9 copper concessions covering a total area of 2,353 hectares &mdash; approximately 5,814 acres &mdash; at 3,800 metres above sea level, 80 km north of the city of Calama in the Antofagasta Region.</p>
        <p class="body">A first drilling campaign has been completed; its findings are set out on <a href="project.html" style="color:var(--cu-lt);border-bottom:1px solid rgba(240,168,104,.35)">the project page</a>. AMAYA is an exploration-stage project: no mineral resources or mineral reserves have been declared.</p>
        <figure class="media" style="aspect-ratio:16/10;margin-top:14px">
          <img src="copper-detail.jpg" alt="Detail of raw copper-bearing ore" width="560" height="350" loading="eager" decoding="async">
          <figcaption class="cap">Copper mineralisation</figcaption>
        </figure>
      </div>
      <div class="rise">
        <dl class="spec">
          <div><dt>Project</dt><dd>AMAYA Copper Exploration Project</dd></div>
          <div><dt>Country</dt><dd>Chile</dd></div>
          <div><dt>Region</dt><dd>Atacama Desert &middot; Regi&oacute;n de Antofagasta</dd></div>
          <div><dt>Concessions</dt><dd>9 copper concessions</dd></div>
          <div><dt>Total area</dt><dd>2,353 hectares (5,814 acres)</dd></div>
          <div><dt>Elevation</dt><dd>3,800 m above sea level</dd></div>
          <div><dt>Nearest city</dt><dd>Calama &mdash; 80 km south</dd></div>
          <div><dt>Target</dt><dd>Porphyry copper</dd></div>
          <div><dt>Structural setting</dt><dd>West Fault corridor</dd></div>
          <div><dt>Stage</dt><dd>Exploration</dd></div>
        </dl>
      </div>
    </div>
  </section>

  <div class="band slot">
    <img src="ore-macro.jpg" alt="Macro view of chalcopyrite copper sulphide crystals in dark host rock" width="1400" height="781" loading="eager" decoding="async">
    <div class="veil"></div>
    <div class="band-txt"><p class="big rise"><span class="k">The target</span>A porphyry copper system beneath the Atacama.</p></div>
    <p class="imgnote">Illustrative mineral imagery</p>
  </div>

  <section id="latest" class="vsec" aria-labelledby="h2-latest">
    <div class="wrap">
      <div class="vhead rise">
        <div>
          <p class="tag">Latest</p>
          <h2 id="h2-latest">From the field.</h2>
          <p class="body">A short view of current activity on the project. Full exploration detail on <a href="project.html" style="color:var(--cu-lt)">The Project</a>.</p>
        </div>
      </div>
      <figure class="vfig rise">
      <div class="vframe">
          <video preload="none" playsinline controls poster="video-project-update-poster.jpg" aria-label="Current activity on the AMAYA project">
            <source src="video-project-update.webm" type="video/webm">
            <source src="video-project-update.mp4" type="video/mp4">
          </video>
          <div class="vph">
            <svg class="vico" viewBox="0 0 48 48" fill="none" aria-hidden="true"><rect x="4" y="11" width="30" height="26" rx="4" stroke="#c87533" stroke-width="1.4"/><path d="M34 21l10-6v18l-10-6z" stroke="#c87533" stroke-width="1.4" stroke-linejoin="round"/><circle cx="19" cy="24" r="5" stroke="#8c95a6" stroke-width="1.2"/></svg>
            <span class="vlabel">Awaiting client footage</span>
            <span class="vhint">Current activity on the AMAYA project</span>
            <span class="vspec">MP4 + WebM &middot; 1920&times;1080 &middot; 16:9 &middot; 15&ndash;30 s &middot; target under 10 MB</span>
          </div>
        </div>
        <figcaption class="vcap">Recorded on site &middot; exploration stage</figcaption>
      </figure>
    </div>
  </section>

  <div class="divider"></div>

  <section id="assets" aria-labelledby="h2-assets">
    <div class="wrap">
      <p class="tag rise">Mining assets</p>
      <h2 class="rise" id="h2-assets">Two mines, in progress.</h2>
      <p class="sub rise">Alongside the Atacama exploration ground, the company holds two mining assets &mdash; one copper ore, one iron ore. Both are currently in progress.</p>
      <div class="minecards">
        <a class="minecard rise" href="mines.html#copper">
          <span class="mc-ico" aria-hidden="true">
            <svg viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.5">
              <path d="M24 6l14 9v18l-14 9-14-9V15l14-9z"/><path d="M24 6v18m0 0l14-9M24 24L10 15m14 9v18"/>
            </svg>
          </span>
          <h3>Copper Ore Mine</h3>
          <p>Copper ore mining asset. Site photography, footage and operational detail are published as the company releases them.</p>
          <span class="go">Explore the mine</span>
        </a>
        <a class="minecard rise" href="mines.html#iron">
          <span class="mc-ico" aria-hidden="true">
            <svg viewBox="0 0 48 48" fill="none" stroke="url(#fe)" stroke-width="1.5">
              <path d="M8 36l10-22 10 14 6-8 6 16z"/><path d="M8 36h32"/>
            </svg>
          </span>
          <h3>Iron Ore Mine</h3>
          <p>Iron ore mining asset. Site photography, footage and operational detail are published as the company releases them.</p>
          <span class="go">Explore the mine</span>
        </a>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <section>
    <div class="wrap">
      <p class="tag rise">Explore</p>
      <h2 class="rise">The company in six parts.</h2>
      <p class="sub rise">Each section stands on its own &mdash; open the one you need.</p>
      <div class="navcards">
        <a class="navcard rise" href="project.html">
          <p class="n">01</p><h3>The Project</h3>
          <p>Full 9-concession breakdown totalling 2,353 hectares, the West Fault setting, and the exploration programme to date.</p>
          <span class="go">Concessions &amp; geology</span>
        </a>
        <a class="navcard rise" href="mines.html">
          <p class="n">02</p><h3>Our Mines</h3>
          <p>The copper ore mine and the iron ore mine &mdash; galleries, site footage and operational detail.</p>
          <span class="go">Mining operations</span>
        </a>
        <a class="navcard rise" href="location.html">
          <p class="n">03</p><h3>Location &amp; Logistics</h3>
          <p>Distances to Calama Airport and to the Tocopilla, Puerto Angamos and Antofagasta export ports, plus neighbouring producing operations.</p>
          <span class="go">Access &amp; logistics</span>
        </a>
        <a class="navcard rise" href="market.html">
          <p class="n">04</p><h3>Copper Market</h3>
          <p>Current indicative copper reference price per metric tonne, and the demand backdrop.</p>
          <span class="go">Market context</span>
        </a>
        <a class="navcard rise" href="leadership.html">
          <p class="n">05</p><h3>Leadership</h3>
          <p>The executive team &mdash; Chief Executive Officer, Managing Director, Chief Financial Officer and Chief Geologist.</p>
          <span class="go">Executive team</span>
        </a>
        <a class="navcard rise" href="about.html">
          <p class="n">06</p><h3>About</h3>
          <p>Our approach to responsible exploration in the high desert, and contact details.</p>
          <span class="go">Approach &amp; contact</span>
        </a>
      </div>
    </div>
  </section>
'''

BODIES['project'] = r'''
  <section class="phead">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="index.html">Amaya</a><span>/</span>The Project
      </nav>
      <p class="eyebrow rise">01 &mdash; The Project</p>
      <h1 class="rise">The Project</h1>
      <p class="lead rise">Nine copper concessions totalling 2,353 hectares on the West Fault corridor, and the exploration work completed to date.</p>
    </div>
  </section>

  <section id="concessions" aria-labelledby="h2-conc">
    <div class="wrap">
      <p class="tag rise">Concessions</p>
      <h2 class="rise" id="h2-conc">Total size of all AMAYA concessions</h2>
      <p class="sub rise">Area by concession (from the documents).</p>

      <div class="figrow">
        <div class="fig rise"><b>9</b><small>Copper concessions</small></div>
        <div class="fig rise"><b>2,353</b><small>Hectares</small></div>
        <div class="fig rise"><b>5,814</b><small>Acres</small></div>
      </div>

      <div class="tablewrap rise">
        <table class="data">
          <caption>AMAYA concessions &mdash; area by concession</caption>
          <thead><tr><th scope="col">Concession</th><th scope="col">Area</th></tr></thead>
          <tbody>
            <tr><td class="name">AMAYA UNO</td><td>300 ha</td></tr>
            <tr><td class="name">AMAYA DOS</td><td>300 ha</td></tr>
            <tr><td class="name">AMAYA TRES</td><td>292 ha</td></tr>
            <tr><td class="name">AMAYA CUATRO</td><td>286 ha</td></tr>
            <tr><td class="name">AMAYA CINCO</td><td>300 ha</td></tr>
            <tr><td class="name">AMAYA SEIS</td><td>245 ha</td></tr>
            <tr><td class="name">AMAYA SIETE</td><td>196 ha</td></tr>
            <tr><td class="name">AMAYA OCHO</td><td>244 ha</td></tr>
            <tr><td class="name">AMAYA NUEVE (1/22)</td><td>190 ha</td></tr>
          </tbody>
          <tfoot><tr><td>Total</td><td>2,353 ha</td></tr></tfoot>
        </table>
      </div>
      <p class="src rise">Total across the 9 concessions: 300 + 300 + 292 + 286 + 300 + 245 + 196 + 244 + 190 = 2,353 hectares. At 2.47105 acres per hectare, that is approximately 5,814 acres.</p>
    </div>
  </section>

  <div class="band slot">
    <img src="drill-core.jpg" alt="Geological drill core segments laid out in a core tray" width="1400" height="781" loading="eager" decoding="async">
    <div class="veil"></div>
    <div class="band-txt"><p class="big rise"><span class="k">First drilling campaign</span>Indicating potential for hidden porphyry copper mineralisation.</p></div>
    <p class="imgnote">Illustrative core imagery</p>
  </div>

  <section id="geology" aria-labelledby="h2-geo">
    <div class="wrap split">
      <div class="rise">
        <p class="tag">Geology</p>
        <h2 id="h2-geo">Positioned on the West Fault.</h2>
        <p class="body">As the project is present through the West Fault, this could indicate the presence in the area of a porphyry copper cluster.</p>
        <p class="body">The West Fault system is the structural corridor that hosts several of the region&rsquo;s major copper deposits &mdash; placing AMAYA in a geologically favourable setting for further exploration.</p>
        <dl class="spec" style="margin-top:24px">
          <div><dt>Deposit model</dt><dd>Porphyry copper</dd></div>
          <div><dt>Structural corridor</dt><dd>West Fault</dd></div>
          <div><dt>Neighbours</dt><dd>El Abra 15 km SE &middot; Chonchi 22 km SE</dd></div>
        </dl>
      </div>
      <div class="strata rise" aria-hidden="true">
        <svg viewBox="0 0 460 320">
          <clipPath id="cl"><rect x="20" y="30" width="420" height="260" rx="12"/></clipPath>
          <g clip-path="url(#cl)">
            <rect x="20" y="30"  width="420" height="60" fill="#141922"/>
            <rect x="20" y="90"  width="420" height="66" fill="#111620"/>
            <rect x="20" y="156" width="420" height="70" fill="#0e131c"/>
            <rect x="20" y="226" width="420" height="64" fill="#0b1018"/>
            <ellipse cx="250" cy="206" rx="112" ry="72" fill="url(#core)" opacity=".22"/>
            <ellipse cx="250" cy="206" rx="72"  ry="46" fill="url(#core)" opacity=".35"/>
            <ellipse cx="250" cy="206" rx="34"  ry="22" fill="url(#core)" opacity=".65" class="pulse"/>
            <path class="vein" d="M120 20 L172 300" stroke="#4fbfa8" stroke-width="2.4" fill="none" opacity=".85"/>
            <g class="vein" stroke="url(#cu)" stroke-width="1.8" fill="none" opacity=".95">
              <path d="M150 120 q60 26 100 12 q54 -18 96 26"/>
              <path d="M170 190 q56 -34 108 -6 q46 26 84 -8"/>
              <path d="M186 252 q52 22 108 4 q48 -16 82 14"/>
            </g>
            <rect class="sweep" x="20" y="30" width="86" height="260" fill="url(#sweepg)"/>
          </g>
          <g stroke="rgba(255,255,255,.18)" stroke-width="1" font-family="Inter,Arial" font-size="9" fill="#8c95a6">
            <line x1="20" y1="30" x2="20" y2="290"/>
            <line x1="14" y1="90"  x2="20" y2="90"/><text x="-4" y="93" text-anchor="end" stroke="none">200</text>
            <line x1="14" y1="156" x2="20" y2="156"/><text x="-4" y="159" text-anchor="end" stroke="none">450</text>
            <line x1="14" y1="226" x2="20" y2="226"/><text x="-4" y="229" text-anchor="end" stroke="none">700</text>
          </g>
          <rect x="20" y="30" width="420" height="260" rx="12" fill="none" stroke="rgba(255,255,255,.12)"/>
          <text x="128" y="20" fill="#4fbfa8" font-size="10" font-family="Inter,Arial" letter-spacing="3">WEST FAULT</text>
          <text x="196" y="308" fill="#8c95a6" font-size="10" font-family="Inter,Arial" letter-spacing="3">PORPHYRY TARGET</text>
        </svg>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <section id="exploration" aria-labelledby="h2-exp">
    <div class="wrap">
      <p class="tag rise">Exploration</p>
      <h2 class="rise" id="h2-exp">From first pass to definition.</h2>
      <ul class="tl">
        <li class="rise"><h3>Concessions secured</h3><p>9 copper concessions consolidated, covering 2,353 hectares (5,814 acres) in the Atacama Desert, 80 km north of Calama.</p></li>
        <li class="rise"><h3>First drilling campaign</h3><p>Indicated significant potential for hidden mineralisation in the form of a porphyry copper system.</p></li>
        <li class="rise"><h3>Structural interpretation</h3><p>Project mapped across the West Fault &mdash; a corridor associated with regional porphyry copper clusters.</p></li>
        <li class="rise"><h3>Next phase</h3><p>Follow-up drilling and geophysics to define the extent and character of the target system.</p></li>
      </ul>
      <p class="note-box rise">AMAYA is an exploration-stage project. Exploration potential is conceptual: no mineral resources or mineral reserves have been estimated or declared, and no copper grades, production volumes or economic forecasts are stated or implied.</p>
    </div>
  </section>

  <div class="divider"></div>

  <section id="field" class="vsec" aria-labelledby="h2-field">
    <div class="wrap">
      <div class="vhead rise">
        <div>
          <p class="tag">On site</p>
          <h2 id="h2-field">Work in progress at AMAYA.</h2>
          <p class="body">Footage recorded on the concessions during the current exploration programme, 3,800 m above sea level in the Atacama Desert.</p>
        </div>
      </div>
      <figure class="vfig rise">
      <div class="vframe">
          <video preload="none" playsinline controls poster="video-field-work-poster.jpg" aria-label="Exploration work under way on the AMAYA concessions">
            <source src="video-field-work.webm" type="video/webm">
            <source src="video-field-work.mp4" type="video/mp4">
          </video>
          <div class="vph">
            <svg class="vico" viewBox="0 0 48 48" fill="none" aria-hidden="true"><rect x="4" y="11" width="30" height="26" rx="4" stroke="#c87533" stroke-width="1.4"/><path d="M34 21l10-6v18l-10-6z" stroke="#c87533" stroke-width="1.4" stroke-linejoin="round"/><circle cx="19" cy="24" r="5" stroke="#8c95a6" stroke-width="1.2"/></svg>
            <span class="vlabel">Awaiting client footage</span>
            <span class="vhint">Exploration work under way on the AMAYA concessions</span>
            <span class="vspec">MP4 + WebM &middot; 1920&times;1080 &middot; 16:9 &middot; target under 15 MB</span>
          </div>
        </div>
        <figcaption class="vcap">Field operations &middot; exploration stage</figcaption>
      </figure>
    </div>
  </section>
'''

BODIES['mines'] = r'''  <section class="phead">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="index.html">Amaya</a><span>/</span>Our Mines
      </nav>
      <p class="eyebrow rise">02 &mdash; Our Mines</p>
      <h1 class="rise">Our Mines</h1>
      <p class="lead rise">The company holds two mining assets &mdash; a copper ore mine and an iron ore mine. Both are currently in progress.</p>
    </div>
  </section>

  <div class="stats four" aria-label="Mining assets at a glance">
    <div class="stat rise"><b data-count="2">0</b><small>Mining assets</small></div>
    <div class="stat rise"><b class="txt">Cu</b><small>Copper ore mine</small></div>
    <div class="stat rise"><b class="txt">Fe</b><small>Iron ore mine</small></div>
    <div class="stat rise"><b class="txt">In progress</b><small>Current status</small></div>
  </div>

  <section aria-labelledby="h2-intro">
    <div class="wrap">
      <p class="tag rise">Mining operations</p>
      <h2 class="rise" id="h2-intro">Two assets, each with its own page of record.</h2>
      <p class="sub rise">Each mine below carries its own gallery, site footage and operational detail. Information is published only once the company has supplied it &mdash; nothing on this page is estimated or inferred.</p>
    </div>
  </section>

  <section id="copper" class="mine" aria-labelledby="h2-copper">
    <div class="wrap">
      <div class="mine-head rise">
        <span class="mine-ico" aria-hidden="true">
          <svg viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.5"><path d="M24 6l14 9v18l-14 9-14-9V15l14-9z"/><path d="M24 6v18m0 0l14-9M24 24L10 15m14 9v18"/></svg>
        </span>
        <div>
          <p class="tag">Asset 01</p>
          <h2 id="h2-copper">Copper Ore Mine</h2>
        </div>
        <span class="status">In progress</span>
      </div>
      <div class="mine-body">
        <div class="rise">
          <p class="body">The Copper Ore Mine is one of two mining assets held by the company. Work at the site is currently in progress.</p>
          <p class="body">Site photography, footage, location detail and operational information are published on this page as the company releases them. No production figures, grades, resources or reserves have been declared for this asset.</p>
          <div class="btns"><a class="cta" href="about.html#contact">Enquire about this mine</a></div>
        </div>
        <dl class="spec rise">
          <div><dt>Asset</dt><dd>Copper Ore Mine</dd></div>
          <div><dt>Commodity</dt><dd>Copper ore</dd></div>
          <div><dt>Status</dt><dd>In progress</dd></div>
          <div><dt>Location</dt><dd class="pend">Awaiting client information</dd></div>
          <div><dt>Operation type</dt><dd class="pend">Awaiting client information</dd></div>
          <div><dt>Infrastructure</dt><dd class="pend">Awaiting client information</dd></div>
        </dl>
      </div>

      <figure class="mine-hero slot rise">
        <img src="assets/images/mines/copper/copper-mine-1.jpg" alt="Copper Ore Mine site" width="1400" height="700" loading="eager" decoding="async">
        <div class="ph-note"><span>Awaiting client photography</span><small>Site photography &middot; 2400&times;1200 or wider &middot; JPG</small></div>
      </figure>

      <h3 class="gal-h rise">Gallery</h3>
      <div class="gal rise" role="list">
        <button class="gitem slot" type="button" role="listitem" data-full="assets/images/mines/copper/copper-mine-1.jpg" data-cap="Copper Ore Mine &mdash; site view" aria-label="Open larger view: Copper Ore Mine &mdash; site view">
          <img src="assets/images/mines/copper/copper-mine-1.jpg" alt="Copper Ore Mine &mdash; site view" width="600" height="420" loading="eager" decoding="async">
          <span class="ph-mini"><small>Photograph to follow</small></span>
        </button>
        <button class="gitem slot" type="button" role="listitem" data-full="assets/images/mines/copper/copper-mine-2.jpg" data-cap="Copper Ore Mine &mdash; mining operation" aria-label="Open larger view: Copper Ore Mine &mdash; mining operation">
          <img src="assets/images/mines/copper/copper-mine-2.jpg" alt="Copper Ore Mine &mdash; mining operation" width="600" height="420" loading="eager" decoding="async">
          <span class="ph-mini"><small>Photograph to follow</small></span>
        </button>
        <button class="gitem slot" type="button" role="listitem" data-full="assets/images/mines/copper/copper-mine-3.jpg" data-cap="Copper Ore Mine &mdash; infrastructure and equipment" aria-label="Open larger view: Copper Ore Mine &mdash; infrastructure and equipment">
          <img src="assets/images/mines/copper/copper-mine-3.jpg" alt="Copper Ore Mine &mdash; infrastructure and equipment" width="600" height="420" loading="eager" decoding="async">
          <span class="ph-mini"><small>Photograph to follow</small></span>
        </button>
      </div>
      <p class="src rise">Photographs are supplied by the company. A slot with no image yet stays empty rather than showing a broken image.</p>

      <h3 class="gal-h rise">Site footage</h3>
      <figure class="vfig rise">
        <div class="vframe">
          <video preload="none" playsinline controls poster="assets/videos/mines/copper/copper-mine-poster.jpg" aria-label="Copper Ore Mine &mdash; site footage">
            <source src="assets/videos/mines/copper/copper-mine-video.webm" type="video/webm">
            <source src="assets/videos/mines/copper/copper-mine-video.mp4" type="video/mp4">
          </video>
          <div class="vph">
            <svg class="vico" viewBox="0 0 48 48" fill="none" aria-hidden="true"><rect x="4" y="11" width="30" height="26" rx="4" stroke="#c87533" stroke-width="1.4"/><path d="M34 21l10-6v18l-10-6z" stroke="#c87533" stroke-width="1.4" stroke-linejoin="round"/><circle cx="19" cy="24" r="5" stroke="#8c95a6" stroke-width="1.2"/></svg>
            <span class="vlabel">Awaiting client footage</span>
            <span class="vhint">Copper Ore Mine &mdash; site footage</span>
            <span class="vspec">MP4 + WebM &middot; 1920&times;1080 &middot; 16:9</span>
          </div>
        </div>
        <figcaption class="vcap">Copper Ore Mine &middot; recorded on site</figcaption>
      </figure>
    </div>
  </section>

  <div class="divider"></div>

  <section id="iron" class="mine" aria-labelledby="h2-iron">
    <div class="wrap">
      <div class="mine-head rise">
        <span class="mine-ico" aria-hidden="true">
          <svg viewBox="0 0 48 48" fill="none" stroke="url(#fe)" stroke-width="1.5"><path d="M8 36l10-22 10 14 6-8 6 16z"/><path d="M8 36h32"/></svg>
        </span>
        <div>
          <p class="tag">Asset 02</p>
          <h2 id="h2-iron">Iron Ore Mine</h2>
        </div>
        <span class="status">In progress</span>
      </div>
      <div class="mine-body">
        <div class="rise">
          <p class="body">The Iron Ore Mine is the company&rsquo;s second mining asset. Work at the site is currently in progress.</p>
          <p class="body">Site photography, footage, location detail and operational information are published on this page as the company releases them. No production figures, grades, resources or reserves have been declared for this asset.</p>
          <div class="btns"><a class="cta" href="about.html#contact">Enquire about this mine</a></div>
        </div>
        <dl class="spec rise">
          <div><dt>Asset</dt><dd>Iron Ore Mine</dd></div>
          <div><dt>Commodity</dt><dd>Iron ore</dd></div>
          <div><dt>Status</dt><dd>In progress</dd></div>
          <div><dt>Location</dt><dd class="pend">Awaiting client information</dd></div>
          <div><dt>Operation type</dt><dd class="pend">Awaiting client information</dd></div>
          <div><dt>Infrastructure</dt><dd class="pend">Awaiting client information</dd></div>
        </dl>
      </div>

      <figure class="mine-hero slot rise">
        <img src="assets/images/mines/iron/iron-mine-1.jpg" alt="Iron Ore Mine site" width="1400" height="700" loading="eager" decoding="async">
        <div class="ph-note"><span>Awaiting client photography</span><small>Site photography &middot; 2400&times;1200 or wider &middot; JPG</small></div>
      </figure>

      <h3 class="gal-h rise">Gallery</h3>
      <div class="gal rise" role="list">
        <button class="gitem slot" type="button" role="listitem" data-full="assets/images/mines/iron/iron-mine-1.jpg" data-cap="Iron Ore Mine &mdash; site view" aria-label="Open larger view: Iron Ore Mine &mdash; site view">
          <img src="assets/images/mines/iron/iron-mine-1.jpg" alt="Iron Ore Mine &mdash; site view" width="600" height="420" loading="eager" decoding="async">
          <span class="ph-mini"><small>Photograph to follow</small></span>
        </button>
        <button class="gitem slot" type="button" role="listitem" data-full="assets/images/mines/iron/iron-mine-2.jpg" data-cap="Iron Ore Mine &mdash; mining operation" aria-label="Open larger view: Iron Ore Mine &mdash; mining operation">
          <img src="assets/images/mines/iron/iron-mine-2.jpg" alt="Iron Ore Mine &mdash; mining operation" width="600" height="420" loading="eager" decoding="async">
          <span class="ph-mini"><small>Photograph to follow</small></span>
        </button>
        <button class="gitem slot" type="button" role="listitem" data-full="assets/images/mines/iron/iron-mine-3.jpg" data-cap="Iron Ore Mine &mdash; infrastructure and equipment" aria-label="Open larger view: Iron Ore Mine &mdash; infrastructure and equipment">
          <img src="assets/images/mines/iron/iron-mine-3.jpg" alt="Iron Ore Mine &mdash; infrastructure and equipment" width="600" height="420" loading="eager" decoding="async">
          <span class="ph-mini"><small>Photograph to follow</small></span>
        </button>
      </div>
      <p class="src rise">Photographs are supplied by the company. A slot with no image yet stays empty rather than showing a broken image.</p>

      <h3 class="gal-h rise">Site footage</h3>
      <figure class="vfig rise">
        <div class="vframe">
          <video preload="none" playsinline controls poster="assets/videos/mines/iron/iron-mine-poster.jpg" aria-label="Iron Ore Mine &mdash; site footage">
            <source src="assets/videos/mines/iron/iron-mine-video.webm" type="video/webm">
            <source src="assets/videos/mines/iron/iron-mine-video.mp4" type="video/mp4">
          </video>
          <div class="vph">
            <svg class="vico" viewBox="0 0 48 48" fill="none" aria-hidden="true"><rect x="4" y="11" width="30" height="26" rx="4" stroke="#c87533" stroke-width="1.4"/><path d="M34 21l10-6v18l-10-6z" stroke="#c87533" stroke-width="1.4" stroke-linejoin="round"/><circle cx="19" cy="24" r="5" stroke="#8c95a6" stroke-width="1.2"/></svg>
            <span class="vlabel">Awaiting client footage</span>
            <span class="vhint">Iron Ore Mine &mdash; site footage</span>
            <span class="vspec">MP4 + WebM &middot; 1920&times;1080 &middot; 16:9</span>
          </div>
        </div>
        <figcaption class="vcap">Iron Ore Mine &middot; recorded on site</figcaption>
      </figure>
    </div>
  </section>
'''

BODIES['location'] = r'''
  <section class="phead">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="index.html">Amaya</a><span>/</span>Location &amp; Logistics
      </nav>
      <p class="eyebrow rise">02 &mdash; Location &amp; Logistics</p>
      <h1 class="rise">Location &amp; Logistics</h1>
      <p class="lead rise">AMAYA sits in the Atacama Desert, Regi&oacute;n de Antofagasta, 80 km north of Calama &mdash; a region served by regional air access and by three Pacific export ports, the nearest at Tocopilla.</p>
    </div>
  </section>

  <section id="access" aria-labelledby="h2-acc">
    <div class="wrap">
      <p class="tag rise">Access</p>
      <h2 class="rise" id="h2-acc">Established mining district, established logistics.</h2>
      <div class="logi">
        <div class="card rise">
          <svg class="ico" viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.6" aria-hidden="true">
            <circle cx="24" cy="20" r="7"/><path d="M24 41c0 0 13-13 13-21a13 13 0 1 0-26 0c0 8 13 21 13 21z"/>
          </svg>
          <p class="lbl">AMAYA Project</p>
          <span class="big">Atacama</span>
          <p class="note">Atacama Desert, Regi&oacute;n de Antofagasta, Chile. Elevation 3,800 m; the ground lies due north of Calama.</p>
        </div>
        <div class="card rise">
          <svg class="ico" viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.6" aria-hidden="true">
            <path d="M4 27l40-13-6 12 6 12-40-13z"/><path d="M14 24v12"/>
          </svg>
          <p class="lbl">Calama Airport (CJC)</p>
          <span class="big">Approx. 85 km</span>
          <p class="note">El Loa International Airport, Calama &mdash; regional air access. Approx. 85 km straight-line; approx. 100 km by road via Ruta 21 / Ruta 24.</p>
        </div>
        <div class="card rise">
          <svg class="ico" viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.6" aria-hidden="true">
            <path d="M6 38h36"/><path d="M24 38V14"/><path d="M24 14l12 8H12l12-8z"/><path d="M10 30h28"/>
          </svg>
          <p class="lbl">Nearest port &mdash; Tocopilla</p>
          <span class="big">Approx. 125&ndash;130 km</span>
          <p class="note">Port of Tocopilla, on the Antofagasta Region coast &mdash; the closest maritime outlet to the project. Distance as advised by the company; indicative pending surveyed coordinates.</p>
        </div>
        <div class="card rise">
          <svg class="ico" viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.6" aria-hidden="true">
            <path d="M6 38h36"/><path d="M24 38V14"/><path d="M24 14l12 8H12l12-8z"/><path d="M10 30h28"/>
          </svg>
          <p class="lbl">Export port &mdash; Puerto Angamos / Mejillones</p>
          <span class="big">Approx. 200&ndash;240 km</span>
          <p class="note">Puerto Angamos at Mejillones &mdash; the region&rsquo;s principal bulk and concentrate terminal. Distance as advised by the company; indicative pending surveyed coordinates.</p>
        </div>
        <div class="card rise">
          <svg class="ico" viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.6" aria-hidden="true">
            <path d="M6 38h36"/><path d="M24 38V14"/><path d="M24 14l12 8H12l12-8z"/><path d="M10 30h28"/>
          </svg>
          <p class="lbl">Export port &mdash; Antofagasta</p>
          <span class="big">Approx. 260 km</span>
          <p class="note">Port of Antofagasta &mdash; a long-established copper export port serving the Calama mining district. Approx. 260 km straight-line; approx. 315 km by road via Ruta 25 / Ruta 5.</p>
        </div>
      </div>

      <p class="src rise">
        Distances are measured from the project&rsquo;s stated position (Atacama Desert, 80 km north of Calama, Regi&oacute;n de Antofagasta). The Tocopilla and Puerto Angamos&nbsp;/ Mejillones figures are as advised by the company. The Calama Airport and Antofagasta figures are great-circle distances calculated from that position, with road figures following the Calama&ndash;Antofagasta corridor (Ruta 25, 119.3 km of highway between Calama and the Ruta 5 junction at Carmen Alto, plus Ruta 5 to Antofagasta); verified 4 September 2026. All figures are indicative pending confirmation of surveyed concession coordinates.
      </p>
    </div>
  </section>

  <div class="band slot">
    <img src="desert-crust.jpg" alt="Cracked high-altitude arid desert ground seen from above" width="1400" height="781" loading="eager" decoding="async">
    <div class="veil"></div>
    <div class="band-txt"><p class="big rise"><span class="k">3,800 metres above sea level</span>2,353 hectares across 9 concessions, 80 km north of Calama.</p></div>
    <p class="imgnote">Illustrative terrain imagery</p>
  </div>

  <section id="neighbours" aria-labelledby="h2-nb">
    <div class="wrap">
      <p class="tag rise">Neighbours</p>
      <h2 class="rise" id="h2-nb">Surrounded by established operations.</h2>
      <p class="sub rise">The project sits within an established mining district, with two producing operations within a short radius to the southeast.</p>
      <div class="cards">
        <div class="card rise">
          <svg class="ico" viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.6" aria-hidden="true">
            <path d="M4 38 L18 14 L27 28 L33 20 L44 38 Z"/><circle cx="18" cy="14" r="2.4" fill="#f0a868" stroke="none"/>
          </svg>
          <h3>Minera El Abra</h3>
          <p>Operated by Freeport-McMoRan &mdash; one of the district&rsquo;s established copper operations.</p>
          <p class="dist">15 km southeast</p>
        </div>
        <div class="card rise">
          <svg class="ico" viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.6" aria-hidden="true">
            <path d="M6 40 h36"/><path d="M12 40 V22 l12-8 12 8 v18"/><path d="M20 40 v-10 h8 v10"/>
          </svg>
          <h3>Chonchi Mine</h3>
          <p>A further nearby operation reinforcing the prospectivity of the surrounding ground.</p>
          <p class="dist">22 km southeast</p>
        </div>
        <div class="card rise">
          <svg class="ico" viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.6" aria-hidden="true">
            <circle cx="24" cy="20" r="7"/><path d="M24 41 c0 0 13-13 13-21 a13 13 0 1 0 -26 0 c0 8 13 21 13 21z"/>
          </svg>
          <h3>Calama</h3>
          <p>Regional mining hub providing logistics, workforce and infrastructure access.</p>
          <p class="dist">80 km south</p>
        </div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <section id="site-access" class="vsec" aria-labelledby="h2-access">
    <div class="wrap">
      <div class="vhead rise">
        <div>
          <p class="tag">Access</p>
          <h2 id="h2-access">The route to site.</h2>
          <p class="body">The approach from Calama and the terrain across the concession block, recorded on site.</p>
        </div>
      </div>
      <figure class="vfig rise">
      <div class="vframe">
          <video preload="none" playsinline controls poster="video-site-access-poster.jpg" aria-label="Access route and terrain across the AMAYA concession block">
            <source src="video-site-access.webm" type="video/webm">
            <source src="video-site-access.mp4" type="video/mp4">
          </video>
          <div class="vph">
            <svg class="vico" viewBox="0 0 48 48" fill="none" aria-hidden="true"><rect x="4" y="11" width="30" height="26" rx="4" stroke="#c87533" stroke-width="1.4"/><path d="M34 21l10-6v18l-10-6z" stroke="#c87533" stroke-width="1.4" stroke-linejoin="round"/><circle cx="19" cy="24" r="5" stroke="#8c95a6" stroke-width="1.2"/></svg>
            <span class="vlabel">Awaiting client footage</span>
            <span class="vhint">Access route and terrain across the AMAYA concession block</span>
            <span class="vspec">MP4 + WebM &middot; 1920&times;1080 &middot; 16:9 &middot; target under 15 MB</span>
          </div>
        </div>
        <figcaption class="vcap">Site access &middot; indicative</figcaption>
      </figure>
    </div>
  </section>
'''

BODIES['market'] = r'''
  <section class="phead">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="index.html">Amaya</a><span>/</span>Copper Market
      </nav>
      <p class="eyebrow rise">03 &mdash; Copper Market</p>
      <h1 class="rise">Copper Market</h1>
      <p class="lead rise">Demand for copper is driven by electrification, renewable energy and grid investment &mdash; and new discoveries are needed to meet it.</p>
    </div>
  </section>

  <section id="price" aria-labelledby="h2-price">
    <div class="wrap">
      <p class="tag rise">Reference price</p>
      <h2 class="rise" id="h2-price">Current copper market reference.</h2>
      <div class="market rise">
        <div>
          <p style="font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:var(--cu-lt);margin-bottom:16px">Copper market</p>
          <p class="price">US$ 14,460</p>
          <p class="price-unit">Per metric tonne</p>
          <p class="price-meta">Indicative market price &middot; Updated: 4 September 2026</p>
        </div>
        <div>
          <figure class="media" style="aspect-ratio:16/9;margin-bottom:20px">
            <img src="copper-ore-sm.jpg" alt="Copper-bearing ore" width="640" height="360" loading="eager" decoding="async">
            <figcaption class="cap">Copper ore</figcaption>
          </figure>
          <p class="body" style="margin-bottom:14px">An indicative benchmark price for copper on international markets, provided for context only.</p>
          <p class="src" style="margin-top:0">Approx. US$14,460 per metric tonne, converted from the benchmark quote of approx. US$6.56 per pound as at 4 September 2026 (1 metric tonne = 2,204.62 lb). Source: Trading Economics copper price data; LME Copper is the global benchmark, quoted in US dollars per metric tonne. Copper prices move continuously &mdash; this figure is a snapshot and should be refreshed before use in any presentation.</p>
        </div>
      </div>
      <p class="note-box rise"><strong style="color:var(--txt)">This is a market reference price.</strong> It is not AMAYA&rsquo;s selling price, and AMAYA does not sell copper at this or any stated price. AMAYA is an exploration-stage project with no declared resources, reserves or production.</p>
    </div>
  </section>

  <div class="divider"></div>

  <section aria-labelledby="h2-demand">
    <div class="wrap">
      <p class="tag rise">Context</p>
      <h2 class="rise" id="h2-demand">Copper for a changing world.</h2>
      <p class="sub rise">Chile is the world&rsquo;s largest copper producer, and the Antofagasta Region hosts several of its largest operations. AMAYA&rsquo;s ground sits within that established belt.</p>
      <div class="cards">
        <div class="card rise"><h3>Electrification</h3><p>Copper is the primary conductor in electric vehicles, charging infrastructure and building services.</p></div>
        <div class="card rise"><h3>Renewable generation</h3><p>Wind and solar installations are materially more copper-intensive per unit of capacity than conventional generation.</p></div>
        <div class="card rise"><h3>Grid investment</h3><p>Transmission and distribution upgrades require sustained copper supply over long build cycles.</p></div>
        <div class="card rise"><h3>New discoveries</h3><p>Meeting that demand depends on bringing new deposits forward &mdash; the purpose of exploration projects such as AMAYA.</p></div>
      </div>
    </div>
  </section>
'''

BODIES['leadership'] = r'''  <section class="phead">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="index.html">Amaya</a><span>/</span>Leadership
      </nav>
      <p class="eyebrow rise">05 &mdash; Leadership</p>
      <h1 class="rise">Leadership</h1>
      <p class="lead rise">AMAYA is directed by a team spanning engineering, corporate finance, operations and field geology.</p>
    </div>
  </section>

  <section id="ceo" aria-labelledby="h2-ceo">
    <div class="wrap">
      <p class="tag rise">Chief Executive Officer</p>
      <article class="feature rise">
        <div class="feature-media">
          <div class="portrait portrait-lg">
            <img src="assets/images/leadership/satish-naidu.jpg" alt="B. Satish Naidu, Chief Executive Officer" width="720" height="900" loading="eager" decoding="async">
            <svg viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.4" aria-hidden="true">
              <circle cx="24" cy="17" r="8"/><path d="M8 42c0-8.8 7.2-14 16-14s16 5.2 16 14"/>
            </svg>
          </div>
        </div>
        <div class="feature-body">
          <h2 id="h2-ceo">B. Satish Naidu</h2>
          <p class="role-lg">Chief Executive Officer</p>
          <p class="body">B. Satish Naidu is an engineering graduate with diverse experience spanning industrial training, maritime operations, aviation infrastructure and emerging aviation technologies. He began his professional career as an NDT Trainer with NDT International, UK, followed by experience in the Merchant Navy, developing strong technical, operational and international exposure.</p>
          <p class="body">He currently focuses on the development and coordination of advanced aviation infrastructure projects in India, with particular expertise in Digital Twin technology, Remote Control Towers (RCT), CNS/ATM systems and vertiport infrastructure.</p>
          <p class="body">As an entrepreneur and business leader, he serves as Executive Director of Params Aero Pvt. Ltd., BTH Aviation Pvt. Ltd., Vertiports Solution Pvt. Ltd. and Sri Raja Lalitha &amp; Co. Through these organisations he is involved in technology-driven aviation initiatives, strategic partnerships, infrastructure development and the implementation of innovative solutions supporting the modernisation of India&rsquo;s aviation ecosystem.</p>
          <p class="body">His professional vision is centred on technology innovation, indigenous capability development and strategic international collaboration, with a focus on contributing to India&rsquo;s next generation of aviation infrastructure and services.</p>
          <h3 class="mini-h">Areas of expertise</h3>
          <ul class="chips">
            <li>Digital Twin technology</li>
            <li>Remote Control Towers (RCT)</li>
            <li>CNS/ATM systems</li>
            <li>Vertiport infrastructure</li>
            <li>Non-destructive testing</li>
            <li>Maritime operations</li>
          </ul>
          <h3 class="mini-h">Directorships</h3>
          <ul class="chips plain-chips">
            <li>Params Aero Pvt. Ltd.</li>
            <li>BTH Aviation Pvt. Ltd.</li>
            <li>Vertiports Solution Pvt. Ltd.</li>
            <li>Sri Raja Lalitha &amp; Co.</li>
          </ul>
        </div>
      </article>
    </div>
  </section>

  <div class="divider"></div>

  <section id="executive" aria-labelledby="h2-exec">
    <div class="wrap">
      <p class="tag rise">Executive leadership</p>
      <h2 class="rise" id="h2-exec">Executive leadership</h2>
      <p class="sub rise">Photographs and full biographies for the executives below are being finalised and will be published here as the company supplies them.</p>
      <div class="people">
        <article class="person rise">
          <div class="portrait">
            <img src="assets/images/leadership/jitendra-khatwani.jpg" alt="Jitendra Khatwani, Managing Director" loading="eager" decoding="async">
            <svg viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.4" aria-hidden="true">
              <circle cx="24" cy="17" r="8"/><path d="M8 42c0-8.8 7.2-14 16-14s16 5.2 16 14"/>
            </svg>
          </div>
          <div class="info">
            <h3>Jitendra Khatwani</h3><p class="role">Managing Director</p>
            <p>Biography, experience and areas of expertise to be provided by the company.</p>
            <span class="pending">Awaiting information</span>
          </div>
        </article>
        <article class="person rise">
          <div class="portrait">
            <img src="assets/images/leadership/gopal-agrawal.jpg" alt="Gopal Agrawal, Chief Financial Officer" loading="eager" decoding="async">
            <svg viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.4" aria-hidden="true">
              <circle cx="24" cy="17" r="8"/><path d="M8 42c0-8.8 7.2-14 16-14s16 5.2 16 14"/>
            </svg>
          </div>
          <div class="info">
            <h3>Gopal Agrawal</h3><p class="role">Chief Financial Officer</p>
            <p>Biography, experience and areas of expertise to be provided by the company.</p>
            <span class="pending">Awaiting information</span>
          </div>
        </article>
        <article class="person rise">
          <div class="portrait">
            <img src="assets/images/leadership/marcelo-astengo-montenegro.jpg" alt="Marcelo Astengo Montenegro, Chief Geologist" loading="eager" decoding="async">
            <svg viewBox="0 0 48 48" fill="none" stroke="url(#cu)" stroke-width="1.4" aria-hidden="true">
              <circle cx="24" cy="17" r="8"/><path d="M8 42c0-8.8 7.2-14 16-14s16 5.2 16 14"/>
            </svg>
          </div>
          <div class="info">
            <h3>Marcelo Astengo Montenegro</h3><p class="role">Chief Geologist</p>
            <p>Geological expertise, mining experience and areas of specialisation to be provided by the company.</p>
            <span class="pending">Awaiting information</span>
          </div>
        </article>
      </div>
      <p class="src rise">Profiles are published as the company supplies them. Until a photograph is provided, a card shows a neutral outline rather than a broken image.</p>
    </div>
  </section>

  <div class="divider"></div>

  <section aria-labelledby="h2-lcon">
    <div class="wrap">
      <p class="tag rise">Contact</p>
      <h2 class="rise" id="h2-lcon">Speak with the team.</h2>
      <p class="body rise">Enquiries from investors, operators and partners are welcome.</p>
      <div class="btns rise"><a class="cta solid" href="about.html#contact">Investor enquiries</a></div>
    </div>
  </section>
'''

BODIES['about'] = r'''
  <section class="phead">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="index.html">Amaya</a><span>/</span>About
      </nav>
      <p class="eyebrow rise">04 &mdash; About</p>
      <h1 class="rise">About AMAYA</h1>
      <p class="lead rise">Our approach to exploring responsibly in the high Atacama, and how to reach us.</p>
    </div>
  </section>

  <div class="band">
    <img src="copper-band.jpg" alt="Close view of copper-bearing ore" width="1400" height="518" loading="eager" decoding="async">
    <div class="veil"></div>
    <div class="band-txt"><p class="big rise"><span class="k">Responsible exploration</span>Working carefully in one of the driest places on earth.</p></div>
  </div>

  <section id="leadership-brief" aria-labelledby="h2-lead">
    <div class="wrap">
      <p class="tag rise">Leadership</p>
      <h2 class="rise" id="h2-lead">Led by an experienced executive team.</h2>
      <p class="sub rise">AMAYA is directed by a Chief Executive Officer, Managing Director, Chief Financial Officer and Chief Geologist. Full profiles, experience and areas of expertise are set out on the leadership page.</p>
      <div class="btns rise"><a class="cta" href="leadership.html">Meet the leadership</a></div>
    </div>
  </section>

  <div class="divider"></div>

  <section id="responsible" aria-labelledby="h2-resp">
    <div class="wrap">
      <p class="tag rise">Responsible exploration</p>
      <h2 class="rise" id="h2-resp">Exploring responsibly in a fragile environment.</h2>
      <p class="sub rise">The Atacama is among the driest places on earth. Our approach to exploration is built around minimising water use, protecting the surrounding environment and working openly with local communities and authorities.</p>
      <div class="cards">
        <div class="card rise"><h3>Water stewardship</h3><p>Minimising consumption and avoiding impact on scarce regional water resources.</p></div>
        <div class="card rise"><h3>Communities</h3><p>Early, transparent engagement with the communities nearest to our licence areas.</p></div>
        <div class="card rise"><h3>Health &amp; safety</h3><p>Safe work at altitude, with procedures matched to remote high-desert conditions.</p></div>
        <div class="card rise"><h3>Land &amp; biodiversity</h3><p>Low-footprint programmes with rehabilitation of disturbed ground after drilling.</p></div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <section id="contact" aria-labelledby="h2-con">
    <div class="wrap">
      <p class="tag rise">Contact</p>
      <h2 class="rise" id="h2-con">Investor enquiries welcome.</h2>
      <p class="body rise">We welcome enquiries from investors, operators and partners with an interest in copper exploration in northern Chile. For information regarding the AMAYA Project, please get in touch.</p>
      <div class="btns rise"><a class="cta solid" href="mailto:info@amayaproject.com">info@amayaproject.com</a></div>
    </div>
  </section>
'''
