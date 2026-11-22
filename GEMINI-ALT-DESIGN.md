# Gemini alternative design — "The Global Terminal" (22 Nov 2026 ~19:55 WIB)

Model: gemini-3.5-flash-lite, text-only spec (helper has no image input).
Full spec as returned, with ichi's corrections noted at the end.

## Concept
Dark-mode command-center dashboard, 10 glowing modular widgets, deep navy #0A0F1D background, cyan #00FFCC / coral #FF3366 / amber #FFB703 accents, 8px gaps.

## Layout (1024x1024)
- Header (0,0) 1024x70 #111827; Footer (0,974) 1024x50 #111827
- Col 1 X16-336 (320w): W1 COP31 Y86-370, W2 Iran Y386-670, W3 El Chapo Y686-958
- Col 2 X352-672 (320w): W4 Shenzhen Y86-270, W5 AI sell-off Y286-470, W6 Peru Y486-670, W7 Indonesia fire Y686-958
- Col 3 X688-1008 (320w): W8 Poland/Ukraine Y86-370, W9 Myanmar Y386-660, W10 GTA 6 Y676-958

## Headlines & decks (as Gemini wrote them)
- W1: COP31 Antalya Overtime on Fossil Fuels | Delegates deadlock over phase-out timeline.
- W2: Iran Strikes Bahrain & Hormuz Tankers | Regional maritime trade faces critical disruption.
- W3: Cartel Boss El Chapo Isidro Captured | 11 dead in high-stakes Mexican raid.
- W4: Trump-Xi-Putin Shenzhen Trilateral | Leaders forge unprecedented nuclear risk pact.
- W5: US Stocks Enter Correction Territory | Aggressive AI sector sell-off triggers panic.
- W6: Magnitude 6.7 Earthquake Hits Peru | Emergency services mobilize after heavy tremors.
- W7: Cikande Indonesia Factory Inferno | 3 dead, 36 missing in chemical blaze.
- W8: Missiles Hit Poland; Kryvyi Rih Struck | NATO drills shaken as 2 die in Ukraine.
- W9: UN Court Rules Myanmar Genocide | Rohingya victims receive historic legal justice.
- W10: GTA 6 Breaks All-Time Records | Launch shatters industry with $3.79B opening.

## Typography (as Gemini wrote it — TOO SMALL, see corrections)
- Header/footer monospace bold 16px #00FFCC; widget titles sans bold 14px white; decks sans regular 11px #94A3B8.

## Motifs (basic shapes)
W1 thermometer bar 90% amber; W2 radar sweep circle coral; W3 target reticle cyan; W4 three intersecting nodes cyan; W5 downward red sparkline; W6 seismograph jagged line; W7 flame triangle amber; W8 crosshair grid coral; W9 scales of justice; W10 controller D-pad cyan.

## Header/footer
Header left `[SYS_DATE: 22 NOV 2026]`, right `GLOBAL SITUATION REPORT`. Footer centre `MAKE.FUN // 22 NOVEMBER 2026 // 24-HOUR GLOBAL SUMMARY`.

## ichi's corrections before rendering (must apply)
1. Font sizes: Gemini's 14px/11px are unreadable at thumbnail scale. Use titles ~28-30pt bold, decks ~19-20pt, header/footer ~18-20pt. If a deck does not fit, shorten the deck, never shrink the font below 18pt.
2. W4 deck is WRONG: they did not "forge a pact" — they agreed to begin talks on nuclear risk reduction. Use: "Leaders agree to begin nuclear-risk talks."
3. W7 deck is WRONG: it was a candy/confectionery factory fire, not a "chemical blaze". Use: "3 dead, 36 missing in candy factory fire."
4. W8 headline is WRONG wording: "Missiles Hit Poland" implies a strike on Poland. Verified: "Russian missiles land in Poland during NATO drills". Use headline "Missiles Land in Poland; Kryvyi Rih Struck" and deck "2 killed in Ukraine as NATO calls it a violation."
5. W5 deck "triggers panic" is editorialising — use "S&P and Dow slide as AI rally reverses."
6. Keep all numbers exactly as verified: 11 dead Sinaloa, 3 dead / 36 missing Cikande, 2 killed Kryvyi Rih, 6.7 Peru, $3.79B GTA 6.
