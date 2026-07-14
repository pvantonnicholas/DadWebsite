# Looking After the Website — A Plain-English Guide

*For Dad. Keep this somewhere easy to find. If anything here is confusing, ask Claude to explain it — that is what it is for.*

---

## 1. The three accounts you now have

| Account | What it is, in plain terms | What you use it for |
|---|---|---|
| **Claude** | Your assistant. Lives in the Claude app on your laptop. | Everything. You talk to Claude; Claude does the technical work. |
| **GitHub** | The filing cabinet. Keeps every version of every page, forever. | You open it once per change, through the **GitHub Desktop** app, to press publish. Claude walks you through it. |
| **Cloudflare** | The publisher. Notices when the filing cabinet changes and puts the new version on the internet, automatically, within a couple of minutes. | Almost never opened directly. |

You mostly work in the **Claude app**. When a change is ready, you press publish once in **GitHub Desktop** — Claude guides you every time (see section 4). Cloudflare then works quietly in the background.

## 2. How a change reaches the website

1. You ask Claude to change something.
2. Claude edits the files in the website folder on your laptop.
3. Claude opens the changed page on your laptop so you can **preview** it — see exactly how it looks before anyone else can.
4. When you are happy, Claude walks you through publishing it in **GitHub Desktop** (section 4).
5. Cloudflare notices the change and updates the live site itself, within a couple of minutes. No further steps.

## 3. Your routine for making a change

1. Open the **Claude** app on your laptop.
2. Choose **Cowork** and open the website folder.
3. Say what you want, in ordinary English. For example:
   - *"Add today's daily reading. Here is the text: …"*
   - *"On the home page, change the Word for the Season to the following: …"*
   - *"There's a spelling mistake on the Malaysia page — 'recieve' should be 'receive'."*
   - *"Show me a preview before publishing anything."*
4. Look at the preview Claude opens for you on your laptop.
5. If it looks right, say **"let's publish it"** and Claude will talk you through the steps in section 4. If not, say what to change.

## 4. Publishing a change in GitHub Desktop

When Claude tells you a change is ready and you have seen the preview, this is how you put it live. Claude will guide you through these same steps each time — you do not need to memorise them.

1. Open the **GitHub Desktop** app.
2. On the left you will see the change Claude made, listed as an edited file. You do not need to understand the details.
3. In the box at the bottom left, type a short note of what changed — for example *"Added daily reading for 14 July"*. This is called the **Summary**.
4. Click the blue **Commit to main** button. (This saves the change into the filing cabinet.)
5. At the top, click **Push origin**. (This sends it off to be published.)
6. That is it. Within a couple of minutes the live website updates itself.

If any button is named slightly differently or you cannot find it, stop and ask Claude — it will look at where you are and tell you the next click.

## 5. The golden rules

1. **You cannot permanently break anything.** Every version of every page is saved. Anything can be undone with one request: *"Please undo the last change and publish the previous version."*
2. **Always look at the preview before publishing.**
3. **One change at a time.** Small steps are easier to check and easier to undo.
4. **Never feel silly asking.** Claude will happily explain anything as many times as needed, and so will Paul.

## 6. If something goes wrong

- Site looks wrong after a change → tell Claude: *"Undo the last change,"* then publish again through GitHub Desktop (section 4).
- Claude seems confused → start a fresh conversation and ask again in different words.
- Locked out of an account → use the printed recovery codes (see box below), or call Paul.
- Anything else → call Paul. Nothing about this website is ever an emergency.

## 7. Key facts *(Paul: fill in / confirm before handover)*

- Live site: **antonnicholas.org.uk** *(confirm)*
- Website folder on this laptop: *(fill in after setup)*
- GitHub account and repository name: *(fill in after transfer)*
- Cloudflare account email: *(fill in)*
- Printed recovery codes kept: *(fill in — e.g. "in the blue folder in the study")*
- Safety net: Paul — mail@nicholaslondon.org — remains an administrator on everything and can fix anything remotely.
