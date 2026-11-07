---
marp: true
theme: gruvbox
paginate: true
footer: "Alberto Cámara · From Python to Markdown · PyConES 2026"
---

<style>
.meme {
  border: 3px dashed var(--gb-orange);
  border-radius: 6px;
  color: var(--gb-gray);
  font-style: italic;
  text-align: center;
  padding: 1.2em 1em;
  margin: 0.6em 0;
}
.todo {
  border: 3px dashed var(--gb-purple);
  border-radius: 6px;
  color: var(--gb-purple);
  padding: 0.6em 1em;
  margin: 0.6em 0;
  font-size: 0.8em;
}
.ladder { display: flex; flex-direction: column; gap: 0.35em; margin-top: 0.4em; }
.rung {
  background: var(--gb-bg1);
  color: var(--gb-gray);
  border-left: 6px solid var(--gb-bg2);
  border-radius: 4px;
  padding: 0.35em 0.8em;
  font-size: 0.8em;
}
.rung.done { color: var(--gb-fg4); border-left-color: var(--gb-green); }
.rung.on { background: var(--gb-bg2); color: var(--gb-yellow); border-left-color: var(--gb-orange); font-weight: 700; }
.poll {
  background: var(--gb-bg1);
  border-left: 5px solid var(--gb-aqua);
  color: var(--gb-aqua);
  padding: 0.5em 0.9em;
  margin: 0.8em 0;
  border-radius: 4px;
}
.receipt {
  font-size: 0.65em;
  color: var(--gb-fg4);
  border-top: 1px solid var(--gb-bg2);
  margin-top: 1em;
  padding-top: 0.4em;
}
.big { font-size: 1.6em; font-weight: 700; color: var(--gb-yellow); }
</style>

<!-- _class: lead -->

# From Python to Markdown

## notes from the AI trenches

Alberto Cámara · PyConES 2026

<!-- 0:00. Backup talk: no live demo, lots of hands up. Field notes from client work over the last year, and the state of the industry according to Gergely Orosz (The Pragmatic Engineer). -->

---

# About me

