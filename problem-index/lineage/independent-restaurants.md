# Lineage: Independent Restaurants

**Industry:** [[industries/independent-restaurants|Independent Restaurants]]
**Wave:** [[series/eras/wave-02-departmental-item-level|2 — Departmental & Item-Level]]
**The tool:** ViewTouch — the graphical touchscreen point-of-sale, a grid of configurable on-screen menu-item buttons on an Atari 520ST, first shown at Fall COMDEX 1986
**Builder:** ViewTouch
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A restaurant order has to travel from a table to a stove, and it used to travel on paper.

A server wrote the order on a guest check, carried it to the kitchen, and later rang the total on a cash register. The handwriting was the kitchen's instruction; the register's total was the owner's record. Neither said which dishes had sold.

The chains solved this first, in hardware. **In 1974 William Brobeck and Associates built McDonald's one of the first microprocessor-controlled cash register systems** — an Intel 8008, a dedicated button for each menu item, the whole order displayed at each station. That works when the menu is fixed and the item names can be printed on the keys.

An independent's menu is not fixed. It moves with the season, the delivery and the chef.

## What Got Built

**A menu drawn on a screen instead of printed on keys.**

ViewTouch ran on an Atari 520ST fitted with a MicroTouch overlay. Each menu item was a coloured on-screen button — a widget — which the operator could configure "without low level programming". A touch rang the item and, by one account, sent it to the kitchen as it was entered: the first time a home computer had carried a sale to a restaurant kitchen in real time.

It was **first demonstrated in public at Fall COMDEX, Las Vegas, in November 1986**, on the Atari booth. Wikipedia calls it the first commercially available POS with a widget-driven colour graphic touchscreen, installed in several restaurants in the US and Canada.

## Who Built It, And Why Them

**A restaurateur, Gene Mosher, with a C programmer, Nick Colley.**

By Mosher's own account he bought an Apple II in 1977 — serial number 753, from the first manufacturing run — and began writing point-of-sale software for his own restaurants in July 1978; the project's README says 1979. Either way, he spent the better part of a decade coding for his own dining rooms before there was a product.

That is why it was an operator and not a register company. **What follows is inference, not something any source states:** a chain could pay a contractor for fixed keys because its menu was set centrally for every unit. An independent's menu changed constantly, so the thing that had to become cheap was *changing the buttons* — and the person who knew that was someone who had re-keyed his own menu. A home computer and a touch overlay turned the menu from hardware into software.

The same year, IBM introduced its 468x series of point-of-sale equipment. The large vendor sold registers; the restaurateur sold a menu.

## What It Cost

**The button became the unit of the restaurant's data — and a button is a menu item, not a recipe.**

The screen records that a chicken parmesan sold at 7:42pm. It does not know how much chicken went into it, what the chicken cost this week, or how much was trimmed and binned. The dining room was digitised; the walk-in stayed on clipboards and invoices.

Configurability cut both ways. Making a new button cheap made it just as cheap to skip — ring the special as an open item at a typed price — and each shortcut erases the item-level record the button existed to create.

## What You Still Touch

A server tapping a grid of dish names on a tablet is using the layout ViewTouch put on sale in 1986, whatever the logo on the screen.

- [[problems/independent-restaurants/high-impact|🔴 Food Cost Control and Menu Engineering Intelligence]] — the sale recorded by item, never joined to the walk-in
- [[niches/independent-restaurants/daily-specials-menu-rotation/profile|Daily Specials & High Menu Rotation Restaurants]] — specials rung as open items, the button skipped
- [[niches/independent-restaurants/restaurant-pos-data-organizations/profile|Restaurant POS Data Organizations]] — the item-level record, now held by the till's vendor

**Sources:** Wikipedia, *Point of sale*, for Brobeck's 1974 McDonald's system (Intel 8008, per-item buttons, order display), ViewTouch on the Atari 520ST with a configurable widget interface "without low level programming", the Fall COMDEX 1986 Atari-booth demonstration, "first commercially available" and installations in the US and Canada, and IBM's 468x series in 1986. ViewTouch's own site (viewtouch.com) for Mosher's Apple II bought in 1977, serial #753, POS software for "my restaurants" from July 1978, and the 1986 Atari ST and MicroTouch overlay; ViewTouch's GitHub README for 1979, Nick Colley as C programmer, and "ComDex, Las Vegas, November 1986". WWNY-TV, "Inventor of touch-screen point-of-sale system has north country ties" (April 14 2023), for "former restaurateur" and the real-time-to-the-kitchen claim. This vault's `niches/independent-restaurants/daily-specials-menu-rotation/profile.md` for specials rung as "open items" (vault material). ⚠️ **Not established:** the names, locations and dates of Mosher's restaurants; a search summary says he sold them in 1983 and moved to Oregon — the source page returned HTTP 429 and this is not asserted; the 1978 vs 1979 start date, both from ViewTouch's own materials; Mosher's claim, reported by WWNY, to have coined "point of sale" in 1980 — not tested and not repeated; and whether any other graphical touchscreen restaurant POS preceded ViewTouch. All builder-side facts come from Mosher's own materials or interviews with him.