![bg right:30% w:300](https://ber2.github.io/images/pingu.jpg)

Alberto Cámara, [ber2.github.io](https://ber2.github.io/)
- Mathematician
- ~~Data Scientist~~
- ~~ML Engineer~~
- **???**
- Freelance
- Associate Professor @ **UB** & **ESADE**
- Member of **PyBcn**

<!-- 0:30. Stop at the "???" and leave it hanging: next slide. -->

---

# "AI engineer". What is even that?

<div class="columns">
<div>

- AI Engineer
- Prompt Whisperer
- Agent Wrangler
- Markdown Engineer
- Senior LGTM Officer
- Token Accountant

</div>
<div>

![width:600](img/travolta.gif)

</div>
</div>

<!-- 1:30. I used to describe my job in one word. Today, in most projects, I genuinely don't know what to call it. MEME: identity crisis / crossed-out business card. -->

---

# I used to write Python

Now I write this:

```markdown
# CLAUDE.md
- Use descriptive names.
- No comments.
- Do TDD. Really. I mean it this time.
```

…and spend most of my day **reviewing code I didn't write**.

<!-- 3:00. The punchline: the language I write most at work in 2026 is Markdown. Specs, skills, instructions. Python is what comes out the other end and what I read. -->

---

# Show of hands 🙋

<div class="poll">Who typed code <b>by hand</b> this week?</div>

<div class="poll">Who opened an <b>IDE</b> this week?</div>

<div class="receipt">

Orosz, 2026: <i>"Nobody writes code by hand anymore."</i> Codex launched as a non-IDE (Feb 2026), Cursor relaunched without an IDE interface (Apr 2026), Antigravity 2.0 moved away from the IDE (May 2026).

</div>

<!-- 4:00. Two polls, one after the other. Expect lots of hands for the IDE, fewer for typing by hand. React to the room. -->

---

<!-- _class: divider -->

# Ladder 1: how we use the tools

<!-- 5:30 -->

---

# Everybody, hands up 🙋

<div class="poll">Keep your hand up while the answer is <b>yes</b>.<br>Lower it when it's <b>no</b>.</div>


<!-- 5:45. Explain the game: elimination poll. We climb the ladder; at each rung, lower your hand if you have never done that. Last one standing wins nothing. -->

---

# Rung 1 · Autocomplete

<div class="columns">
<div>

The world's most expensive **Tab** key.

<div class="poll">Keep it up if you've accepted an LLM autocomplete suggestion.</div>

</div>
<div class="ladder">
<div class="rung on">1 · Autocomplete</div>
</div>
</div>

<!-- 6:00. Copilot era. Nearly every hand should stay up. -->

---

# Rung 2 · Small tasks

<div class="columns">
<div>

*"Write me a function that parses this date."*

Copy from the chat, paste into the editor, fix the imports.

<div class="poll">Keep it up if you've had an LLM write a whole function for you.</div>

</div>
<div class="ladder">
<div class="rung done">1 · Autocomplete</div>
<div class="rung on">2 · Small tasks</div>
</div>
</div>

<!-- 7:00. The chat-window era. Still small, still fully reviewed, still "my code". -->

---

# Rung 3 · One-shots

<div class="columns">
<div>

One prompt, a whole feature.

- **90%** of the time: right
- **10%** of the time: garbage
- You **don't know** which is which

<div class="poll">Keep it up if you've merged a feature built from a single prompt.</div>

</div>
<div>


<div class="ladder">
<div class="rung done">1 · Autocomplete</div>
<div class="rung done">2 · Small tasks</div>
<div class="rung on">3 · One-shots</div>
</div>

![width:200](img/baby-run.gif)

</div>
</div>

<!-- 8:00. Since the late-2025 models, one-shots got very good. The problem isn't the 10%, it's that the 10% looks exactly like the 90%. That's what pushes you to the next rung. MEME: dice roll / Schrödinger's PR. -->

---

# Rung 4 · Skills

<div class="columns">
<div>

Stop asking for **what**. Start telling it **how**.

- *Use this code style*
- *Do TDD: red, green, refactor*
- *Grill me before you write anything*

<div class="poll">Keep it up if you've written a skill or an AGENTS.md / CLAUDE.md rule.</div>

</div>
<div class="ladder">
<div class="rung done">1 · Autocomplete</div>
<div class="rung done">2 · Small tasks</div>
<div class="rung done">3 · One-shots</div>
<div class="rung on">4 · Skills</div>
</div>
</div>

<div class="receipt">Factory AI: 83% of users use skills, up 2.5× since February (via Orosz, 2026).</div>

<!-- 9:30. Skills in the CLI are how you buy back precision: you encode your team's way of working once and reuse it. This is where Python code turns into Markdown. -->

---

# Rung 5 · The factory

<div class="columns">
<div>

Specs in, PRs out.

- Several agents **in parallel**
- Planner → implementer → reviewer
- **Spec-driven development** (SDD)

<div class="poll">Keep it up if you've run several agents in parallel from a spec.</div>

</div>
<div class="ladder">
<div class="rung done">1 · Autocomplete</div>
<div class="rung done">2 · Small tasks</div>
<div class="rung done">3 · One-shots</div>
<div class="rung done">4 · Skills</div>
<div class="rung on">5 · The factory</div>
</div>
</div>

<div class="receipt">Orosz, 2026: agent-authored PRs outnumbered human-authored PRs on GitHub in August 2026. Heavy users run 5–10 agent sessions at a time.</div>

<!-- 11:00. Few hands left. Ask one of them what their setup looks like. -->

---

# The SDD zoo

| Tool | The idea |
|---|---|
| **OpenSpec** | Lightweight specs, one folder per change: proposal → specs → tasks |
| **GitHub Spec Kit** | Specify → plan → tasks → implement |
| **Superpowers** | Skills library: brainstorm → plan → TDD with subagents |
| **Matt Pocock's skills** | Small composable skills: grill me, TDD, PRD → issues |

<div class="poll">Anyone still up? You're running a <b>software factory in your backyard</b>. 🏭</div>

<!-- 12:00. Don't compare them in depth; the point is that they converge on the same shape: write the spec, let the agents do the rest, review. Applause for the last hands standing. -->

---

<!-- _class: divider -->

# Ladder 2: what we're asked to do

<!-- 13:30 -->

---

# The scope keeps growing

| Then | Now |
|---|---|
| Narrow, specific projects | End-to-end, all-encompassing |
| Big teams | A couple of engineers + their agents |
| A week reading docs to assess a tool | A throwaway prototype before lunch |
| Train and deliver an ML model | Build the app and deploy it with IaC on the cloud |

<!-- 13:45. My own field notes. A few years ago a client hired me to train a model and hand it over. Today the same kind of client expects the model, the API, the frontend, the infra and the CI/CD, from two people. -->

---

# It's not just me

- **1–2 engineers** per project is the max (Katelyn Lesse, Anthropic)
- **Migrations take weeks, not years**
  - Bun, Zig → Rust: 11 days (est. 1.5 engineer-years)
  - Asana, 4,000 test files: 2 weeks (est. 5 years)
- **Generalists over specialists**: demand for iOS, Android and frontend specialists is falling

<div class="receipt">Orosz, "The state of the tech industry in 2026", The Pragmatic Engineer.</div>

<!-- 16:00. Tell one client story, sector only, no names. -->

---

<!-- _class: divider -->

# Whose data, whose model?

<!-- 18:00 -->

---

# There's a lot of room for open models

<div class="columns-3">
<div>

### Sovereignty

Many clients won't send their data to US-based providers.

</div>
<div>

### Cost

Open models + smart routing: Uber's per-token cost down **50%+**.

</div>
<div>

### Reliability

*"98% uptime is the new normal."* CPU and GPU shortages.

</div>
</div>

<div class="poll">Hands up if you're <b>allowed</b> to send company data to a US API.<br>Now keep it up if you do it <b>anyway</b>. 🤫</div>

<div class="receipt">Uber and uptime (Mario Zechner) via Orosz, 2026. Run it yourself: Ollama, vLLM, llama.cpp.</div>

<!-- 18:15. Keep the slide factual; tell incident stories out loud. In Europe, data sovereignty is often a blocker before any technical discussion starts. -->

---

<!-- _class: divider -->

# Who's in control?

<!-- 20:30 -->

---

# Code is exponential. Reviewers are not.

<div class="columns">
<div>

![width:350](img/seal-of-approval.png)

</div>
<div>

- More code than any human can read
- Code review becomes **theater**: *LGTM, LGTM, LGTM*
- PRs are reviewed **only by agents**
- *Engineers stop reading the code*
- *Code complexity through the roof*

</div>
</div>

<div class="receipt">Orosz, 2026, citing GitHub and Linear data.</div>

<!-- 20:45. The sense of losing control is real: I'm responsible for code I've skimmed at best. MEME: LGTM rubber stamp. -->

---

# So… we don't need software engineers anymore?

<div class="meme">MEME: "software engineering is dead" headline / tombstone</div>

<!-- 22:00. Pause. Let people laugh or nod. -->

---

<!-- _class: divider -->

# No.

<!-- 22:15 -->

---

# What's still the same

- **Teams** still own software, on-call, iteration
- **Planning** still matters for complex work
- **Tests** matter *more*: writing them takes about as long as writing code used to
- **Old practices are back**: tracer bullets, unit tests, upfront architecture
- **Non-engineers aren't shipping to prod**

<div class="receipt">Orosz, 2026: Katelyn Lesse, Jarred Sumner, Matt Pocock.</div>

<!-- 23:00. Everything the factory needs to work is classic software engineering. -->

---

# Wanted: systems thinkers

- Projects are **more ambitious than ever**
- The bottleneck moved from **typing** to **deciding**
- Someone has to see the whole system: data, infra, cost, security, users
- Domain expertise and judgment are worth more, not less

**Plenty of room left to do proper Engineering**

<!-- 24:00. This is the takeaway. Say the last line slowly. -->

---

<!-- _class: lead -->

# Let's discuss

## Would you ship code you haven't read?
## What does a junior engineer learn in 2027?
## Who reviews the reviewer agent?

[The state of the tech industry in 2026](https://newsletter.pragmaticengineer.com/p/the-state-of-the-tech-industry-in) · [ber2.github.io](https://ber2.github.io)

<!-- 25:00–30:00. First question is Charity Majors' (via Orosz). Pick whichever question the room reacts to. -->
